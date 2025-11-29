#------ KLASSER --------
class User:
    def __init__(self, user_id, username, email, password_hash):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.is_logged_in = False
        self.is_premium = False

    def upgrade_to_premium(self):
        self.is_premium = True
        return f"{self.username} is now a premium user."
    
    def login(self):
        pass

    def logout(self):
        pass

class Listener(User):
    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash)
        self.history = []

    def add_to_history(self, song):
        self.history.append(song)

class Artist(User):
    def __init__(self, user_id, username, email, password_hash, bio=""):
        super().__init__(user_id, username, email, password_hash)
        self.bio = bio
        self.songs = []

    def upload_song(self, song):
        pass

class Admin(User):
    def ban_user(self, user):
        pass

    def remove_song(self, song):
        pass

class Song:
    def __init__(self, song_id, title, duration, genre, filepath):
        self.song_id = song_id
        self.title = title
        self.duration = duration
        self.genre = genre
        self.filepath = filepath
        self.play_count = 0

    def play(self):
        self.play_count += 1


class Playlist:
    def __init__(self, playlist_id, name):
        self.playlist_id = playlist_id
        self.name = name
        self.songs = []

    def add_song(self, song):
        pass

class PlaybackSession:
    def __init__(self, session_id, listener, device):
        self.session_id = session_id
        self.listener = listener
        self.device = device

    def start(self, song):
        pass

    def stop(self):
        pass

#------ REKOMMENDATION -------
def generate_recommendations(listener, all_songs):
    #Om användaren inte har historik
    if not listener.history:
        return []

    #Ta de senaste 5 låtarna
    recent_songs = listener.history[-5:]

    #Hitta den vanligaste genren
    genres = []
    for song in recent_songs:
        genres.append(song.genre)

    top_genre = max(set(genres), key=genres.count)

    #Plocka ut alla låtar med samma genre
    recommended = []
    for song in all_songs:
        if song.genre == top_genre:
            recommended.append(song)


    return recommended
