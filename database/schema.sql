CREATE TABLE IF NOT EXISTS basic_users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    user_type TEXT NOT NULL,
    password_hash TEXT NOT NULL
);

/* searches info */

CREATE TABLE IF NOT EXISTS searches (
    search_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    search TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS searches_time (
    search_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    time_stamp DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

/* org info section */

CREATE TABLE IF NOT EXISTS orgs (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    org_name TEXT NOT NULL, 
    user_id INT NOT NULL, /* i.e. who is this org account owned by. don't autoincrement this */
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS orgs_info (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    org_name TEXT NOT NULL, 
    desc_ TEXT NOT NULL,
    website TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

CREATE TABLE IF NOT EXISTS orgs_loc (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    org_name TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT NOT NULL, /*this just means the state (in the US)*/
    zip INT NOT NULL,
    city TEXT NOT NULL,
    street_address TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

CREATE TABLE IF NOT EXISTS orgs_contact (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    org_name TEXT NOT NULL,
    phone TEXT NOT NULL, /*interpret as an int, and remove the "-" and "()"*/
    email TEXT NOT NULL,
    FOREIGN KEY (org_name) REFERENCES orgs(org_name)
);

/* there's a weird CREATE TABLE sqlite_sequence(name,seq); when you create it idk why lol */