import graphene

from graphene_django.types import DjangoObjectType

from webapp.models import Student, User


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    allStudents = graphene.List(StudentType)

    def resolve_allStudents(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Student.objects.all()