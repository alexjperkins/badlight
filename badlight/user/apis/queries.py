import graphene

from .types import User
from ..services import UserService


class GetUser(graphene.ObjectType):
    user = graphene.Field(User, uuid=graphene.String(required=True))

    @staticmethod
    def resolve_user(parent, info, uuid):
        return UserService.get_user_by_uuid(uuid=uuid)
