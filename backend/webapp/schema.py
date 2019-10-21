import graphene

from graphene_django.types import DjangoObjectType

from webapp.models import Institute, User, Student

from django.contrib.auth import get_user_model


class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(object):
    allStudents = graphene.List(StudentType)
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return user

    def resolve_allStudents(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Student.objects.select_related('user')
