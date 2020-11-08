import os
import requests
from dotenv import load_dotenv
load_dotenv()


def market_costs(start_date, end_date, store):
    """
    :param start_date: 2020-09-23 will be + 00:00:00
    :param end_date: 2020-09-23 will be 23:59:59
    :param store: market_moscow_store, market_green_house, market_saratov, market_internet
    :return: [{'store': moscow, 'quantity': 7, 'sum': 123123.0, 'date': 'start_date, end_date'}
    """
    headers = {
        "Content-Type": "application/json",
        # "Lognex-Pretty-Print-JSON": "true",
        "charset": "UTF-8"
    }
    store_ = os.getenv(store)
    auth = (os.getenv('market_moysclad_login'), os.getenv('market_moysclad_pass'))
    info_about_costs = {'store': store,
                        'quantity': 0,
                        'sum': 0,
                        'date': (start_date, end_date)}
    if store != 'market_internet':
        request_url = f"https://online.moysklad.ru/api/remap/1.2/report/sales/plotseries?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:59&interval=day&filter=retailStore=https://online.moysklad.ru/api/remap/1.2/entity/retailstore/{store_}"
        response = requests.get(request_url, auth=auth, headers=headers)
        stock = response.json()
        series = stock.get('series')
        for day in series:
            info_about_costs['quantity'] += day.get('quantity')
            info_about_costs['sum'] += day.get('sum') / 100
    if store == 'market_internet':
        request_url = f'https://online.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:59&interval=day&filter=project=https://online.moysklad.ru/api/remap/1.2/entity/project/{store_}'
        response = requests.get(request_url, auth=auth, headers=headers)
        stock = response.json()
        rows = stock.get('rows')
        for row in rows:
            info_about_costs['quantity'] += row.get('salesCount')
            info_about_costs['sum'] += row.get('sellSum') / 100
    return info_about_costs
