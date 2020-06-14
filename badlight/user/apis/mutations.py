import graphene

from ..services import UserService


class RegisterUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user_id = graphene.String()
    name = graphene.String()
    email = graphene.String()

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, password):
        user = UserService.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password,
        )
        return cls(
            user_id=user.uuid,
            name=user.name,
            email=user.email,
        )
