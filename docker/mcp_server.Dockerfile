FROM python:3.10-slim-bullseye
LABEL maintainer="architect@enterprise.com"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV SERVICE_NAME=mcp_server
EXPOSE 8155
ENTRYPOINT ["python", "main.py"]
