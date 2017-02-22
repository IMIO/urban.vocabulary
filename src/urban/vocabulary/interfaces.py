# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.supermodel import model
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from plone.directives import form
from collective.z3cform.select2.widget.widget import MultiSelect2FieldWidget

from urban.vocabulary import _


class IUrbanVocabularyLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISettings(model.Schema):

    model.fieldset(
        'pca',
        label=_('PCA Vocabulary'),
        fields=[
            'pca_url',
            'pca_title_attribute',
            'pca_token_attribute',
            'pca_boolean_mapping',
            'pca_boolean_mapping_value',
        ],
    )

    pca_url = schema.TextLine(
        title=_(u'URL'),
        required=True,
    )

    pca_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    pca_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(pca_boolean_mapping=MultiSelect2FieldWidget)
    pca_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.PCAZones',
        ),
        required=False,
    )

    pca_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )

    model.fieldset(
        'natura_2000',
        label=_('Natura 2000 Vocabulary'),
        fields=[
            'natura_2000_url',
            'natura_2000_title_attribute',
            'natura_2000_token_attribute',
            'natura_2000_boolean_mapping',
            'natura_2000_boolean_mapping_value',
        ],
    )

    natura_2000_url = schema.TextLine(
        title=_(u'URL'),
        required=True,
    )

    natura_2000_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    natura_2000_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(natura_2000_boolean_mapping=MultiSelect2FieldWidget)
    natura_2000_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.Natura2000',
        ),
        required=False,
    )

    natura_2000_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )


class IVocabularies(Interface):

    pca_cached = schema.List(
        title=_(u'PCA cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
        ),
        required=False,
    )

    natura_2000_cached = schema.List(
        title=_(u'Natura 2000 cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
        ),
        required=False,
    )
