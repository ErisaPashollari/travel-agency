from django.db import models
from django.utils.translation import gettext_lazy as _

class Continent(models.Model):
    name = models.CharField(_("name"), max_length=32)

    class Meta:
        verbose_name = _("continent")
        verbose_name_plural = _("continents")


class Country(models.Model):
    name = models.CharField(_("name"), max_length=128)
    continent = models.ForeignKey(Continent, verbose_name=_("continent"), null=True, blank=True,
            on_delete=models.SET_NULL, related_name="countries")

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")
        # db_table = "countries"

    



