import uuid
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.TextField(blank=True)
    consent = models.BooleanField(default=True)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField(help_text="Use {{name}} where customer name should appear")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


# Create your models here.
