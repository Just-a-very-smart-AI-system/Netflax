from fetch_movies import *
from sql import *
import pymysql 

# Kết nối đến cơ sở dữ liệu
connect = connect_to_db()
cursor = connect.cursor()

# Các danh mục phim
categories = {
    "Trending_Now": get_trending_now,
    "Original": get_originals,
    "Top_Rated": get_top_rated,
    "Action": get_action_movies,
    "Adventure": get_adventure_movies,
    "Animation": get_animation_movies,
    "Crime": get_crime_movies,
    "Comedy": get_comedy_movies,
    "Documentary": get_documentary_movies,
    "Drama": get_drama_movies,
    "Family": get_family_movies,
    "Fantasy": get_fantasy_movies,
    "History": get_history_movies,
    "Horror": get_horror_movies,
    "Music": get_music_movies,
    "Mystery": get_mystery_movies,
    "Science_Fiction": get_science_fiction_movies,
    "Thriller": get_thriller_movies,
    "TV_Movies": get_tv_movies,
    "War": get_war_movies,
    "Western": get_western_movies
}

# Hàm lưu phim vào cơ sở dữ liệu
def save_movies(movie):
    try:
        sql_query = """
        INSERT INTO movies(id, name, url)
        VALUES(%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            url = VALUES(url)
        """
        cursor.execute(sql_query, (movie['id'], movie['name'], movie['url']))
        connect.commit()
        print(f"Đã lưu phim: {movie['name']}")
    except Exception as e:
        print(f"Lỗi khi lưu phim {movie['name']} (ID: {movie['id']}): {e}")
        
def save_to_category(id_category, movies):
    try:
        sql_query = """
        INSERT INTO movie_category(movie_id, category_id)
        VALUES(%s, %s)
        ON DUPLICATE KEY UPDATE
            category_id = VALUES(category_id)
        """
        for movie in movies:
            cursor.execute(sql_query, (movie['id'], id_category))
            connect.commit()
            print(f"Đã lưu phim: {movie['name']}")
    except Exception as e:
        print(f"Lỗi khi lưu phim (ID: {movie.get('id', 'Unknown')}): {e}")
        
        
categories = {
    "Trending_Now": get_trending_now,
    "Original": get_originals,
    "Top_Rated": get_top_rated,
    "Action": get_action_movies,
    "Adventure": get_adventure_movies,
    "Animation": get_animation_movies,
    "Crime": get_crime_movies,
    "Comedy": get_comedy_movies,
    "Documentary": get_documentary_movies,
    "Drama": get_drama_movies,
    "Family": get_family_movies,
    "Fantasy": get_fantasy_movies,
    "History": get_history_movies,
    "Horror": get_horror_movies,
    "Music": get_music_movies,
    "Mystery": get_mystery_movies,
    "Science_Fiction": get_science_fiction_movies,
    "Thriller": get_thriller_movies,
    "TV_Movies": get_tv_movies,
    "War": get_war_movies,
    "Western": get_western_movies
}

save_to_category(1, categories["Trending_Now"]());
save_to_category(2, categories["Original"]());
save_to_category(3, categories["Top_Rated"]());
save_to_category(5, categories["Action"]());
save_to_category(6, categories["Adventure"]());
save_to_category(7, categories["Animation"]());
save_to_category(8, categories["Crime"]());
save_to_category(9, categories["Comedy"]());
save_to_category(10, categories["Documentary"]());
save_to_category(11, categories["Drama"]());
save_to_category(12, categories["Family"]());
save_to_category(13, categories["Fantasy"]());
save_to_category(14, categories["History"]());
save_to_category(15, categories["Horror"]());
save_to_category(16, categories["Music"]());
save_to_category(17, categories["Mystery"]());
save_to_category(18, categories["Science_Fiction"]());
save_to_category(19, categories["Thriller"]());
save_to_category(20, categories["TV_Movies"]());
save_to_category(21, categories["War"]());
save_to_category(22, categories["Western"]());



# # Lặp qua từng danh mục và lưu phim
# for category, fetch_function in categories.items():
#     try:
#         print(f"Đang lấy phim từ danh mục {category}...")
#         movies = fetch_function()  # Lấy danh sách phim từ danh mục
#         for movie in movies:
#             save_movies(movie)  # Lưu từng phim
#     except Exception as e:
#         print(f"Lỗi khi xử lý danh mục {category}: {e}")


# Đóng kết nối cơ sở dữ liệu
cursor.close()
connect.close()
