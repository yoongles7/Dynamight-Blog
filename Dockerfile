# BASE STAGE ----------------------------
FROM python:3.12-slim-bookworm as base

WORKDIR /Dynamight-Blog

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements/base.txt requirements/
RUN pip install --no-cache-dir -r requirements/base.txt


# DEVELOPMENT STAGE --------------------------------------
FROM base as development

# Install development dependencies
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
#FROM base as production