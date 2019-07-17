from django.db import models

from apps.base.utils import custom_uuid


class IdModel(models.Model):
    """ IdModel
    An abstract base class model that provides "id" field.
    """
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )

    class Meta:
        abstract = True
