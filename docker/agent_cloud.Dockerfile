FROM python:3.10-slim-bullseye
LABEL maintainer="architect@enterprise.com"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV SERVICE_NAME=agent_cloud
EXPOSE 8044
ENTRYPOINT ["python", "main.py"]
