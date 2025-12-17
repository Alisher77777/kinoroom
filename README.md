# kinoroom
# 🎬 KinoRoom: Movie Recommendation System

## 📌 Project Overview
KinoRoom is a sophisticated web application designed to help users navigate the vast world of cinema. By leveraging **Machine Learning** and metadata from **The Movie Database (TMDb) API**, it provides highly relevant movie suggestions based on user input.

## 🚀 Key Features
* **Content-Based Filtering:** Recommends movies by analyzing genres, keywords, and plot summaries.
* **Live API Integration:** Fetches up-to-date movie posters, ratings, and descriptions directly from TMDb.
* **Vectorization Logic:** Uses **TF-IDF** (Term Frequency-Inverse Document Frequency) to process movie metadata.
* **Responsive UI:** A sleek, user-friendly interface built for a seamless browsing experience.

## 🛠 Tech Stack
* **Backend:** Python & Flask
* **Data Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Cosine Similarity)
* **Frontend:** HTML5, CSS3, JavaScript
* **External Data:** TMDb API

## 🧠 How it Works
1.  **Data Extraction:** Movie details are gathered via API calls.
2.  **Natural Language Processing:** Movie tags and overviews are processed into numerical vectors.
3.  **Similarity Calculation:** The system calculates the "Cosine Similarity" between your favorite movie and thousands of others to find the best match.

## 📁 Repository Structure
* `app.py`: The main Flask application.
* `Documentation.docx`: Full technical breakdown of the system.
* `templates/`: HTML structures for the web interface.
