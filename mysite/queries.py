import graphene
from .types import CommentType, PostType
from blog.models import Comment, Post


class Query(graphene.ObjectType):
    feed = graphene.List(PostType)
    post = graphene.Field(PostType, postId=graphene.String())
    all_authors = graphene.Field(CommentType)
    author = graphene.Field(CommentType, authorId=graphene.String())

    # Resolver for feed field
    def resolve_feed(parent, info):
        return Post.objects.all().order_by('created_at')

    # Resolver for post field
    def resolve_post(parent, info, postId):
        return Post.objects.get(id=postId)

    # Resolver for all_authors field
    def resolve_all_authors(parent, info, postId):
        return Comment.objects.all()

    # Resolver for author field
    def resolve_author(parent, info, authorId):
        return Comment.objects.get(id=authorId)