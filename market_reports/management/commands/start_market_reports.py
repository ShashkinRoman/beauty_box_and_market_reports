from django.core.management.base import BaseCommand
from market_reports.utils.google_sheets import main as google_main


class Command(BaseCommand):
    help = 'load report in google sheets: start_market_reports, -sr -start_report'

    def handle(self, *args, **options):
        google_main()

