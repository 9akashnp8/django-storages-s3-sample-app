from django.db import models

# Helpers
def invoice_storage_path(instance, filename):
    from datetime import datetime
    TODAY = datetime.now()
    YEAR = TODAY.strftime('%Y')
    MONTH = TODAY.strftime('%B')
    return f'{YEAR}/{MONTH}/{instance.invoice_number}-{filename}'

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)
    invoice_doc = models.FileField(upload_to=invoice_storage_path)