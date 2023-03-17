-- Dumped database `|”
SELECT tv_s.title, tv_s_g.genre_id FROM tv_shows tv_s
JOIN tv_show_genres tv_s_g ORDER BY tv_s.title, tv_s_g.genre_id
