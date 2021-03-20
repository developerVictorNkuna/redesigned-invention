import graphene

from graphene_django.types import DjangoObjectType

from blog.models import Post

from .queries import Query
from .mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
