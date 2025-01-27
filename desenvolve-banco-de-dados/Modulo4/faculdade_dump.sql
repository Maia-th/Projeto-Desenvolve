-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: Faculdade
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Aluno`
--

DROP TABLE IF EXISTS `Aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Aluno` (
  `matricula` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `data_nascimento` date NOT NULL,
  `endereco` varchar(255) NOT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Aluno`
--

LOCK TABLES `Aluno` WRITE;
/*!40000 ALTER TABLE `Aluno` DISABLE KEYS */;
INSERT INTO `Aluno` VALUES (1,'João Pereira','2000-03-15','Rua A, 123'),(2,'Maria Oliveira','1999-07-22','Avenida B, 456');
/*!40000 ALTER TABLE `Aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Disciplina`
--

DROP TABLE IF EXISTS `Disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Disciplina` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `ementa` text,
  `carga_horaria` int NOT NULL DEFAULT '60',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Disciplina`
--

LOCK TABLES `Disciplina` WRITE;
/*!40000 ALTER TABLE `Disciplina` DISABLE KEYS */;
INSERT INTO `Disciplina` VALUES (1,'Banco de Dados','Estudo de modelos relacionais e SQL',80),(2,'Estruturas de Dados','Listas, filas e árvores',60);
/*!40000 ALTER TABLE `Disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Professor`
--

DROP TABLE IF EXISTS `Professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Professor` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `contato` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Professor`
--

LOCK TABLES `Professor` WRITE;
/*!40000 ALTER TABLE `Professor` DISABLE KEYS */;
INSERT INTO `Professor` VALUES ('123.456.789-00','Carlos Silva','carlos@email.com'),('987.654.321-00','Ana Souza','ana@email.com');
/*!40000 ALTER TABLE `Professor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-27 16:52:57
