CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    user_type TEXT NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS searches (
    search TEXT NOT NULL,
    time_stamp DATETIME
);

/* org info section */

CREATE TABLE IF NOT EXISTS orgs (
    org_name TEXT PRIMARY KEY AUTOINCREMENT NOT NULL, 
    username TEXT NOT NULL, /* i.e. who is this org account owned by */
    desc_ TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orgs_loc (
    org_name TEXT PRIMARY KEY AUTOINCREMENT NOT NULL,
    country TEXT NOT NULL,
    region TEXT NOT NULL, /*this just means the state (in the US)*/
    zip INT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orgs_contact (
    org_name TEXT PRIMARY KEY AUTOINCREMENT NOT NULL,
    phone TEXT NOT NULL, /*interpret as an int, and remove the "-" and "()"*/
    email TEXT NOT NULL
);

/* there's a weird CREATE TABLE sqlite_sequence(name,seq); when you create it idk why lol */