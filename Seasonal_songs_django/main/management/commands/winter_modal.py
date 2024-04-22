import csv
from django.core.management.base import BaseCommand
from main.models import *
from django.conf import settings

model_name =  Winter_Modal_chart #모델이름을 적어주세요

class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'


    def handle(self, *args, **options):#manage.py 위치에 파일이름을 넣어주세요
        datafile = settings.BASE_DIR /'winter_mt3_final.csv' 
        with open(datafile, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                model_name.objects.create(
                    title=row['title'],
                    singer=row['singer'],
                    years=row['years'],
                )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))
