import graphene
from graphene_django import DjangoObjectType, DjangoListField
from blog.models import Comment, Post


    
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id","author", "title", "slug","topic_category","content",  "created_on","updated_on","publish_status","published_date")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id","post", "name", "email","body","created_on","active")

    posts = DjangoListField(PostType)


    def resolve_posts(self, info):
        return Post.objects.filter(author=self.id)

class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    post = graphene.String()



class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    created_on = graphene.Date()
    author_id = graphene.String(required=True, name="author")

