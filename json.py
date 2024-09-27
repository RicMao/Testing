import random
import base58

key_array = [4,182,130,247,119,117,227,207,112,73,170,126,222,197,244,99,215,107,255,202,33,43,36,17,104,111,157,246,196,192,174,95,240,23,238,206,118,215,154,238,229,96,11,37,156,123,51,223,5,231,17,117,86,136,103,14,75,95,175,132,148,54,1,46]
random_array = ''.join(random.choice(key_array))
secret_key = random_array[0:64]
public_key = random_array[32:64]

sk = base58.b58encode(bytes(secret_key))
pk = base58.b58encode(bytes(public_key))

print(sk)
print(pk)
