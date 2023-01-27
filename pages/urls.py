from django.urls import path

from .views import (
    HomePageView,
    JobPageView,
    JobCreateView,
    JobDeleteView,
    JobDetailView,
    JobUpdateView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("jobs/", JobPageView.as_view(), name="jobs"),
    path("jobs/<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("jobs/create/", JobCreateView.as_view(), name="job_create"),
    path("jobs/<int:pk>/update/", JobUpdateView.as_view(), name="job_update"),
    path("jobs/<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
]
