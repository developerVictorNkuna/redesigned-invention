

from django.db import models

from django.conf  import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core import serializers
from django.urls  import reverse


"""we are going to create a comment model for our database"""










class Category(models.Model):
    """this a category of topic"""

    name = models.CharField(max_length=255)


    def __str__(self):
        """this meta data to tel django that  the title ought to be a string"""
        return self.name 

    def get_absolute_url(self):
        """this id,is the primary key =pk,this abs url will direct to post_detai;"""

        # return reverse ("home",args=(str(self.id)))
        return reverse('home')







STATUS =(
    (0,"Draft"), 
    (1,"Publish")
)




class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=False)
    topic_category=models.CharField(max_length=200, default="uncategorized")
    content   =models.TextField()
    email = models.EmailField()
    created_on =models.DateField(default=timezone.now,blank=True)
    updated_on =models.DateTimeField(auto_now=True)
    publish_status = models.IntegerField(choices=STATUS,default=0)
    published_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        """this meta data to tel django that  the title ought to be a string"""
        return self.title + "|" + str(self.author)


    def get_absolute_url(self):
        """this id,is the primary key =pk,this abs url will direct to post_detai;"""

        # return reverse ("home",args=(str(self.id)))
        return reverse('home')





    class Meta:
        ordering =['-created_on']


    """ below are the methods,behaviour of my objbect,my POST MODEL OBJECT MUST
    ALLOW THE USER TO PUBLISH, TO COMMNT,D ON POST"""



    




    def publish(self):
        """this will publish the Post in the Post data  obejct model to put in the Post table"""
        self.published_date = timezone.now()
        self.save() 


    

    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering =['-created_on']


    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)
