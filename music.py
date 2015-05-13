
import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Track")
    cur.execute("CREATE TABLE Track(UId INT PRIMARY KEY,track_id INT ,Track_type VARCHAR(25),album_id VARCHAR(25))")
    cur.execute("DROP TABLE IF EXISTS Album")
    cur.execute("CREATE TABLE Album(album_id INT PRIMARY KEY,album_name VARCHAR(25),gnid INT,album_url VARCHAR(25))")
    cur.execute("DROP TABLE IF EXISTS mood")
    cur.execute("CREATE TABLE mood(mood_id INT PRIMARY KEY,mood_name VARCHAR(25))")
    cur.execute("DROP TABLE IF EXISTS Track_mood")
    cur.execute("CREATE TABLE Track_mood(track_id INT PRIMARY KEY,mood_id INT )")
    cur.execute("DROP TABLE IF EXISTS Playlist_phone")
    cur.execute("CREATE TABLE Playlist_phone(UID INT,track_id INT,album_name VARCHAR(25),artist_name VARCHAR(25),PRIMARY KEY(UID,track_id))")
    cur.execute("DROP TABLE IF EXISTS Recomm_tracks")
    cur.execute("CREATE TABLE Recomm_tracks(track_id INT,recomm_track_id INT)")
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("CREATE TABLE User(UID INT PRIMARY KEY,fb_id VARCHAR(40),fb_name VARCHAR(25),first_name VARCHAR(25))")
    
    
