from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(unique = True)
    name = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    size = models.IntegerField()
    description = models.TextField()

    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name