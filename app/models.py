from django.db import models

class Detail(models.Model):
    detail = models.JSONField(default=dict)
    
    def __str__(self):
        return str(self.detail)