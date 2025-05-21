FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install flask redis geoip2
EXPOSE 5003
CMD ["python", "count.py"]