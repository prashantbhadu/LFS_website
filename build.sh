#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --no-input

echo "=== Applying database migrations ==="
python manage.py migrate

echo "=== Loading romantic data and memories ==="
if [ -f initial_data.json ]; then
    python manage.py loaddata initial_data.json || python manage.py seed_love_data
else
    python manage.py seed_love_data
fi

echo "=== Build finished successfully ==="
