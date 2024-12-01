CREATE USER 'diot'@'localhost' IDENTIFIED BY 'Diot@1234';

GRANT ALL PRIVILEGES ON weather_db.* TO 'diot'@'localhost';

FLUSH PRIVILEGES;
