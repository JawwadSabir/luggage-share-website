-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 13, 2022 at 09:32 PM
-- Server version: 8.0.28
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact us`
--

CREATE TABLE `contact us` (
  `message` varchar(45) DEFAULT NULL,
  `user_index_user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `messenger` int DEFAULT NULL,
  `messenger_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `recipient_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `message` text,
  `traveler_travelerindex` int UNSIGNED NOT NULL,
  `message_index` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`messenger`, `messenger_name`, `recipient_name`, `message`, `traveler_travelerindex`, `message_index`) VALUES
(1, 'Bob Smith', 'Jane Doe', 'Request has been accepted.', 1, 1),
(1, 'Bob Smith', 'Jane Doe', 'Request has been accepted.', 2, 2),
(2, 'Jane Doe', 'Bob Smith', 'asdasdas', 1, 4),
(2, 'Jane Doe', 'Bob Smith', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1, 5),
(1, 'Bob Smith', 'Test Person', 'Request has been accepted.', 1, 7),
(1, 'Bob Smith', 'Jane Doe', 'test', 1, 11),
(1, 'Bob Smith', 'John Daniels', 'Request has been accepted.', 1, 12),
(1, 'Bob Smith', 'John Daniels', 'Request has been accepted.', 1, 13),
(1, 'Bob Smith', 'John Daniels', 'test', 1, 14),
(4, 'John Daniels', 'John Daniels', 'test', 1, 15),
(1, 'Bob Smith', 'Jane Doe', 'Request has been accepted.', 2, 16),
(1, 'Bob Smith', 'Jane Doe', 'Request has been accepted.', 3, 17);

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

CREATE TABLE `requests` (
  `address_destination` varchar(45) DEFAULT NULL,
  `city_destination` varchar(45) DEFAULT NULL,
  `arrival_time` date DEFAULT NULL,
  `departure_time` date DEFAULT NULL,
  `zipcode` int DEFAULT NULL,
  `sender_id` int DEFAULT NULL,
  `request_id` int DEFAULT NULL,
  `requestfor` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `requestby` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `traveler_travelerindex1` int UNSIGNED NOT NULL,
  `acceptstatus` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `requests`
--

INSERT INTO `requests` (`address_destination`, `city_destination`, `arrival_time`, `departure_time`, `zipcode`, `sender_id`, `request_id`, `requestfor`, `requestby`, `traveler_travelerindex1`, `acceptstatus`) VALUES
('9233 Midbury Ct', 'Los Angeles', '2022-05-13', '2022-05-12', 90001, 2, 1, 'Bob Smith', 'Jane Doe', 3, 1),
('4589 Q Dr.', 'Los Angeles', '2022-05-12', '2022-05-11', 90001, 2, 1, 'Bob Smith', 'Jane Doe', 2, 0),
('6754 I St.', 'Los Angeles', '2022-05-12', '2022-05-11', 90001, 3, 1, 'Bob Smith', 'Pat Roberts', 2, 0),
('8745 H Ct.', 'Los Angeles', '2022-05-12', '2022-05-11', 90001, 4, 1, 'Bob Smith', 'John Daniels', 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `traveler`
--

CREATE TABLE `traveler` (
  `destination` varchar(45) DEFAULT NULL,
  `asking_price` float DEFAULT NULL,
  `departure_time` date DEFAULT NULL,
  `zipcode` int DEFAULT NULL,
  `arrival_time` date DEFAULT NULL,
  `user_index_user_id` int NOT NULL,
  `fullname` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `travelerindex` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `traveler`
--

INSERT INTO `traveler` (`destination`, `asking_price`, `departure_time`, `zipcode`, `arrival_time`, `user_index_user_id`, `fullname`, `travelerindex`) VALUES
('Los Angeles', 20, '2022-05-08', 90001, '2022-05-09', 1, 'Bob Smith', 1),
('Los Angeles', 20, '2022-05-11', 90001, '2022-05-12', 1, 'Bob Smith', 2),
('Los Angeles', 15, '2022-05-12', 90001, '2022-05-13', 1, 'Bob Smith', 3),
('Los Angeles', 35, '2022-05-10', 90001, '2022-05-12', 2, 'Jane Doe', 4),
('San Francisco', 35, '2022-05-11', 87849, '2022-05-14', 3, 'Pat Roberts', 5),
('San Diego', 10, '2022-05-10', 92126, '2022-05-24', 4, 'John Daniels', 6);

-- --------------------------------------------------------

--
-- Table structure for table `user_index`
--

CREATE TABLE `user_index` (
  `email address` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `phone number` varchar(45) DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `user_index`
--

INSERT INTO `user_index` (`email address`, `password`, `firstname`, `lastname`, `phone number`, `user_id`) VALUES
('user1@sdsu.edu', 'pass1', 'Bob', 'Smith', '858649754', 1),
('user2@sdsu.edu', 'pass2', 'Jane', 'Doe', '858452378', 2),
('user3@sdsu.edu', 'pass3', 'Pat', 'Roberts', '858120545', 3),
('user4@sdsu.edu', 'pass4', 'John', 'Daniels', '858121345', 4),
('user5@sdsu.edu', 'pass5', 'Guy', 'Phillips', '858123789', 5),
('testuser@gmail.com', 'test', 'Test', 'Person', '8374948374', 6),
('user6@sdsu.edu', 'pass6', 'Ryan', 'Santana', '8588318878', 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`message_index`),
  ADD KEY `message_id` (`message_index`);

--
-- Indexes for table `traveler`
--
ALTER TABLE `traveler`
  ADD PRIMARY KEY (`travelerindex`);

--
-- Indexes for table `user_index`
--
ALTER TABLE `user_index`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  ADD UNIQUE KEY `email address_UNIQUE` (`email address`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `message_index` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `traveler`
--
ALTER TABLE `traveler`
  MODIFY `travelerindex` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_index`
--
ALTER TABLE `user_index`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
