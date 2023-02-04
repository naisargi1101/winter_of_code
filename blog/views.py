from django.shortcuts import render,redirect
from django.views import generic
from .forms import PostForm
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/display_blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def postSave(request):
    context ={}    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homeUser")
    else:
        form = PostForm()
    context['form']= form
    return render(request, "blog/create_blog.html", context)
