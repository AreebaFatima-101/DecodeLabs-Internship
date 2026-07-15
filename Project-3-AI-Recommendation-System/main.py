# ============================================================
# Project 3 : AI Recommendation Logic
# DecodeLabs Artificial Intelligence Internship
# Author : Areeba Fatima
# Description:
# A simple recommendation system that recommends
# movies based on user interests.
# ============================================================

print("=" * 65)
print("              AI RECOMMENDATION SYSTEM")
print("=" * 65)
print("DecodeLabs Artificial Intelligence Internship")
print("=" * 65)

# ------------------------------------------------
# Movie Database
# ------------------------------------------------

movies = {
    "Action": [
        "John Wick",
        "Mission Impossible",
        "The Dark Knight",
        "Mad Max Fury Road"
    ],

    "Comedy": [
        "The Mask",
        "Mr Bean's Holiday",
        "Home Alone",
        "Rush Hour"
    ],

    "Science Fiction": [
        "Interstellar",
        "The Martian",
        "Inception",
        "Avatar"
    ],

    "Horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "The Nun"
    ],

    "Animation": [
        "Toy Story",
        "Frozen",
        "Finding Nemo",
        "Kung Fu Panda"
    ],

    "Adventure": [
        "Jumanji",
        "Jurassic Park",
        "Pirates of the Caribbean",
        "The Jungle Book"
    ]
}

# ------------------------------------------------
# Display Categories
# ------------------------------------------------

print("\nAvailable Categories\n")

for category in movies:
    print("-", category)

print("\nEnter your interests.")
print("Example: Action, Comedy")
print()

# ------------------------------------------------
# User Input
# ------------------------------------------------

user_input = input("Your Interests: ")

interests = []

for item in user_input.split(","):
    interests.append(item.strip().title())

# ------------------------------------------------
# Recommendation Logic
# ------------------------------------------------

recommended_movies = []

for interest in interests:

    if interest in movies:

        for movie in movies[interest]:

            if movie not in recommended_movies:
                recommended_movies.append(movie)

# ------------------------------------------------
# Display Recommendations
# ------------------------------------------------

print("\n" + "=" * 65)
print("RECOMMENDED MOVIES")
print("=" * 65)

if len(recommended_movies) > 0:

    for index, movie in enumerate(recommended_movies, start=1):
        print(f"{index}. {movie}")

else:

    print("Sorry!")
    print("No recommendations found.")
    print("Please choose from the available categories.")

# ------------------------------------------------
# Similarity Score
# ------------------------------------------------

total_categories = len(interests)

matched_categories = 0

for interest in interests:

    if interest in movies:
        matched_categories += 1

if total_categories > 0:

    similarity_score = (
        matched_categories / total_categories
    ) * 100

    print("\nSimilarity Score:",
          round(similarity_score, 2), "%")

print("\nThank you for using the AI Recommendation System!")
print("=" * 65)