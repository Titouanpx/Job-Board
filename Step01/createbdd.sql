CREATE DATABASE jobboardbdd;

CREATE TABLE advertisements 
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	description VARCHAR(255), 
	wage INT, 
	place VARCHAR(255), 
	working_time INT
);
CREATE TABLE people
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(255),
	lastname VARCHAR(255), 
	email VARCHAR(255),
	phone VARCHAR(255),
	identifiant VARCHAR(255), 
	password VARCHAR(255), 
	role VARCHAR(255)
);
CREATE TABLE companies
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	name VARCHAR(255),
	description VARCHAR(255)
);
CREATE TABLE jobApplication
(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	email VARCHAR(255)
);
ALTER TABLE advertisements
ADD id_people INT;
ALTER TABLE advertisements
ADD FOREIGN KEY (id_people) REFERENCES people(id); 

ALTER TABLE advertisements
ADD id_companies INT;
ALTER TABLE advertisements
ADD FOREIGN KEY (id_companies) REFERENCES companies(id); 

ALTER TABLE jobApplication
ADD id_ad INT;
ALTER TABLE jobApplication
ADD FOREIGN KEY (id_ad) REFERENCES advertisements(id);

ALTER TABLE jobApplication
ADD id_people INT;
ALTER TABLE jobApplication
ADD FOREIGN KEY (id_people) REFERENCES people(id);

ALTER TABLE advertisements
ADD id_company INT;
ALTER TABLE advertisements
ADD FOREIGN KEY (id_company) REFERENCES companies(id);

ALTER TABLE people
ADD id_company INT;
ALTER TABLE people
ADD FOREIGN KEY (id_company) REFERENCES companies(id);


