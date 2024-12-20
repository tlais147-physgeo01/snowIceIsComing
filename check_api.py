#import mysecrets
import os
import requests
#from urllib.parse import urlparse
import json


def inqUrl(url):
   response = requests.get(url)
   response.encoding = response.apparent_encoding
   jsonData = None
   if(response.text):
       jsonData = json.loads(response.text)
   return jsonData


def checkNewsApi():
    results = []
    apiKey = os.getenv('NEWSAPI_KEY')
    if(apiKey == '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'): 
        results.append("### NewsAPI")
        results.append("1. Please register at https://newsapi.org/register")
        results.append("2. Login and get your API key at https://newsapi.org/account")
        results.append("3. Assign the API key as new organization secret at https://github.com/organizations/newsWhisperer/settings/secrets/actions/new")       
        results.append("   Name:  NEWSAPI_KEY ")
        results.append("   Value: <Your key here> ")   
    return results


# https://stackoverflow.com/questions/48364398/github-api-determine-if-user-or-org
#  'https://api.github.com/users/'+gitOrg   "type": "Organization" / "type": "User" ??
# https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28
#  'https://api.github.com/orgs/ORG/members'    -> type,url

def checkGithubOrganization():
    gitOrg = os.getenv('GITHUB_OWNER')
    gitRepo = os.getenv('GITHUB_REPO')
    print(['Org',gitOrg,'Repo',gitRepo])
    if(gitOrg):
      test1 = inqUrl('https://api.github.com/users/'+gitOrg)
      print(test1)    # check for 'type': 'Organization', 'user_view_type': 'public'
      test2 = inqUrl('https://api.github.com/orgs/'+gitOrg+'/members')
      print(test2)
    else:
      print('Running locally?') 
    htmlReq = requests.get('https://github.com/'+gitOrg)
    if(htmlReq.text):
      print(htmlReq.text)
    else:
      print('people list failed')


checkGithubOrganization()


