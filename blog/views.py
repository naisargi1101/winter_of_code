from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .forms import CommentForm, PostForm
from .models import Post
from login.models import Profile

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/display_blog.html'

def postDetail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def postSave(request,slug=None):
    context ={}     
    if slug:
        post = get_object_or_404(Post, slug=slug)   
    else:
        post = None  
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("homeUser")
    context['form']= form
    return render(request, "blog/create_blog.html", context)

class profile(generic.ListView):
    queryset = Post.objects.filter(author_id=1).order_by('-created_on')
    template_name = 'blog/profile.html'

