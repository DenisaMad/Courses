from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('O', 'Open'),
        ('C', 'Completed'),
        ('IP','In Progress'),
    ]
    
    TYPE_CHOICES = [
        ('B', 'Business'),
        ('D', 'Diplomacy'),
        ('L', 'Leadership'),
        ('T','Trolling'),
    ]

    title=models.CharField(null=False , blank=False, unique=True,max_length=50)
    content=models.CharField(null=False, blank=False,unique=True, max_length=200)
    status=models.CharField(null=False, blank=False, choices=STATUS_CHOICES, max_length=20)
    type=models.CharField(null=False, blank=False, choices=TYPE_CHOICES,max_length=20)
    due_date=models.DateField(null=False, blank=False)
    create_date=models.DateField(null=False, blank=False)