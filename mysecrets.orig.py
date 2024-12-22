import os
## copy this file to mysecrets.py and adapt your private settings (cp mysecrets.orig.py mysecrets.py)

## setings for inquiring articles from newsapi.org
#  Get API Key: https://newsapi.org/register &  https://newsapi.org/account

if(not os.getenv('NEWSAPI_KEY')):
    print("NEWSAPI_KEY not yet set.")
    os.environ['NEWSAPI_KEY'] = '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'
else:
    print("NEWSAPI_KEY already set.")

## Get API key: https://rapidapi.com/auth/sign-up
if(not os.getenv('RAPIDAPI_KEY')):
    print("RAPIDAPI_KEY not yet set.")
    os.environ['RAPIDAPI_KEY'] = '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y'
else:
    print("RAPIDAPI_KEY already set.")
#


## Get API key: https://rapidapi.com/auth/sign-up
if(not os.getenv('GEONAMES_KEY')):
    print("GEONAMES_KEY not yet set.")
    os.environ['GEONAMES_KEY'] = 'demo_demo_123'
else:
    print("GEONAMES_KEY already set.")

