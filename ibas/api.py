from ibas.models import Student, Lecturer, Course, Assessment, Result, ResearchTopic, ResearchProject, Issue, \
    Programme, Assignment, Enrolment
from rest_framework import viewsets, permissions

from .serializers import StudentSerializer, LecturerSerializer, CourseSerializer, \
    AssessmentSerializer, ResultSerializer, ResearchProjectSerializer, ResearchTopicSerializer, IssueSerializer, \
    ProgrammeSerializer, AssignmentSerializer, EnrolmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LecturerSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssessmentSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResultSerializer


class ResearchTopicViewSet(viewsets.ModelViewSet):
    queryset = ResearchTopic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResearchTopicSerializer


class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = ResearchProject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResearchProjectSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IssueSerializer


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProgrammeSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssignmentSerializer


class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EnrolmentSerializer
