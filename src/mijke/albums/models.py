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
