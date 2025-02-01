#!/bin/sh
git init -b master
git add .
git commit -m "Initial commit"
cp .docker.env .env
docker compose build
docker compose up -d db redis
sleep 2
docker compose run --rm web python manage.py generate_tailwind_directories
docker compose run --rm web npm i && npm run tailwind:build
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py makesuperuser

docker compose up -d
echo "Run 'make dev' to start the server"
echo "Run 'make tw' to start tailwind watch"
echo "Run 'make mm' to make migrations"
echo "Run 'make m' to migrate"
echo "Open your browser at http://127.0.0.1:9000"