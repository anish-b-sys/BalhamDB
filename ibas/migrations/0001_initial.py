# Generated by Django 3.0.8 on 2020-10-20 02:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('AssessmentID', models.AutoField(primary_key=True, serialize=False)),
                ('AssessmentNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('AssessmentName', models.TextField(max_length=30)),
                ('Type', models.CharField(choices=[('Assignment', 'Assignment'), ('Written Test', 'Written Test'), ('Practical Test', 'Practical Test'), ('Final Exam', 'Final Exam')], max_length=14)),
                ('Weighting', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(10)])),
                ('MaximumMark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=40)),
                ('Credits', models.IntegerField(validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(5)])),
                ('Fee', models.FloatField(validators=[django.core.validators.MaxValueValidator(8000), django.core.validators.MinValueValidator(200)])),
                ('Status', models.CharField(choices=[('Current', 'Current'), ('Suspended', 'Suspended')], max_length=9)),
                ('Programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Programme')),

            ],
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('EnrolmentID', models.AutoField(primary_key=True, serialize=False)),
                ('Level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(2018)])),
                ('Semester', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Complete', 'Complete')], max_length=8)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('LecturerID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('StreetAddress', models.CharField(max_length=50)),
                ('Suburb', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=25)),
                ('EmailAddress', models.EmailField(blank=True, max_length=30, null=True)),
                ('PhoneNumber', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Ranking', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('Type', models.CharField(choices=[('Academic', 'Academic'), ('Contract', 'Contract')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('ProgrammeID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgrammeName', models.TextField(max_length=25)),
                ('Level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='ResearchTopic',
            fields=[
                ('ResearchTopicID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.TextField(max_length=40)),
                ('Impact', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('StreetAddress', models.CharField(max_length=50)),
                ('Suburb', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=25)),
                ('EmailAddress', models.EmailField(blank=True, max_length=30, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=16, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Status', models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('ResultID', models.AutoField(primary_key=True, serialize=False)),
                ('ResultDate', models.DateField()),
                ('Mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
                ('Assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Assessment')),
                ('Enrolment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Enrolment')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('ResearchProjectID', models.AutoField(primary_key=True, serialize=False)),
                ('Output', models.TextField(max_length=30)),
                ('Description', models.TextField(max_length=40)),
                ('StartDate', models.DateField()),
                ('Lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Lecturer')),
                ('ResearchTopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.ResearchTopic')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('IssueID', models.AutoField(primary_key=True, serialize=False)),
                ('IssueDescription', models.TextField(max_length=40)),
                ('IssueDate', models.DateField()),
                ('ActionTaken', models.TextField(max_length=20)),
                ('Enrolment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Enrolment')),
            ],
        ),
        migrations.AddField(
            model_name='enrolment',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='Programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Programme'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('AssignmentID', models.AutoField(primary_key=True, serialize=False)),
                ('Role', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary')], max_length=9)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Course')),
                ('Lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Lecturer')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ibas.Course'),
        ),
    ]
