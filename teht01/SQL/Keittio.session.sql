-- Checkpoint 4: QSL-jutut

-- luodaan tietokanta
CREATE DATABASE "Keittio";

-- luodaan taulu
CREATE TABLE "Astia" (Id SERIAL PRIMARY KEY, nimi varchar(255) NOT NULL, lkm int NOT NULL);