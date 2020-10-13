from rest_framework import routers
from .api import StudentViewSet, LecturerViewSet, CourseViewSet, AssessmentViewSet, ResultViewSet, \
    ResearchTopicViewSet, ResearchProjectViewSet, IssueViewSet, ProgrammeViewSet, AssignmentViewSet, EnrolmentViewSet

router = routers.DefaultRouter()
router.register('api/Student', StudentViewSet, 'Student')
router.register('api/Lecturer', LecturerViewSet, 'Lecturer')
router.register('api/Course', CourseViewSet, 'Course')
router.register('api/Assessment', AssessmentViewSet, 'Assessment')
router.register('api/Result', ResultViewSet, 'Result')
router.register('api/ResearchTopic', ResearchTopicViewSet, 'ResearchTopic')
router.register('api/ResearchProject', ResearchProjectViewSet, 'ResearchProject')
router.register('api/Issue', IssueViewSet, 'Issue')
router.register('api/Programme', ProgrammeViewSet, 'Programme')
router.register('api/Assignment', AssignmentViewSet, 'Assignment')
router.register('api/Enrolment', EnrolmentViewSet, 'Enrolment')

urlpatterns = router.urls
