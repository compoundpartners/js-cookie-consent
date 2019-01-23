# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_client import forms


class Form(forms.BaseForm):
    name = forms.CharField(
        'name of consent cookie that remembers user choice',
        help_text='Default: cookie_consent',
        required=False
    )
    max_age = forms.NumberField(
        'max-age of consent cookie',
        help_text='Default: 1 year',
        required=False
    )
    decline = forms.CharField(
        'decline value',
        help_text='Default: -1',
        required=False
    )
    enabled = forms.CheckboxField(
        'Enabled', required=False, initial=True
    )
    opt_out = forms.CheckboxField(
        'opt-out cookies', required=False, initial=False,
        help_text='opt-out cookies are set until declined opt-in cookies are set only if accepted'

    )
    cache_backend = forms.CharField(
        'Alias for backend to use for caching',
        help_text='Default: default',
        required=False
    )

    def to_settings(self, data, settings):
        if data['name']:
            settings['COOKIE_CONSENT_NAME'] = data['name']
        if data['max_age']:
            settings['COOKIE_CONSENT_MAX_AGE'] = int(data['max_age'])
        if data['decline']:
            settings['COOKIE_CONSENT_DECLINE'] = data['decline']
        settings['COOKIE_CONSENT_ENABLED'] = data['enabled']
        settings['COOKIE_CONSENT_OPT_OUT'] = data['opt_out']
        if data['cache_backend']:
            settings['COOKIE_CONSENT_CACHE_BACKEND'] = data['cache_backend']
        #settings['ADDON_URLS'].append('cookie_consent.urls')

        return settings

