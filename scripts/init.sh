#!/bin/bash
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE ROLE dev_user WITH ENCRYPTED PASSWORD '$APP_DB_PASSWORD';
    ALTER ROLE "dev_user" WITH LOGIN;
    ALTER USER dev_user WITH SUPERUSER;
    CREATE DATABASE dev_db;
    GRANT ALL PRIVILEGES ON DATABASE dev_db TO dev_user;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to dev_user;
EOSQL