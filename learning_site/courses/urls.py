from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    #url(r'^$', views.course_list),
    #url(r'(?P<pk>\d+)/$', views.course_detail),
    path('<course_pk>/t<step_pk>', views.text_detail,
        name='text'),
    path('<course_pk>/q<step_pk>', views.quiz_detail,
        name='quiz'),
    path('<course_pk>/create_quiz', views.quiz_create, name = 'create_quiz'),
    path('<pk>', views.course_detail, name='detail'),
]
