#!/usr/bin/env python3
import requests, bs4, sys, re
#Written by h00p; inspired by @Jun34u_sec
#https://blog.liquidsec.net/2021/03/02/iis-shortnames-the-bug-that-became-a-feature/

if len(sys.argv) != 2:
    print("[!] Invalid arguments.  Usage: ./shortname_lookup.py admini | tee wordlist.txt",file=sys.stderr)
    sys.exit(1)

print("Making web request to thefreedictionary.com...",file=sys.stderr)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
shortname = sys.argv[1]
try:
    response = requests.get(f'https://www.thefreedictionary.com/words-that-start-with-{shortname}',headers=headers)
except Exception as e:
    print("[!] failed to make HTTP request.  Exiting...",file=sys.stderr)
    sys.exit(1)

print("\nResults:",file=sys.stderr)
soup = bs4.BeautifulSoup(response.text,'html.parser')
results = soup.find_all('a')
for a in results:
    if a.text.startswith(shortname):
        print(a.text)
