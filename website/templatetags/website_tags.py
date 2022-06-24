from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.inclusion_tag('website/recent-blog-area.html')
def latest_blog_posts(arg=3):
    latest_blog_posts = Post.objects.filter(
        status=1).order_by('-published_date')[:arg]
    return {'latest_blog_posts': latest_blog_posts}
