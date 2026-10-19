# database.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime
import hashlib

@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = get_supabase()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def upload_image(file, folder="berita"):
    if file is None: return None
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        ext = file.name.split(".")[-1].lower()
        filename = f"{folder}/{timestamp}_{abs(hash(file.name))}.{ext}"
        file_bytes = file.getvalue()
        supabase.storage.from_("dprk-images").upload(filename, file_bytes, file_options={"content-type": file.type, "upsert": "true"})
        return supabase.storage.from_("dprk-images").get_public_url(filename)
    except Exception as e:
        st.error(f"Upload error: {e}")
        return None

# ================= BERITA =================
def get_all_berita():
    try:
        return supabase.table("berita").select("*").order("created_at", desc=True).execute().data or []
    except Exception as e:
        st.error(f"⚠️ Gagal memuat berita: {e}")
        return []

def create_berita(title, date, desc_text, image_url, kategori):
    return supabase.table("berita").insert({"title": title, "date": date, "desc_text": desc_text, "image_url": image_url, "kategori": kategori, "views": 0}).execute().data

def update_berita(id, **kwargs):
    kwargs["updated_at"] = datetime.now().isoformat()
    return supabase.table("berita").update(kwargs).eq("id", id).execute().data

def delete_berita(id):
    supabase.table("berita").delete().eq("id", id).execute()

# ================= AGENDA =================
def get_all_agenda():
    try: return supabase.table("agenda").select("*").order("created_at", desc=True).execute().data or []
    except Exception: return []

def create_agenda(hari, bulan_tahun, tanggal_full, judul, deskripsi):
    return supabase.table("agenda").insert({"hari": hari, "bulan_tahun": bulan_tahun, "tanggal_full": tanggal_full, "judul": judul, "deskripsi": deskripsi}).execute().data

def delete_agenda(id):
    supabase.table("agenda").delete().eq("id", id).execute()

# ================= GALERI =================
def get_all_galeri():
    try: return supabase.table("galeri").select("*").order("created_at", desc=True).execute().data or []
    except Exception: return []

def create_galeri(title, image_url):
    return supabase.table("galeri").insert({"title": title, "image_url": image_url}).execute().data

def delete_galeri(id):
    supabase.table("galeri").delete().eq("id", id).execute()

# ================= RUNNING TEXT =================
def get_running_text_active():
    try: return supabase.table("running_text").select("*").eq("is_active", True).execute().data or []
    except Exception: return []

def create_running_text(content):
    return supabase.table("running_text").insert({"content": content, "is_active": True}).execute().data

def delete_running_text(id):
    supabase.table("running_text").delete().eq("id", id).execute()

# ================= KESEKRETARIATAN =================
def get_all_kesekretariatan():
    try: return supabase.table("kesekretariatan").select("*").order("created_at", desc=True).execute().data or []
    except Exception: return []

def create_kesekretariatan(title, date):
    return supabase.table("kesekretariatan").insert({"title": title, "date": date}).execute().data

def delete_kesekretariatan(id):
    supabase.table("kesekretariatan").delete().eq("id", id).execute()

# ================= PENGADUAN =================
def create_pengaduan(nama, nik, kategori, prioritas, lokasi, isi, tiket):
    return supabase.table("pengaduan").insert({"nama": nama, "nik": nik, "kategori": kategori, "prioritas": prioritas, "lokasi": lokasi, "isi": isi, "tiket": tiket, "status": "Baru"}).execute().data

def get_all_pengaduan():
    try: return supabase.table("pengaduan").select("*").order("created_at", desc=True).execute().data or []
    except Exception: return []

def update_status_pengaduan(id, status):
    supabase.table("pengaduan").update({"status": status}).eq("id", id).execute()

def delete_pengaduan(id):
    supabase.table("pengaduan").delete().eq("id", id).execute()

# ================= ADMIN USERS =================
def login_admin(username, password):
    try:
        res = supabase.table("admin_users").select("*").eq("username", username).execute()
        if res.data and res.data[0]["password_hash"] == hash_password(password): return res.data[0]
        return None
    except Exception: return None

def create_admin(username, password):
    return supabase.table("admin_users").insert({"username": username, "password_hash": hash_password(password)}).execute().data

