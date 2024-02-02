from django.shortcuts import get_object_or_404, redirect
from account.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def delete_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if post.author == request.user:
        post.delete()
        return redirect('profile')