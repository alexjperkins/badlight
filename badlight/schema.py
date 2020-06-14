import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .app import _VERSION
from .user.apis import RegisterUser, GetUser


class Mutations(graphene.ObjectType):
    # users
    register_user = RegisterUser.Field()


class Query(GetUser,):
    # __internal__
    node = relay.Node.Field()
    version = graphene.String(name=graphene.String())

    @staticmethod
    def resolve_version(parent, info):
        return _VERSION


schema = graphene.Schema(query=Query, mutation=Mutations)
