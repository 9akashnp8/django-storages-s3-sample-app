from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    invoice_doc = models.FileField()