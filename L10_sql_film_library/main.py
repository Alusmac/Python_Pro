from film_library.db import init_db
from film_library.services.movie_service import MovieService
from film_library.services.actor_service import ActorService
from film_library.services.reporting_service import ReportingService
from film_library.tools.inspectors import (
    validate_movie_title,
    validate_movie_year,
    validate_genre,
    normalize_title_case,
    validate_actor_name,
    validate_actor_birth_year,
    get_int,
    non_empty_string
)

init_db()

movie_service = MovieService()
actor_service = ActorService()
reporting_service = ReportingService()


def print_menu():
    print("""
1. Add movie
2. Add actor
3. Show all movies with actors
4. Show unique genres
5. Show number of movies by genre
6. Show average birth year of actors in a specific genre
7. Search movie by title
8. Show movies (with pagination)
9. Show all actors and movie titles
10. Show movies with their age
0. Exit
""")


def main():
    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            try:
                title = non_empty_string("Movie title: ")
                validate_movie_title(title)
                title = normalize_title_case(title)

                release_year = get_int("Release year: ", min_value=1888, max_value=2100)
                validate_movie_year(release_year)

                genre = non_empty_string("Genre: ")
                validate_genre(genre)
                genre = normalize_title_case(genre)

                actors_input = input("Actor names separated by comma (leave empty if none): ")
                actor_names = (
                    [normalize_title_case(a.strip()) for a in actors_input.split(",") if a.strip()]
                    if actors_input else None
                )

                movie_id = movie_service.add_movie(title, release_year, genre, actor_names)
                print(f"Movie added with ID: {movie_id}")

            except ValueError as e:
                print(f"Input error: {e}")


        elif choice == "2":
            try:
                name = non_empty_string("Actor name: ")
                validate_actor_name(name)
                name = normalize_title_case(name)

                birth_year_input = input("Birth year (optional): ").strip()
                birth_year = int(birth_year_input) if birth_year_input else None
                validate_actor_birth_year(birth_year)

                actor_id = actor_service.add_actor(name, birth_year)
                print(f"Actor added with ID: {actor_id}")

            except ValueError as e:
                print(f"Input error: {e}")



        elif choice == "3":
            print("\nMovies with actors:")
            movies_with_actors = reporting_service.movies_with_actors()
            if not movies_with_actors:
                print("No movies found.")
            else:
                for idx, (title, actors) in enumerate(movies_with_actors, start=1):
                    if actors and isinstance(actors, str):
                        actors = [a.strip() for a in actors.split(",") if a.strip()]
                    actor_list = ", ".join(actors) if actors else "No actors"
                    print(f"{idx}. Movie: \"{title}\", Actors: {actor_list}")


        elif choice == "4":
            print("\nUnique genres:")
            genres = reporting_service.unique_genres()

            if not genres:
                print("No genres found.")
            else:
                for g in genres:
                    print(f"- {g}")


        elif choice == "5":
            print("\nGenres and number of movies:")
            movies_by_genre = reporting_service.count_movies_by_genre()

            if not movies_by_genre:
                print("No genres found.")
            else:
                for idx, (genre, count) in enumerate(movies_by_genre, start=1):
                    print(f"{idx}. {genre}: {count}")


        elif choice == "6":
            genre = normalize_title_case(non_empty_string("Enter genre: "))
            avg_year = reporting_service.avg_actor_birth_by_genre(genre)

            if avg_year:
                print(f"Average birth year of actors in '{genre}': {avg_year:.2f}")
            else:
                print(f"No data found for genre '{genre}'.")


        elif choice == "7":
            keyword = non_empty_string("Enter keyword to search: ")
            movies = reporting_service.search_movies_like(keyword)

            if movies:
                print("Found movies:")
                for m in movies:
                    print(f"- {m[1]} ({m[2]})")
            else:
                print("No movies found.")


        elif choice == "8":
            limit = get_int("How many movies per page? ", min_value=1)

            total = movie_service.get_total_count()
            if total == 0:
                print("No movies available.")
                continue

            for offset in range(0, total, limit):
                movies = movie_service.get_paginated_movies(limit, offset)
                print(f"\nPage {offset // limit + 1}:")

                for m in movies:
                    print(f"- {m[1]}")

                cont = input("Next page? (y/n): ").strip().lower()
                if cont != "y":
                    break


        elif choice == "9":
            print("\nAll actors and movie titles:")
            for name in reporting_service.all_actors_and_movies_union():
                print(f"- {name}")


        elif choice == "10":
            print("\nMovies with age:")
            for title, age in reporting_service.movies_with_age():
                print(f"- {title}: {age} years old")


        elif choice == "0":
            print("Exiting... Have a nice day!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
