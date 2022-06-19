from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    latest_posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories ():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat_name in categories:
        cat_dict[cat_name] = posts.filter(category=cat_name).count()
    return {'cat_dict': cat_dict}
