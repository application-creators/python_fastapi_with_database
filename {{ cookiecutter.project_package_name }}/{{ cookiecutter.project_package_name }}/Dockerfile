FROM python:3.10


ARG SERVICE_NAME={{ cookiecutter.project_package_name }}

ARG WORK_DIR=/code
ARG REQUIREMENTS_FILENAME=requirements.frozen

ENV WAIT_SERVICE_FILENAME=wait-service.sh

ENV DATABASE_HOST=database
ENV DATABASE_PORT=5432

ENV API_HOST=0.0.0.0
ENV API_PORT={{ cookiecutter.api_port }}


EXPOSE ${API_PORT}


WORKDIR ${WORK_DIR}


COPY ${REQUIREMENTS_FILENAME} .
RUN pip install -r ${REQUIREMENTS_FILENAME}


COPY ${SERVICE_NAME} .


CMD ./${WAIT_SERVICE_FILENAME} ${DATABASE_HOST} ${DATABASE_PORT} && uvicorn main:app --host ${API_HOST} --port ${API_PORT} --reload
