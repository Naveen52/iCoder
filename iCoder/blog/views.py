from blog.templatetags import extras
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from.models import Post, blogComments
# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = blogComments.objects.filter(post=post, parent=None)
    replies = blogComments.objects.filter(post=post).exclude(parent=None)
    replydict = {}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno] = [reply]
        else:
            replydict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'replydict': replydict}
    return render(request, 'blog/blogPost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        post = Post.objects.get(sno=postSno)
        if parentSno == "":
            comment = blogComments(comment=comment, User=user, post=post)
            comment.save()
            messages.success(
                request, "your comments has been successfully added")
        else:
            parent = blogComments.objects.get(sno=parentSno)
            comment = blogComments(
                comment=comment, User=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "your reply has been successfully added")

    return redirect(f"/blog/{post.slug}")
