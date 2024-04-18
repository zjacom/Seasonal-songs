from django.db import models

# Create your models here.
class Spring_Modal_chart(models.Model):
    class Meta:
        db_table = 'spring_modal_chart'
        
    title = models.CharField(max_length=100, default='')
    singer = models.CharField(max_length=100, default='')
    years = models.CharField(max_length=100, default='')


class Winter_Modal_chart(models.Model):
    class Meta:
        db_table = 'winter_modal_chart'
        
    title = models.CharField(max_length=100, default='')
    singer = models.CharField(max_length=100, default='')
    years = models.CharField(max_length=100, default='')
    
class All_chart(models.Model):
    class Meta:
        db_table = 'All_chart'
        
    rank = models.IntegerField()    
    title = models.CharField(max_length=100, default='')
    singer = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    date = models.DateField()
    month = models.IntegerField() 
    day = models.IntegerField() 
    week = models.IntegerField()
    season = models.IntegerField() 
		

class Combine_season_chart(models.Model):
    class Meta:
        db_table = 'Combine_season_chart'
        
    title = models.CharField(max_length=100, default='')    
    singer = models.CharField(max_length=100, default='')
    years = models.CharField(max_length=100, default='')