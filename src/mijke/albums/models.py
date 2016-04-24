from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.blocks import (
    CharBlock, RichTextBlock, StreamBlock, StructBlock
)
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


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


class OverviewPageLink(Orderable):
    page = ParentalKey('OverviewPage', related_name='links')
    target_page = models.ForeignKey(Page, related_name='+')
    title = models.CharField(_('title'), max_length=255, blank=True)

    panels = [
        PageChooserPanel('target_page'),
        FieldPanel('title'),
    ]


class OverviewPage(Page):

    """
    Page used as tree node, to distribute to other pages.
    """

    cover = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        help_text=_("Main image for this page. The body will be overlaid.")
    )

    body = StreamField(OverviewStreamBlock())

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover'),
        StreamFieldPanel('body'),
        InlinePanel('links', label=_("page links")),
    ]
