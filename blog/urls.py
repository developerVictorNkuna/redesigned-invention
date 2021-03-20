from . import views

from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView




urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path(r'graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True))),

    path('detail/<int:pk>/', views.PostDetail.as_view() ,name='post_detail'),
    path('posts/',views.Posts.as_view() ,name='post'),
    path('add_post/',views.AddPostView.as_view() ,name='add_post'),
    path(r'add_category/',views.AddCategory.as_view(),name="add_category"),

    path(r'article/edit/<int:pk>',views.UpdatePostView.as_view(),name="update_post"),
    path(r'article/<int:pk>/remove',views.DeletePost.as_view(),name="delete_post"),
    path('category/<str:category>/',views.CategoryView,name='category '),
    path('about/',views.about,name='about')

] 

