import pprint
import requests
import typer

from typing_extensions import Annotated
from typing import Optional

AUTH_URL = 'https://auth.garveks.ru/api/Authenticate/Authenticate'
AZS_API_BASE_URL = 'https://azs.garveks.ru'

app = typer.Typer()

@app.command()
def auth(login: str, password: str):   
    params = {'Email': login, 'Password': password} 
    response = requests.post(AUTH_URL, params=params)
    print('RESPONSE STATUS: ', response.status_code)
    print('RESPONSE MESSAGE: ')
    response_json = response.json()
    pprint.pprint(response_json)

    jwt_token = response_json['data']['accessToken']

    if response.status_code == 200:
        print('Saving JWT token to jwt_token.txt...')
        with open('jwt_token.txt', 'w') as f:
            f.write(jwt_token)
    else:
        print('Error occured')

@app.command()
def cards(card_id: Annotated[Optional[str], typer.Argument()] = None):
    jwt_token = None
    with open('jwt_token.txt', 'r') as f:
        jwt_token = f.read(jwt_token)

    if jwt_token:
        headers = {"Authorization": "Bearer {token}".format(token=jwt_token)}
        card_id_qs = '?cardIds={card_id}'.format(card_id=card_id) if card_id else ''
 
        card_list = requests.get(AZS_API_BASE_URL + '/api/Cards/GetCards' + card_id_qs, headers=headers)

        if card_list.status_code == 200:
            card_list_json = card_list.json()
            for card in card_list_json['objects']:
                print(str(card), '\n')
        else:
            print('Error occured')
    else:
        print('No token found')


@app.command()
def events(card_id: str, date_start_unix: str, date_end_unix: str):
    jwt_token = None
    with open('jwt_token.txt', 'r') as f:
        jwt_token = f.read(jwt_token)

    if jwt_token:
        headers = {"Authorization": "Bearer {token}".format(token=jwt_token)}
        card_id_qs = '?cardIds={card_id}&DateStart={date_start_unix}&DateEnd={date_end_unix}'.format(
            card_id=card_id, 
            date_start_unix=date_start_unix, 
            date_end_unix=date_end_unix
        ) if card_id else ''
	
        card_list = requests.get(AZS_API_BASE_URL + '/api/Events/DeviceEvents' + card_id_qs, headers=headers)

        if card_list.status_code == 200:
            card_list_json = card_list.json()
            for event in card_list_json['objects']:
                print(str(event), '\n')
        else:
            print('Error occured')
    else:
        print('No token found')


if __name__ == "__main__":
    app()
#    typer.run(main)
