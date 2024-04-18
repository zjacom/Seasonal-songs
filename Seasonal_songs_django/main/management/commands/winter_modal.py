import csv
from django.core.management.base import BaseCommand
from main.models import Winter_Modal_chart

class Command(BaseCommand):
    help = 'Import selected fields from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Winter_Modal_chart.objects.create(
                    title=row['title'],
                    singer=row['singer'],
                    years=row['years'],
                )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))
