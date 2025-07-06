CREATE TABLE tourists (
    tourist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    passport_no VARCHAR(50) UNIQUE,
    CHECK (CHAR_LENGTH(name) >= 8),
    CHECK (email LIKE '%_@__%.__%')
);

CREATE TABLE reserves (
    reserve_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    area_sq_km FLOAT,
    description TEXT
);

CREATE TABLE wildlife (
    animal_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    species VARCHAR(100),
    reserve_id INT,
    population_estimate INT,
    FOREIGN KEY (reserve_id) REFERENCES reserves(reserve_id)
);

CREATE TABLE safari_packages (
    package_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    duration_days INT,
    price DECIMAL(10,2),
    reserve_id INT,
    description TEXT,
	FOREIGN KEY (reserve_id) REFERENCES reserves(reserve_id)
);

CREATE TABLE guides (
    guide_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    language_spoken VARCHAR(100),
    experience_years INT,
    reserve_id INT,
    FOREIGN KEY (reserve_id) REFERENCES reserves(reserve_id)
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    tourist_id INT,
    package_id INT,
    guide_id INT,
    booking_date DATE,
    travel_date DATE,
    num_people INT,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    FOREIGN KEY (tourist_id) REFERENCES tourists(tourist_id),
    FOREIGN KEY (package_id) REFERENCES safari_packages(package_id),
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id)
);

CREATE TABLE transport_services (
    transport_id INT PRIMARY KEY AUTO_INCREMENT,
    service_type VARCHAR(50),
    capacity INT,
    available BOOLEAN,
    reserve_id INT,
    FOREIGN KEY (reserve_id) REFERENCES reserves(reserve_id)
);


