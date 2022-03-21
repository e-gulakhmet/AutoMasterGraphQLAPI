import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType, ObjectType

from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        user_id = kwargs.get('id')
        if user_id is None:
            return None
        return User.objects.get(pk=user_id)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    email = graphene.String()
    password = graphene.String()

    first_name = graphene.String()
    second_name = graphene.String()
    middle_name = graphene.String()
    car_model = graphene.String()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserInput(required=True)

    @staticmethod
    def mutate(info, input: UserInput):
        instance = get_user_model()(email=input.email, first_name=input.first_name, second_name=input.second_name,
                                    middle_name=input.middle_name, car_model=input.car_model)

        instance.set_password(input.password)
        return CreateUser(user=instance)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input):
        try:
            instance = User.objects.get(pk=id)
        except User.DoesNotExist:
            return UpdateUser(user=None)

        instance.first_name = input.first_name
        instance.second_name = input.second_name
        instance.middle_name = input.middle_name
        instance.car_model = input.car_model
        instance.save()

        return UpdateUser(ok=True, user=instance)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
