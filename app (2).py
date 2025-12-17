from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import requests
import hashlib
import json
import os

app = Flask(__name__)

# TMDb API Configuration
API_KEY = '442c7f8a2c7afee906ee1c759f530f11'  # Ваш API-ключ
BASE_URL = 'https://api.themoviedb.org/3'

# Function to fetch movie trailers
def fetch_trailer(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('results', [])
            for video in data:
                if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                    return f"https://www.youtube.com/watch?v={video['key']}"
        print(f"No trailer found for Movie ID {movie_id}.")
    except Exception as e:
        print(f"Error fetching trailer for Movie ID {movie_id}: {e}")
    return "#"  # Fallback ссылка

# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            poster_path = response.json().get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"  # Fallback изображение
        else:
            print(f"Failed to fetch poster for Movie ID {movie_id}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching poster for Movie ID {movie_id}: {e}")
    return "https://via.placeholder.com/500x750?text=No+Image"  # Fallback изображение

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to load users
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return {}

# Function to save users
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Load and enhance movies dataset
print("Loading movies dataset...")
movies = pd.read_csv('movies_dataset.csv')

# Добавляем постеры и трейлеры, если их ещё нет
if 'poster_path' not in movies.columns or 'trailer_link' not in movies.columns:
    print("Fetching posters and trailers for movies...")
    movies['poster_path'] = movies['id'].apply(fetch_poster)
    movies['trailer_link'] = movies['id'].apply(fetch_trailer)
    movies.to_csv('movies_dataset_enhanced.csv', index=False)
    print("Updated movies dataset saved as 'movies_dataset_enhanced.csv'.")
else:
    print("Movies dataset already enhanced. Skipping API requests.")

@app.route('/')
def home():
    return render_template('index.html', movies=movies.to_dict(orient='records'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and users[username] == hash_password(password):
            return redirect(url_for('home'))
        return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if len(password) < 8:
            return render_template('register.html', error="Password must be at least 8 characters long.")
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match.")

        users = load_users()
        if username in users:
            return render_template('register.html', error="Username already exists.")

        users[username] = hash_password(password)
        save_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
