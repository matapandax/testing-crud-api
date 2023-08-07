# Menggunakan base image Python
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Membuat dan mengatur working directory di dalam container
WORKDIR /app

# Menyalin requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh isi proyek ke dalam container
COPY . /app/

# Jalankan perintah untuk melakukan migrasi database (jika diperlukan)
# RUN python manage.py migrate

# Expose port yang digunakan oleh Django (biasanya port 8000)
EXPOSE 8000

# Menjalankan aplikasi Django menggunakan perintah "runserver"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
