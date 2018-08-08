
from django.conf.urls import url
from django.contrib import admin

from myresumeapp.views import HomeView,RegistrationFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RegistrationFormView.as_view()),
    url(r'^home/', HomeView.as_view()),
]
