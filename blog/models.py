from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag
from modelcluster.models import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.tags import ClusterTaggableManager

class Blogpage (Page):
    description = models.CharField(max_length=250, blank=True)   
    
    content_panels = Page.content_panels + [
        FieldPanel ("description"),
    ]
    

class PostPage (Page):
    header_image = models.ForeignKey ("wagtailimages.Image", on_delete = models.SET_NULL, null=True, blank=True, related_name="+")
    tags = ClusterTaggableManager(through="PostPageTags", blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        FieldPanel("tags"),
        InlinePanel("categories", label="Category"),
    ]
    

class PostPageBlogCategory(models.Model):
    Page = ParentalKey("blog.PostPage", on_delete=models.CASCADE, blank=True, related_name="categories")
    blog_category = models.ForeignKey("BlogCategory", blank=True, on_delete=models.CASCADE, related_name="post_pages")
    
    panels = [
        FieldPanel("blog_category")
    ]
    class Meta:
        unique_together = ("Page", "blog_category")
        

@register_snippet
class BlogCategory (models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=80, unique=True)
    
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),

    ]
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PostPageTags(TaggedItemBase):
    content_object = ParentalKey("blog.PostPage", blank=True)


@register_snippet
class Tag (TaggitTag):
    
    class Meta:
        proxy = True


