import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TRAINER_TOKEN'
HEADERS = {'Content-Type' : 'application/json',
           "trainer_token" : TOKEN}

# Функция авто-теста проверки статуса ответа 200 от БэкЭнда
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id":499})
    assert response.status_code == 200

# Функция авто-теста проверки имени тренера по id
def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id":499})
    assert response.json()['data'][0]['trainer_name'] == 'VasyaDzen'
