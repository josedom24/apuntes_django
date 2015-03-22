from django.conf.urls import patterns,include, url
from partes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html','redirect_field_name':'next'}),
)