# -*- coding: utf-8 -*-

import requests, json

def __init__(giris):
    r = requests.get('https://tr.wikipedia.org/w/api.php?action=query&list=search&format=json&srnamespace=0&srwhat=text&srprop=score&srlimit=1&srsearch='+giris+'&format=json')
    try:
        cozunmus_data = json.loads(r.text)
        bulunan_baslik = cozunmus_data['query']['search'][0]['title']
        if bulunan_baslik:
            r = requests.get('https://tr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&explaintext=&titles='+bulunan_baslik+'&format=json')
            cozunmus_data = json.loads(r.text)
            for data in cozunmus_data['query']['pages']:
                metin = cozunmus_data['query']['pages'][data]['extract']
                metin = metin.split('\n')
                return metin[0]
        else:
            return 'Aradığın kişiyi bulamadım.'
    except (ValueError, KeyError, TypeError, IndexError), e:
        return 'Aradığın kişiyi bulamadım.'