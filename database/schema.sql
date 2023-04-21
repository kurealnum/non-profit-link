CREATE TABLE IF NOT EXISTS basic_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS searches (
    search TEXT NOT NULL,
    time_stamp DATETIME
);

CREATE TABLE IF NOT EXISTS orgs (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL, 
    zip INT NOT NULL,
    desc_ TEXT NOT NULL,
    phone INT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);

/* there's a weird CREATE TABLE sqlite_sequence(name,seq); when you create it idk why lol