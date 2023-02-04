from django.db import models
from login.models import Profile
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT,default=1)
    #tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)