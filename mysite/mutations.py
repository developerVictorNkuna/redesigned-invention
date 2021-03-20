import graphene
from .types import CommentType, PostType ,PostInput,AuthorInput
from blog.models import Comment, Post


class AddPost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)

    post = graphene.Field(PostType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddPost(post=None)
        _post = Post.objects.create(**input)
        return AddPost(post=_post)


class AddAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    author = graphene.Field(CommentType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddAuthor(author=None)
        _author = Comment.objects.create(**input)
        return AddAuthor(author=_author)

class Mutation(graphene.ObjectType):
    add_post = AddPost.Field()
    add_author = AddAuthor.Field()