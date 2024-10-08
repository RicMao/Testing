import base58
from solders.keypair import Keypair
import time
from colorama import Fore

    # Random generate address & private key 
    account = Keypair()
    privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')

    # Sample Output
    address : account.pubkey
    private_key : privateKey
    
    print(Fore.GREEN + f"Adr: (address")
    print(Fore.YELLOW + f"Key: (private_key)")
    time.sleep(0.001)
 
    
