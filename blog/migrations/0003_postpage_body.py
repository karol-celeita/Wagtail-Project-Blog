# Generated by Django 5.0.3 on 2024-03-10 18:15

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blogcategory_tag_postpagetags_postpage_tags_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("h1", wagtail.blocks.CharBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "bullet_list",
                        wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()),
                    ),
                    (
                        "image_text",
                        wagtail.blocks.StructBlock(
                            [
                                ("image1", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption1", wagtail.blocks.CharBlock()),
                                ("image2", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption2", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote_by", wagtail.blocks.CharBlock()),
                                ("quotes", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]