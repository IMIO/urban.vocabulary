# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.schema.vocabulary import SimpleVocabulary


def vocabulary_from_items(items):
    """
    Create a zope.schema vocabulary from a list of tuple e.g.
    [('value1', 'title1'), ('value2', 'title2')]
    """
    return SimpleVocabulary(
        [SimpleVocabulary.createTerm(item[0], item[0], item[1])
         for item in items],
    )


def extend_vocabulary(voc, items):
    """Add new terms to an existing vocabulary"""
    for value, title in items:
        if value in voc.by_token or value in voc.by_value:
            continue
        term = SimpleVocabulary.createTerm(value, value, title)
        voc._terms.append(term)
        voc.by_token[value] = term
        voc.by_value[value] = term
    return voc
