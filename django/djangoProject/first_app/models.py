from django.db import models
from django.utils import timezone
# Create your models here.


class first_model(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name