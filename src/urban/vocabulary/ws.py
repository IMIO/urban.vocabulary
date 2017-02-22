# -*- coding: utf-8 -*-
"""
urban.vocabulary
----------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

import requests

from urban.vocabulary.interfaces import ISettings
from urban.vocabulary.interfaces import IVocabularies


class UrbanWebservice(object):

    def __init__(self, registry_key):
        self.registry_key = registry_key

    def get_registry_value(self, key):
        return api.portal.get_registry_record(
            name='{0}_{1}'.format(self.registry_key, key),
            interface=ISettings,
        )

    @property
    def ws_url(self):
        return self.get_registry_value('url')

    @property
    def mapping(self):
        return {
            'title': self.get_registry_value('title_attribute'),
            'token': self.get_registry_value('token_attribute'),
        }

    def _call_ws(self):
        """Call and return the response from the webservice"""
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
        if not isinstance(result, dict):
            mapping = {k: int(v) for k, v in self.mapping.items()}
        return [[unicode(normalizer.normalize(e[mapping['token']])),
                 e[mapping['title']],
                 u'1']
                for e in result if e]

    def store_values(self):
        """Store the webservice result into the registry"""
        json_result = self._call_ws()
        if not json_result:
            return False
        api.portal.set_registry_record(
            name='{0}_cached'.format(self.registry_key),
            value=self._map_result(json_result),
            interface=IVocabularies,
        )
        return True


def convert_value(value):
    if isinstance(value, basestring):
        return [value]
    return value
