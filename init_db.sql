PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE personages(naam TEXT PRIMARY KEY, speelbaar integer, rol TEXT);
CREATE TABLE vriendschappen(naam TEXT, met TEXT, FOREIGN KEY(naam) REFERENCES personages(naam), FOREIGN KEY(met) REFERENCES personages(naam));

INSERT INTO "personages" VALUES('Jon Snow',1, 'Krijger');
INSERT INTO "personages" VALUES('Tyrion Lannister',1, 'Diplomaat');
INSERT INTO "personages" VALUES('Jaime Lannister',0, 'Krijger');
INSERT INTO "personages" VALUES('Sansa Stark',0, 'Diplomaat');

INSERT INTO "vriendschappen" VALUES('Jon Snow','Sansa Stark');
INSERT INTO "vriendschappen" VALUES('Sansa Stark', 'Jon Snow');
INSERT INTO "vriendschappen" VALUES('Tyrion Lannister','Jaime Lannister');
INSERT INTO "vriendschappen" VALUES('Jaime Lannister', 'Tyrion Lannister');

COMMIT;
