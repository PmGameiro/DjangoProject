from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from ckeditor.fields import RichTextField


class Blog(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    class Meta:
        verbose_name_plural = "Blogs"

    body = RichTextField()
