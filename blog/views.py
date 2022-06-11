from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
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
