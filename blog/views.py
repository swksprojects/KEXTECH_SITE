from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    print("going to blog")
    posts = Post.published.all()
    print("got the posts")
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})
