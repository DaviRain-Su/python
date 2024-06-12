import json

filename = '../data/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
