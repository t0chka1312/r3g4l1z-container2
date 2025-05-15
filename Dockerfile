FROM python:3.9-slim

WORKDIR /app
COPY . .

# Instalar dependencias como usuario no-root
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser
RUN pip install --no-warn-script-location -r requirements.txt

# Crear flag
RUN echo "r3g4l1z{SSTI_RCE_0n_Fl4sk_2024}" > /app/flag.txt

EXPOSE 5000
CMD ["python", "app.py"]
