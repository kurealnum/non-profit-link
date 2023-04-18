CREATE TABLE IF NOT EXISTS searches (
    search TEXT NOT NULL,
    time_stamp DATETIME
);

CREATE TABLE IF NOT EXISTS orgs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    zip INT NOT NULL,
    desc_ TEXT,
    phone INT,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orgs_contact (
    email TEXT NOT NULL,
    phone INT NOT NULL
);
    