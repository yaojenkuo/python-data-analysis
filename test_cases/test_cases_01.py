import unittest

class TestWebScraping(unittest.TestCase):
    def test_number_of_nba_teams(self):
        self.assertEqual(number_of_nba_teams("http://data.nba.net/prod/v2/2019/teams.json"), 30)
    def test_find_atlantic_southwest_teams(self):
        atlantic_southwest_teams = find_atlantic_southwest_teams("http://data.nba.net/prod/v2/2019/teams.json")
        self.assertEqual(atlantic_southwest_teams['Atlantic'], ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers', 'Toronto Raptors'])
        self.assertEqual(atlantic_southwest_teams['Southwest'], ['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans', 'San Antonio Spurs'])
    def test_get_tpe_711_stores(self):
        tpe_711_stores = get_tpe_711_stores("https://emap.pcsc.com.tw/EMapSDK.aspx")
        self.assertEqual(tpe_711_stores["松山區"][0], {'POIID': '170945', 'POIName': '上弘', 'Longitude': 121.548287390895, 'Latitude': 25.056390968531797, 'Address': '台北市松山區敦化北路168號B2'})
        self.assertEqual(tpe_711_stores["信義區"][0], {'POIID': '167651', 'POIName': '一零一', 'Longitude': 121.565077, 'Latitude': 25.033373, 'Address': '台北市信義區信義路五段7號35樓'})
        self.assertEqual(tpe_711_stores["大安區"][0], {'POIID': '153319', 'POIName': '大台', 'Longitude': 121.53261437826, 'Latitude': 25.0179598345753, 'Address': '台北市大安區羅斯福路三段283巷14弄16號1樓'})
    def test_find_endgame_genre(self):
        self.assertEqual(find_endgame_genre("https://www.imdb.com/title/tt4154796"), ['Action', 'Adventure', 'Drama'])
    def test_find_endgame_cast(self):
        self.assertEqual(find_endgame_cast("https://www.imdb.com/title/tt4154796"), ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly'])
    def test_get_movie_data(self):
        movie_data = get_movie_data("https://www.imdb.com/title/tt4154796")
        self.assertEqual(movie_data["movieTitle"], 'Avengers: Endgame(2019)')
        self.assertEqual(movie_data["moviePoster"], 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg')
        self.assertEqual(movie_data["movieGenre"], ['Action', 'Adventure', 'Drama'])
        self.assertEqual(movie_data["movieCast"], ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestWebScraping)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)