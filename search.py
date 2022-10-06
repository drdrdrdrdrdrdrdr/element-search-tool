import requests


def searchele(kw):
    info = []
    url = 'https://ptable.com/JSON/properties-650220d.json'
    response = requests.get(url).json()
    for i in response:
        if i.get('symbol') == kw:
            info += [i['weight'], i['melt'].strip('.'), i['boil'].strip('.'),
                     i['discover'], str(i['isotopes']), i['electroneg']]
            break
    url = 'https://ptable.com/JSON/compounds/formula='+kw
    response = requests.get(url).json()
    for i in range(1, 4):
        info += [response['matches'][i]['molecularformula']]
    return info
