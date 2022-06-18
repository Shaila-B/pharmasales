from django.db import models


# Create your models here.
class PharmaSales(models.Model):
    pharmasale_id = models.IntegerField(default=0)
    date = models.DateField()
    year = models.IntegerField()
    atc_code = models.FloatField()
    atc_classification = models.CharField(max_length=200)
    drug_classification = models.CharField(max_length=200)


class DrugReview(models.Model):
    drug_id = models.IntegerField(default=0)
    condition = models.CharField(max_length=300)
    date = models.DateField()
    drug_name = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    review = models.TextField()
    unique_id = models.IntegerField(default=0)
    useful_count = models.IntegerField(default=0)
