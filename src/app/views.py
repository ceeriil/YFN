# from django.shortcuts import render
from django.views.generic import TemplateView
from app.vars import NAME
from django.shortcuts import render, redirect, get_object_or_404
import json
from .models import PostModel, Like
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.conf import settings
from django.contrib.auth.models import User
from users.models import Follow

class HomeView(TemplateView):
    template_name = f"{NAME}/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(settings.BASE_DIR / 'app' / 'data' / 'card_data.json') as f:
            data = json.load(f)

        context['card_data_list'] = data['card_data_list']
        context['trending_card_list'] = data['trending_card_list']
        return context

def blog(request):
    posts = PostModel.objects.all()
    if request.method == 'POST': 
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog')
    else:
        form = PostModelForm()
       
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, f"{NAME}/blog.html", context)

def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if 'like' in request.POST:
            Like.objects.create(user=request.user, post=post)
            return redirect('app:post-detail', pk=post.id)
        elif 'unlike' in request.POST:
            Like.objects.filter(user=request.user, post=post).delete()
            return redirect('app:post-detail', pk=post.id)
        else:
            if c_form.is_valid():
                instance = c_form.save(commit=False)
                instance.user = request.user
                instance.post = post
                instance.save()
                return redirect('app:post-detail', pk=post.id)
    else:
        c_form = CommentForm()

    likes = Like.objects.filter(post=post)
    liked = True if request.user in [like.user for like in likes] else False

    context = {
        'post': post,
        'c_form': c_form,
        'likes': likes,
        'liked': liked
    }
    return render(request, 'app/post_detail.html', context)


def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('app:post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, f"{NAME}/post_edit.html", context)


def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    context = {
        'post': post
    }
    return render(request, 'app/post_delete.html', context)

def author_profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = PostModel.objects.filter(author=author)

    followers_count = Follow.objects.filter(following=author).count()
    following_count = Follow.objects.filter(follower=author).count()
    followers = [follow.follower for follow in Follow.objects.filter(following=author)]
    following = [follow.following for follow in Follow.objects.filter(follower=author)]

    if request.method == 'POST':
        if 'follow' in request.POST:
            Follow.objects.create(follower=request.user, following=author)
        elif 'unfollow' in request.POST:
            Follow.objects.filter(follower=request.user, following=author).delete()

        return redirect('app:author-profile', username=username)

    is_following = Follow.objects.filter(follower=request.user, following=author).exists()

    context = {
        'author': author,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
        'followers': followers,
        'following': following,
    }
    return render(request, 'app/author_profile.html', context)
