from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin
import reminder.views as reminder_views

urlpatterns = [
   url(r'^$', reminder_views.manage),
   url(r'^admin/', admin.site.urls),
   url(r'^del_reminder/', reminder_views.del_reminder),
   url(r'^test_email/', reminder_views.test_email),
   url(r'^secret_trigger/', reminder_views.secret_trigger),
   url(r'^accounts/', include('allauth.urls')),
]