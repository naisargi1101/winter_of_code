from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .forms import CommentForm, PostForm
from .models import Post
from login.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
class PostList(generic.ListView):
    def get_context_data(self,**kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['userId'] = self.kwargs['userId']
        return context
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 3
    template_name = 'blog/display_blog.html'

def postDetail(request,slug,userId):
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
                                           'comment_form': comment_form,
                                           'userId':userId})

def postSave(request,id=0,userId=None):
    context ={}     
    if id>0:
        post = get_object_or_404(Post, id=id)   
    else:
        post = None  
    form = PostForm(request.POST or None, instance=post, initial={'author': userId})
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profileView",userId)
    context['form']= form
    return render(request, "blog/create_blog.html", context)

class profile(generic.ListView):    
    def get_queryset(self):
        return Post.objects.filter(author_id = self.kwargs['userId']).order_by('-created_on')
    def get_context_data(self,**kwargs):
        context = super(profile, self).get_context_data(**kwargs)
        context['userId'] = self.kwargs['userId']
        return context
    paginate_by = 3
    template_name = 'blog/profile.html'

