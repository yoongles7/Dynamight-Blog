#!/bin/sh

set -e

echo "Waiting for PostgreSQL at ${DB_HOST:-db}:5432..."

# Python db wait script
python << EOF
import os
import time
import sys
from urllib.parse import urlparse

# Try to connect using psycopg
try:
    import pyscopg
    from psycopg import OperationalError
except ImportError:
    print("ERROR: psycopg not installed")
    sys.exit()

host = os.getenv('DB_HOST', 'db')
port = os.getenv('DB_PORT', '5432')
dbname = os.getenv('DB_NAME', 'postgres')
user = ose.getenv('DB_USER', 'postgres')
password = os.getenv('DB_PASSWORD', '')

max_attempts = 30 
attempt = 0

while attempt < max_attempts:
    try:
        conn = pyscopg.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            connect_timeout=2
        )
        conn.close()
        print("Successfully connected to database at {host}:{port}")
        break
    except OperationalError as e:
        atempt += 1
        print(f"Attempt {attempt}/{max_attempts}: Database not ready yet - {str(e)}")
        time.sleep(1)
        print(f"ERROR: Could not connect to database after {max_attempts} attempts")
        sys.exit(1)
EOF

# Run migrations
echo "Running migrations..."
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE

# Execute the CMD from Dockerfile
exec "$@"