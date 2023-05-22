CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    user_type TEXT NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS searches (
    user_id INTEGER NOT NULL,
    search TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS searches_time (
    user_id INTEGER NOT NULL,
    time_stamp DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

/* org info section */

CREATE TABLE IF NOT EXISTS orgs (
    org_name TEXT PRIMARY KEY NOT NULL, 
    user_id INT NOT NULL, /* i.e. who is this org account owned by. don't autoincrement this */
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS orgs_info (
    org_name TEXT PRIMARY KEY NOT NULL, 
    desc_ TEXT NOT NULL,
    website TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

CREATE TABLE IF NOT EXISTS orgs_loc (
    org_name TEXT PRIMARY KEY NOT NULL,
    country TEXT NOT NULL,
    region TEXT NOT NULL, /*this just means the state (in the US)*/
    zip INT NOT NULL,
    city TEXT NOT NULL,
    street_address TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

CREATE TABLE IF NOT EXISTS orgs_contact (
    org_name TEXT PRIMARY KEY NOT NULL,
    phone TEXT NOT NULL, /*interpret as an int, and remove the "-" and "()"*/
    email TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

/* there's a weird CREATE TABLE sqlite_sequence(name,seq); when you create it idk why lol */