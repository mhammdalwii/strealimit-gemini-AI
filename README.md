# streamlit-gemini-AI

## Langkah 1: Aktifkan Layanan yang Diperlukan

1. Buka Google Cloud Console: `https://console.cloud.google.com/`

2. Aktifkan Vertex AI API:
   Pada menu navigasi (ikon tiga garis horizontal di kiri atas), pilih `APIs & Services` > `Library`.
   Cari `Vertex AI API` dan klik pada hasilnya.
   Jika API belum diaktifkan, klik tombol "Enable".

3. Aktifkan Cloud Run API:
   Kembali ke `APIs & Services` > `Library`.
   Cari `Cloud Run Admin API` dan klik pada hasilnya.
   Jika API belum diaktifkan, klik tombol "Enable".

4. Aktifkan Container Registry API (atau Artifact Registry API):
   Kembali ke `APIs & Services` > `Library`.
   Cari `Container Registry API` atau `Artifact Registry API` (pilih salah satu, Artifact Registry lebih direkomendasikan).
   Jika API belum diaktifkan, klik tombol "Enable".

## Langkah 2: Buat Direktori Aplikasi

1. Di Cloud Shell, buat direktori untuk aplikasi Anda:
2. mkdir streamlit-gemini-app
3. cd streamlit-gemini-app

## Langkah 3: Buat File app.py

1. Gunakan editor teks nano (atau editor lain yang Anda kuasai) untuk membuat file app.py:
2. buat requirements
3. buat file Dockerfile

## RUN Terminal

4. kalo ada kesalahan bisa ke "echo $PROJECT_ID"
5. export PROJECT_ID="code-lab-wii"
6. Jika PROJECT_ID tidak diatur atau salah, atur di sini
   `gcloud config set project code-lab-wii`
7. `gcloud config list`
8. `docker build -t gcr.io/$PROJECT_ID/streamlit-gemini:latest .`
9. `docker build -t gcr.io/$PROJECT_ID/streamlit-gemini:latest .`
10. `gcloud auth configure-docker`
11. `docker push gcr.io/$PROJECT_ID/streamlit-gemini:latest`
12. Jika menggunakan Artifact Registry (lebih direkomendasikan):
    `gcloud artifacts repositories create streamlit-repo       --repository-format=DOCKER --location=us-central1 --project=$PROJECT_ID`
13. Buat Repository (jika belum): `gcloud artifacts repositories create streamlit-repo--repository-format=DOCKER --location=us-central1 --project=$PROJECT_ID`
14. `docker tag gcr.io/$PROJECT_ID/streamlit-gemini:latest us-central1-docker.pkg.dev/$PROJECT_ID/streamlit-repo/streamlit-gemini:latest`
15. `docker push us-central1-docker.pkg.dev/$PROJECT_ID/streamlit-repo/streamlit-gemini:latest`

## Langkah 7: Deploy ke Cloud Run (melalui Google Cloud Console)

1. Buka menu navigasi dan pilih Cloud Run.
2. Klik Create Service.
3. Source: Pilih Container image.
4. Container image URL: Masukkan URL image Docker Anda (dari Container Registry atau Artifact Registry).
5. Service name: Berikan nama untuk layanan Anda.
6. Region: Pilih region yang sesuai.
7. Authentication: Pilih Allow all unauthenticated invocations (untuk pengujian).
8. Container port: Pastikan diatur ke 8501.
9. Klik Create.

![Logo]('img/gemini.png')

## Demo

https://streamlit-geminiku-600439127623.europe-west1.run.app

## Authors

- [@alwi](https://www.github.com/mhammdalwii
