#from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from task.views import GenerateRandomUserView, UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('generate/', GenerateRandomUserView.as_view(), name='generate')

]