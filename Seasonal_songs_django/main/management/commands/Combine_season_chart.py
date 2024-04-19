import csv
from django.core.management.base import BaseCommand
from main.models import Combine_season_chart
from django.conf import settings


model_name =  Combine_season_chart #모델이름을 적어주세요
class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options): 
        datafile = settings.BASE_DIR /'combined_mt3.csv' #filtered_melon_chart.csv 부분만 수정        
        with open(options['csv_file'], newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                model_name.objects.create(
                    title=row['title'],
                    singer=row['singer'],
                    years=row['combined_years'],
                )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))
