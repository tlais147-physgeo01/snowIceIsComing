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


def checkNewsApi(results=[]):
    apiKey = os.getenv('NEWSAPI_KEY')
    results.append("### NewsAPI")
    if(apiKey == '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'): 
        results.append("NewsAPI missing:")
        results.append("1. Please register at https://newsapi.org/register")
        results.append("2. Login and get your API key at https://newsapi.org/account")
        results.append("3. Assign the API key as new organization secret at https://github.com/organizations/newsWhisperer/settings/secrets/actions/new")       
        results.append("   * Name:  NEWSAPI_KEY ")
        results.append("   * Value: <Your key here> ")   
    return results


# https://stackoverflow.com/questions/48364398/github-api-determine-if-user-or-org
#  'https://api.github.com/users/'+gitOrg   "type": "Organization" / "type": "User" ??
# https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28
#  'https://api.github.com/orgs/ORG/members'    -> type,url
# https://stackoverflow.com/questions/31338803/only-few-of-my-github-organizations-are-shown-in-my-public-github-profile

def checkGithubOrganization(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    gitRepo = os.getenv('GITHUB_REPO')
    print(['Org',gitOrg,'Repo',gitRepo])
    results.append("### Github Organization")
    if(gitOrg):
      orgData = inqUrl('https://api.github.com/users/'+gitOrg)
      print(orgData)    # check for 'type': 'Organization', 'user_view_type': 'public'
      if(not 'Organization'==orgData['type']):
        results.append("Github Organization missing:")   

        results.append("1. Please")
        results.append("2. Logt")
        results.append("3. Assifgn") 
      else:
        results.append("Github Organization exists") 
        #orgMembers = inqUrl('https://api.github.com/orgs/'+gitOrg+'/members')
        #print(orgMembers)
        orgAssigned = False
        myOrgs = inqUrl('https://api.github.com/users/KMicha/orgs')
        print(myOrgs) 
        for org in myOrgs:
          if(org['id']==orgData['id']):
            orgAssigned = True
        if(orgAssigned):
          results.append("Github Organization assigned")   
        else:
          results.append("Github Organization not assigned (or not public):")
          results.append("1. Please")
          results.append("2. Logt")
          results.append("3. Assifgn")      
    else:
      print('No check possible: maybe running locally?') 

results=[]
checkGithubOrganization(results)
print(results)


