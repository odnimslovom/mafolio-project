from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def all_blogs(request):
    posts = BlogPost.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
