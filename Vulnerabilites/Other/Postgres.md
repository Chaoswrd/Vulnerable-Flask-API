# Postgresql
The first thing worth noticing is that this project uses the default postgres user in the docker compose.
It probably has a lot of permissions that this API does not need.
The API only sends a select query to the database and therefore it would be better to set up a user with only the permissions that this API needs.
If the user would get exposed somehow then it has full admin privilegies and the attacker could use that.
