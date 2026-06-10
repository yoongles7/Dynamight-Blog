#!/bin/sh

set -e

# Wait for postgres to be ready
while ! nc  -z db 5432; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 1
done

echo "PostgreSQL is ready. Running migrations..."
# Confirmation message

# Run migrations
python manage.py migrate --settings=config.settings.development

echo "Starting Django development server..."
# Another confirmation message

# Run CMD after everything is ready
exec "$@"