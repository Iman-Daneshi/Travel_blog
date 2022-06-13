from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def function(a=7):
    return a + 2

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    latest_posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'latest_posts': latest_posts}
