# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import defaultdict

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cookie_consent import models


class CookieConsentPlugin(CMSPluginBase):
    name = _('Cookie consent')
    render_template = 'cookie_consent/plugin.html'
    model = models.CookieConsentPlugin
    cache = False

    def render(self, context, instance, placeholder):
        groups = instance.groups
        if not groups:
            groups = models.CookieGroup.all()
        context['instance'] = instance
        context['enabled_cookie_groups'] = groups.all()

        return context


plugin_pool.register_plugin(CookieConsentPlugin)
