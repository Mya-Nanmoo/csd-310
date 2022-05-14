/*
    whatabook.init.sql
    Mya Nanmoo
    May 06,2022
*/


DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('603 N Lamar Blvd, Austin, TX 78703');

INSERT INTO store(hours)
	VALUES('9am to 7pm');

INSERT INTO book(book_name, author)
    VALUES('In Search of Lost Time', 'Marcel Proust');

INSERT INTO book(book_name, author)
    VALUES('Ulysses', 'James Joyce');

INSERT INTO book(book_name, author)
    VALUES('Don Quixote', 'Miguel de Cervantes');

INSERT INTO book(book_name, author)
    VALUES('One Hundred Years of Solitude', 'Gabriel Garcia Marquez');

INSERT INTO book(book_name, author)
    VALUES(' The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('Moby Dick', 'Herman Melville');

INSERT INTO book(book_name, author)
    VALUES('War and Peace', 'Leo Tolstoy');

INSERT INTO book(book_name, author)
    VALUES('Hamlet', 'William Shakespeare');

INSERT INTO book(book_name, author)
    VALUES('The Odyssey', 'Homer');


INSERT INTO user(first_name, last_name)
    VALUES('Hyin', 'Bin');

INSERT INTO user(first_name, last_name)
    VALUES('Micheal', 'Doung');

INSERT INTO user(first_name, last_name)
    VALUES('Anderson', 'Holmes');


INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Hyin'),
        (SELECT book_id FROM book WHERE book_name = 'Hamlet')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Micheal'),
        (SELECT book_id FROM book WHERE book_name = 'The Odyssey')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Anderson'),
        (SELECT book_id FROM book WHERE book_name = 'In Search of Lost Time')
    );
