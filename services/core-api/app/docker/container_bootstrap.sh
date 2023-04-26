#!/bin/bash
# entrypoint.sh file of Dockerfile
# Section 1 - Bash options
set -o errexit  
set -o pipefail  
set -o nounset

# Section 2 - Django autoinit
if [ -n "$1" ]; then
  python manage.py collectstatic --noinput  
  python manage.py migrate
fi
