from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from blog.models import Post, Comment
from blog.forms import CommentForm



def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        print ((kwargs['author_username']))
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
   
    if request.method != 'POST':
        form = CommentForm()
       
    else: 
        form = CommentForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been saved successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment has not been saved successfully.')
    
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    index = list(posts).index(post)
    next_post = posts[index-1] if index > 0 else None
    prev_post = posts[index+1] if index < len(posts)-1 else None
    context = {
        'prev_post': prev_post,
        'post': post,
        'next_post': next_post,
        'comments': comments,
        'form': form,
        }
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


