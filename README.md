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

1.Download docker image of **YugabyteDB** from [docker image registry](https://hub.docker.com/r/yugabytedb/yugabyte)

```bash
docker pull yugabytedb/yugabyte
```

2.Start up persistent container using volume mapping.

```bash
docker run -d --name flight_db  -p 7000:7000 -p 9000:9000 -p 5433:5433 -p 9042:9042\
-v ~/yb_data:/home/yugabyte/var\
-v ${PWD}:/home/flight_db\
yugabytedb/yugabyte:latest bin/yugabyted start\
 --daemon=false
```

3.Verify **docker** container is running and project directory is correctly mapped:

```bash
docker ps
docker exec -it flight_db bash
```

Inside docker container

```bash
cd /home/flight_db
ls -laF
```

5.Visit Yugabyte [admin panel](http://localhost:7000)

6.Populate database with scripts
Open ysqlsh command line tool for **YugabyteDB**

```bash
docker exec -it flight_db /home/yugabyte/bin/ysqlsh --echo-queries
```

Inside container, connect to **flight_db** and verify database is empty:

```postgresql
\c flight_db
\dt
```

Create DB schema and upload data

```postgresql
\i flight_db/scripts/sql/create_tables.sql
\i flight_db/scripts/sql/populate_db.sql
```

Verify Database contents:

```postgresql
SELECT * FROM airline;
SELECT * FROM airport WHERE origin_country='Poland';
```

All steps are available at [YugabyteDB docs](https://docs.yugabyte.com/)

## Register geolocations

[Docs](https://docs.yugabyte.com/latest/admin/yb-admin/)
[Tables](https://docs.yugabyte.com/latest/explore/multi-region-deployments/row-level-geo-partitioning/)

0.Optional set, clean-up previous docker containers and volumes

```bash
docker-compose down
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker-compose up -d
```

1.Start up all required containers using

```bash
docker-compose up -d
```

2.Enter master container and create two clusters

```bash
docker exec -it yb-master-n1 bash
```

3.Create clusters

```bash
./bin/yb-ctl create --data_dir /home/yugabyte/yb-datacenter-europe --ip_start 1
./bin/yb-ctl create --data_dir /home/yugabyte/yb-datacenter-america --ip_start 2
```

4.Enter **ysqlsh** prompt in create cluster

```bash
.\bin\ysqlsh -h 127.0.0.1
```

5.To connect to **ysqlsh** on tserver from master container use:

```bash
./bin/ysqlsh -h yb-tserver-n1-europe
```

To set-up replication see: [YugabyteDB Docs](https://docs.yugabyte.com/latest/explore/multi-region-deployments/asynchronous-replication-ysql/)
