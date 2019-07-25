import graphene

from graphene_django.types import DjangoObjectType

from webapp.models import Institute, User


class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    allStudents = graphene.List(UserType)

    def resolve_allStudents(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return User.objects.select_related('instituteId').all()