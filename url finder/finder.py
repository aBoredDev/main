import requests
import datetime


url_seeds = ['http://nastylist-instatop%s.me', 'http://nastyinsta-list%s.me', 'http://nastyinsta-top%s.me', 'http://top%s-nastylist.me']

logfile = open('log.txt', 'a+')

good_urls = []

for number in range(1, 1001):
    logfile.write('=%s=\n' % number)

    for url in url_seeds:
        try:
            r = requests.get(url % number, timeout=5)
            logfile.write('At %s, %s worked' % (datetime.datetime.now(), (url % number)))
            print('At %s, %s worked' % (datetime.datetime.now(), (url % number)))
            good_urls.append(url % number)
        except requests.exceptions.Timeout:
            logfile.write('%s timed out\n' % (url % number))
            print('%s timed out\n' % (url % number))
        except:
            logfile.write('%s didn\'t work\n' % (url % number))
            print('%s didn\'t work\n' % (url % number))

print(good_urls)
logfile.close()
