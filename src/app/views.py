# from django.shortcuts import render
from django.views.generic import TemplateView
from app.vars import NAME
from django.shortcuts import render, redirect, get_object_or_404
import json
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm
from django.conf import settings

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
    context = {
        'post': post,
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
