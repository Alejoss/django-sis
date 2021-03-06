from django.conf.urls import *
from ecwsp.admissions import views
from responsive_dashboard.views import generate_dashboard
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    (r'^$', generate_dashboard, {'app_name': 'admissions'}),
    (r'^applicants_to_students/(?P<year_id>\d+)/$', views.applicants_to_students),
    (r'^ajax_check_duplicate_applicant/(?P<fname>[A-z]+)/(?P<lname>[A-z]+)/$', views.ajax_check_duplicate_applicant),
    (r'^reports/$', views.reports),
    (r'^reports/funnel/$', views.funnel),
    (r'^inquiry_form/$', views.inquiry_form),
    url(r'^custom-application-editor/', 
        TemplateView.as_view(template_name='admissions/custom_application_editor.html'), 
        name="custom-application-editor"
        ),
    url(r'^application/(?P<pk>\d+)/$', 
        TemplateView.as_view(template_name='admissions/review_student_application.html'), 
        name="review-student-application",
        ),
    url(r'^application/', 
        TemplateView.as_view(template_name='admissions/student_application.html'), 
        name="student-application"
        ),
)
