CREATE DATABASE  IF NOT EXISTS `Boosterz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Boosterz`;
-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Boosterz
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BuyTab`
--

DROP TABLE IF EXISTS `BuyTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BuyTab` (
  `idBuyTab` varchar(45) NOT NULL,
  `trNumber` int NOT NULL AUTO_INCREMENT,
  `date` varchar(45) DEFAULT NULL,
  `symbol` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL,
  `bPrice` varchar(45) DEFAULT NULL,
  `orderCoinQt` varchar(45) DEFAULT NULL,
  `isAvailable` varchar(5) DEFAULT NULL,
  `field1` varchar(45) DEFAULT NULL,
  `field2` varchar(45) DEFAULT NULL,
  `filed3` varchar(45) DEFAULT NULL,
  `field4` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`trNumber`,`idBuyTab`)
) ENGINE=InnoDB AUTO_INCREMENT=1354 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CentralTab`
--

DROP TABLE IF EXISTS `CentralTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CentralTab` (
  `idCentralTab` varchar(45) NOT NULL,
  `trNumber` int NOT NULL AUTO_INCREMENT,
  `date` varchar(45) DEFAULT NULL,
  `symbol` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL,
  `fayda` varchar(45) DEFAULT NULL,
  `actualCash` varchar(45) DEFAULT NULL,
  `actualCoin` varchar(45) DEFAULT NULL,
  `action` varchar(10) DEFAULT NULL,
  `field1` varchar(45) DEFAULT NULL,
  `field2` varchar(45) DEFAULT NULL,
  `filed3` varchar(45) DEFAULT NULL,
  `field4` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`trNumber`,`idCentralTab`)
) ENGINE=InnoDB AUTO_INCREMENT=2707 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `SellTab`
--

DROP TABLE IF EXISTS `SellTab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SellTab` (
  `idSellTab` varchar(45) NOT NULL,
  `trNumber` int NOT NULL AUTO_INCREMENT,
  `date` varchar(45) DEFAULT NULL,
  `symbol` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL,
  `sPrice` varchar(45) DEFAULT NULL,
  `bPrice` varchar(45) DEFAULT NULL,
  `fayda` varchar(45) DEFAULT NULL,
  `orderCoinQt` varchar(45) DEFAULT NULL,
  `isAvailable` varchar(5) DEFAULT NULL,
  `field1` varchar(45) DEFAULT NULL,
  `field2` varchar(45) DEFAULT NULL,
  `filed3` varchar(45) DEFAULT NULL,
  `field4` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`trNumber`,`idSellTab`)
) ENGINE=InnoDB AUTO_INCREMENT=1353 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-11  3:14:23
