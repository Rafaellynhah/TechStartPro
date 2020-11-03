-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bd_olist
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bd_olist
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bd_olist` DEFAULT CHARACTER SET utf8 ;
USE `bd_olist` ;

-- -----------------------------------------------------
-- Table `bd_olist`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_olist`.`category` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_olist`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_olist`.`product` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  `value` DOUBLE NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bd_olist`.`product_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_olist`.`product_category` (
  `category_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`category_id`, `product_id`),
  INDEX `fk_category_has_product_product1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_category_has_product_category_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_category_has_product_category`
    FOREIGN KEY (`category_id`)
    REFERENCES `bd_olist`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_category_has_product_product1`
    FOREIGN KEY (`product_id`)
    REFERENCES `bd_olist`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
