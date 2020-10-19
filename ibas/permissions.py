from rest_framework import permissions

class IsCourseAdministrator(permissions.BasePermission):
    message = 'you are not a Course Administrator'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_CourseAdministrator = bool("Course Administrator" in user_groups)
        return is_CourseAdministrator

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_CourseAdministrator = bool("Course Administrator" in user_groups)
        return is_CourseAdministrator

class IsEnrolmentClerk(permissions.BasePermission):
    message = 'you are not a Enrolment Clerk'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_EnrolmentClerk = bool("Enrolment Clerk" in user_groups)
        return is_EnrolmentClerk

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_EnrolmentClerk = bool("Enrolment Clerk" in user_groups)
        return is_EnrolmentClerk

class IsHumanResourcesClerk(permissions.BasePermission):
    message = 'you are not a Human Resources Clerk'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_HumanResourcesClerk = bool("Human Resources Clerk" in user_groups)
        return is_HumanResourcesClerk

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_HumanResourcesClerk = bool("Human Resources Clerk" in user_groups)
        return is_HumanResourcesClerk

class IsProgrammeAdministrator(permissions.BasePermission):
    message = 'you are not a Programme Administrator'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_ProgrammeAdministrator = bool("Programme Administrator" in user_groups)
        return is_ProgrammeAdministrator

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_ProgrammeAdministrator = bool("Programme Administrator" in user_groups)
        return is_ProgrammeAdministrator

class IsResearchAdministrator(permissions.BasePermission):
    message = 'you are not a Research Administrator'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_esearchAdministrator = bool("Research Administrator" in user_groups)
        return is_esearchAdministrator

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_esearchAdministrator = bool("Research Administrator" in user_groups)
        return is_esearchAdministrator

class IsStudentSupportClerk(permissions.BasePermission):
    message = 'you are not a Student Support Clerk'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_StudentSupportClerk = bool("Student Support Clerk" in user_groups)
        return is_StudentSupportClerk

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_StudentSupportClerk = bool("Student Support Clerk" in user_groups)
        return is_StudentSupportClerk
