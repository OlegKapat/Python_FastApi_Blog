psql -U  postgres -c "CREATE USER bloguser WITH PASSWORD'blogpass';" 
createdb -U postgres -O bloguser blog
alembic init -t async alembic 
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
psql blog -U bloguser 
