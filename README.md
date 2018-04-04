Peptide Dashboard
=====


Python Server Instructions
----

run `docker-compose up` from root directory. That will build images,
start DB and python server. The python server will start with unit
tests, so if they fail your server will not be running

Client Instructions
-----

In client directory, run `npm install` once and then use `npm run start` to
begin webpack in watch mode. Viewable at `localhost:9000`