CREATE DATABASE donatori;
DROP TABLE IF EXISTS utenti;
CREATE TABLE utenti (
    nome varchar(20),
    cognome varchar(20),
    email varchar(50) PRIMARY KEY
);

INSERT INTO utenti (nome, cognome, email) VALUES (
    'Pippo',
    'Franco',
    'pippo.franco@gail.com'

);

INSERT INTO utenti (nome, cognome, email) VALUE (
    'Ciccio',
    'Graziani',
    'ciccio.graziani@gmail.com',

);