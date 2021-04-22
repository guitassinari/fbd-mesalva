# FBD-MESALVA

This project uses Docker to create a Django project with a postgres database.

To set it running, install [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/).

Then just run the following command and everything should be working fine.

```
docker-compose up
```

Access [localhost:8000](http://localhost:8000) on your machine. It should show the initial Django webpage.

### The database

Once `docker-compose` is run for the first time, it will create a database named `mesalva` using user `postgres` (see the [Docker compose file](./docker-compose.yml) for further details).

After setting up the database, it will be initialized by running any `*.sh` or `*.sql` script inside [./db](./db) (See the **Initialization scripts** section of the [postgres Docker image documentation](https://hub.docker.com/_/postgres) for further details).

Currently we have two files in [./db](./db): `tables.sql` and `seeds.sql`.

The `tables.sql` file creates all tales for our database, while `seeds.sql` creates the initial records in each database table.

To see if everything is working, after running `docker-compose up`, open another terminal and execute the following commands:

```bash
# first run "docker ps" to see all currently running containers
$ docker ps 
CONTAINER ID              IMAGE             COMMAND                  CREATED         STATUS         PORTS                    NAMES
<django-container-id>     fbd-mesalva_web   "python manage.py ru…"   9 minutes ago   Up 9 minutes   0.0.0.0:8000->8000/tcp   fbd-mesalva_web_1
<postgres-container-id>   postgres          "docker-entrypoint.s…"   9 minutes ago   Up 9 minutes   5432/tcp                 fbd-mesalva_db_1

# using the ID of the postgres container, connect to it and execute the command line
$ docker exec -it <postgres-container-id> /bin/bash 

# Now you're inside the postgres container.
# Connect to the mesalva database using the postgres user
$ root@c6d685251f99:/$
$ root@c6d685251f99:/$ psql -U postgres -d mesalva 
psql (13.2 (Debian 13.2-1.pgdg100+1))
Type "help" for help.

# Now you're in the postgres command line. use the "\dt" command to see all tables
mesalva=$
mesalva=$ \d
              List of relations
 Schema |      Name       | Type  |  Owner   
--------+-----------------+-------+----------
 public | class_          | table | postgres
 public | comment_        | table | postgres
 public | consumption     | table | postgres
 public | content_        | table | postgres
 public | course          | table | postgres
 public | coursemodule    | table | postgres
 public | creditcard      | table | postgres
 public | essay           | table | postgres
 public | essayevaluation | table | postgres
 public | evaluation      | table | postgres
 public | exercise        | table | postgres
 public | extramaterial   | table | postgres
 public | module_         | table | postgres
 public | modulecontent   | table | postgres
 public | option_         | table | postgres
 public | order_          | table | postgres
 public | plan            | table | postgres
 public | product         | table | postgres
 public | question        | table | postgres
 public | questionanswer  | table | postgres
 public | student         | table | postgres
(21 rows)

# Execute the \q command to quit the postres command line
mesalva=$ \q

# back in the container command line, type "exit" to go back to your host machine command line
$ root@c6d685251f99:/$ exit

# Now everything is back to normal
$
```