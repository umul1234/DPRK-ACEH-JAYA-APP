# admin_panel.py
import streamlit as st
from datetime import datetime
from database import (
    login_admin, change_password, create_admin, get_all_admins, delete_admin,
    get_all_berita, create_berita, update_berita, delete_berita, upload_image,
    get_all_agenda, create_agenda, delete_agenda,
    get_all_galeri, create_galeri, delete_galeri,
    get_running_text_active, create_running_text, delete_running_text,
    get_all_kesekretariatan, create_kesekretariatan, delete_kesekretariatan,
    get_all_pengaduan, update_status_pengaduan, delete_pengaduan,
    get_all_pimpinan, create_pimpinan, delete_pimpinan,
    get_all_pejabat, create_pejabat, delete_pejabat,
    get_all_jdih, create_jdih, delete_jdih,
    get_all_anggota, create_anggota, delete_anggota,
)

# =========================================================
# KONFIGURASI & CSS DASAR
# =========================================================
LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

ADMIN_CSS = """
<style>
/* CSS minimalis agar admin tidak berantakan, tanpa merusak style lain */
.block-container { padding-top: 2rem !important; }
.stButton > button { width: 100%; border-radius: 8px; }
</style>
"""

# =========================================================
# LOGIN PAGE
# =========================================================
def admin_login():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>🔐 Login Admin</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Panel Admin DPRK Aceh Jaya</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk", type="primary", use_container_width=True)
            
            if submit:
                if not username or not password:
                    st.error("⚠️ Username dan password wajib diisi")
                else:
                    user = login_admin(username, password)
                    if user:
                        st.session_state.admin_logged_in = True
                        st.session_state.admin_user = user
                        st.success("✅ Login berhasil!")
                        st.rerun()
                    else:
                        st.error("❌ Username atau password salah")
        st.write("Kembali ke web utama: [Klik di sini](/)")

