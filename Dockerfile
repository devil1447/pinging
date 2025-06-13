FROM python:3.11-slim

WORKDIR /app

COPY render_requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ping_monitor.py .

CMD ["python", "ping_monitor.py"]