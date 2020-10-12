CREATE DATABASE jobboarddb;

CREATE TABLE jobboarddb.advertisements 
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	description VARCHAR(255), 
	wage INT, 
	place VARCHAR(255), 
	working_time INT
);
CREATE TABLE jobboarddb.people
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(255),
	lastname VARCHAR(255), 
	email VARCHAR(255) UNIQUE,
	phone VARCHAR(255),
	pseudonym VARCHAR(255) UNIQUE, 
	password VARCHAR(255), 
	role VARCHAR(255)
);
CREATE TABLE jobboarddb.companies
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	name VARCHAR(255),
	description VARCHAR(255)
);
CREATE TABLE jobboarddb.jobApplication
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	email VARCHAR(255)
);
ALTER TABLE jobboarddb.advertisements
ADD id_people INT;
ALTER TABLE jobboarddb.advertisements
ADD FOREIGN KEY (id_people) REFERENCES people(id); 

ALTER TABLE jobboarddb.jobApplication
ADD id_ad INT;
ALTER TABLE jobboarddb.jobApplication
ADD FOREIGN KEY (id_ad) REFERENCES advertisements(id);

ALTER TABLE jobboarddb.jobApplication
ADD id_people INT;
ALTER TABLE jobboarddb.jobApplication
ADD FOREIGN KEY (id_people) REFERENCES people(id);

ALTER TABLE jobboarddb.advertisements
ADD id_company INT;
ALTER TABLE jobboarddb.advertisements
ADD FOREIGN KEY (id_company) REFERENCES companies(id);

ALTER TABLE jobboarddb.people
ADD id_company INT;
ALTER TABLE jobboarddb.people
ADD FOREIGN KEY (id_company) REFERENCES companies(id);

INSERT INTO jobboarddb.companies (id, name, description)
VALUES ('1', 'Epitech', "Coding school");
INSERT INTO jobboarddb.companies (id, name, description)
VALUES ('2', 'Samsic', "Cleaning company");
INSERT INTO jobboarddb.companies (id, name, description)
VALUES ('3', 'BMC', "Engineering company");

INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role, id_company)
VALUES ('1', 'Titouan', 'Proux', 'titouan@gmail.com', '0712345678', 'titouanpx', 'titouanmdp', 'admin', '1');
INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role, id_company)
VALUES ('2', 'Georges', 'Dupont', 'georges@free.fr', '0600305078', 'gdupont', 'mdpgeorges', 'in charge', '2');
INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role)
VALUES ('3', 'Bob', 'Durant', 'bobd@gmail.com', '0102030405', 'bobdrt', 'bobmdpbob', 'applying');
INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role, id_company)
VALUES ('4', 'Joe', 'Robert', 'joe@gmail.com', '0032211000', 'joerobert', 'joemdr', 'in charge', '3');
INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role)
VALUES ('5', 'Marius', 'Crusson', 'mamacru@gmail.com', '0105101520', 'marius15', 'mdpmarius15', 'applying');
INSERT INTO jobboarddb.people (id, firstname, lastname, email, phone, pseudonym, password, role)
VALUES ('6', 'Camille', 'Didier', 'cadi@gmail.com', '0650505080', 'cadi', 'cadimdp', 'applying');

INSERT INTO jobboarddb.advertisements (id, title, description, wage, place, working_time, id_people, id_company)
VALUES ('1', 'Full Stack Dev', 'looking for a full stack developer in our new company location', '2000', 'Nantes', '35', '1', '1');
INSERT INTO jobboarddb.advertisements (id, title, description, wage, place, working_time, id_people, id_company)
VALUES ('2', 'DevOps', 'looking for a devOps developer in our company', '3000', 'Paris', '40', '1', '1');
INSERT INTO jobboarddb.advertisements (id, title, description, wage, place, working_time, id_people, id_company)
VALUES ('3', 'Maid', 'looking for a maid to do the cleaning', '1200', 'Nantes', '30', '2', '2');
INSERT INTO jobboarddb.advertisements (id, title, description, wage, place, working_time, id_people, id_company)
VALUES ('4', 'Engineer R&D', 'Dental Monitoring is built around the idea of providing Dental Professionals with a way to remotely monitor their patients’ treatments, more accurately and regardless of their geographic location, thanks to our easy to use and unique AI driven device.', '5000', 'London', '40', '4', '3');

INSERT INTO jobboarddb.jobApplication (id, email, id_ad, id_people)
VALUES ('1', 'list of mails', '1', '3');
INSERT INTO jobboarddb.jobApplication (id, email, id_ad, id_people)
VALUES ('2', 'list of mails 2', '3', '5');
INSERT INTO jobboarddb.jobApplication (id, email, id_ad, id_people)
VALUES ('3', 'list of mails 3', '1', '6');

