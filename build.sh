#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --no-input

echo "=== Applying database migrations ==="
python manage.py migrate

echo "=== Seeding default romantic data ==="
python manage.py seed_love_data

echo "=== Build finished successfully ==="
