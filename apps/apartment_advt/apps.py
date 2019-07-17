from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApartmentAdvtConfig(AppConfig):
    name = "apps.apartment_advt"
    verbose_name = _("Apartment advertises")

    def ready(self):
        try:
            import apps.apartment_advt.signals  # noqa F401
        except ImportError:
            pass
