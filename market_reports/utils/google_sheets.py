from market_reports.utils.config import DateFormat, connect_google_sheets
from dotenv import load_dotenv
from market_reports.utils.moysklad import market_costs
from datetime import datetime, timedelta
load_dotenv()


def write_day_reports(sheet, result_costs, date_for_parse, date_):
    search_field = sheet.find(date_.correct_date(date_for_parse, 'google_sheets'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 1, result_costs[0].get('sum'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 2, result_costs[0].get('quantity'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 3, result_costs[1].get('sum'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 4, result_costs[1].get('quantity'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 5, result_costs[2].get('sum'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 6, result_costs[2].get('quantity'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 7, result_costs[3].get('sum'))
    sheet.update_cell(int(search_field.row), int(search_field.col) + 8, result_costs[3].get('quantity'))


def main():
    sheet = connect_google_sheets()
    date_ = DateFormat()
    date_for_parse = datetime.now() + timedelta(days=-1)
    source_costs = ['market_internet', 'market_saratov', 'market_green_house', 'market_moscow_store']
    result_costs = []
    for source in source_costs:
        yesterday = date_.correct_date(date_for_parse, 'moysclad')
        result_costs.append(market_costs(yesterday, yesterday, source))
    write_day_reports(sheet, result_costs, date_for_parse, date_)


if __name__ == '__main__':
    main()
