# Base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the poetry files
COPY pyproject.toml poetry.lock /app

# Install Poetry and dependencies
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Copy the source code
COPY . /app

RUN chmod a+x /app/deploy/*.sh

# Run the app
CMD ["gunicorn", "app.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0:8000"]