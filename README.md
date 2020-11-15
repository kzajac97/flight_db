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

## Yugabyte DB

To start an instance of Distributed SQL using **Yugabyte** and **Docker** follow steps:

1. Download docker image of **YugabyteDB** from [docker image registry](https://hub.docker.com/r/yugabytedb/yugabyte)
```bash
docker pull yugabytedb/yugabyte
```

2. Start up persistent container using volume mapping.
```bash
docker run -d --name yugabyte  -p 7000:7000 -p 9000:9000 -p 5433:5433 -p 9042:9042\
-v ~/yb_data:/home/yugabyte/var\
 yugabytedb/yugabyte:latest bin/yugabyted start\
 --daemon=false
```

3. Verify **docker** container is running:
```bash
docker ps
```

4. Visit Yugabyte [admin panel](http://localhost:7000)

All steps are available at [YugabyteDB docs](https://docs.yugabyte.com/)
