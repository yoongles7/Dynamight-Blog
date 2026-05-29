from django.db import models

class Details(models.Model):
    age = models.CharField(max_length=200)
    
    def __str__(self):
        return self.age