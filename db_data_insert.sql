## Insert Data into tourists Table.
INSERT INTO tourists (name, nationality, email, phone, passport_no) VALUES
('Anil Kumar', 'India', 'anil@example.com', '+91-9000000001', 'INP123456'),
('Emily Smith', 'USA', 'emily@example.com', '+1-555-1234', 'US123456'),
('Thabo Mokoena', 'South Africa', 'thabo@example.co.za', '+27-845678900', 'SA789012');


## Insert Data into reverse Table.
INSERT INTO reserves (name, location, area_sq_km, description) VALUES
('Kruger National Park', 'Limpopo and Mpumalanga', 19485.0, 'One of Africa’s largest game reserves.'),
('Addo Elephant Park', 'Eastern Cape', 1640.0, 'Known for elephants and Big Five.'),
('Pilanesberg Game Reserve', 'North West Province', 572.0, 'Volcanic crater reserve.');


## Insert Data into wildlife Table.
INSERT INTO wildlife (name, species, reserve_id, population_estimate) VALUES
('African Elephant', 'Loxodonta africana', 1, 13000),
('Lion', 'Panthera leo', 1, 1500),
('Cape Buffalo', 'Syncerus caffer', 2, 3000),
('Rhinoceros', 'Ceratotherium simum', 3, 500);


##Insert Data into safari_packages Table.
INSERT INTO safari_packages (name, duration_days, price, reserve_id, description) VALUES
('Big Five Safari', 5, 25000.00, 1, 'See all Big Five animals in Kruger.'),
('Elephant Experience', 3, 15000.00, 2, 'Focus on elephants and nature walks.'),
('Volcano Trail Safari', 2, 10000.00, 3, 'Scenic safari inside extinct volcano.');



##Insert Data into guide Table.
INSERT INTO guides (name, language_spoken, experience_years, reserve_id) VALUES
('Sipho Dlamini', 'English, Zulu', 10, 1),
('Linda Mabuza', 'English, Afrikaans', 5, 2),
('Mark Peterson', 'English', 7, 3);


##Insert Data into bookings Table.
INSERT INTO bookings (tourist_id, package_id, guide_id, booking_date, travel_date, num_people, total_amount, status) VALUES
(1, 1, 1, '2025-06-01', '2025-07-10', 2, 50000.00, 'Confirmed'),
(2, 2, 2, '2025-06-10', '2025-08-05', 1, 15000.00, 'Pending'),
(3, 3, 3, '2025-06-15', '2025-09-01', 3, 30000.00, 'Confirmed');


##Insert Data into transport_services.
INSERT INTO transport_services (service_type, capacity, available, reserve_id) VALUES
('Jeep', 6, TRUE, 1),
('Bus', 20, TRUE, 2),
('Helicopter', 4, FALSE, 3);


