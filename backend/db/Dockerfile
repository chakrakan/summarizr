# pull official base img
FROM postgres:12-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
