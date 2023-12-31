from django.db import models
from django.contrib.auth.models import UserManager,User
from django.urls import reverse

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_choices = [
        ('Data Science', 'Data Science'),
        ('Full stack', 'Full stack'),
    ]
    id =models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    course_enrolled = models.CharField(max_length=20, choices=course_choices)
    dob = models.DateField()
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=50)
    upload_resume = models.FileField(upload_to='resumes/')
    photo = models.ImageField(upload_to='photos/')
    signature = models.ImageField(upload_to='signatures/')
    branch_location = [
        ('', 'Select Branch Location'),
        ('Borivali', 'Borivali'),
        ('Andheri', 'Andheri'),
        ('Malad', 'Malad'),
    ]
    branch_location = models.CharField(max_length=50, choices=branch_location, default='')
    password = models.CharField(max_length=128, default='')
    
    def get_dashboard_url(self):
        return reverse('dashboard',kwargs={'pk':self.pk})


class Professor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField(default=0)
    courses_teaching = models.CharField(max_length=50,default="")
    photo = models.ImageField(upload_to='professor_photos/')
    branch_location = [
        ('', 'Select Branch Location'),
        ('Borivali', 'Borivali'),
        ('Andheri', 'Andheri'),
        ('Malad', 'Malad'),
    ]
    branch_location = models.CharField(max_length=50, choices=branch_location, default='')

class BranchManager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    branch_location = [
        ('', 'Select Branch Location'),
        ('Borivali', 'Borivali'),
        ('Andheri', 'Andheri'),
        ('Malad', 'Malad'),
    ]
    number = models.IntegerField(default=0)
    branch_location = models.CharField(max_length=50, choices=branch_location, default='')
    photo = models.ImageField(upload_to='manager_photos/')


#student
    
class studentlog(models.Model):
    username=models.CharField(max_length=254,primary_key=True,default="")
    password=models.CharField(max_length=100)


#dashboard videos

class Course(models.Model):
    id=models.AutoField(primary_key = True)
    name = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    title=models.CharField(max_length=250)
    video_file = models.FileField(upload_to='video/')
    e_book = models.FileField(upload_to='e_books/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
#quiz

class Question(models.Model):
    text = models.CharField(max_length=200)

    def _str_(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def _str_(self):
        return self.text
    