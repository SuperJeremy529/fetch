
from dto.receipts import RecepientDTO
from service.abstract.base_pointer_strategy import BasePointerStrategy
import re
import math
from datetime import datetime, time 

class SimplePointerStrategy(BasePointerStrategy):
    def _points_for_every_alphanumeric_character(self, retailer: str):
        return len(re.findall(r'[a-zA-Z0-9]', retailer))
    
    def _points_if_the_total_is_a_round_dollar_amount(self, total: str):
        splited_total = total.split('.')[1]
        if float(splited_total) == 0.0:
            return 50.0
        return 0.0
    
    def _points_if_the_total_is_a_multiple(self, total: str): 
        if float(total) % 0.25 == 0.0:
            return 25.0
        return 0.0
    def _points_for_every_two_items_on_the_receipt(self, items: list[dict]):
        return 5 * (len(items) // 2)
    
    def _points_for_trimmed_length_of_the_item_description(self, items: list[dict]):
        aggregated = 0.0
        for item in items:
            if len(item['shortDescription']) % 3 == 0:
                aggregated += math.ceil(float(item['price']) * 0.2)
        return aggregated
            

    def _points_if_the_day_in_the_purchase_date_is_odd(self, purchaseDate: str):
        if int(purchaseDate.split('-')[2]) % 2 != 0:
            return 6.0
        return 0.0
    
    def _points_for_the_time_of_purchase(self, purchaseTime: str):
        given_time = datetime.strptime(purchaseTime, "%H:%M").time()
        if time(14, 0) <= given_time <= time(16, 0):
            return 10.0
        return 0.0

    def calculate(self, recepient_dto: RecepientDTO):
        points = 0.0
        points += self._points_for_every_alphanumeric_character(retailer=recepient_dto.retailer)
        points += self._points_if_the_total_is_a_round_dollar_amount(total=recepient_dto.total)
        points += self._points_if_the_total_is_a_multiple(total=recepient_dto.total)
        points += self._points_for_every_two_items_on_the_receipt(items=recepient_dto.items)
        points += self._points_for_trimmed_length_of_the_item_description(items=recepient_dto.items)
        points += self._points_if_the_day_in_the_purchase_date_is_odd(purchaseDate=recepient_dto.purchaseDate)
        points += self._points_for_the_time_of_purchase(purchaseTime=recepient_dto.purchaseTime)
        return points
    
    def execute(self, recepient_dto: RecepientDTO):
        return self.calculate(recepient_dto=recepient_dto)

