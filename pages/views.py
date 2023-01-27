from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Job


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class JobPageView(ListView):
    template_name = "pages/jobs.html"
    model = Job
    context_object_name = "jobs"


class JobDetailView(DetailView):
    template_name = 'pages/job_detail.html'
    model = Job


class JobUpdateView(UpdateView):
    template_name = 'pages/job_update.html'
    model = Job
    fields = "__all__"


class JobCreateView(CreateView):
    template_name = 'pages/job_create.html'
    model = Job
    fields = "__all__"


class JobDeleteView(DeleteView):
    template_name = "pages/job_delete.html"
    model = Job
    success_url = reverse_lazy("jobs")

