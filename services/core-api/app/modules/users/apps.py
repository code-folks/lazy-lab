from contextlib import suppress

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.users"
    verbose_name = _("Users")

    def ready(self):
        with suppress(ImportError):
            import modules.users.signals  # noqa: F401
