import json
from classes import Listener, Artist
import os

users = {}
songs = {}

def save_to_json(filename = "users.json"):
    data = {}
    for uid, user in users.items():
        data[str(uid)] = {
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "is_premium": user.is_premium,
            "role": "Listener" if isinstance(user, Listener) else "Artist"
        }
    with open(filename, "w") as f:
        json.dump(data, f)

def load_users(filename="users.json"):
    global users
    if not os.path.exists(filename):
        users = {}
        return
    with open(filename, "r") as f:
        data = json.load(f)
        for uid, user in data.items():
            if user["role"] == "Listener":
                obj = Listener(int(uid), user["username"], user["email"], user["password"])
            else:
                obj = Artist(int(uid), user["username"], user["email"], user["password"])

            obj.is_premium = user["is_premium"]
            users[int(uid)] = obj

