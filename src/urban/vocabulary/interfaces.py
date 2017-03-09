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


class IPCASettings(model.Schema):

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


class INatura2000Settings(model.Schema):

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


class IReparcellingSettings(model.Schema):

    model.fieldset(
        'reparcelling',
        label=_('Reparcelling Vocabulary'),
        fields=[
            'reparcelling_url',
            'reparcelling_title_attribute',
            'reparcelling_token_attribute',
            'reparcelling_boolean_mapping',
            'reparcelling_boolean_mapping_value',
        ],
    )

    reparcelling_url = schema.TextLine(
        title=_(u'URL'),
        required=True,
    )

    reparcelling_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    reparcelling_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(reparcelling_boolean_mapping=MultiSelect2FieldWidget)
    reparcelling_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.Reparcelling',
        ),
        required=False,
    )

    reparcelling_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )


class IParcellingsSettings(model.Schema):

    model.fieldset(
        'parcellings',
        label=_('Parcellings Vocabulary'),
        fields=[
            'parcellings_url',
            'parcellings_title_attribute',
            'parcellings_token_attribute',
            'parcellings_boolean_mapping',
            'parcellings_boolean_mapping_value',
        ],
    )

    parcellings_url = schema.TextLine(
        title=_(u'URL'),
        required=True,
    )

    parcellings_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    parcellings_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(parcellings_boolean_mapping=MultiSelect2FieldWidget)
    parcellings_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.Parcellings',
        ),
        required=False,
    )

    parcellings_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )


class IProtectedBuildingSettings(model.Schema):

    model.fieldset(
        'protected_building',
        label=_('ProtectedBuilding Vocabulary'),
        fields=[
            'protected_building_url',
            'protected_building_title_attribute',
            'protected_building_token_attribute',
            'protected_building_boolean_mapping',
            'protected_building_boolean_mapping_value',
        ],
    )

    protected_building_url = schema.List(
        title=_(u'URL(s)'),
        value_type=schema.TextLine(title=_(u'URL')),
        required=True,
    )

    protected_building_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    protected_building_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(protected_building_boolean_mapping=MultiSelect2FieldWidget)
    protected_building_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.ProtectedBuilding',
        ),
        required=False,
    )

    protected_building_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )


class INoteworthyTreesSettings(model.Schema):

    model.fieldset(
        'noteworthy_trees',
        label=_('NoteworthyTrees Vocabulary'),
        fields=[
            'noteworthy_trees_url',
            'noteworthy_trees_title_attribute',
            'noteworthy_trees_token_attribute',
            'noteworthy_trees_boolean_mapping',
            'noteworthy_trees_boolean_mapping_value',
        ],
    )

    noteworthy_trees_url = schema.List(
        title=_(u'URL(s)'),
        value_type=schema.TextLine(title=_(u'URL')),
        required=True,
    )

    noteworthy_trees_title_attribute = schema.TextLine(
        title=_(u'Title attribute'),
        required=True,
    )

    noteworthy_trees_token_attribute = schema.TextLine(
        title=_(u'Token attribute'),
        required=True,
    )

    form.widget(noteworthy_trees_boolean_mapping=MultiSelect2FieldWidget)
    noteworthy_trees_boolean_mapping = schema.List(
        title=_(u'Mapping of vocabularies values to boolean'),
        value_type=schema.Choice(
            title=_(u'Value'),
            vocabulary='urban.vocabulary.NoteworthyTrees',
        ),
        required=False,
    )

    noteworthy_trees_boolean_mapping_value = schema.Choice(
        title=_(u'Boolean mapping value'),
        values=(True, False),
        required=True,
        default=True,
    )


class ISettings(IPCASettings,
                INatura2000Settings,
                IReparcellingSettings,
                IParcellingsSettings,
                IProtectedBuildingSettings,
                INoteworthyTreesSettings):
    pass


class IVocabularies(Interface):

    pca_cached = schema.List(
        title=_(u'PCA cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )

    natura_2000_cached = schema.List(
        title=_(u'Natura 2000 cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )

    reparcelling_cached = schema.List(
        title=_(u'Reparcelling cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )

    parcellings_cached = schema.List(
        title=_(u'Parcellings cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )

    protected_building_cached = schema.List(
        title=_(u'ProtectedBuilding cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )

    noteworthy_trees_cached = schema.List(
        title=_(u'PCA cached value'),
        value_type=schema.List(
            title=u'Vocabulary record',
            value_type=schema.TextLine(title=u'Value'),
            required=False,
        ),
        required=False,
    )
