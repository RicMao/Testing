import requests

url = "https://nd-326-444-187.p2pify.com/9de47db917d4f69168e3fed02217d15b/"

payload = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "getBalance",
    "params": ["9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
