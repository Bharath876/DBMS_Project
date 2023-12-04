-- Create Database
CREATE DATABASE IF NOT EXISTS WildlifeConservationDB;
USE WildlifeConservationDB;


-- Create Table for Animal Species
CREATE TABLE Users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL,
    pswd VARCHAR(50) NOT NULL
);

-- Create Table for Animal Species
CREATE TABLE Animal_Species (
    species_id INT PRIMARY KEY AUTO_INCREMENT,
    species_name VARCHAR(50) NOT NULL,
    scientific_name VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(20) NOT NULL,
    conservation_status VARCHAR(20) NOT NULL
);

-- Create Table for Individual Animals
CREATE TABLE Individual_Animals (
    animal_id INT PRIMARY KEY AUTO_INCREMENT,
    species_id INT,
    name VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female', 'Unknown') NOT NULL,
    birth_date DATE,
    arrival_date DATE,
    CONSTRAINT fk_species_id FOREIGN KEY (species_id) REFERENCES Animal_Species(species_id)
);



-- Create Table for Conservation Organizations
CREATE TABLE ConservationOrganizations (
    org_id INT PRIMARY KEY AUTO_INCREMENT,
    org_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(50),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20)
);

-- Create Table for Conservation Projects
CREATE TABLE ConservationProjects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2),
    org_id INT,
    CONSTRAINT fk_org_id FOREIGN KEY (org_id) REFERENCES ConservationOrganizations(org_id)
);



-- Create Table for Staff Members
CREATE TABLE Staff_Members (
    vet_id INT PRIMARY KEY AUTO_INCREMENT,
    vet_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20)
);

-- Create Table for Donations
CREATE TABLE Donations (
        DonationID INT AUTO_INCREMENT PRIMARY KEY,
        DonorName VARCHAR(255) NOT NULL,
        Amount DECIMAL(10, 2),
        DonationDate DATE,
        project_id INT,
        FOREIGN KEY (project_id) REFERENCES ConservationProjects(project_id)
    );

-- Insert Sample Data

-- Insert Sample Users
INSERT INTO Users (user_id, username, pswd)
VALUES
    (1, 'Bharath', '234'),
    (2, 'Harshal', '789');
    
-- Insert Sample Species
INSERT INTO Animal_Species (species_name, scientific_name, category, conservation_status)
VALUES 
    ('Lion', 'Panthera leo', 'Mammal', 'Vulnerable'),
    ('Bald Eagle', 'Haliaeetus leucocephalus', 'Bird', 'Least Concern'),
    ('Sea Turtle', 'Cheloniidae', 'Reptile', 'Endangered');

-- Insert Sample Animals
INSERT INTO Individual_Animals (species_id, name, gender, birth_date, arrival_date)
VALUES
    (1, 'Simba', 'Male', '2018-05-10', '2019-02-20'),
    (2, 'Freedom', 'Female', '2017-09-15', '2018-03-30'),
    (3, 'Shelly', 'Unknown', '2020-01-25', '2020-07-10');


-- Insert Sample Conservation Organizations
INSERT INTO ConservationOrganizations (org_name, contact_person, contact_email, contact_phone)
VALUES
    ('Wildlife Alliance', 'John Smith', 'john@wildlifealliance.org', '+1234567890'),
    ('Nature Conservation Society', 'Emily Johnson', 'emily@natureconservation.org', '+9876543210');

-- Insert Sample Conservation Projects
INSERT INTO ConservationProjects (ProjectID,project_name, start_date, end_date, budget, org_id)
VALUES
    (1,'Savanna Protection Project', '2021-01-01', '2022-01-01', 50000.00, 1),
    (2,'Sea Turtle Conservation', '2021-03-15', '2022-03-15', 35000.00, 2);

-- Insert Sample Staff_Members
INSERT INTO Staff_Members (vet_id,vet_name,specialization,contact_email,contact_phone)
VALUES
    (1, 'Rajesh','Zoological medicine','rajesh675@gmail.com', '8561237890'),
    (2, 'Mahesh','Ophthalmology','mahesh436@gmail.com','9456781232');
    
INSERT INTO Donations (DonationID, DonorName, Amount, DonationDate)
VALUES
	(1,'John Doe', 10000.00, '2023-11-20'),
    (2,'Jane Smith', 5000.00, '2023-11-21'),
    (3,'Bob Johnson', 75000.00, '2023-11-22');

-- Trigger to update last_updated timestamp on INSERT or UPDATE
DELIMITER //
CREATE TRIGGER update_animal_species_timestamp
BEFORE INSERT ON animal_species
FOR EACH ROW
SET NEW.last_updated = NOW();
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_animal_species_timestamp_update
BEFORE UPDATE ON animal_species
FOR EACH ROW
SET NEW.last_updated = NOW();
//
DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetSpeciesInfo(IN speciesName VARCHAR(50))
BEGIN
    SELECT * FROM Animal_Species WHERE species_name = speciesName;
END //

-- Create Database
CREATE DATABASE IF NOT EXISTS WildlifeConservationDB;
USE WildlifeConservationDB;

-- Create Tables (Previous code remains the same)

-- Trigger to update last_updated timestamp on INSERT or UPDATE
DELIMITER //
CREATE TRIGGER update_animal_species_timestamp
BEFORE INSERT ON Animal_Species
FOR EACH ROW
SET NEW.last_updated = NOW();
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_animal_species_timestamp_update
BEFORE UPDATE ON Animal_Species
FOR EACH ROW
SET NEW.last_updated = NOW();
//
DELIMITER ;

-- Stored Procedure to Get Species Info with JOIN
DELIMITER //
DELIMITER //

CREATE PROCEDURE GetProjectDetails(IN projectID INT)
BEGIN
    DECLARE orgName VARCHAR(100);
    DECLARE vetName VARCHAR(50);
    
    -- Get project details
    SELECT
        cp.project_id,
        cp.project_name,
        cp.start_date,
        cp.end_date,
        cp.budget,
        co.org_name
    INTO
        @project_id,
        @project_name,
        @start_date,
        @end_date,
        @budget,
        orgName
    FROM
        ConservationProjects cp
    JOIN
        ConservationOrganizations co ON cp.org_id = co.org_id
    WHERE
        cp.project_id = projectID;

    -- Get staff members involved in the project
    SELECT
        GROUP_CONCAT(sm.vet_name SEPARATOR ', ') AS staff_members
    INTO
        @staff_members
    FROM
        Staff_Members sm
    JOIN
        ConservationProjects cp ON sm.vet_id = cp.project_id
    WHERE
        cp.project_id = projectID;

    -- Return the result
    SELECT
        @project_id AS project_id,
        @project_name AS project_name,
        @start_date AS start_date,
        @end_date AS end_date,
        @budget AS budget,
        orgName AS organization_name,
        @staff_members AS staff_members;
END //

DELIMITER ;


-- Commit Changes
COMMIT;


DELIMITER ;
-- Commit Changes
COMMIT;
