from django.db import models
from django.conf import settings


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100, unique=True)
    branch_code = models.CharField(max_length=20, unique=True, null=False)

class Scheme(models.Model):
    scheme_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    scheme_evaluation = models.CharField(max_length=100)

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)

class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100, unique=True, null=False)
    sub_code = models.CharField(max_length=20)
    sub_scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sub_credit = models.IntegerField()

class Staff(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    experience = models.IntegerField()
    sub_handling = models.ForeignKey(Subject, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=100)
    stu_sem = models.IntegerField()
    stu_usn = models.CharField(max_length=20, unique=True, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    sec = models.CharField(max_length=2)
    roll_no = models.CharField(max_length=20)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')

class IA_marks(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ia_1_marks = models.DecimalField(max_digits=5, decimal_places=2)
    ia_2_marks = models.DecimalField(max_digits=5, decimal_places=2)
    ia_3_marks = models.DecimalField(max_digits=5, decimal_places=2)
    quiz = models.DecimalField(max_digits=5, decimal_places=2)
    assignment = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
