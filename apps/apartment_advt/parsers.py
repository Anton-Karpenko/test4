import json
from time import sleep

import requests
from django.conf import settings

from apps.apartment_advt.models import ApartmentAdvt


class DomRiaParser:
    items = ('title', 'checkup_id', 'price', 'num_of_rooms', 'district', 'description')

    BASE_URL = f"https://developers.ria.com/dom/search?category=1&realty_type=2&operation_type=3&" \
        f"state_id=10&city_id=10&fullCategoryOperation=1_2_3&api_key={settings.DOM_RIA_TOKEN}"

    def __init__(self, params=None):
        self.downloaded = 0
        self.params = params or {}

    def parse(self):
        current_page = 0
        while True:
            items, count = self.get_items(current_page)
            advertises = list()
            for item in items:
                item_content = self.get_detail_item(item)
                params = self.gather_params(item_content)
                advertises.append(ApartmentAdvt(**params))
            self.save_advertises(advertises)
            self.downloaded += len(advertises)
            current_page += 1
            if self.downloaded < count:
                continue
            else:
                break

    def gather_params(self, item):
        params = {}
        for x in self.items:
            params.update({x: getattr(self, f'get_{x}')(item)})
        return params

    def get_items(self, page):
        params = self.params
        params.update({'page': page})
        parsed = self.get_parsed_response(self.BASE_URL, params=params)
        try:
            return parsed['items'], parsed['count']
        except KeyError as e:
            if parsed.get('error'):
                print("Sleep because of: \n", parsed['error']['message'])
                sleep(60 * 60)  # 1 hour
            else:
                self.log_error(str(e))

    def get_detail_item(self, item_id):
        url = self.get_detail_info_url(item_id)
        return self.get_parsed_response(url=url)

    def save_advertises(self, advertises):
        try:
            ApartmentAdvt.objects.bulk_create(advertises, ignore_conflicts=True)
        except Exception as e:
            self.log_error(str(e))

    @staticmethod
    def get_parsed_response(url, params=None):
        params = params or {}
        resp = requests.get(url=url, params=params)
        return json.loads(resp.content)

    @staticmethod
    def get_detail_info_url(item_id):
        return f"https://developers.ria.com/dom/info/{item_id}?api_key={settings.DOM_RIA_TOKEN}"

    @staticmethod
    def get_checkup_id(item):
        return item.get('realty_id')

    @staticmethod
    def get_title(item):
        return f"р-н {item.get('district_name', '')} {item.get('street_name', '')}, {item.get('rooms_count', '')} " \
            f"ком. г.{item.get('city_name', '')}"

    @staticmethod
    def get_price(item):
        return item.get('price')

    @staticmethod
    def get_num_of_rooms(item):
        return item.get('rooms_count')

    @staticmethod
    def get_district(item):
        return item.get('district_name', '')

    @staticmethod
    def get_description(item):
        return item.get('description', '')

    @staticmethod
    def log_error(e):
        print(e)
