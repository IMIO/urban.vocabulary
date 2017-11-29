# -*- coding: utf-8 -*-
"""
urban.vocabulary
------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.statusmessages.interfaces import IStatusMessage
from plone.app.registry.browser import controlpanel
from plone.app.registry.browser.controlpanel import _ as PMF
from z3c.form import button
from zope.i18n import translate

from urban.vocabulary import _
from urban.vocabulary.interfaces import ISettings
from urban.vocabulary.ws import UrbanWebservice


class SettingsEditForm(controlpanel.RegistryEditForm):
    schema = ISettings
    label = _(u'Urban Vocabulary Settings')

    # Imported from plone.app.registry.browser.controlpanel
    @button.buttonAndHandler(PMF(u"Save"), name='save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(
            PMF(u"Changes saved."),
            "info")
        self.request.response.redirect(self.request.getURL())

    @button.buttonAndHandler(_(u'Update vocabularies'))
    def handleUpdate(self, action):
        data, errors = self.extractData()
        messages = IStatusMessage(self.request)

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            messages.addStatusMessage(self.status, type="error")
            return
        ws_keys = [e.replace('_url', '') for e in data.keys()
                   if e.endswith('_url')]
        result = update_all(ws_keys)
        message = translate(
            _(u'Vocabularies updated : {0}'),
            context=self.request,
        )
        messages.addStatusMessage(
            message.format(', '.join(result)),
            'info',
        )

    # Imported from plone.app.registry.browser.controlpanel
    @button.buttonAndHandler(PMF(u"Cancel"), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            PMF(u"Changes canceled."),
            "info")
        self.request.response.redirect("%s/%s" % (
            self.context.absolute_url(),
            self.control_panel_view))


class SettingsView(controlpanel.ControlPanelFormWrapper):
    form = SettingsEditForm


def update_all(keys):
    """Update all vocabularies"""
    result = []
    for key in keys:
        ws = UrbanWebservice(key)
        response = ws.store_values(force=True)
        if response is True:
            result.append(key)
    return result
