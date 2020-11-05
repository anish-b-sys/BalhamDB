from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db import models

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30, null=False, blank=False)
    LastName = models.CharField(max_length=30, null=False, blank=False)
    StreetAddress = models.CharField(max_length=50, null=False, blank=False)
    Suburb = models.CharField(max_length=20, null=False, blank=False)
    City = models.CharField(max_length=25, null=False, blank=False)
    EmailAddress = models.EmailField(max_length=30, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=16, validators=[MinLengthValidator(7)], null=False, blank=False)
    statusList = (
        ('Part-Time', 'Part-Time'),
        ('Full-Time', 'Full-Time'),
    )
    Status = models.CharField(max_length=9, choices=statusList, null=False, blank=False)


class Lecturer(models.Model):
    LecturerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30, null=False, blank=False)
    LastName = models.CharField(max_length=30, null=False, blank=False)
    StreetAddress = models.CharField(max_length=50, null=False, blank=False)
    Suburb = models.CharField(max_length=20, null=False, blank=False)
    City = models.CharField(max_length=25, null=False, blank=False)
    EmailAddress = models.EmailField(max_length=30, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=16, validators=[MinLengthValidator(7)], null=False, blank=False)
    rankingList = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    Ranking = models.CharField(max_length=1, choices=rankingList, null=False, blank=False)
    TypeList = (
        ('Academic', 'Academic'),
        ('Contract', 'Contract'),
    )
    Type = models.CharField(max_length=8, choices=TypeList, null=False, blank=False)

class ResearchTopic(models.Model):
    ResearchTopicID = models.AutoField(primary_key=True)
    Description = models.TextField(max_length=40, null=False, blank=False)
    impactList = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    Impact = models.CharField(max_length=6, choices=impactList, null=False, blank=False)

class ResearchProject(models.Model):
    ResearchProjectID = models.AutoField(primary_key=True)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, to_field='LecturerID', null=False, blank=False)
    ResearchTopic = models.ForeignKey(ResearchTopic, on_delete=models.CASCADE, to_field='ResearchTopicID', null=False,
                                      blank=False)
    Output = models.TextField(max_length=30, null=False, blank=False)
    Description = models.TextField(max_length=40, null=False, blank=False)
    StartDate = models.DateField(null=False, blank=False)

class Programme(models.Model):
    ProgrammeID = models.AutoField(primary_key=True)
    ProgrammeName = models.TextField(max_length=25, null=False, blank=False)
    Level = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], null=False, blank=False)

class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=40, null=False, blank=False)
    Credits = models.IntegerField(validators=[MaxValueValidator(120), MinValueValidator(5)], null=False, blank=False)
    Fee = models.FloatField(validators=[MaxValueValidator(8000), MinValueValidator(200)], null=False, blank=False)
    statusList = (
        ('Current', 'Current'),
        ('Suspended', 'Suspended'),
    )
    Status = models.CharField(max_length=9, choices=statusList, null=False, blank=False)
    Programme = models.ForeignKey(Programme, on_delete=models.CASCADE, to_field='ProgrammeID', null=False, blank=False)


class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='CourseID', null=False, blank=False)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, to_field='LecturerID', null=False, blank=False)
    roleList = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
    )
    Role = models.CharField(max_length=9, choices=roleList, null=False, blank=False)

class Assessment(models.Model):
    AssessmentID = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='CourseID', null=False, blank=False)
    AssessmentNumber = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False,
                                           blank=False)
    AssessmentName = models.TextField(max_length=30, null=False, blank=False)
    typeList = (
        ('Assignment', 'Assignment'),
        ('Written Test', 'Written Test'),
        ('Practical Test', 'Practical Test'),
        ('Final Exam', 'Final Exam'),
    )
    Type = models.CharField(max_length=14, choices=typeList, null=False, blank=False)
    Weighting = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(10)], null=False, blank=False)
    MaximumMark = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(50)], null=False,
              blank=False)

class Enrolment(models.Model):
    EnrolmentID = models.AutoField(primary_key=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='StudentID', null=False, blank=False)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='CourseID', null=False, blank=False)
    Year = models.IntegerField(validators=[MaxValueValidator(2050), MinValueValidator(2018)], null=False, blank=False)
    Semester = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)], null=False, blank=False)
    statusList = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Complete', 'Complete'),
    )
    Status = models.CharField(max_length=8, choices=statusList, null=False, blank=False)
class Issue(models.Model):
    IssueID = models.AutoField(primary_key=True)
    IssueDescription = models.TextField(max_length=40, null=False, blank=False)
    IssueDate = models.DateField(null=False, blank=False)
    ActionTaken = models.TextField(max_length=20, null=False, blank=False)
    Enrolment = models.ForeignKey(Enrolment, on_delete=models.CASCADE, to_field='EnrolmentID', null=False, blank=False)

class Result(models.Model):
    ResultID = models.AutoField(primary_key=True)
    Assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, to_field='AssessmentID', null=False,
                                   blank=False)
    Enrolment = models.ForeignKey(Enrolment, on_delete=models.CASCADE, to_field='EnrolmentID', null=False, blank=False)
    ResultDate = models.DateField(null=False, blank=False)
    Mark = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(0)], null=False, blank=False)




