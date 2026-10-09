# database.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime
import hashlib

# =========================================================
# KONEKSI SUPABASE
# =========================================================
@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = get_supabase()

# =========================================================
# HELPER
# =========================================================
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def upload_image(file, folder="berita"):
    """Upload file ke Supabase Storage, return public URL"""
    if file is None:
        return None
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        ext = file.name.split(".")[-1].lower()
        filename = f"{folder}/{timestamp}_{abs(hash(file.name))}.{ext}"
        file_bytes = file.getvalue()
        
        supabase.storage.from_("dprk-images").upload(
            filename,
            file_bytes,
            file_options={"content-type": file.type, "upsert": "true"}
        )
        public_url = supabase.storage.from_("dprk-images").get_public_url(filename)
        return public_url
    except Exception as e:
        st.error(f"Upload error: {e}")
        return None

# =========================================================
# BERITA
# =========================================================
def get_all_berita():
    try:
        res = supabase.table("berita").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception as e:
        st.warning(f"Gagal load berita: {e}")
        return []

def get_berita_by_kategori(kategori):
    if kategori == "Semua":
        return get_all_berita()
    try:
        res = supabase.table("berita").select("*").eq("kategori", kategori).order("created_at", desc=True).execute()
        return res.data or []
    except Exception:
        return []

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

def increment_berita_views(id):
    try:
        res = supabase.table("berita").select("views").eq("id", id).execute()
        if res.data:
            current = res.data[0].get("views", 0) or 0
            supabase.table("berita").update({"views": current + 1}).eq("id", id).execute()
    except Exception:
        pass

# =========================================================
# AGENDA
# =========================================================
def get_all_agenda():
    try:
        res = supabase.table("agenda").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception:
        return []

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
# GALERI
# =========================================================
def get_all_galeri():
    try:
        res = supabase.table("galeri").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception:
        return []

def create_galeri(title, image_url):
    res = supabase.table("galeri").insert({"title": title, "image_url": image_url}).execute()
    return res.data

def delete_galeri(id):
    supabase.table("galeri").delete().eq("id", id).execute()

# =========================================================
# RUNNING TEXT
# =========================================================
def get_running_text_active():
    try:
        res = supabase.table("running_text").select("*").eq("is_active", True).execute()
        return res.data or []
    except Exception:
        return []

def create_running_text(content):
    res = supabase.table("running_text").insert({"content": content, "is_active": True}).execute()
    return res.data

def delete_running_text(id):
    supabase.table("running_text").delete().eq("id", id).execute()

# =========================================================
# KESEKRETARIATAN
# =========================================================
def get_all_kesekretariatan():
    try:
        res = supabase.table("kesekretariatan").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception:
        return []

def create_kesekretariatan(title, date):
    res = supabase.table("kesekretariatan").insert({"title": title, "date": date}).execute()
    return res.data

def delete_kesekretariatan(id):
    supabase.table("kesekretariatan").delete().eq("id", id).execute()

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
    try:
        res = supabase.table("pengaduan").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception:
        return []

def update_status_pengaduan(id, status):
    supabase.table("pengaduan").update({"status": status}).eq("id", id).execute()

def delete_pengaduan(id):
    supabase.table("pengaduan").delete().eq("id", id).execute()

# =========================================================
# USERS ADMIN
# =========================================================
def login_admin(username, password):
    try:
        res = supabase.table("admin_users").select("*").eq("username", username).execute()
        if res.data:
            user = res.data[0]
            if user["password_hash"] == hash_password(password):
                return user
        return None
    except Exception as e:
        st.error(f"Login error: {e}")
        return None

def create_admin(username, password):
    data = {"username": username, "password_hash": hash_password(password)}
    res = supabase.table("admin_users").insert(data).execute()
    return res.data

def change_password(user_id, new_password):
    supabase.table("admin_users").update(
        {"password_hash": hash_password(new_password)}
    ).eq("id", user_id).execute()

def get_all_admins():
    res = supabase.table("admin_users").select("id, username, created_at").execute()
    return res.data or []

def delete_admin(user_id):
    supabase.table("admin_users").delete().eq("id", user_id).execute()

# =========================================================
# PROFIL (PIMPINAN & PEJABAT)
# =========================================================
def get_all_pimpinan():
    try:
        res = supabase.table("pimpinan").select("*").order("urutan").execute()
        return res.data or []
    except Exception:
        return []

def create_pimpinan(nama, jabatan, urutan, foto_url=None):
    data = {"nama": nama, "jabatan": jabatan, "urutan": urutan, "foto_url": foto_url}
    res = supabase.table("pimpinan").insert(data).execute()
    return res.data

def update_pimpinan(id, **kwargs):
    res = supabase.table("pimpinan").update(kwargs).eq("id", id).execute()
    return res.data

def delete_pimpinan(id):
    supabase.table("pimpinan").delete().eq("id", id).execute()

def get_all_pejabat():
    try:
        res = supabase.table("pejabat_sekretariat").select("*").order("urutan").execute()
        return res.data or []
    except Exception:
        return []

def create_pejabat(nama, jabatan, urutan):
    data = {"nama": nama, "jabatan": jabatan, "urutan": urutan}
    res = supabase.table("pejabat_sekretariat").insert(data).execute()
    return res.data

def delete_pejabat(id):
    supabase.table("pejabat_sekretariat").delete().eq("id", id).execute()

# =========================================================
# JDIH
# =========================================================
def get_all_jdih():
    try:
        res = supabase.table("jdih").select("*").order("nomor").execute()
        return res.data or []
    except Exception:
        return []

def create_jdih(nomor, tentang, status, file_url=None):
    data = {"nomor": nomor, "tentang": tentang, "status": status, "file_url": file_url}
    res = supabase.table("jdih").insert(data).execute()
    return res.data

def delete_jdih(id):
    supabase.table("jdih").delete().eq("id", id).execute()

# =========================================================
# INISIALISASI DATA DEFAULT (jalankan sekali)
# =========================================================
def seed_default_admin():
    """Buat admin default jika belum ada"""
    try:
        res = supabase.table("admin_users").select("*").execute()
        if not res.data:
            username = st.secrets.get("admin", {}).get("default_username", "admin")
            password = st.secrets.get("admin", {}).get("default_password", "admin123")
            create_admin(username, password)
            return True
    except Exception:
        pass
    return False
