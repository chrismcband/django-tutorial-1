from django.conf.urls import patterns, url
from signup import views


urlpatterns = patterns('',
    url(r'^$', views.form, name='form'),
    url(r'^questions/(?P<signup_id>\d+)$', views.questions, name='questions'),
    url(r'^thanks$', views.ThanksView.as_view(), name='thanks'),
)
