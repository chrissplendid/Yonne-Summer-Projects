"""
Favorite Movies List
Author: Senior Software Engineer
Description: Manage and display a list of favorite movies 
             using lists and tuples.
"""

def display_movies(movies_list):
    """
    Prints the current list of favorite movies.
    :param movies_list: List of movies
    """
    print("\n🎬 Your Favorite Movies:")
    for idx, movie in enumerate(movies_list, start=1):
        print(f"{idx}. {movie}")


def main():
    # Initial favorite movies list (mutable)
    favorite_movies = ["Inception", "The Dark Knight", "Interstellar"]

    # Tuple of suggested movies (immutable)
    suggested_movies = ("The Matrix", "Gladiator", "Forrest Gump")

    # Display initial list
    display_movies(favorite_movies)

    # Append a new movie
    new_movie = input("\nEnter a new favorite movie to add: ").strip()
    favorite_movies.append(new_movie)
    print(f"✅ '{new_movie}' has been added to your list.")

    # Show index of a movie
    movie_to_find = input("\nEnter a movie title to find its position: ").strip()
    if movie_to_find in favorite_movies:
        position = favorite_movies.index(movie_to_find)
        print(f"🔍 '{movie_to_find}' is at position {position + 1}.")
    else:
        print(f"⚠️ '{movie_to_find}' is not in your favorites.")

    # Demonstrate slicing
    print("\n📌 First two favorite movies:")
    print(favorite_movies[:2])

    print("\n📌 Last two favorite movies:")
    print(favorite_movies[-2:])

    # Show suggested movies from tuple
    print("\n💡 Suggested Movies:")
    for movie in suggested_movies:
        print(f"- {movie}")

    # Final display
    display_movies(favorite_movies)


if __name__ == "__main__":
    main()
