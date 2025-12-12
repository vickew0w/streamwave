from classes import *
from database import *

def main_menu():
    print("---STREAMWAVE MUSIC APP---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def register_user():
    print("Register as 1 or 2: ")
    print("1: Listener")
    print("2: Artist")
    choice = input("Choose 1 or 2: ")

    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    if choice == "1":
        user = Listener(len(users)+1, username, email, password)
    elif choice == "2":
        user = Artist(len(users)+1, username, email, password)
    else:
        print("Not a valid choice")

    users[user.user_id] = user
    print("Registration successfuul")
    save_to_json()

def login_user():
    username = input("Username: ")
    password = input("Password: ")

    for user in users.values():
        if username == user.username and password == user.password:
            user.is_logged_in = True
            current_user = user
            print("You logged in")
            return user
    print("Login failed")
    return None

def user_menu(user):
    while True:
        print(f"Welcome {user.username}")
        if isinstance(user, Artist):
            print("1. Upload song")
            print("2. Edit bio")
            print("3. Logout")
            choice = input("Choose 1, 2 or 3: ")
            if choice == "1":
                title = input("Song title: ")
                duration = input("Duration in seconds: ")
                genre = input("Genre: ")
                filepath = input("Filepath: ")
                new_song = Song(len(songs) + 1, title, duration, genre, filepath)
                user.upload_song(new_song)
                songs[new_song.song_id] = new_song
                save_to_json
            elif choice == "2":
                user.bio = input("")
                save_to_json()
            elif choice == "3":
                break
            
        elif isinstance(user, Listener):
            print("1. Browse songs")
            print("2. Create playlist")
            print("3. Edit playlists")
            print("4. Recommendations")
            print("5. Premium options")
            print("6. Logout")
            choice = input("Choose from 1 to 6: ")
            if choice == "1":
                print(songs)
                input("> ")
            elif choice == "2":
                playlist_name = input("Create playlist name: ")
                playlist_id = len(user.playlists) + 1
                new_playlist = Playlist(playlist_id, playlist_name)
                user.playlists.append(new_playlist)
                print(f"Playlist {playlist_name} created")
            elif choice == "3":
                pass
            elif choice == "4": 
                if user.history:
                    generate_recommendations()
                else:
                    print("Listen to more songs to get recommendations")
                    input("> ")
            elif choice == "5":
                while True:
                    print("Premium Options:")
                    print("1. Upgrade to premium")
                    print("2. Remove premium")
                    print("3. Back")
                    premium_choice = input("Choose 1, 2 or 3: ")

                    if premium_choice == "1":
                        if user.is_premium:
                            print("You are already a premium user!")
                        else:
                            print(user.upgrade_to_premium())
                            save_to_json()

                    elif premium_choice == "2":
                        if not user.is_premium:
                            print("You are not a premium user!")
                        else:
                            print(user.remove_premium())
                            save_to_json()

                    elif premium_choice == "3":
                        break 
                    else:
                        print("Invalid choice, try again.")

            elif choice == "6":
                user.is_logged_in = False
                print("Logged out")
                break

def generate_recommendations(user, songs):
    recent_songs = user.history[-5:]
    genres = []
    for song in recent_songs:
        genres.append(song.genre)

    top_genre = max(set(genres), key=genres.count)

    recommended = []
    for song in songs:
        if song.genre == top_genre:
            recommended.append(song)

    return recommended