-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: itshopsdata
-- ------------------------------------------------------
-- Server version	9.2.0

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
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (67,1,1,20),(69,3,1,20);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `image` varchar(500) DEFAULT NULL,
  `details` text,
  `price` decimal(10,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'iPhone 16 Pro Max – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003679_iphone-16-pro-max-256gb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',29000000.00,'2025-04-07 08:58:02'),(2,'iPhone 16 Pro Max 512G – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003725_iphone-16-pro-max-512gb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',34000000.00,'2025-04-07 08:58:02'),(3,'iPhone 16 Pro Max 1TB – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003747_iphone-16-pro-max-1tb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',49000000.00,'2025-04-07 08:58:02'),(4,'iPhone 15 Pro Max 256GB – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003683_iphone-15-pro-max-256gb-quoc-te-new-nguyen-seal_415.webp','iPhone 15 Pro Max 256GB – Quốc tế / New nguyên seal',26000000.00,'2025-04-07 08:58:02'),(5,'iPhone 15 Pro Max 512GB – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003194_iphone-15-pro-max-512gb-quoc-te-new-nguyen-seal_415.webp','iPhone 15 Pro Max 512GB – Quốc tế / New nguyên seal',30000000.00,'2025-04-07 08:58:02'),(6,'iPhone 15 Pro Max 1TB – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003686_iphone-15-pro-max-1tb-quoc-te-new-nguyen-seal_415.webp','iPhone 15 Pro Max 1TB – Quốc tế / New nguyên seal',33000000.00,'2025-04-07 08:58:02'),(7,'iPad Mini 6 Wifi - New nguyên seal','https://itshoponline.vn/images/thumbs/0003758_ipad-mini-6-wifi-64gb-new-nguyen-seal_415.webp','iPad Mini 6 Wifi - New nguyên seal',10900000.00,'2025-04-07 08:58:02'),(8,'iPad Gen 9 Wifi 64GB - New nguyên seal','https://itshoponline.vn/images/thumbs/0003456_ipad-gen-9-wifi-64gb-new-nguyen-seal_415.webp','iPad Gen 9 Wifi 64GB - New nguyên seal',9000000.00,'2025-04-07 08:58:02'),(9,'iPhone 16 Pro Max – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003679_iphone-16-pro-max-256gb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',29000000.00,'2025-04-07 08:58:02'),(10,'iPhone 16 Pro Max – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003679_iphone-16-pro-max-256gb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',29000000.00,'2025-04-07 08:58:02'),(11,'iPhone 16 Pro Max – Quốc tế / New nguyên seal','https://itshoponline.vn/images/thumbs/0003679_iphone-16-pro-max-256gb-quoc-te-new-nguyen-seal_415.webp','iPhone 16 Pro Max – Quốc tế / New nguyên seal',29000000.00,'2025-04-07 08:58:02');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'nguyenvana','12345678','nguyenvana@example.com','Nguyễn Văn A','2025-04-11 09:20:41'),(2,'mhfj','casddsd','minhdangvan23@gmail.com','dasdsad','2025-04-11 09:20:59'),(15,'nguyenvanaw','scrypt:32768:8:1$JquUBwbxoYyM48qK$3236c9065fa9c64e65512a866033546d1cbdc179021c5b4ef503367fab719de993cb1f275363a798c52f020287030e94c3f6fc7ef095509be202a5a88dbac860','nguyenvanaw@example.com','Nguyễn Văn A','2025-04-14 01:38:54'),(16,'ddddd','scrypt:32768:8:1$DzPXUnqzEdJ6OtNE$fe9c763693486136c1efd5c1d5bbd2af1c459158013001a408c003849722045c59d596cb6abfbc929c8593f41e246c6f6c929a81e44e86492aec4a9721f26e82','minhdangvan233@gmail.com','dddd','2025-04-14 01:40:13'),(17,'2051150146','scrypt:32768:8:1$apfuwBbLMX5zUDBX$fce93d3d18992957c533a007a9175fe59b7c22131fe04b7f63bdf8cdc7cdb15b5ff14d5f57b6f546c6ecf53adaaef1dc970db259a0daae4cdbd064c6d48d01c5','minhdangvan235@gmail.com','Đặng Văn Minh123','2025-04-14 02:45:19'),(20,'minhdv20','scrypt:32768:8:1$YOPKnfvWil9AgLrF$6e2f9ac62e1a04683c0d1b5315b5d2be47b05b65a4968da6c4dd7fcc80e2d1fbab2bcae75a130cf8d6f6d45044cd421cc2da3e0f0b1460677a4f6cfe06e421e1','minhdangvan234@gmail.com','Dang Van Minh','2025-04-14 05:29:19'),(21,'admin','scrypt:32768:8:1$fRpNOodAFeM1bkUv$a18e6e943b819b3067ecb5d4dc72274d4b8d2c162b89218f5cd4c919890724f69b05ea1192c7d9ba96d86cab73df80f77aabedec946c1d12b0b1e194f958c763','minhdangvan33@gmail.com','Nguyen Thi Hue','2025-04-17 10:03:35');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-07 11:00:59
