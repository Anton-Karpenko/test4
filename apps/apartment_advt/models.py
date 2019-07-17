from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from apps.base.models import IdModel


class ApartmentAdvt(IdModel, TimeStampedModel):
    title = models.CharField(
        max_length=400,
    )
    checkup_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        help_text=_("Id from third party service."),
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
    )
    num_of_rooms = models.PositiveIntegerField(
        null=True,
    )
    district = models.CharField(
        max_length=100,
    )
    description = models.TextField()

    class Meta:
        db_table = 'apartment_advt'

    @property
    def short_description(self):
        return f'{self.description[:140]}...'
