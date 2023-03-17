-- Dumped database `|”
USE hbtn_0d_tvshows;
SELECT tv_s.title, tv_s_g.genre_id FROM hbtn_0d_tvshows.tv_shows tv_s
JOIN hbtn_0d_tvshows.tv_show_genres tv_s_g
ORDER BY tv_s.title, tv_s_g.genre_id
