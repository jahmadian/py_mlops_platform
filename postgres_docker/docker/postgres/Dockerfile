FROM postgres:12.7-alpine3.14
# use the Debian variant (not the Alpine) to "fake" /etc/passwd contents for initdb
# see: https://github.com/docker-library/docs/tree/master/postgres#arbitrary---user-notes

COPY init.sql /docker-entrypoint-initdb.d/
