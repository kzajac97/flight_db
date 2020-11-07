# flight_db

Distributed database for airport management system.

## sqllite DB

To create running instance of Flight Database using **sqlite** follow steps:

1. Install sqlite and it to **PATH** variable <br>
2. Create empty database with: ```sqlite3 flight.db```
3. Enter sqlite prompt and execute SQL scripts:
```sqlite
.read create_tables.sql
.read populate_db.sql
```

To verify tables are correct:
```sqlite
.tables
```

To verify data content is correct
```sqlite
select * from Airline
```
