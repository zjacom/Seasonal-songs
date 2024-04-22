import csv
from django.core.management.base import BaseCommand
from main.models import *
from django.conf import settings

model_name =  Spring_Modal_chart #모델이름을 적어주세요

class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR /'spring_mt3_final.csv' #'filtered_melon_chart.csv' 부분만 수정        
        with open(datafile, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:#모델이름에 맞춰서 칼럼명 반드시 수정해주세요
                model_name.objects.create(
                    title=row['title'],
                    singer=row['singer'],
                    years=row['years'],
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