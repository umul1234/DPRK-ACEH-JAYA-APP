# database.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime
import hashlib

# =========================================================
# KONFIGURASI SUPABASE
# =========================================================
# Simpan di .streamlit/secrets.toml (JANGAN hardcode!)
# [supabase]
# url = "https://xxx.supabase.co"
# key = "eyJxxx..."

@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = get_supabase()

# =========================================================
# BERITA CRUD
# =========================================================
def get_all_berita():
    res = supabase.table("berita").select("*").order("created_at", desc=True).execute()
    return res.data

def get_berita_by_kategori(kategori):
    if kategori == "Semua":
        return get_all_berita()
    res = supabase.table("berita").select("*").eq("kategori", kategori).order("created_at", desc=True).execute()
    return res.data

def create_berita(title, date, desc_text, image_url, kategori):
    data = {
        "title": title, "date": date, "desc_text": desc_text,
        "image_url": image_url, "kategori": kategori, "views": 0
    }
    res = supabase.table("berita").insert(data).execute()
    return res.data

def update_berita(id, **kwargs):
    kwargs["updated_at"] = datetime.now().isoformat()
    res = supabase.table("berita").update(kwargs).eq("id", id).execute()
    return res.data

def delete_berita(id):
    supabase.table("berita").delete().eq("id", id).execute()

# =========================================================
# AGENDA CRUD
# =========================================================
def get_all_agenda():
    res = supabase.table("agenda").select("*").order("created_at", desc=True).execute()
    return res.data

def create_agenda(hari, bulan_tahun, tanggal_full, judul, deskripsi):
    data = {
        "hari": hari, "bulan_tahun": bulan_tahun,
        "tanggal_full": tanggal_full, "judul": judul, "deskripsi": deskripsi
    }
    res = supabase.table("agenda").insert(data).execute()
    return res.data

def update_agenda(id, **kwargs):
    res = supabase.table("agenda").update(kwargs).eq("id", id).execute()
    return res.data

def delete_agenda(id):
    supabase.table("agenda").delete().eq("id", id).execute()

# =========================================================
# GALERI CRUD
# =========================================================
def get_all_galeri():
    res = supabase.table("galeri").select("*").order("created_at", desc=True).execute()
    return res.data

def create_galeri(title, image_url):
    res = supabase.table("galeri").insert({"title": title, "image_url": image_url}).execute()
    return res.data

def delete_galeri(id):
    supabase.table("galeri").delete().eq("id", id).execute()

# =========================================================
# RUNNING TEXT CRUD
# =========================================================
def get_running_text_active():
    res = supabase.table("running_text").select("*").eq("is_active", True).execute()
    return res.data

def create_running_text(content):
    res = supabase.table("running_text").insert({"content": content}).execute()
    return res.data

def delete_running_text(id):
    supabase.table("running_text").delete().eq("id", id).execute()

# =========================================================
# UPLOAD FOTO KE SUPABASE STORAGE
# =========================================================
def upload_image(file, folder="berita"):
    """Upload file ke Supabase Storage, return public URL"""
    if file is None:
        return None
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{folder}/{timestamp}_{file.name}"
    file_bytes = file.getvalue()
    
    supabase.storage.from_("dprk-images").upload(
        filename, file_bytes,
        file_options={"content-type": file.type}
    )
    public_url = supabase.storage.from_("dprk-images").get_public_url(filename)
    return public_url

# =========================================================
# PENGADUAN
# =========================================================
def create_pengaduan(nama, nik, kategori, prioritas, lokasi, isi, tiket):
    data = {
        "nama": nama, "nik": nik, "kategori": kategori,
        "prioritas": prioritas, "lokasi": lokasi,
        "isi": isi, "tiket": tiket, "status": "Baru"
    }
    res = supabase.table("pengaduan").insert(data).execute()
    return res.data

def get_all_pengaduan():
    res = supabase.table("pengaduan").select("*").order("created_at", desc=True).execute()
    return res.data

def update_status_pengaduan(id, status):
    supabase.table("pengaduan").update({"status": status}).eq("id", id).execute()

# =========================================================
# AUTH ADMIN
# =========================================================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_admin(username, password):
    res = supabase.table("admin_users").select("*").eq("username", username).execute()
    if res.data:
        user = res.data[0]
        if user["password_hash"] == hash_password(password):
            return user
    return None
