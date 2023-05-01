#!/bin/bash
# entrypoint.sh file of Dockerfile
# Section 1 - Bash options
set -o errexit  
set -o pipefail  
set -o nounset

postgres_ready() {  
    python << END
import sys

from psycopg2 import connect  
from psycopg2.errors import OperationalError

try:  
    connect(  
        dbname="${POSTGRES_DATABASE}",  
        user="${POSTGRES_USER}",  
        password="${POSTGRES_PASSWORD}",  
        host="${POSTGRES_HOST}",  
        port="${POSTGRES_PORT}",  
    )  
except OperationalError:  
    sys.exit(-1)  
END
}

until postgres_ready; do  
  >&2 echo "Waiting for PostgreSQL to become available..."  
  sleep 5  
done  
>&2 echo "PostgreSQL is available"

# Section 2 - Django autoinit
if [ -n "$AUTOMIGRATE" ]; then
  python manage.py collectstatic --noinput  
  python manage.py migrate
fi


exec "$@"