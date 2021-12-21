from math import floor
from typing import Dict, Any


class Statement:

    @staticmethod
    def format_currency(value):
        return f'${value:,.2f}'

    def statement(self, invoice, plays):
        total_amount = 0
        volume_credits = 0
        result = {}
        result['plays'] = []

        # while not ["performances"]:
        for perf in invoice["performances"]:
            play = plays[perf["playID"]]
            this_amount = 0

            if play["type"] == "tragedy":
                this_amount = 40000
                if perf["audience"] > 30:
                    this_amount += 1000 * (perf["audience"] - 30)
            elif play["type"] == "comedy":
                this_amount = 30000
                if perf['audience'] > 20:
                    this_amount += 10000 + 500 * (perf["audience"] - 20)
                this_amount += 300 * perf["audience"]
            else:
                raise Exception(f'Unknown type: {play["type"]}')
            # add volume credits
            volume_credits += max(perf['audience'] - 30, 0)
            # add extra credits for every ten comedy attendees
            if 'comedy' == play["type"]:
                volume_credits += floor(perf["audience"]/5)
            result['plays'].append({'earn': Statement.format_currency(this_amount/100), "seats": perf["audience"], "name": play["name"]})
            total_amount += this_amount
        print(f'Amount owed is {Statement.format_currency(total_amount/100)}')
        result['total_amount'] = Statement.format_currency(total_amount/100)
        print(f'credit {volume_credits} credits')
        result['total_credit'] = volume_credits
        return result
