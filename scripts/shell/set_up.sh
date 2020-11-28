#!/bin/bash

cd ..
echo $PWD  # Safety check

# Create data base
echo "building database schema..."
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\i flight_db/scripts/sql/create_database.sql"
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\i flight_db/scripts/sql/create_database.sql"
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\c flight_db" -c "\i flight_db/scripts/sql/create_tables.sql"

echo "set up geo partitioning...."
./bin/yb-admin --master_addresses yb-master-n1 modify_table_placement_info ysql.flight_db flight_europe local.europe.europe-1a 1
./bin/yb-admin --master_addresses yb-master-n1 modify_table_placement_info ysql.flight_db flight_america local.america.america-1a 1

echo "populating database..."
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\c flight_db" -c "\i flight_db/scripts/sql/populate/airlines.sql"
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\c flight_db" -c "\i flight_db/scripts/sql/populate/airports.sql"
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\c flight_db" -c "\i flight_db/scripts/sql/populate/routes.sql"
/yugabyte/bin/ysqlsh -h yb-tserver-n1-europe -c "\c flight_db" -c "\i flight_db/scripts/sql/populate/flights.sql"
