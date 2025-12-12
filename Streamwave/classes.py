class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.is_logged_in = False
        self.is_premium = False

    def remove_premium(self):
        self.is_premium = False
        return f"{self.username} is no longer premium user"

    def upgrade_to_premium(self):
        self.is_premium = True
        return f"{self.username} is now a premium user."
    
    def login(self):
        self.is_logged_in = True
        return f"{self.username} is now logged in."

    def logout(self):
        self.is_logged_in = False
        return f"{self.username} has logged out."

class Listener(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id, username, email, password)
        self.history = []
        self.playlists = []

    def add_to_history(self, song):
        self.history.append(song)

class Artist(User):
    def __init__(self, user_id, username, email, password, bio=""):
        super().__init__(user_id, username, email, password)
        self.bio = bio
        self.songs = []

    def upload_song(self, song):
        self.songs.append(song)

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