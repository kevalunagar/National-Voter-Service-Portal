from django.db import models

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to="forms")


    def __str__(self):
        return self.title
