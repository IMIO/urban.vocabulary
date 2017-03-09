# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from urban.vocabulary.vocabularies.base import BaseVocabulary
from urban.vocabulary.vocabularies.base import BaseBooleanVocabulary


class RedesignSitesVocabulary(BaseVocabulary):
    config_vocabulary_path = None
    config_vocabulary_options = {}
    registry_key = 'redesign_sites'


class RedesignSitesBooleanVocabulary(RedesignSitesVocabulary,
                                     BaseBooleanVocabulary):
    pass
