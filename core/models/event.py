from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from ckeditor.fields import RichTextField


class Event(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    class Meta:
        verbose_name_plural = "Our Event"

    body = RichTextField()
