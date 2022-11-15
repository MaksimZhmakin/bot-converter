import re
import json
import requests
import configparser
import telebot

conf = configparser.ConfigParser()
conf.read('config.ini')

bot = telebot.TeleBot(conf['auth']['token'])

cur = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
    
}


class APIException(Exception):
    """Ошибки формата запроса"""


class Price:
    @staticmethod
    def get_price(text):
        cur_keys = [*cur.keys()]
        try:
            m = re.match(rf'^{cur_keys[0]}|{cur_keys[1]}|{cur_keys[2]}\s{cur_keys[0]}|{cur_keys[1]}|'
                         rf'{cur_keys[2]}\s(\w+)$', text)
            if m:
                base, quote, amount = text.split(' ')
                if base == quote:
                    raise APIException
            else:
                raise APIException
        
        except APIException:
            return f'Данные об ошибке: введите данные в правильном формате'
        
        except Exception:
            return f'Данные об ошибке: введите данные в правильном формате'
        
        return f'Цена {amount} {base} в {quote} -  ' + str(
            json.loads(requests.request("GET", f"https://api.apilayer.com/currency_data/convert?to={cur[quote]}&from="
                                               f"{cur[base]}&amount={amount}",
                                        headers={"apikey": conf['auth']['apikey']}).text)['result'])
