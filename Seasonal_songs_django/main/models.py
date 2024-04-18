from django.db import models

# Create your models here.
class Modal_chart(models.Model):
    class Meta:
        db_table = 'modal_chart'
        
    title = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    chartin_counts = models.IntegerField()