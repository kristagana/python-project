-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2023 at 11:39 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_for_task`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Customer_ID` int(6) NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Customer_ID`, `firstname`, `lastname`, `email`, `phone`) VALUES
(123, 'Kate', 'Mer', 'k.mer@mail.com', '1234567'),
(124, 'Emma', 'Sol', 'e.sol@mail.com', '9870989890');

-- --------------------------------------------------------

--
-- Table structure for table `orderlist`
--

CREATE TABLE `orderlist` (
  `Orderlist_ID` int(6) NOT NULL,
  `Product_ID` int(6) DEFAULT NULL,
  `Customer_ID` int(6) DEFAULT NULL,
  `Quantity` int(10) NOT NULL,
  `OrderTotal` float(5,2) NOT NULL,
  `OrderStatus` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orderlist`
--

INSERT INTO `orderlist` (`Orderlist_ID`, `Product_ID`, `Customer_ID`, `Quantity`, `OrderTotal`, `OrderStatus`) VALUES
(1, 3, 123, 2, 39.00, 'In process'),
(2, 1, 124, 1, 99.99, 'In process');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_ID` int(6) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(30) NOT NULL,
  `price` float(4,2) DEFAULT NULL,
  `Productline_ID` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_ID`, `name`, `description`, `price`, `Productline_ID`) VALUES
(1, 'Asus VivaBook', 'Small, portable personal compu', 99.99, '324'),
(2, 'Samsung No Frost', 'Keeps yout things cold', 86.00, '556'),
(3, 'IPhone 13 Pro', 'Fastes smartphone', 19.50, '768');

-- --------------------------------------------------------

--
-- Table structure for table `productline`
--

CREATE TABLE `productline` (
  `Productline_ID` varchar(50) NOT NULL,
  `warranty` varchar(30) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `Supplier_ID` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `productline`
--

INSERT INTO `productline` (`Productline_ID`, `warranty`, `description`, `Supplier_ID`) VALUES
('324', '2027', 'Laptop', 1558),
('556', '2033', 'Fridge', 1605),
('768', '2025', 'Phone', 1442);

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `Supplier_ID` int(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`Supplier_ID`, `name`, `telephone`, `email`) VALUES
(1442, 'Ksenukai', '37122334455', 'info@ksenukai.lv'),
(1558, '220', '37133445566', 'info@220.lv'),
(1605, '1a', '37144556677', 'info@1a.lv');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `orderlist`
--
ALTER TABLE `orderlist`
  ADD PRIMARY KEY (`Orderlist_ID`),
  ADD KEY `Product_ID` (`Product_ID`),
  ADD KEY `Customer_ID` (`Customer_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`Product_ID`),
  ADD KEY `Productline_ID` (`Productline_ID`);

--
-- Indexes for table `productline`
--
ALTER TABLE `productline`
  ADD PRIMARY KEY (`Productline_ID`),
  ADD KEY `Supplier_ID` (`Supplier_ID`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`Supplier_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orderlist`
--
ALTER TABLE `orderlist`
  ADD CONSTRAINT `orderlist_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`),
  ADD CONSTRAINT `orderlist_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`Productline_ID`) REFERENCES `productline` (`Productline_ID`);

--
-- Constraints for table `productline`
--
ALTER TABLE `productline`
  ADD CONSTRAINT `productline_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `supplier` (`Supplier_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
