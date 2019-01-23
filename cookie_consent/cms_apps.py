# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class CookieConsentApp(CMSApp):
    name = _('Cookie consent')
    urls = ['cookie_consent.urls']  # COMPAT: CMS3.2

    def get_urls(self, *args, **kwargs):
        return self.urls


apphook_pool.register(CookieConsentApp)
