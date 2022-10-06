import requests


def searchele(kw):
    info = []
    url = 'https://ptable.com/JSON/properties-650220d.json'
    response = requests.get(url).json()
    for i in response:
        if i.get('symbol') == kw:
            info += [i['weight'], i.get('melt', 'N/A').strip('.'), i.get('boil', 'N/A').strip('.'),
                     i['discover'], str(i['isotopes']), i.get('electroneg', 'N/A')]
            break
    url = 'https://ptable.com/JSON/compounds/formula='+kw
    response = requests.get(url).json()
    count = 0
    for i in response['matches']:
        if i['molecularformula'] != kw:
            info += [i['molecularformula']]
            count += 1
            if count == 3:
                break
    return info
