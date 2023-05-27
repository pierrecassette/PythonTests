import requests
import pytest

HOST = 'https://pokemonbattle.me:9104/'
TOKEN = 'token'

def test_status_code():
    response = requests.get(f'{HOST}trainers', params={'trainer_id':4577})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get(f'{HOST}trainers', params={'trainer_id':4577})
    assert response.json()['trainer_name'] == 'Урал'
