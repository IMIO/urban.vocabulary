# -*- coding: utf-8 -*-
"""
urban.vocabulary
----------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.memoize import ram
from time import time
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

import requests

from urban.vocabulary import utils


def _call_ws_cachekey(method, self):
    return (getattr(self, 'ws_url'), time() // (60 * 5))


class UrbanWebservice(object):

    def __init__(self, registry_key):
        self.registry_key = registry_key

    def get_registry_value(self, key):
        key = '{0}.{1}_{2}'.format(
            'urban.vocabulary.interfaces.ISettings',
            self.registry_key,
            key,
        )
        return api.portal.get_registry_record(key, default=None)

    @property
    def ws_url(self):
        return self.get_registry_value('url')

    @property
    def mapping(self):
        return {
            'title': utils.to_int(self.get_registry_value('title_attribute')),
            'token': utils.to_int(self.get_registry_value('token_attribute')),
        }

    @ram.cache(_call_ws_cachekey)
    def _call_ws(self):
        """Call and return the response from the webservice"""
        if not self.ws_url:
            return
        r = requests.get(self.ws_url)
        if r.status_code == 200:
            return r.json()

    def _map_result(self, json):
        """
        Map the webservice result based on the mapping attributes from the
        registry
        """
        result = map(convert_value, json['result']['features'])
        mapping = self.mapping
        normalizer = getUtility(IIDNormalizer)
        return [[unicode(normalizer.normalize(e[mapping['token']])),
                 self._format_title(e[mapping['title']]),
                 u'1']
                for e in result
                if e[mapping['title']] and e[mapping['token']]]

    @staticmethod
    def _format_title(value):
        return utils.to_str(value).strip()

    def store_values(self):
        """Store the webservice result into the registry"""
        json_result = self._call_ws()
        if not json_result:
            return False
        try:
            values = self._map_result(json_result)
        except KeyError:
            return False
        key = '{0}.{1}_cached'.format(
            'urban.vocabulary.interfaces.IVocabularies',
            self.registry_key,
        )
        api.portal.set_registry_record(key, values)
        return True


def convert_value(value):
    if isinstance(value, basestring):
        return [value]
    return value
