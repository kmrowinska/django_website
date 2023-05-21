from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Author
from django.contrib.auth.models import User
# 
# Create your views here.
def post_list_view(request, category_name=None):
    if category_name:
        obj = Post.objects.filter(category__name=category_name, public=True)
    else:
        obj = Post.objects.filter(public=True)
    context = { 
        'object_list': obj.order_by('-date_publish'),
        'category_list': Category.objects.all(),
        'category_name': category_name,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, post_id):
    try:
        context = {
            'object': Post.objects.get(id=post_id),
            'category_list': Category.objects.all(),
            'category_name': None,
        }
    except Post.DoesNotExist:
        raise Http404('No post matches the given query')
    return render(request, 'blog/post_detail.html', context)

def post_authors_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)
    context = {'author': author, 'posts': posts}
    return render(request, 'blog/post_list.html', context)


