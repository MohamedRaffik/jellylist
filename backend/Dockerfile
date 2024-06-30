FROM python:3.12

WORKDIR /app
RUN pip install -U pip && pip install poetry
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install
VOLUME [ "/app/.venv" ]
COPY . .
ENTRYPOINT [ "poetry", "run" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000" ]
