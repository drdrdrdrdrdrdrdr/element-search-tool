import requests
import re


def searchele(kw):
    # Get the information of the inputted element 'kw'. If 'kw' is not an element, return two 'error'.
    tableinfo = []
    moreinfo = []
    url = 'https://ptable.com/JSON/properties-650220d.json'
    response = requests.get(url).json()
    for i in response:
        if i.get('symbol') == kw:
            tableinfo += [i['weight'], i.get('melt', 'N/A').strip('.'), i.get('boil', 'N/A').strip('.'),
                          i['discover'], str(i['isotopes']), i.get('electroneg', 'N/A')]
            moreinfo += [i.get('series', 'N/A'), i['electronstring'], i['abundance'].get('universe', 'N/A'),
                         i['abundance'].get('solar', 'N/A'), i['abundance'].get('ocean', 'N/A'),
                         i['abundance'].get('human', 'N/A')]
            break
    else:
        return 'error', 'error'
    url = 'https://ptable.com/JSON/compounds/formula='+kw
    response = requests.get(url).json()
    count = 0
    for i in response['matches']:
        if kw in i['molecularformula']:
            a = i['molecularformula'].replace(kw, '')
            if bool(re.search('[a-zA-Z]', a)):
                tableinfo += [i['molecularformula']]
                count += 1
                if count == 5:
                    break
    return tableinfo, moreinfo
