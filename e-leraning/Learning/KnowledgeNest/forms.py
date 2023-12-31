from django import forms
from django.forms import ModelForm
from .models import Course, Student, Professor, BranchManager,Video,Course
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput, TextInput,Textarea

class StudentForm(ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Insert DOB from the calendar (format: YYYY-MM-DD)'
    )
    
    class Meta:
        model = Student
        fields = ['name', 'middle_name', 'last_name', 'qualification', 'course_enrolled', 'dob',
                  'address', 'email', 'phone_number', 'nationality', 'upload_resume',
                  'photo', 'signature', 'branch_location', 'password']
        
        
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'email', 'courses_teaching', 'photo', 'branch_location']

class BranchManagerForm(forms.ModelForm):
    class Meta:
        model = BranchManager
        fields = ['name', 'email', 'branch_location', 'photo']

#signup & login

class StudentLoginForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    qualification = forms.CharField(max_length=100,required=True)
    course_enrolled = forms.ChoiceField( choices=[('Data Science', 'Data Science'),('Full stack', 'Full stack'),], required=True)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1970,2023)),required=False)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(widget=forms.EmailInput,required=True)
    phone_number = forms.CharField(max_length=15,required=True)
    nationality = forms.CharField(max_length=50, required=True)
    upload_resume = forms.FileField(widget=forms.FileInput)
    photo = forms.ImageField(widget=forms.FileInput)
    signature = forms.ImageField(widget=forms.FileInput)
    branch_location = forms.ChoiceField( choices=[('', 'Select Branch Location'),('Borivali', 'Borivali'),('Andheri', 'Andheri'),('Malad', 'Malad'),], required=True)
    class meta:
        model = Student
        fields = ['username','password1','password2','name', 'middle_name', 'last_name', 'qualification', 'course_enrolled', 'dob',
                  'address', 'email', 'phone_number', 'nationality', 'upload_resume',
                  'photo', 'signature', 'branch_location']
        
    def save(self, commit=True):
        user= super(StudentLoginForm, self).save(commit=False)
        user_profile = Student(name=self.cleaned_data['name'], 
                               middle_name=self.cleaned_data['middle_name'],
                               last_name=self.cleaned_data['last_name'],
                               qualification=self.cleaned_data['qualification'],
                               course_enrolled=self.cleaned_data['course_enrolled'],
                               dob=self.cleaned_data['dob'],
                               address=self.cleaned_data['address'],
                               email=self.cleaned_data['email'],
                               phone_number=self.cleaned_data['phone_number'],
                               nationality=self.cleaned_data['nationality'],
                               upload_resume=self.cleaned_data['upload_resume'],
                               photo=self.cleaned_data['photo'],
                               signature=self.cleaned_data['signature'],
                               branch_location=self.cleaned_data['branch_location'],)
        if commit:
            user.save()
            user_profile.user = user
            user_profile.save()
        return user, user_profile
        
        
#video upload
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file','e_book']

from django.forms import formset_factory

class QuestionForm(forms.Form):
    text = forms.CharField(label='Question', max_length=200)
    choice1 = forms.CharField(label='Choice 1', max_length=200)
    choice2 = forms.CharField(label='Choice 2', max_length=200)
    choice3 = forms.CharField(label='Choice 3', max_length=200)
    choice4 = forms.CharField(label='Choice 4', max_length=200)
    correct_choice = forms.ChoiceField(
        label='Correct Choice',
        choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')]
    )

QuestionFormSet = formset_factory(QuestionForm, extra=1)