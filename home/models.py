from django.db import models

# Create your models here.
class ShortName(models.Model):
    short_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.short_name
    
    
