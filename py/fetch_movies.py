import requests

# Hàm fetchMovies sẽ thực hiện yêu cầu GET và trả về danh sách các bộ phim
def fetch_movies(url, path_type):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        movies_list = []
        
        for movie in data['results']:
            movie_data = {
                'id': movie['id'],
                'url': f"https://image.tmdb.org/t/p/original{movie[path_type]}",
                'name': movie.get('title', movie.get('name', 'No Title'))
            }
            movies_list.append(movie_data)
        # for movie in movies_list:
        #     print(f"Movie: ", movie)
        return movies_list
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

# ** Function that fetches Netflix Originals **
def get_originals():
    url = 'https://api.themoviedb.org/3/discover/tv?api_key=19f84e11932abbc79e6d83f82d6d1045&with_networks=213&page=1'
    return fetch_movies(url, 'poster_path')

# ** Function that fetches Trending Movies **
def get_trending_now():
    url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=19f84e11932abbc79e6d83f82d6d1045&language=en-US&page=1'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Top Rated Movies **
def get_top_rated():
    url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=19f84e11932abbc79e6d83f82d6d1045&language=en-US&page=1'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Action Movies **
def get_action_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=28'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Adventure Movies **
def get_adventure_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=12'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Animation Movies **
def get_animation_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=16'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Thriller Movies **
def get_thriller_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=53'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Science Fiction Movies **
def get_science_fiction_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=878'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Crime Movies **
def get_crime_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=80'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Comedy Movies **
def get_comedy_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=35'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Documentary Movies **
def get_documentary_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=99'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Drama Movies **
def get_drama_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=18'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Family Movies **
def get_family_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=10751'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Fantasy Movies **
def get_fantasy_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=14'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches History Movies **
def get_history_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=36'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Horror Movies **
def get_horror_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=27'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Music Movies **
def get_music_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=10402'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Mystery Movies **
def get_mystery_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=9648'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches TV Movies **
def get_tv_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=10770'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches War Movies **
def get_war_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=10752'
    return fetch_movies(url, 'backdrop_path')

# ** Function that fetches Western Movies **
def get_western_movies():
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=19f84e11932abbc79e6d83f82d6d1045&with_genres=37'
    return fetch_movies(url, 'backdrop_path')