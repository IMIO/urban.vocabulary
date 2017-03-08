# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.urban.UrbanVocabularyTerm import UrbanVocabulary
from datetime import datetime
from plone import api
from time import time
from plone.app.async.interfaces import IAsyncService
from zope.component import getUtility

from urban.vocabulary import utils
from urban.vocabulary.interfaces import ISettings
from urban.vocabulary.ws import UrbanWebservice


class BaseVocabulary(object):
    config_vocabulary_path = None
    config_vocabulary_options = {}
    # See Products.Urban.UrbanVocabularyTerm.UrbanVocabulary for options
    registry_key = None
    _registry_interface = 'urban.vocabulary.interfaces.IVocabularies'
    _expire_delay = 3600  # in seconds

    def __call__(self, context):
        vocabulary = self._vocabulary_from_urban_vocabulary(
            self._get_config_vocabulary(),
            context,
        )
        if self.registry_key:
            vocabulary = utils.extend_vocabulary(
                vocabulary,
                self._get_registry_items(context),
            )
        return vocabulary

    @classmethod
    def _get_config_vocabulary(cls):
        """Return the vocabulary created from urban config"""
        if not cls.config_vocabulary_path:
            return
        return UrbanVocabulary(
            cls.config_vocabulary_path,
            **cls.config_vocabulary_options
        )

    def _get_registry_items(self, context):
        key = '{0}.{1}_cached'.format(
            self._registry_interface,
            self.registry_key,
        )
        record = api.portal.get_registry_record(key, default=[])
        self._refresh_registry()
        return [(e[0], e[1]) for e in record]

    def _vocabulary_from_urban_vocabulary(self, urban_vocabulary, context):
        """Convert an urban vocabulary to a zope.schema vocabulary"""
        items = [(t.id, t.title) for t in
                 urban_vocabulary.getAllVocTerms(context).values()]
        return utils.vocabulary_from_items(items)

    @classmethod
    def urban_vocabulary(cls, context):
        """Return an archetype vocabulary with the current vocabulary values"""
        return cls._get_config_vocabulary()

    def _refresh_registry(self):
        """Refresh (if necessary) the values stored in the registry"""
        async = get_async()
        portal = api.portal.get()
        if async:
            async.queueJob(
                refresh_registry,
                portal,
                self.registry_key,
                self.__class__,
            )
        else:
            refresh_registry(portal, self.registry_key, self.__class__)

    @classmethod
    def set_delay_key(cls):
        cls._delay_key = time() // cls._expire_delay

    @classmethod
    def _get_delay_key(cls):
        return getattr(cls, '_delay_key', None)

    @classmethod
    def verify_delay(cls):
        """Verify if there is a delay and if it expired"""
        return getattr(cls, '_delay_key', None) != time() // cls._expire_delay


class BaseBooleanVocabulary(BaseVocabulary):

    def __call__(self, context):
        vocabulary = super(BaseBooleanVocabulary, self).__call__(context)
        return self._generate_vocabulary(vocabulary)

    def _generate_vocabulary(self, base_vocabulary):
        keys, value = self.boolean_mapping
        default_value = not value
        return utils.vocabulary_from_items(
            [(t.value, t.value in keys and value or default_value)
             for t in base_vocabulary],
        )

    @property
    def boolean_mapping(self):
        mapping_keys = api.portal.get_registry_record(
            '{0}_boolean_mapping'.format(self.registry_key),
            interface=ISettings,
            default=None,
        )
        mapping_value = api.portal.get_registry_record(
            '{0}_boolean_mapping_value'.format(self.registry_key),
            interface=ISettings,
            default=None,
        )
        return mapping_keys, mapping_value


def refresh_registry(context, registry_key, cls):
    if cls.verify_delay() is True:
        ws = UrbanWebservice(registry_key)
        result = ws.store_values()
        if result is True:
            cls.set_delay_key()


def get_async():
    """Ensure that the async worker is running and return it"""
    async = getUtility(IAsyncService)
    try:
        queues = async.getQueues()
        queue = queues['']
        if len(queue) > 0:
            message_date = queue[0]._begin_after.replace(tzinfo=None)
            msg_duration = datetime.utcnow() - message_date
            if msg_duration.total_seconds() > 60:
                return
    except KeyError:  # No worker declared
        return
    return async