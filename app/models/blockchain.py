import os
from web3 import Web3

def getAQHeros(ownerAddress):
  rpc_server = 'https://api.harmony.one'
  w3 = Web3(Web3.HTTPProvider(rpc_server))
  mainQuesterAddr = "0xcCa755BB6193fA582a122D89100b92fF179745Fd";
  mainQuesterABI = """""" + os.environ['abi'] + """"""
  
  contract_address = Web3.toChecksumAddress(mainQuesterAddr)
  contract = w3.eth.contract(contract_address, abi=mainQuesterABI)
  
  heroes = contract.functions.getHeroes(ownerAddress).call()
  return(",".join(str(e) for e in heroes))