# =========================================================
# HALAMAN DASHBOARD & NAVIGASI
# =========================================================
def render_admin_dashboard():
    user = st.session_state.admin_user
    
    # Sidebar Navigasi
    with st.sidebar:
        st.image(LOGO_URL, width=80)
        st.title("Menu Admin")
        st.write(f"Login sebagai: **{user['username']}**")
        
        if "admin_page" not in st.session_state:
            st.session_state.admin_page = "Beranda"
            
        menu = ["Beranda", "Berita", "Agenda", "Galeri", "Anggota", "JDIH", "Pengaduan", "Pengaturan"]
        pilihan = st.radio("Pilih Halaman:", menu, index=menu.index(st.session_state.admin_page))
        
        if pilihan != st.session_state.admin_page:
            st.session_state.admin_page = pilihan
            st.rerun()
            
        st.markdown("---")
        if st.button("🌐 Lihat Website", use_container_width=True):
            st.query_params["page"] = "public"
            st.rerun()
            
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.admin_logged_in = False
            st.session_state.admin_user = None
            st.rerun()

    # Konten Utama
    st.title(f"📁 {st.session_state.admin_page}")
    
    if st.session_state.admin_page == "Beranda":
        st.write(f"Selamat datang, **{user['username']}**!")
        st.info("Gunakan menu di sidebar kiri untuk mengelola konten website.")
        
    elif st.session_state.admin_page == "Berita":
        st.subheader("Tambah Berita Baru")
        with st.form("form_berita", clear_on_submit=True):
            title = st.text_input("Judul *")
            desc = st.text_area("Deskripsi *")
            kategori = st.selectbox("Kategori", ["Paripurna", "Rapat", "Reses", "Lainnya"])
            img = st.file_uploader("Foto (opsional)", type=["jpg", "png"])
            
            if st.form_submit_button("Simpan Berita", type="primary"):
                if title and desc:
                    url = upload_image(img, "berita") if img else ""
                    create_berita(title, datetime.now().strftime("%d %B %Y"), desc, url, kategori)
                    st.success("✅ Berita tersimpan!")
                    st.rerun()
                else:
                    st.error("Judul dan Deskripsi wajib diisi.")
                    
        st.subheader("Daftar Berita")
        for b in get_all_berita():
            with st.expander(f"📰 {b['title']}"):
                st.write(f"Tanggal: {b.get('date')} | Kategori: {b.get('kategori')}")
                st.write(b.get('desc_text'))
                if st.button("Hapus Berita", key=f"del_b_{b['id']}"):
                    delete_berita(b['id'])
                    st.rerun()

    elif st.session_state.admin_page == "Agenda":
        st.subheader("Tambah Agenda")
        with st.form("form_agenda", clear_on_submit=True):
            judul = st.text_input("Judul Agenda *")
            deskripsi = st.text_area("Deskripsi")
            if st.form_submit_button("Simpan", type="primary"):
                if judul:
                    create_agenda("-", "-", datetime.now().strftime("%A, %d %B %Y"), judul, deskripsi)
                    st.success("✅ Agenda tersimpan!")
                    st.rerun()
                    
        st.subheader("Daftar Agenda")
        for a in get_all_agenda():
            st.write(f"📅 **{a['judul']}** - {a.get('tanggal_full')}")
            if st.button("Hapus", key=f"del_ag_{a['id']}"):
                delete_agenda(a['id'])
                st.rerun()

    elif st.session_state.admin_page == "Anggota":
        st.subheader("Tambah Anggota")
        with st.form("form_anggota", clear_on_submit=True):
            nama = st.text_input("Nama *")
            jabatan = st.text_input("Jabatan", "Anggota")
            if st.form_submit_button("Simpan", type="primary"):
                if nama:
                    create_anggota(nama, jabatan, "-", "-", "-", 1, None)
                    st.success("✅ Anggota tersimpan!")
                    st.rerun()
                    
        st.subheader("Daftar Anggota")
        for a in get_all_anggota():
            st.write(f"👤 **{a['nama']}** - {a.get('jabatan')}")
            if st.button("Hapus", key=f"del_a_{a['id']}"):
                delete_anggota(a['id'])
                st.rerun()

    elif st.session_state.admin_page == "JDIH":
        st.subheader("Tambah Produk Hukum")
        with st.form("form_jdih", clear_on_submit=True):
            nomor = st.text_input("Nomor *")
            tentang = st.text_input("Tentang *")
            if st.form_submit_button("Simpan", type="primary"):
                if nomor and tentang:
                    create_jdih(nomor, tentang, "Berlaku")
                    st.success("✅ Tersimpan!")
                    st.rerun()
                    
        st.subheader("Daftar JDIH")
        for j in get_all_jdih():
            st.write(f"📜 **{j['nomor']}** - {j.get('tentang')}")
            if st.button("Hapus", key=f"del_j_{j['id']}"):
                delete_jdih(j['id'])
                st.rerun()

    elif st.session_state.admin_page == "Pengaduan":
        st.subheader("Daftar Pengaduan Masuk")
        pengaduan = get_all_pengaduan()
        if not pengaduan:
            st.info("Belum ada pengaduan.")
        for p in pengaduan:
            with st.expander(f"🎫 {p['tiket']} - {p['nama']}"):
                st.write(p['isi'])
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Hapus", key=f"del_p_{p['id']}"):
                        delete_pengaduan(p['id'])
                        st.rerun()
                with col2:
                    st.write(f"Status: **{p['status']}**")

    elif st.session_state.admin_page == "Pengaturan":
        st.subheader("⚙️ Pengaturan Akun")
        with st.form("form_password"):
            p1 = st.text_input("Password Lama", type="password")
            p2 = st.text_input("Password Baru", type="password")
            if st.form_submit_button("Ganti Password", type="primary"):
                user_check = login_admin(st.session_state.admin_user["username"], p1)
                if not user_check:
                    st.error("Password lama salah")
                elif len(p2) < 6:
                    st.error("Password minimal 6 karakter")
                else:
                    change_password(st.session_state.admin_user["id"], p2)
                    st.success("✅ Password berhasil diubah!")

# =========================================================
# FUNGSI UTAMA
# =========================================================
def render_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
        
    if not st.session_state.admin_logged_in:
        admin_login()
    else:
        render_admin_dashboard()
