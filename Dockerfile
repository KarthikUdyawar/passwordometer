FROM python:alpine

WORKDIR /code

COPY ./ .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

RUN python src/utils/generate_kaggle_keys.py

RUN python src/utils/build_pipeline.py

EXPOSE 80

CMD ["uvicorn", "src.api.app:app", "--workers", "4", "--host", "0.0.0.0", "--port", "80"]
