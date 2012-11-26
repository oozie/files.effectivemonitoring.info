#!/usr/bin/python
import sys
import time
import urllib2

COLLECTION_INTERVAL = 300
CITIES = ['Beijing', 'Cambridge', 'Farnham', 'Koeln', 'Sebastopol', 'Tokyo']
WEATHER_API = 'http://citytemp.effectivemonitoring.info/get'

def get_temperature(city, scale='c'):
    """Get temperature for a city."""
    city_url = WEATHER_API + '?city=%s&scale=%s' % (city, scale)
    api_response = urllib2.urlopen(city_url).read()
    if api_response.strip().isdigit():
        return eval(api_response)

def main():
    while True:
        for city in CITIES:
            ts = int(time.time())
            city_temp = get_temperature(city, scale='f')
            city_label = city.lower().replace(' ', '_')
            print 'temperature %d %s city=%s' % (ts, city_temp, city_label)
        sys.stdout.flush()
        time.sleep(COLLECTION_INTERVAL)

if __name__ == "__main__":
    main()
