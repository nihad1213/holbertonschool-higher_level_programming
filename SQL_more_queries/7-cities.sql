-- Cities
CREATE DATABASE `hbtn_0d_usa`;

CREATE TABLE `hbtn_0d_usa`.`cities` (
	`id` 		INT 		NOT NULL AUTO_INCREMENT,
	`state_id` 	INT 		NOT NULL,
	`name` 		VARCHAR(256) 	NOT NULL,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
