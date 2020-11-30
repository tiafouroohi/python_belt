from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("success", views.success),
    path("edit_job/<int:job_id>", views.edit_job),
    path("process_edit_a_job", views.process_edit_a_job),
    path("job_details/<int:job_id>", views.job_details),
    path("create_a_job", views.create_a_job),
    path("process_create_a_job",views.process_create_a_job),
    path("destroy/<int:job_id>",views.destroy),
    path("logout", views.logout)
]
