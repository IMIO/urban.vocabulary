# -*- coding: utf-8 -*-

from urban.vocabulary.vocabularies.base import BaseVocabulary
from urban.vocabulary.vocabularies.base import BaseBooleanVocabulary


class CatchmentAreaVocabulary(BaseVocabulary):
    registry_key = 'catchment_area'


class CatchmentAreaBooleanVocabulary(CatchmentAreaVocabulary,
                                     BaseBooleanVocabulary):
    pass
