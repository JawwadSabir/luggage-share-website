-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 04, 2022 at 04:24 AM
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
-- Table structure for table `address id`
--

CREATE TABLE `address id` (
  `street address` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `zip code` int DEFAULT NULL,
  `user_index_user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

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
  `recipient` int DEFAULT NULL,
  `message` text,
  `traveler_travelerindex` int UNSIGNED NOT NULL,
  `message_index` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`messenger`, `messenger_name`, `recipient`, `message`, `traveler_travelerindex`, `message_index`) VALUES
(1, 'Bob Smith', 2, 'Request has been accepted.', 3, 1),
(1, 'Bob Smith', 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 3, 2),
(1, 'Bob Smith', 2, 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 3, 3),
(1, 'Bob Smith', 2, 'Request has been accepted.', 3, 4);

-- --------------------------------------------------------

--
-- Table structure for table `package information`
--

CREATE TABLE `package information` (
  `package id` int NOT NULL,
  `Dimension` float DEFAULT NULL,
  `weight pound` int DEFAULT NULL,
  `package content` varchar(45) DEFAULT NULL,
  `sender_user_index_user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

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
  `requestfor` int DEFAULT NULL,
  `traveler_travelerindex1` int UNSIGNED NOT NULL,
  `acceptstatus` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `requests`
--

INSERT INTO `requests` (`address_destination`, `city_destination`, `arrival_time`, `departure_time`, `zipcode`, `sender_id`, `requestfor`, `traveler_travelerindex1`, `acceptstatus`) VALUES
('9233 Midbury Ct', 'San Diego', '2022-05-01', '2022-05-03', 92126, 2, 1, 3, 1),
('3049 Test St.', 'Somewhere', '2022-05-10', '2022-05-14', 85648, 2, 1, 8, 1),
('8349 test', 'test', '2022-05-05', '2022-05-24', 92126, 2, 1, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `sender`
--

CREATE TABLE `sender` (
  `address_destination` varchar(45) DEFAULT NULL,
  `city_destination` varchar(45) DEFAULT NULL,
  `arrival_time` date DEFAULT NULL,
  `departure_time` date DEFAULT NULL,
  `zipcode` int DEFAULT NULL,
  `user_index_user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `sender`
--

INSERT INTO `sender` (`address_destination`, `city_destination`, `arrival_time`, `departure_time`, `zipcode`, `user_index_user_id`) VALUES
('9233 Midbury Ct', 'San Diego', '2022-05-01', '2022-05-03', 92126, 2),
('9233 Midbury Ct', 'San Diego', '2022-04-29', '2022-05-30', 92126, 1);

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
  `travelerindex` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `traveler`
--

INSERT INTO `traveler` (`destination`, `asking_price`, `departure_time`, `zipcode`, `arrival_time`, `user_index_user_id`, `travelerindex`) VALUES
('Los Angeles', 30, '2022-05-01', 92126, '2022-05-03', 2, 4),
('Los Angeles', 60, '2022-05-01', 92126, '2022-05-03', 3, 5),
('Los Angeles', 30, '2022-04-29', 92126, '2022-04-30', 4, 6),
('San Francisco', 40, '2022-05-05', 65458, '2022-05-10', 5, 7);

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
('user5@sdsu.edu', 'pass5', 'Guy', 'Phillips', '858123789', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `address id`
--
ALTER TABLE `address id`
  ADD PRIMARY KEY (`user_index_user_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`message_index`),
  ADD KEY `message_id` (`message_index`);

--
-- Indexes for table `package information`
--
ALTER TABLE `package information`
  ADD PRIMARY KEY (`package id`);

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
  MODIFY `message_index` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `traveler`
--
ALTER TABLE `traveler`
  MODIFY `travelerindex` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_index`
--
ALTER TABLE `user_index`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
