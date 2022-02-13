#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys, getopt, os, pickle, tempfile, requests

SAVE_LOCATION = os.path.join(tempfile.gettempdir(), 'alertWallapop.pkl')

API_URL = 'https://api.wallapop.com/api/v3/general/search?'
PARAMS = {
    "keywords":"new%20nintendo%203ds%20xl",
    "filters_source":"quick_filters",
    "latitude":"40.4893538",
    "longitude":"-3.6827461",
    "order_by":"newest",
    "max_sale_price":"150"
}

API_HEADERS =  {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es,es-ES;q=0.9",
    "deviceos": "0",
    "sec-ch-ua": "\"Chromium\";v=\"96\", \"Opera GX\";v=\"82\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-deviceos": "0",
    "Referer": "https://es.wallapop.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

pushToken = '<your token here>'
email = '<your email here>'

def keywords(str='') -> str:
    return str.replace(' ', '+')

def generate(url, params) -> str:
    for attr, value in params.items():
        url+= attr + '=' + value + '&'
    
    return url[0:-1]


def api(url, header) -> json:
    response = requests.get(url, headers=header, json=PARAMS)
    print('Request Made! Returning result')
    print('Sending URL: ' + response.url)
    return response.json()


def main():
    """
    Vamos por partes.
    
    Lo primero es con los datos que ya tenemos, generar la query, obtener los datos y poder lopear.
    Una vez hecho eso, lo tengo que guardar en algun contenedor accesible.

    Previo a ser guardados, se debe chequear si ya existe ese registro, por lo cual, de ya existir, no se inserta.
    Si el registro no existe (es nuevo), se debe generar con PushBullet una notificacion para avisar al usuario
    (Investigar pushbullet api, como y qué enviar por parametros)

    Luego en una segunda etapa se pule el programa y se hace que tome los keywords desde los args de arranque
    """
    url = generate(API_URL, PARAMS)
    print("URL DE IDA: " + url)
    recivedItems = api(url, API_HEADERS)
    print(recivedItems["search_objects"])
    # api(API_URL, API_HEADERS, API_BODY)



if __name__ == '__main__':
    main()