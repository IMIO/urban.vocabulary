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
from urlparse import urlparse
from urlparse import parse_qs

import logging
import requests

from urban.vocabulary import utils


logger = logging.getLogger('urban.vocabulary')


def _call_ws_cachekey(method, self, force=0):
    return (getattr(self, 'ws_url'), force, time() // (60 * 5))


class UrbanWebservice(object):

    def __init__(self, registry_key):
        self.registry_key = registry_key

    def get_registry_value(self, key, default=None):
        key = '{0}.{1}_{2}'.format(
            'urban.vocabulary.interfaces.ISettings',
            self.registry_key,
            key,
        )
        return api.portal.get_registry_record(key, default=default)

    @property
    def polygon(self):
        key = 'urban.vocabulary.interfaces.ISettings.polygon'
        return api.portal.get_registry_record(key, default=None)

    @property
    def ws_url(self):
        base_url = api.portal.get_registry_record('urban.vocabulary.interfaces.ISettings.base_url')
        url = self.get_registry_value('url', default=[])
        if isinstance(url, basestring):
            full_url = url.format(base_url)
            return [full_url]
        full_url = [url_.format(base_url) for url_ in url]
        return full_url

    @property
    def mapping(self):
        return {
            'title': utils.to_int(self.get_registry_value('title_attribute')),
            'token': utils.to_int(self.get_registry_value('token_attribute')),
        }

    def _request_query(self, url):
        parser = urlparse(url)
        params = parse_qs(parser.query)
        if not self.polygon:
            logger.error('Missing polygon for ws queries')
        else:
            params['area'] = self.polygon
        return parser._replace(query=None).geturl(), params

    @ram.cache(_call_ws_cachekey)
    def _call_ws(self, force=0):
        """Call and return the response from the webservice"""
        if not self.ws_url:
            return
        result = []
        for url in self.ws_url:
            url, data = self._request_query(url)
            r = requests.post(url, data=data)
            if r.status_code != 200:
                return
            json = r.json()
            if json.get('success', True) is False:
                return
            result.append((data, json))
        return result

    def _map_result(self, json, mapping):
        """
        Map the webservice result based on the mapping attributes from the
        registry
        """
        result = map(convert_value, json['result']['features'])
        normalizer = getUtility(IIDNormalizer)
        return [[unicode(normalizer.normalize(e[mapping['token']])),
                 self._format_title(e[mapping['title']]),
                 u'1']
                for e in result
                if e[mapping['title']] and e[mapping['token']]]

    @staticmethod
    def _format_title(value):
        return utils.to_str(value).strip()

    def store_values(self, force=False):
        """Store the webservice result into the registry"""
        if force is True:
            force = time()
        json_results = self._call_ws(force=force)
        values = []
        if not json_results:
            return False
        try:
            for data, json in json_results:
                mapping = {k: v for k, v in zip(('title', 'token'),
                                                data['att'][0].split(','))}
                values.extend(self._map_result(json, mapping))
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
