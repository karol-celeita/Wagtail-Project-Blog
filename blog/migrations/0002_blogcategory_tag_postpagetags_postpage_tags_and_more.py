# Generated by Django 5.0.3 on 2024-03-09 22:29

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250)),
                ("slug", models.SlugField(max_length=80, unique=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("taggit.tag",),
        ),
        migrations.CreateModel(
            name="PostPageTags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.postpage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="postpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.PostPageTags",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.CreateModel(
            name="PostPageBlogCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Page",
                    modelcluster.fields.ParentalKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="blog.postpage",
                    ),
                ),
                (
                    "blog_category",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_pages",
                        to="blog.blogcategory",
                    ),
                ),
            ],
            options={
                "unique_together": {("Page", "blog_category")},
            },
        ),
    ]