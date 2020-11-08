import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()


def connect_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('market_json_keyfile'), scope)
    client = gspread.authorize(creds)
    sheet = client.open(os.getenv('market_name_sheet')).sheet1
    return sheet


class DateFormat:
    def __init__(self):
        self.yesterday = datetime.now() + timedelta(days=-1)
        self.today = datetime.now()
        self.tomorrow = datetime.now() + timedelta(days=+1)

    def correct_date(self, day, for_what):
        """for_what: yesterday, today, tomorrow or 2020-11-03"""
        if for_what == 'google_sheets':
            if day == 'yesterday':
                yesterday_correct = datetime.strftime(self.yesterday, '%d.%m.%Y')
                return yesterday_correct
            if day == 'today':
                today_correct = datetime.strftime(self.today, '%d.%m.%Y')
                return today_correct
            if day == 'tomorrow':
                tomorrow_correct = datetime.strftime(self.tomorrow, '%d.%m.%Y')
                return tomorrow_correct
            if type(day) == datetime:
                day_correct = datetime.strftime(day, '%d.%m.%Y')
                return day_correct
        if for_what == 'moysclad':
            if day == 'yesterday':
                yesterday_correct = datetime.strftime(self.yesterday, '%Y-%m-%d')
                return yesterday_correct
            if day == 'today':
                today_correct = datetime.strftime(self.today, '%Y-%m-%d')
                return today_correct
            if day == 'tomorrow':
                tomorrow_correct = datetime.strftime(self.tomorrow, '%Y-%m-%d')
                return tomorrow_correct
            if type(day) == datetime:
                day_correct = datetime.strftime(day, '%Y-%m-%d')
                return day_correct
