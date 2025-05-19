# app.py
import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig

# Inisialisasi Vertex AI
PROJECT_ID = "code-lab-wii"  # Ganti dengan Project ID Anda
REGION = "us-central1"
vertexai.init(project=PROJECT_ID, location=REGION)

# Load model Gemini
model = GenerativeModel("gemini-2.0-flash-001")

# Konfigurasi halaman
st.set_page_config(page_title="Gemini Prompt App", page_icon="✨", layout="centered")

st.title("✨ Aplikasi Gemini dengan Streamlit")

# Input Prompt
prompt_input = st.text_area("Masukkan prompt Anda:", "Ceritakan tentang kota Makassar.")

# Gaya penulisan
style = st.selectbox("Pilih gaya penulisan:", ["Default", "Formal", "Santai", "Lucu", "Puitis"])

# Token konfigurasi
max_tokens = st.slider("Pilih panjang jawaban (token):", min_value=50, max_value=1024, value=200, step=50)

# Tombol Kirim
if st.button("Kirim Prompt 🚀"):
    if prompt_input.strip():
        # Tambahkan gaya ke prompt
        style_prefix = {
            "Default": "",
            "Formal": "Tuliskan secara formal: ",
            "Santai": "Jelaskan dengan gaya bahasa santai: ",
            "Lucu": "Tuliskan dengan gaya lucu dan ringan: ",
            "Puitis": "Tuliskan secara puitis: "
        }

        modified_prompt = style_prefix[style] + prompt_input

        config = GenerationConfig(max_output_tokens=max_tokens)

        with st.spinner("Sedang menghubungi Gemini..."):
            response = model.generate_content(modified_prompt, generation_config=config)

        st.success("Berhasil mendapatkan respons!")
        st.subheader("Jawaban dari Gemini:")
        st.write(response.text)
    else:
        st.warning("Prompt tidak boleh kosong!")