
from django.conf.urls import patterns, include, url
from myloginsystem.views import *
from django.core.urlresolvers import reverse
from django.contrib.auth import views as auth_views
 
urlpatterns = patterns('',
#    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', launch_page),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/(?P<slug>[\-\w]+)/$', UpdateProfile.as_view(), name='update_user'),
    url(r'^home/$', home, name = "home"),
    url(r'^changepassword/$', auth_views.password_change,{'template_name':'changepassword.html', 'post_change_redirect' : 'myloginsystem/password/change/done' } ),
    url(r'^password/change/done/$',auth_views.password_change_done, name='password_change_done'),
)
