-- checkpointdb.sql

-- Drop tables if they exist to make the script re-runnable
DROP TABLE IF EXISTS ITEMS;
DROP TABLE IF EXISTS CONTACTS;
DROP TABLE IF EXISTS CONTACT_TYPES;
DROP TABLE IF EXISTS CONTACT_CATEGORIES;

-- Create CONTACT_TYPES table
CREATE TABLE CONTACT_TYPES (
    id SERIAL PRIMARY KEY,
    contact_type VARCHAR(50)
);

-- Create CONTACT_CATEGORIES table
CREATE TABLE CONTACT_CATEGORIES (
    id SERIAL PRIMARY KEY,
    contact_category VARCHAR(50)
);

-- Create CONTACTS table
CREATE TABLE CONTACTS (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    title VARCHAR(50),
    organization VARCHAR(100)
);

-- Create ITEMS table
CREATE TABLE ITEMS (
    id SERIAL PRIMARY KEY,
    contact VARCHAR(100),
    contact_id INT,
    contact_type_id INT,
    contact_category_id INT,
    FOREIGN KEY (contact_id) REFERENCES CONTACTS(id),
    FOREIGN KEY (contact_type_id) REFERENCES CONTACT_TYPES(id),
    FOREIGN KEY (contact_category_id) REFERENCES CONTACT_CATEGORIES(id)
);

-- Insert data into CONTACT_TYPES table
INSERT INTO CONTACT_TYPES (contact_type) VALUES
('Email'),
('Phone'),
('Skype'),
('Instagram');

-- Insert data into CONTACT_CATEGORIES table
INSERT INTO CONTACT_CATEGORIES (contact_category) VALUES
('Home'),
('Work'),
('Fax');

-- Insert data into CONTACTS table
INSERT INTO CONTACTS (first_name, last_name, title, organization) VALUES
('Erik', 'Eriksson', 'Teacher', 'Utbildning AB'),
('Anna', 'Sundh', NULL, NULL),
('Goran', 'Bregovic', 'Coach', 'Dalens IK'),
('Ann-Marie', 'Bergqvist', 'Cousin', NULL),
('Herman', 'Appelkvist', NULL, NULL);

-- Insert data into ITEMS table
INSERT INTO ITEMS (contact, contact_id, contact_type_id, contact_category_id) VALUES
('011-12 33 45', 3, 2, 1),
('goran@infoab.se', 3, 1, 2),
('010-88 55 44', 4, 2, 2),
('erik57@hotmail.com', 1, 1, 1),
('@annapanna99', 2, 4, 1),
('077-563578', 2, 2, 1),
('070-156 22 78', 3, 2, 2);

-- Task 1.5: Add your own name and a contact
INSERT INTO CONTACTS (first_name, last_name, title, organization) VALUES
('Zakariya', 'Farah', 'Data Engineer', 'Academic Work');

INSERT INTO ITEMS (contact, contact_id, contact_type_id, contact_category_id) VALUES
('zakariya@yahoo.com', 6, 1, 2);

-- Task 1.6: Query to list unused contact_types
-- This query identifies contact_types that are not used in the ITEMS table
SELECT ct.contact_type
FROM CONTACT_TYPES ct
LEFT JOIN ITEMS i ON ct.id = i.contact_type_id
WHERE i.contact_type_id IS NULL;

-- Task 1.7: Create a VIEW to list contacts
CREATE VIEW view_contacts AS
SELECT c.first_name, c.last_name, i.contact, ct.contact_type, cc.contact_category
FROM CONTACTS c
JOIN ITEMS i ON c.id = i.contact_id
JOIN CONTACT_TYPES ct ON i.contact_type_id = ct.id
JOIN CONTACT_CATEGORIES cc ON i.contact_category_id = cc.id;

-- Task 1.8: Query to list all information without id columns
SELECT c.first_name, c.last_name, c.title, c.organization, i.contact, ct.contact_type, cc.contact_category
FROM CONTACTS c
JOIN ITEMS i ON c.id = i.contact_id
JOIN CONTACT_TYPES ct ON i.contact_type_id = ct.id
JOIN CONTACT_CATEGORIES cc ON i.contact_category_id = cc.id;

--Task 1.9: Provide feedback on an alternate ITEMS table solution:
--Another possible design for the ITEMS table would be to further normalise the contact information.
--For example, rather of putting contact information straight in the ITEMS table, we could make a different -- table (like EMAIL_CONTACTS or PHONE_CONTACTS) and include references to these tables in the ITEMS table.
--By guaranteeing that all contact detail is kept in a table unique to its kind, this method would lessen redundancy and enhance data integrity. Sample SQL for this kind of design:

-- CREATE TABLE EMAIL_CONTACTS (
--     id SERIAL PRIMARY KEY,
--     email VARCHAR(100)
-- );

-- CREATE TABLE PHONE_CONTACTS (
--     id SERIAL PRIMARY KEY,
--     phone_number VARCHAR(20)
-- );

-- CREATE TABLE ITEMS (
--     id SERIAL PRIMARY KEY,
--     contact_id INT,
--     contact_type_id INT,
--     contact_category_id INT,
--     email_contact_id INT,
--     phone_contact_id INT,
--     FOREIGN KEY (contact_id) REFERENCES CONTACTS(id),
--     FOREIGN KEY (contact_type_id) REFERENCES CONTACT_TYPES(id),
--     FOREIGN KEY (contact_category_id) REFERENCES CONTACT_CATEGORIES(id),
--     FOREIGN KEY (email_contact_id) REFERENCES EMAIL_CONTACTS(id),
--     FOREIGN KEY (phone_contact_id) REFERENCES PHONE_CONTACTS(id)
-- );

-- In this alternative design, the ITEMS table contains references to the appropriate contact type tables.
-- This allows for more detailed and structured storage of contact information.

