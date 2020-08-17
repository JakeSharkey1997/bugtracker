DROP TABLE IF EXISTS bugs;

CREATE TABLE bugs (
    id TEXT UNIQUE NOT NULL,
    bug TEXT NOT NULL,
    brakes_id TEXT
);