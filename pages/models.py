from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=256)
    found_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")
    date_applied = models.DateField(auto_now_add=True)
    site_url = models.URLField(default="https://www.indeed.com/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])