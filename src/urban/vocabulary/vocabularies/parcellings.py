# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from urban.vocabulary.vocabularies.base import BaseVocabulary
from urban.vocabulary.vocabularies.base import BaseBooleanVocabulary


class ParcellingsVocabulary(BaseVocabulary):
    config_vocabulary_path = u'parcellings'
    config_vocabulary_options = {
        'inUrbanConfig': False,
    }
    registry_key = 'parcellings'


class ParcellingsBooleanVocabulary(ParcellingsVocabulary, BaseBooleanVocabulary):
    pass
