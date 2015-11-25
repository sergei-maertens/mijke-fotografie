from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import (
    CharBlock, RichTextBlock, StreamBlock, StructBlock
)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class AlbumPage(Page):
    photos = StreamField([
        ('photo', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('photos'),
    ]


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()


class OverviewStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageBlock(label=_('image'), icon="image")


class OverviewPage(Page):

    """
    Page used as tree node.
    """

    body = StreamField(OverviewStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
