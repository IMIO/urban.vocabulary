# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.registry.browser import controlpanel

from urban.vocabulary import _
from urban.vocabulary.interfaces import ISettings


class SettingsEditForm(controlpanel.RegistryEditForm):
    schema = ISettings
    label = _(u'Urban Vocabulary Settings')


class SettingsView(controlpanel.ControlPanelFormWrapper):
    form = SettingsEditForm
