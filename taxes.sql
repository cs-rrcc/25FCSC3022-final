-- CSC 3022: Security Fundamentals and Databases
-- Instructor: Thyago Mota
-- Student(s): 
-- Description: MySQL Script for the taxes database

CREATE DATABASE taxes;

use taxes

CREATE TABLE Clients (
    Email VARCHAR(100) NOT NULL PRIMARY KEY,
    Name VARCHAR(100),
    SSN CHAR(11) UNIQUE,
    MaritalStatus ENUM('Single', 'Married', 'Divorced', 'Widowed'),
    SpouseName VARCHAR(100),
    SpouseSSN CHAR(11),
    Address TEXT,
    FilingJointly BOOLEAN
);

INSERT INTO Clients VALUES (
    'alice.johnson@example.com', 'Alice Johnson', '123-45-6789', 'Single', NULL, NULL,
    '123 Maple Street, Denver, CO 80201', FALSE
);

INSERT INTO Clients VALUES (
    'bob.smith@example.com', 'Bob Smith', '987-65-4321', 'Single', NULL, NULL,
    '456 Oak Avenue, Lakewood, CO 80226', FALSE
);

INSERT INTO Clients VALUES (
    'carol.martinez@example.com', 'Carol Martinez', '111-22-3333', 'Married', 'David Martinez', '444-55-6666',
    '789 Pine Road, Aurora, CO 80012', TRUE
);

CREATE TABLE FiscalYears (
    ClientEmail VARCHAR(100),
    Year YEAR,
    FinalTaxAmount DECIMAL(12,2),
    TaxesCompleted BOOLEAN,
    PRIMARY KEY (ClientEmail, Year),
    FOREIGN KEY (ClientEmail) REFERENCES Clients(Email)
);

INSERT INTO FiscalYears VALUES
('alice.johnson@example.com', 2022, 6200.00, TRUE),
('alice.johnson@example.com', 2023, 6400.00, TRUE),
('alice.johnson@example.com', 2024, 6600.00, FALSE);

INSERT INTO FiscalYears VALUES
('bob.smith@example.com', 2022, 7800.00, TRUE),
('bob.smith@example.com', 2023, 8000.00, TRUE),
('bob.smith@example.com', 2024, 8200.00, TRUE);

INSERT INTO FiscalYears VALUES
('carol.martinez@example.com', 2022, 9200.00, TRUE),
('carol.martinez@example.com', 2023, 9500.00, TRUE),
('carol.martinez@example.com', 2024, 9800.00, FALSE);

CREATE TABLE Earnings (
    ClientEmail VARCHAR(100),
    Year YEAR,
    Seq INT, 
    SourceName VARCHAR(100),
    Amount DECIMAL(12,2),
    PRIMARY KEY (ClientEmail, Year, SourceName, Seq),
    FOREIGN KEY (ClientEmail, Year) REFERENCES FiscalYears(ClientEmail, Year)
);

INSERT INTO Earnings VALUES
('alice.johnson@example.com', 2022, 1, 'TechCorp', 45000.00),
('alice.johnson@example.com', 2022, 2, 'Freelance Design', 10000.00);

INSERT INTO Earnings VALUES
('alice.johnson@example.com', 2023, 1, 'TechCorp', 47000.00),
('alice.johnson@example.com', 2023, 2, 'Freelance Design', 11000.00);

INSERT INTO Earnings VALUES
('alice.johnson@example.com', 2024, 1, 'TechCorp', 48000.00),
('alice.johnson@example.com', 2024, 2, 'Freelance Design', 12000.00);

INSERT INTO Earnings VALUES
('bob.smith@example.com', 2022, 1, 'HealthPlus', 60000.00),
('bob.smith@example.com', 2022, 2, 'Stock Dividends', 12000.00);

INSERT INTO Earnings VALUES
('bob.smith@example.com', 2023, 1, 'HealthPlus', 62000.00),
('bob.smith@example.com', 2023, 2, 'Stock Dividends', 13000.00);

INSERT INTO Earnings VALUES
('bob.smith@example.com', 2024, 1, 'HealthPlus', 63000.00),
('bob.smith@example.com', 2024, 2, 'Stock Dividends', 14000.00);

INSERT INTO Earnings VALUES
('carol.martinez@example.com', 2022, 1, 'EduWorld', 50000.00),
('carol.martinez@example.com', 2022, 2, 'BuildCo', 48000.00);

INSERT INTO Earnings VALUES
('carol.martinez@example.com', 2023, 1, 'EduWorld', 52000.00),
('carol.martinez@example.com', 2023, 2, 'BuildCo', 50000.00);

INSERT INTO Earnings VALUES
('carol.martinez@example.com', 2024, 1, 'EduWorld', 53000.00),
('carol.martinez@example.com', 2024, 2, 'BuildCo', 52000.00);

-- TODO: Create a view named ClientYearlyEarnings that generates the following output based on the initial data inserted above.
-- +----------------------------+----------------+------+-------------+
-- | Email                      | Name           | Year | TotalEarned |
-- +----------------------------+----------------+------+-------------+
-- | alice.johnson@example.com  | Alice Johnson  | 2022 |    55000.00 |
-- | alice.johnson@example.com  | Alice Johnson  | 2023 |    58000.00 |
-- | alice.johnson@example.com  | Alice Johnson  | 2024 |    60000.00 |
-- | bob.smith@example.com      | Bob Smith      | 2022 |    72000.00 |
-- | bob.smith@example.com      | Bob Smith      | 2023 |    75000.00 |
-- | bob.smith@example.com      | Bob Smith      | 2024 |    77000.00 |
-- | carol.martinez@example.com | Carol Martinez | 2022 |    98000.00 |
-- | carol.martinez@example.com | Carol Martinez | 2023 |   102000.00 |
-- | carol.martinez@example.com | Carol Martinez | 2024 |   105000.00 |
-- +----------------------------+----------------+------+-------------+

-- This table is for the app authentication purposes
CREATE TABLE Users (
    Id VARCHAR(30) NOT NULL PRIMARY KEY, 
    Name VARCHAR(30) NOT NULL, 
    Password VARCHAR(255) NOT NULL,
    Authorized BOOLEAN NOT NULL DEFAULT FALSE
);

-- Use the following statement to authorized registered users
-- UPDATE Users
-- SET Authorized = TRUE
-- WHERE Id = 'janet';

CREATE USER 'tax_reader'@'%' IDENTIFIED BY '024680';
GRANT SELECT ON taxes.* TO 'tax_reader'@'%';

CREATE USER 'tax_writer'@'%' IDENTIFIED BY '135791';
GRANT ALL ON taxes.* TO 'tax_writer'@'%';
