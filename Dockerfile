FROM python:3.10-slim

WORKDIR /code

COPY ./ .

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install .

# RUN --mount=type=secret,id=KAGGLE_USERNAME \
#     --mount=type=secret,id=KAGGLE_KEY \
#     --mount=type=secret,id=MONGODB_CONN_STRING \
#     export KAGGLE_USERNAME=$(cat /run/secrets/KAGGLE_USERNAME) && \
#     export KAGGLE_KEY=$(cat /run/secrets/KAGGLE_KEY) && \
#     export MONGODB_CONN_STRING=$(cat /run/secrets/MONGODB_CONN_STRING) && \
#     python src/utils/generate_kaggle_keys.py

# RUN --mount=type=secret,id=KAGGLE_USERNAME \
#     --mount=type=secret,id=KAGGLE_KEY \
#     --mount=type=secret,id=MONGODB_CONN_STRING \
#     export KAGGLE_USERNAME=$(cat /run/secrets/KAGGLE_USERNAME) && \
#     export KAGGLE_KEY=$(cat /run/secrets/KAGGLE_KEY) && \
#     export MONGODB_CONN_STRING=$(cat /run/secrets/MONGODB_CONN_STRING) && \
#     python src/utils/build_pipeline.py

RUN --mount=type=secret,id=KAGGLE_USERNAME \
    --mount=type=secret,id=KAGGLE_KEY \
    --mount=type=secret,id=MONGODB_CONN_STRING \
    export KAGGLE_USERNAME=$(cat /run/secrets/KAGGLE_USERNAME) && \
    export KAGGLE_KEY=$(cat /run/secrets/KAGGLE_KEY) && \
    export MONGODB_CONN_STRING=$(cat /run/secrets/MONGODB_CONN_STRING) && \
    python src/utils/build_model.py --train

# RUN python src/utils/build_model.py --train

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]
