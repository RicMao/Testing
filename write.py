from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
import random
import requests, os, requests_random_user_agent
import secrets
from eth_keys import keys
from eth_account import Account
from web3 import Web3
from colorama import Fore
import time, re, platform

a=0
def ethBal(addr: str):
    url = f"https://mainnet.infura.io/v3/4e779a6e40c14cfabd41fcc6a612e413"
    req = requests.get(url)
    if req.status_code == 200:
        ret = int(dict(req.json())['balance'])
        return ret / 1000000000000000000
    else:
        return 0

while a<=1000000:
    private_key = ''.join(random.choice('0d12b3e45c6a78f9') for i in range(64))
    #address = Account.from_key(private_key).address
    address = '0xbF3aEB96e164ae67E763D9e050FF124e7c3Fdd28'
    balance_ether = ethBal(address)

    print(Fore.GREEN + f"Key: {private_key}")
    print(Fore.YELLOW + f"Adr: {address}")
    print(Fore.WHITE + f"Eth: {balance_ether}")

    if balance_ether > 0.001: break
    a=a+1
    
