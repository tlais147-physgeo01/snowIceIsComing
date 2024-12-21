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

def inqNewsApi(results=[]):
  apiKey = os.getenv('NEWSAPI_KEY')
  url = ('https://newsapi.org/v2/everything?q=Klimawandel&language=de&apiKey='+apiKey)
  response = requests.get(url)
  response.encoding = response.apparent_encoding
  if(response.text):
    jsonData = json.loads(response.text)
    if ('ok'==jsonData['status']):
      results.append("NewsAPI status fine")
      if(jsonData['totalResults']>0):
         results.append(":white_check_mark: NewsAPI results found")
      else:
         results.append(":no_entry: NewsAPI results **not** found")
    else:
      results.append(":no_entry: NewsAPI status **failed**:")
      results.append("Please recheck the API key and its assignment:")
      results.append("1. Please register at https://newsapi.org/register")
      results.append("2. Login and get your API key at https://newsapi.org/account")
      results.append("3. Assign the API key as new organization secret at https://github.com/organizations/newsWhisperer/settings/secrets/actions/new")         


def checkNewsApi(results=[]):
    apiKey = os.getenv('NEWSAPI_KEY')
    results.append("### NewsAPI")
    apiKeyExists = True
    if(apiKey):
      if(apiKey == '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'):
        apiKeyExists = False
    else:
        apiKeyExists = False      
    if(not apiKeyExists): 
        results.append(":no_entry: NewsAPI key **missing**:")
        results.append("1. Please register at https://newsapi.org/register")
        results.append("2. Login and get your API key at https://newsapi.org/account")
        results.append("3. Assign the API key as new organization secret at https://github.com/organizations/newsWhisperer/settings/secrets/actions/new")       
        results.append("   * Name:  NEWSAPI_KEY ")
        results.append("   * Value: <Your key here> ")   
    else:
        results.append(":white_check_mark: NewsAPI key exists")
        inqNewsApi(results)  
    return results


# https://stackoverflow.com/questions/48364398/github-api-determine-if-user-or-org
#  'https://api.github.com/users/'+gitOrg   "type": "Organization" / "type": "User" ??
# https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28
#  'https://api.github.com/orgs/ORG/members'    -> type,url
# https://stackoverflow.com/questions/31338803/only-few-of-my-github-organizations-are-shown-in-my-public-github-profile

def checkGithubOrganization(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    gitRepo = os.getenv('GITHUB_REPO')
    #print(['Org',gitOrg,'Repo',gitRepo])
    results.append("### Github Organization")
    if(gitOrg):
      orgData = inqUrl('https://api.github.com/users/'+gitOrg)
      #print(orgData)    # check for 'type': 'Organization', 'user_view_type': 'public'
      if(not 'Organization'==orgData['type']):
        results.append(":no_entry: Github Organization **missing**:")   

        results.append("1. Please")
        results.append("2. Logt")
        results.append("3. Assifgn") 
      else:
        results.append(":white_check_mark: Github Organization exists") 
        orgAssigned = False
        myOrgs = inqUrl('https://api.github.com/users/KMicha/orgs')
        #print(myOrgs) 
        for org in myOrgs:
          if(org['id']==orgData['id']):
            orgAssigned = True
        if(orgAssigned):
          results.append(":white_check_mark: Github Organization assigned")   
        else:
          results.append(":no_entry: Github Organization **not** assigned (or not public):")
          results.append("1. Please")
          results.append("2. Logt")
          results.append("3. Assifgn")      
    else:
      results.append("No check possible: maybe running locally?") 

results=[]
checkGithubOrganization(results)
results.append("---")
checkNewsApi(results)
print(results)


f = open("CHECK.md", "w")
for res in results:
  f.write(res+"  \n")
f.close()


