from django.db import models,migrations

# Create your models here.
class ApplicationData(models.Model) :
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    dob = models.DateField()
    relation = models.CharField(max_length=10)
    relativeName = models.CharField(max_length=50)
    relativeSurname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100 , null=True)
    mobile = models.CharField(max_length=15 , null=True)
    declarationPlace = models.CharField(max_length=50)
    declarationDate = models.DateField()