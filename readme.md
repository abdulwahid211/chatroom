docker exec -it mysqld mysql -u root -p

CREATE TABLE chats
( id INT(11) NOT NULL AUTO_INCREMENT,
  user_name VARCHAR(30) NOT NULL,
  message VARCHAR(25),
  CONSTRAINT contacts_pk PRIMARY KEY (id)
);