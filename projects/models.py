from django.db import models

class Project(models.Model):
    title = models.CharField( max_length=100)
    descrition = models.TextField()
    tecnology = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title