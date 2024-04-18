import csv
from django.core.management.base import BaseCommand
from main.models import *
from django.conf import settings


class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR /'all_song_filter.csv' #filtered_melon_chart.csv 부분만 수정        
        with open(options['csv_file'], newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                All_chart.objects.create(
                    rank  =row['rank'],                                         
                    title=row['title'],
                    singer=row['singer'],
                    year =row['year'],
                    date = row['date'],
                    month = row['month'], 
                    day = row['day'], 
                    week = row['week'],
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