import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        only_fields = [
            "email",
        ]

    id = graphene.String()
    name = graphene.String()

    @staticmethod
    def resolve_id(parent, info):
        return parent.uuid

    @staticmethod
    def resolve_name(parent, info):
        return parent.name
