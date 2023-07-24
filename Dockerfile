FROM python:3.10-slim

WORKDIR /code

COPY ./ .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]
