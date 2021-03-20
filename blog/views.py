from django.views import generic ,View  
# SAME AS from django.views import view


from . models import Post ,Category


from django.shortcuts import render ,redirect ,get_object_or_404

# Create your views here.


from .forms import PostForm ,EditForm

from django.contrib.auth.models import User


class PostList(generic.ListView):
    """this is my home page ,landing page"""
    queryset = Post.objects.filter(publish_status=1).order_by('-created_on')
    template_name = "index.html"
    cats = Category.objects.all()

    def get_context_data(self,*args,**kwargs):
        category_menu = Category.objects.all() #grab everything in our category model
        context = super(PostList,self).get_context_data(*args,**kwargs)
        context["category_menu"] =category_menu
        return context







class PostDetail(generic.DetailView):
    """this one is putitng one blog post on our page"""
    model =Post
    template_name = "post_detail.html"






def CategoryView(request,category):
    """category/name_of_catogry_to_display
    we need to query our database in our class view it was doing for us,
    but in a function i must do iut explicitly"""

    category_post = Post.objects.filter(topic_category=category)
    return render(request, "category.html",{"category":category,"category_post":category_post})


class Posts(generic.CreateView):

    model =Post
    template_name ="post_detail.html"
    context_object_name ="posts"
    fields  = '__all__'  # we can specify  field to be display when adding post =("body","title"),taken from model,py
    # paginate_by = 5


    def get_queryset(request):
        post = Post.objects.filter(publish_status=1).order_by('-created_on')
        return render(request,"post_detail.html",{"post":post})
        
    


class AddPostView(generic.CreateView):
    model =Post
    form_class = PostForm
    template_name ="add_post.html"




class UpdatePostView(generic.UpdateView):
    model =Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields =["title","topic_category","content"]


class DeletePost(generic.DeleteView):


    model =Post
    template_name = "delete_post.html"

class AddCategory(generic.CreateView):
    model = Category
    template_name = "add_category.html"
    fields ='__all__'
    # form_class = PostForm
def about(request):
    return render(request,'about.html')


