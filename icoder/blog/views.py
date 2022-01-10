from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages
from collections import defaultdict
from blog.templatetags import extras

# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts': allPosts}
    # print(allPosts)
    return render(request,'blog/blogHome.html', context)

def blogPost(request, slug):
    post= Post.objects.filter(slug=slug).first()
    if not post: 
        return HttpResponse("404 - Not Foumd")
    print(request.user)

    post.views=post.views+1
    post.save()
    comments=BlogComment.objects.filter(post=post, parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict=defaultdict(list)
    for reply in replies:
        replyDict[reply.parent.sno].append(reply)

    context={'post':post, "comments":comments, "replyDict": replyDict}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST['comment']
        user=request.user
        postSno=request.POST['postSno']
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST["parentSno"]
        if parentSno=="":
            comment=BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request,"Your comment has been posted sucessfully")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request,"Your reply has been posted sucessfully")
        

    return redirect(f"/blog/blogpost/{post.slug}/")