def change_password(user_id, new_password):
    supabase.table("admin_users").update({"password_hash": hash_password(new_password)}).eq("id", user_id).execute()

def get_all_admins():
    try: return supabase.table("admin_users").select("id, username, created_at").execute().data or []
    except Exception: return []

def delete_admin(user_id):
    supabase.table("admin_users").delete().eq("id", user_id).execute()

# ================= PIMPINAN & PEJABAT =================
def get_all_pimpinan():
    try: return supabase.table("pimpinan").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_pimpinan(nama, jabatan, urutan, foto_url=None):
    return supabase.table("pimpinan").insert({"nama": nama, "jabatan": jabatan, "urutan": urutan, "foto_url": foto_url}).execute().data

def delete_pimpinan(id):
    supabase.table("pimpinan").delete().eq("id", id).execute()

def get_all_pejabat():
    try: return supabase.table("pejabat_sekretariat").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_pejabat(nama, jabatan, urutan):
    return supabase.table("pejabat_sekretariat").insert({"nama": nama, "jabatan": jabatan, "urutan": urutan}).execute().data

def delete_pejabat(id):
    supabase.table("pejabat_sekretariat").delete().eq("id", id).execute()

# ================= JDIH =================
def get_all_jdih():
    try: return supabase.table("jdih").select("*").order("nomor").execute().data or []
    except Exception: return []

def create_jdih(nomor, tentang, status, file_url=None):
    return supabase.table("jdih").insert({"nomor": nomor, "tentang": tentang, "status": status, "file_url": file_url}).execute().data

def delete_jdih(id):
    supabase.table("jdih").delete().eq("id", id).execute()

# ================= ANGGOTA, FRAKSI, KOMISI, FAQ =================
def get_all_anggota():
    try: return supabase.table("anggota").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_anggota(nama, jabatan, komisi, dapil, fraksi, urutan=1, foto_url=None):
    return supabase.table("anggota").insert({"nama": nama, "jabatan": jabatan, "komisi": komisi, "dapil": dapil, "fraksi": fraksi, "urutan": urutan, "foto_url": foto_url}).execute().data

def update_anggota(id, **kwargs):
    return supabase.table("anggota").update(kwargs).eq("id", id).execute().data

def delete_anggota(id):
    supabase.table("anggota").delete().eq("id", id).execute()

def get_all_fraksi():
    try: return supabase.table("fraksi").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_fraksi(nama, ketua, jumlah_anggota, urutan=1):
    return supabase.table("fraksi").insert({"nama": nama, "ketua": ketua, "jumlah_anggota": jumlah_anggota, "urutan": urutan}).execute().data

def update_fraksi(id, **kwargs):
    return supabase.table("fraksi").update(kwargs).eq("id", id).execute().data

def delete_fraksi(id):
    supabase.table("fraksi").delete().eq("id", id).execute()

def get_all_komisi():
    try: return supabase.table("komisi").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_komisi(nama, ketua, bidang, urutan=1):
    return supabase.table("komisi").insert({"nama": nama, "ketua": ketua, "bidang": bidang, "urutan": urutan}).execute().data

def update_komisi(id, **kwargs):
    return supabase.table("komisi").update(kwargs).eq("id", id).execute().data

def delete_komisi(id):
    supabase.table("komisi").delete().eq("id", id).execute()

def get_all_faq():
    try: return supabase.table("faq").select("*").order("urutan").execute().data or []
    except Exception: return []

def create_faq(pertanyaan, jawaban, urutan=1):
    return supabase.table("faq").insert({"pertanyaan": pertanyaan, "jawaban": jawaban, "urutan": urutan}).execute().data

def update_faq(id, **kwargs):
    return supabase.table("faq").update(kwargs).eq("id", id).execute().data

def delete_faq(id):
    supabase.table("faq").delete().eq("id", id).execute()

# ================= SEED DEFAULT =================
def seed_default_admin():
    try:
        if not supabase.table("admin_users").select("*").execute().data:
            create_admin(st.secrets.get("admin", {}).get("default_username", "admin"), st.secrets.get("admin", {}).get("default_password", "admin123"))
    except Exception: pass
