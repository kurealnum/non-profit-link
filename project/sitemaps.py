from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.accounts.models import Org


class StaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            "credits",
            "about_us",
            "faq",
            "index",
            "login",
            "register",
            "search_items",
        ]

    def location(self, item):
        return reverse(item)


# the part of the sitemap for organizations homepages
class DynamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Org.objects.all()
