

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
def get_lyrics(song_title, artist):
    api_url = f"https://api.lyrics.ovh/v1/{artist}/{song_title}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('lyrics', 'Lyrics not found')
    else:
        return 'Error fetching lyrics'
def fetch_lyrics():
    song_title = song_entry.get()
    artist = artist_entry.get()
    
    if not song_title or not artist:
        messagebox.showwarning("Input Error", "Please enter both song title and artist.")
        return
    
    lyrics = get_lyrics(song_title, artist)
    lyrics_text.delete(1.0, tk.END)
    lyrics_text.insert(tk.END, lyrics)
root = tk.Tk()
root.title("Lyrics Extractor")
tk.Label(root, text="Song Title:").grid(row=0, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=50)
song_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Artist:").grid(row=1, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=50)
artist_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, columnspan=2, pady=20)

lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
lyrics_text.grid(row=3, columnspan=2, padx=10, pady=10)
root.mainloop()