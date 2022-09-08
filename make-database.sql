PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE wallops (
    id      INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    sender  TEXT NOT NULL,
    server  TEXT NOT NULL,
    ts      INTEGER NOT NULL
);
CREATE TABLE globals (
    id      INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    sender  TEXT NOT NULL,
    server  TEXT NOT NULL,
    ts      INTEGER NOT NULL
);
COMMIT;
