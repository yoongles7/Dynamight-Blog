# BASE STAGE ----------------------------
FROM python:3.12-slim-bookworm as base

WORKDIR /Dynamight-Blog

# Copy requirements
COPY requirements/base.txt requirements/
RUN pip install --no-cache-dir -r requirements/base.txt


# DEVELOPMENT STAGE --------------------------------------
FROM base as development

# Copy and install development dependencies
COPY requirements/development.txt requirements/
RUN pip install --no-cache-dir -r requirements/development.txt

# Copy application code
COPY . .

# Copy and set up entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

# Development command (runserver)
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.development" ]


# PRODUCTION STAGE ----------------------------------------
FROM base as production

# Copy and install production dependencies
COPY requirements/production.txt requirements/
RUN pip install --no-cache-dir -r requirements/production.txt

# Copy application code
COPY . .

# Copy and set up entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

# Production command (gunicorn)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]