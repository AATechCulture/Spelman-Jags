INSERT INTO "Pairings" VALUES
("D11620", "DFW", 7, (SELECT seat FROM Users WHERE employee_id IS 7), (SELECT "domestic" FROM Users WHERE employee_id IS 7), (SELECT "plane" FROM Users WHERE employee_id IS 7)),
("D00301", "DFW", 2, (SELECT seat FROM Users WHERE employee_id IS 2), (SELECT "domestic" FROM Users WHERE employee_id IS 2), (SELECT "plane" FROM Users WHERE employee_id IS 2)),
("D00302", "DFW", 2, (SELECT seat FROM Users WHERE employee_id IS 2), (SELECT "domestic" FROM Users WHERE employee_id IS 2), (SELECT "plane" FROM Users WHERE employee_id IS 2)),
("D11623", "ATL", 27, (SELECT seat FROM Users WHERE employee_id IS 27), (SELECT "domestic" FROM Users WHERE employee_id IS 27), (SELECT "plane" FROM Users WHERE employee_id IS 27)),
("D11624", "DFW", 1, (SELECT seat FROM Users WHERE employee_id IS 1), (SELECT "domestic" FROM Users WHERE employee_id IS 1), (SELECT "plane" FROM Users WHERE employee_id IS 1))