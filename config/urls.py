from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
]