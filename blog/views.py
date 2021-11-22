from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blog(request):
    all_blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blog.html', {"all_blogs": all_blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {"blog": blog})
