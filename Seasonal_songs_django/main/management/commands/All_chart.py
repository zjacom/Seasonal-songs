import csv
from django.core.management.base import BaseCommand
from main.models import *
from django.conf import settings
from datetime import datetime


class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'

    def handle(self, *args, **options):#chart_in_mt3_all.csv 부분만 수정
        datafile = settings.BASE_DIR /'chart_in_mt3_all.csv'         
        with open(datafile, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                All_chart.objects.create(
                    rank  =row['rank'],                                         
                    title=row['title'],
                    singer=row['singer'],
                    year =row['year'],
                    date = row['date'] , 
                    month = row['month'], 
                    day = row['day'], 
                    week = row['week'],
                    season = row['season'],
                )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))

'''rank = models.IntegerField()    
    title = models.CharField(max_length=100, default='')
    singer = models.CharField(max_length=100, default='')
    years = models.CharField(max_length=100, default='')
    date = models.DateField()
    month = models.IntegerField() 
    day = models.IntegerField() 
    week = models.IntegerField()
'''