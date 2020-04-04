from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from post.models import Post
from post.forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def post_index(request):
    post_list = Post.objects.all().exclude(active=False).order_by('id')
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 10)  # Her sayfada 5 tane gözükecek

    page = request.GET.get('sayfa')
    posts = paginator.get_page(page)
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'post/detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)


@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')
