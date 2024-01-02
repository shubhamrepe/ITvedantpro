from django.urls import path
from . import views
from .views import sqlVideoCreateView,djangoVideoCreateView,webVideoCreateView,pythonVideoCreateView,djangoVideoListView,webVideoListView,sqlVideoListView,pythonVideoListView
urlpatterns = [
    # Other URL patterns...

    # URL pattern for the login page
    path('student/profile/<int:student_id>/', views.student_profile, name='student_profile'),
    path('student/<int:student_id>/update/', views.update_student, name='update_student'),
    path('adm/', views.admin_portal, name='admin_portal'),
    path('students/', views.student_list, name='student_list'),
    path('professors/',views.professor_list, name='professor_list'),
    path('student/<int:student_id>/',views.student_detail, name='student_detail'),
    path('add_student/',views.add_student, name='add_student'),
    path('update_student/<int:student_id>/',views.update_student, name='update_student'),
    path('remove_student/<int:student_id>/', views.remove_student, name='remove_student'),
    path('add_professor/',views.add_professor, name='add_professor'),
    path('update_professor/<int:professor_id>/', views.update_professor, name='update_professor'),
    path('remove_professor/<int:professor_id>/', views.remove_professor, name='remove_professor'),


    #student
    path('detail/',views.add_student,name='detail'),
    path('signup/',views.student_signup,name='signup'),
    path('slogin/',views.student_login,name='slogin'),
    path('slogout/',views.student_logout,name='slogout'),
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/ds',views.dash,name='dashboard_ds'),
    path('fsd/',views.fsd,name='fsd'),
    path('ds/',views.ds,name='ds'),
    
    
    #video

    path('courses/django/videos',djangoVideoListView.as_view(), name='django-video-list'),
    path('courses/django/upload',djangoVideoCreateView.as_view(), name='django-video-upload'),
    
    path('courses/python/videos',pythonVideoListView.as_view(), name='python-video-list'),
    path('courses/python/upload',pythonVideoCreateView.as_view(), name='python-video-upload'),
    
    path('courses/web/videos',webVideoListView.as_view(), name='web-video-list'),
    path('courses/web/upload',webVideoCreateView.as_view(), name='web-video-upload'),
    
    path('courses/sql/videos',sqlVideoListView.as_view(), name='sql-video-list'),
    path('courses/sql/upload',sqlVideoCreateView.as_view(), name='sql-video-upload'),
    
    #path('courses/<str:course_name>/videos',VideoListView.as_view(), name='video-list'),
    #path('courses/<str:course_name>/upload',VideoCreateView.as_view(), name='video-upload'),
    #Courses 
    path('course/',views.COURSE, name='course_list'),
    path('remove_course/<int:course_id>/', views.remove_course, name='remove_course'),
    path('add_course/',views.add_course, name='add_course'),


    path('quiz/', views.quiz_view, name='quiz'),
    path('evaluate/', views.evaluate_quiz, name='evaluate'),
    path('add/', views.add_question, name='add_question'),
    path('success/', views.success_page, name='success'),

    
    #student payment
    path('spayment/',views.payment_main,name="spayment"),
    path('sucpayment/',views.payment_suc,name='sucpayment'),
]
