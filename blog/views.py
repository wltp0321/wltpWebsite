from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden
import re
import markdown

def replace_checkboxes(html):
    # 체크된 박스 (disabled + checked) → ✅
    html = re.sub(
        r'<input[^>]*type=["\']checkbox["\'][^>]*disabled[^>]*checked[^>]*\/?>',
        '✅',
        html,
        flags=re.IGNORECASE
    )
    # 체크 안 된 박스 (disabled, checked 없는) → ⬛
    html = re.sub(
        r'<input[^>]*type=["\']checkbox["\'][^>]*disabled(?![^>]*checked)[^>]*\/?>',
        '⬛',
        html,
        flags=re.IGNORECASE
    )
    return html


def is_staff(user):
    return user.is_staff

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_delete_confirm.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.select_related('author').all()

    raw_html = markdown.markdown(
        post.content,
        extensions=[
            'fenced_code',
            'codehilite',
            'tables',
            'pymdownx.tilde',
            'pymdownx.tasklist',
        ],
        extension_configs={
            'pymdownx.tasklist': {'custom_checkbox': False}
        }
    )
    content = replace_checkboxes(raw_html)

    # 댓글 폼 등 컨텍스트 넣기
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'formatted_markdown': content,  # 템플릿 변수 이름과 맞춰주세요
    })


@login_required
def like_post(request, pk):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        data = {
            'liked': liked,
            'total_likes': post.likes.count(),
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
@user_passes_test(lambda u: u.is_staff)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=pk)
    return redirect('blog:post_detail', pk=pk)

@login_required
def add_reply(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    parent_comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.parent = parent_comment
            reply.author = request.user
            reply.save()
            return redirect('blog:post_detail', pk=post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_reply.html', {'form': form, 'post': post, 'parent': parent_comment})

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form, 'comment': comment})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        return redirect('blog:post_detail', pk=post_pk)
    return render(request, 'blog/comment_delete_confirm.html', {'comment': comment})
