from django.db import models

# Create your models here.

class product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='prod/images')
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    price=models.IntegerField()

    def __str__(self):
        return self.name
