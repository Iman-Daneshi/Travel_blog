from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.templatetags.blog_tags import post_categories

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    index = list(posts).index(post)
    next_post = posts[index-1] if index > 0 else None
    prev_post = posts[index+1] if index < len(posts)-1 else None
    context = {
        'prev_post': prev_post,
        'post': post,
        'next_post': next_post,
        
        }
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


