FROM mongo:7.0

RUN mkdir -p /data/db /data/configdb /docker-entrypoint-initdb.d \
  && chown -R mongodb:mongodb /data/db /data/configdb /docker-entrypoint-initdb.d

COPY init-blog-db.js /docker-entrypoint-initdb.d/01-init-blog-db.js
RUN chmod 755 /docker-entrypoint-initdb.d/01-init-blog-db.js \
  && chown mongodb:mongodb /docker-entrypoint-initdb.d/01-init-blog-db.js

USER mongodb
