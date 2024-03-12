from blog.models import Tag, BlogCategory
from django import template

register = template.Library()

@register.inclusion_tag("components/main_categories.html", takes_context=True)
def category_list(context):
    categories = BlogCategory.objects.all()
    return {
        "request":context["request"],
        "blogpage":context["blogpage"],
        "categories": categories
    }
    

@register.inclusion_tag("components/main_tags.html", takes_context=True)
def tag_list(context):
    tags = Tag.objects.all()
    return {
        "request":context["request"],
        "blogpage":context["blogpage"],
        "tags": tags
    }
    
    
@register.inclusion_tag("components/post_tags.html", takes_context=True)
def post_tag_list(context):
    page = context["page"]
    post_tags = page.tags.all()
    return{
        "request":context["request"],
        "post_tags": post_tags
    }


@register.inclusion_tag("components/post_categories.html", takes_context=True)
def post_categories_list(context):
    page = context["page"]
    post_categories = page.categories.all()
    return{
        "request":context["request"],
        "post_categories": post_categories
    }


@register.simple_tag()
def post_page_date_slug_url(postpage, blogpage):
    post_date = postpage.post_date
    url = blogpage.full_url + blogpage.reverse_subpage(
        "post_by_date_slug",
        args = (
            post_date.year,
            "{0:02}".format(post_date.month),
            "{0:02}".format(post_date.day),
            postpage.slug,
        )
    )
    
    return url