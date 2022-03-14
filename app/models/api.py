import requests
import json
import time

def querySlackers(heroes):

  query = """query{
    heroes(where:{
      id_in:["""+heroes+"""],
      staminaFullAt_lt:""" + str(int(time.time())) + """
      currentQuest: "0x0000000000000000000000000000000000000000"
    		}) {
      id,
      mainClass,
      staminaFullAt,
      summons,
      generation,
      profession      
    }
  }"""
  
  url = 'https://defi-kingdoms-community-api-gateway-co06z8vi.uc.gateway.dev/graphql/'
  r = requests.post(url, json={'query': query})
  print(r.status_code)
  response_dict = json.loads(r.text)  
  for item in response_dict['data']['heroes']:
    item['staminaFullAt']=int((time.time()-item['staminaFullAt'])/60)
  print(response_dict['data']['heroes'])
  return(response_dict['data']['heroes'])