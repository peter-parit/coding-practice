SELECT DISTINCT ON
    (player_id) player_id,
    event_date as first_login
FROM Activity
ORDER BY player_id, event_date