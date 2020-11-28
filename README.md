# FLIGHT DB

Distributed data base system for managing flight connections between Europe and America. <br>
System is built using distributed **YugabyteDB** engine and **docker**

## Set up

To set-up database follow steps:

1.Pull from repo or download released archive, store it in target location

2.Start-up docker containers

If necessary pull required docker images

```bash
docker pull yugabytedb/yugabyte
```

```bash
docker-compose up -d
```

If restarting clean-up old volumes and running containers

```bash
docker-compose down --remove-orphans
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker-compose up -d
```

2.Enter master container and start database

```bash
docker exec -it yb-master-n1 bash
```

In container move to */home* directory and run script:

```bash
cd /home
./flight_db/scripts/shell/set_up.sh
```

Wait for script to complete and verify database content and integrity:

```bash
./bin/ysqlsh -h yb-tserver-n1-europe
```

In **ysqlsh**

```postgre
\c flight_db
\dt
```
