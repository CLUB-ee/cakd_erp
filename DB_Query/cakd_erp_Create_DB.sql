-- DB Name : cakd7_erp
-- DB Create / cakd7_erp --
-- CREATE SCHEMA IF NOT EXISTS `cakd7_erp` DEFAULT CHARACTER SET UTF8MB4;
CREATE DATABASE cakd7_erp DEFAULT CHARACTER SET UTF8MB4;
USE cakd7_erp;

-- DROP DATABASE cakd7_erp;
-- ---------------------------------------------------------

-- TABLE Create --

-- material --
CREATE TABLE IF NOT EXISTS material(
	mateId int PRIMARY KEY AUTO_INCREMENT,
	mateName varchar(20) NOT NULL,
	lCat varchar(10) DEFAULT 'etc',
	mCat varchar(10) DEFAULT 'etc',
	sCat varchar(10) DEFAULT 'etc',
	unitCost int,
	stock int NOT NULL DEFAULT 0
	);
ALTER TABLE material AUTO_INCREMENT=600000001;

-- SELECT * FROM material;
-- DROP TABLE material;

		
-- manager --
CREATE TABLE IF NOT EXISTS manager(
	manId int PRIMARY KEY AUTO_INCREMENT,
	manName varchar(10) NOT NULL,
	manPw varchar(20) NOT NULL,
	manPhone varchar(15) NOT NULL,
	manAddr varchar(50) NOT NULL,
	manMail varchar(50),
	manSafe FLOAT NOT NULL DEFAULT 1.2,
	bizNum varchar(15),
	CONSTRAINT manager_bizNum_uk UNIQUE(bizNum)
	);
ALTER TABLE manager AUTO_INCREMENT=900000001;

--  SELECT * FROM manager;
-- DROP TABLE manager;


-- menu --
CREATE TABLE IF NOT EXISTS menu(
	menuId int PRIMARY KEY AUTO_INCREMENT,
	menuPic varchar(10),
	menuName varchar(20) NOT NULL,
	menuPri int NOT NULL
	);
ALTER TABLE menu AUTO_INCREMENT=500000001;

-- SELECT * FROM menu;
-- DROP TABLE menu;


-- recipe --
CREATE TABLE IF NOT EXISTS recipe(
	menuId int NOT NULL,
	mateId int NOT NULL,
	mateUsage int DEFAULT 0,
	CONSTRAINT recipe_menuId_menu_menuId_fk FOREIGN KEY (menuId) REFERENCES menu(menuId),
	CONSTRAINT recipe_mateId_material_mateId_fk FOREIGN KEY (mateId) REFERENCES material(mateId)
	);

-- SELECT * FROM menu;
-- DROP TABLE menu;


-- ord --
CREATE TABLE ord(
	ordNum int PRIMARY KEY AUTO_INCREMENT,
	inTime datetime NOT NULL DEFAULT now()
	);
	ALTER TABLE ord AUTO_INCREMENT=100000001;

-- SELECT * FROM ord;
-- DROP TABLE ord;


-- inStock --
CREATE TABLE IF NOT EXISTS inStock(
	inNum int PRIMARY KEY AUTO_INCREMENT,
	inTime datetime NOT NULL DEFAULT now(),
	ordNum int NOT NULL,
	mateId int NOT NULL,
	inQuan int NOT NULL DEFAULT 0,
	CONSTRAINT inStock_ordNum_ord_ordNum_fk FOREIGN KEY (ordNum) REFERENCES ord(ordNum),
	CONSTRAINT inStock_mateId_material_mateId_fk FOREIGN KEY (mateId) REFERENCES material(mateId)
	);
	ALTER TABLE inStock AUTO_INCREMENT=200000001;

-- SELECT * FROM inStock;	
-- DROP TABLE inStock;


-- cusOrd --
CREATE TABLE IF NOT EXISTS cusOrd(
	cusOrdNum int PRIMARY KEY AUTO_INCREMENT,
	outTime datetime NOT NULL DEFAULT now(),
	menuId int NOT NULL,
	CONSTRAINT cusOrd_menuId_menu_menuId_fk FOREIGN KEY (menuId) REFERENCES menu(menuId)
	);

	ALTER TABLE cusOrd AUTO_INCREMENT=300000001;
	
-- SELECT * FROM cusOrd;
-- DROP TABLE cusOrd;


-- outStock --
CREATE TABLE IF NOT EXISTS outStock(
	outNum int PRIMARY KEY AUTO_INCREMENT,
	outTime datetime NOT NULL DEFAULT now(),
	cusOrdNum int NOT NULL,
	mateId int NOT NULL,
	outQuan int NOT NULL DEFAULT 0,
	CONSTRAINT outStock_cusOrdNum_cusOrd_cusOrdNum_fk FOREIGN KEY (cusOrdNum) REFERENCES cusOrd(cusOrdNum),
	CONSTRAINT outStock_mateId_material_mateId_fk FOREIGN KEY (mateId) REFERENCES material(mateId)
	);
	ALTER TABLE outStock AUTO_INCREMENT=400000001;


-- SELECT * FROM outStock;	
-- DROP TABLE outStock;




