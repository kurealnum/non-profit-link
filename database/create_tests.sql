INSERT INTO basic_users (username, user_type, password_hash) VALUES ('TESTDUMMY', 'FIGUREOUTUSERTYPE', 'password');

INSERT INTO orgs (org_name, user_id) VALUES ('myorg', 1);

INSERT INTO orgs_info (org_name, desc_, website) VALUES ('myorg', 'A test org', 'mywebsite.com');

INSERT INTO orgs_loc (org_name, country, region, zip, city, street_address) VALUES ('myorg', 'United States of America', 'New Mexico', '87104', 'Albuquerque','308 Negra Arroyo Lane');

INSERT INTO orgs_contact(org_name, phone, email) VALUES ('myorg', '540-400-4000', 'walterhartwellwhite@gmail.com');
