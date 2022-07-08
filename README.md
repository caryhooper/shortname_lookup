# shortname_lookup
This is a helper program to create wordlist of possible English words corresponding to the filename of a shortlink.

Given a 'shortlink' such as 'ADMIN~
```bash
user@machine:/$ python3 shortname_lookup.py admini | tee wordlist.txt
Making web request to thefreedictionary.com...

Results:
administratorship
administratively
administratrices
administratrixes
administrations
administrativia
administrablely
administration
administratrix

```

[source/inspiration](https://twitter.com/Jun34u_sec/status/1545146184846680071)
[Additional Resource](https://blog.liquidsec.net/2021/03/02/iis-shortnames-the-bug-that-became-a-feature/)
