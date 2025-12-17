import pandas as pd
import requests

# Конфигурация API
API_KEY = '442c7f8a2c7afee906ee1c759f530f11'  # Укажите ваш ключ TMDb API
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_all_movies():
    all_movies = []
    for page in range(1, 251):  # 250 страниц * 20 фильмов на страницу = 5000 фильмов
        print(f"Fetching page {page}...")
        url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('results', [])
            all_movies.extend(data)
        else:
            print(f"Error fetching page {page}: {response.status_code}")
            break
    return all_movies

# Скачивание фильмов
movies_data = fetch_all_movies()

# Преобразование в DataFrame и сохранение в
if movies_data:
    movies = pd.DataFrame(movies_data)
    movies.to_csv('movies_dataset.csv', index=False)
    print("Файл 'movies_dataset.csv' успешно создан с 5000 фильмами.")
else:
    print("Не удалось получить данные. Проверьте API-ключ и подключение к интернету.")
