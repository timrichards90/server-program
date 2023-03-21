import requests

if __name__ == '__main__':
    uri = 'https://www.7timer.info/bin/astro.php?lon=174.8&lat=-36.9&ac=0&unit=metric&output=json&tzshift=0'
    gdata = {'long': 174.8, 'lat': 36.9}
    response = requests.get(uri, params=gdata)
    output = response.json()
    print(output)
    print(output.get('dataseries'))


