from ibas.models import Student, Lecturer, Course, Assessment, Result, ResearchTopic, ResearchProject, Issue, \
    Programme, Assignment, Enrolment
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .permissions import IsCourseAdministrator, IsEnrolmentClerk, IsHumanResourcesClerk, IsProgrammeAdministrator, IsResearchAdministrator, IsStudentSupportClerk

from .serializers import StudentSerializer, LecturerSerializer, CourseSerializer, \
    AssessmentSerializer, ResultSerializer, ResearchProjectSerializer, ResearchTopicSerializer, IssueSerializer, \
    ProgrammeSerializer, AssignmentSerializer, EnrolmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'update':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'destroy':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'list':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'retrieve':
            permission = [IsEnrolmentClerk()]
        return permission


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LecturerSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsHumanResourcesClerk()]
        elif self.action == 'update':
            permission = [IsHumanResourcesClerk()]
        elif self.action == 'destroy':
            permission = [IsHumanResourcesClerk()]
        elif self.action == 'list':
            permission = [IsHumanResourcesClerk(), IsProgrammeAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsHumanResourcesClerk(), IsProgrammeAdministrator()]
        return permission


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'update':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'destroy':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'list':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsProgrammeAdministrator()]
        return permission

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssessmentSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsCourseAdministrator()]
        elif self.action == 'update':
            permission = [IsCourseAdministrator()]
        elif self.action == 'destroy':
            permission = [IsCourseAdministrator()]
        elif self.action == 'list':
            permission = [IsCourseAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsCourseAdministrator()]
        return permission

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResultSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsCourseAdministrator()]
        elif self.action == 'list':
            permission = [IsCourseAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsCourseAdministrator()]
        return permission



class ResearchTopicViewSet(viewsets.ModelViewSet):
    queryset = ResearchTopic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResearchTopicSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsResearchAdministrator()]
        elif self.action == 'update':
            permission = [IsResearchAdministrator()]
        elif self.action == 'destroy':
            permission = [IsResearchAdministrator()]
        elif self.action == 'list':
            permission = [IsResearchAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsResearchAdministrator()]
        return permission


class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = ResearchProject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResearchProjectSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsResearchAdministrator()]
        elif self.action == 'destroy':
            permission = [IsResearchAdministrator()]
        elif self.action == 'list':
            permission = [IsResearchAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsResearchAdministrator()]
        return permission

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IssueSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsStudentSupportClerk()]
        elif self.action == 'list':
            permission = [IsStudentSupportClerk()]
        elif self.action == 'retrieve':
            permission = [IsStudentSupportClerk()]
        return permission

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProgrammeSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'update':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'destroy':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'list':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsProgrammeAdministrator()]
        return permission

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssignmentSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'update':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'destroy':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'list':
            permission = [IsProgrammeAdministrator()]
        elif self.action == 'retrieve':
            permission = [IsProgrammeAdministrator()]
        return permission

class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EnrolmentSerializer

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'update':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'destroy':
            permission = [IsEnrolmentClerk()]
        elif self.action == 'list':
            permission = [IsEnrolmentClerk(), IsCourseAdministrator(), IsStudentSupportClerk()]
        elif self.action == 'retrieve':
            permission = [IsEnrolmentClerk(), IsCourseAdministrator(), IsStudentSupportClerk()]
        return permission