# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from urban.vocabulary.vocabularies.base import BaseVocabulary
from urban.vocabulary.vocabularies.base import BaseBooleanVocabulary


class NoteworthyTreesVocabulary(BaseVocabulary):
    config_vocabulary_path = u'noteworthy_trees'
    config_vocabulary_options = {
        'inUrbanConfig': False,
    }
    registry_key = 'noteworthy_trees'


class NoteworthyTreesBooleanVocabulary(NoteworthyTreesVocabulary,
                                       BaseBooleanVocabulary):
    pass
