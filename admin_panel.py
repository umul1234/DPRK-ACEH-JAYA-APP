# admin_panel.py
import streamlit as st
from datetime import datetime
from database import *

def admin_login():
    st.markdown("## 🔐 Login Admin")
    st.caption("Portal Admin DPRK Aceh Jaya")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login", use_container_width=True)
            
            if submit:
                user = login_admin(username, password)
                if user:
                    st.session_state.admin_logged_in = True
                    st.session_state.admin_user = user
                    st.success("Login berhasil!")
                    st.rerun()
                else:
                    st.error("Username atau password salah")

def admin_dashboard():
    st.markdown(f"## 👋 Selamat Datang, {st.session_state.admin_user['username']}")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📰 Berita", "📅 Agenda", "🖼️ Galeri", 
        "📢 Running Text", "📥 Pengaduan", "⚙️ Pengaturan"
    ])
    
    # ============================================
    # TAB BERITA
    # ============================================
    with tab1:
        st.subheader("Kelola Berita")
        
        # Form Tambah Berita
        with st.expander("➕ Tambah Berita Baru", expanded=False):
            with st.form("form_tambah_berita", clear_on_submit=True):
                title = st.text_input("Judul *")
                date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
                kategori = st.selectbox("Kategori", ["Paripurna", "Lingkungan", "Hukum", "Legislasi", "Kunjungan", "Lainnya"])
                desc_text = st.text_area("Deskripsi *", height=100)
                
                # Upload foto dari device
                uploaded = st.file_uploader("Upload Foto", type=["jpg", "jpeg", "png", "webp"])
                image_url_manual = st.text_input("Atau URL Foto (opsional)")
                
                if st.form_submit_button("💾 Simpan Berita", type="primary"):
                    if title and desc_text:
                        image_url = image_url_manual
                        if uploaded:
                            with st.spinner("Upload foto..."):
                                image_url = upload_image(uploaded, folder="berita")
                        
                        create_berita(title, date, desc_text, image_url, kategori)
                        st.success("✅ Berita berhasil ditambahkan!")
                        st.rerun()
                    else:
                        st.error("Judul dan deskripsi wajib diisi")
        
        # List Berita
        st.markdown("### 📋 Daftar Berita")
        berita_list = get_all_berita()
        
        for item in berita_list:
            with st.container():
                col1, col2, col3 = st.columns([1, 4, 1])
                with col1:
                    if item.get("image_url"):
                        st.image(item["image_url"], width=100)
                with col2:
                    st.markdown(f"**{item['title']}**")
                    st.caption(f"📅 {item.get('date', '-')} | 🏷️ {item.get('kategori', '-')} | 👁️ {item.get('views', 0)}")
                with col3:
                    if st.button("🗑️ Hapus", key=f"del_berita_{item['id']}"):
                        delete_berita(item["id"])
                        st.success("Terhapus!")
                        st.rerun()
                    
                    # Edit inline
                    with st.popover("✏️ Edit"):
                        with st.form(f"edit_berita_{item['id']}"):
                            new_title = st.text_input("Judul", value=item["title"])
                            new_date = st.text_input("Tanggal", value=item.get("date", ""))
                            new_kat = st.text_input("Kategori", value=item.get("kategori", ""))
                            new_desc = st.text_area("Deskripsi", value=item.get("desc_text", ""))
                            new_uploaded = st.file_uploader("Ganti Foto", type=["jpg", "png", "jpeg", "webp"], key=f"up_{item['id']}")
                            
                            if st.form_submit_button("Update"):
                                new_img = item.get("image_url")
                                if new_uploaded:
                                    new_img = upload_image(new_uploaded, folder="berita")
                                
                                update_berita(item["id"], 
                                    title=new_title, date=new_date, 
                                    desc_text=new_desc, kategori=new_kat,
                                    image_url=new_img)
                                st.success("Updated!")
                                st.rerun()
                st.divider()
    
    # ============================================
    # TAB AGENDA
    # ============================================
    with tab2:
        st.subheader("Kelola Agenda")
        
        with st.expander("➕ Tambah Agenda"):
            with st.form("form_agenda", clear_on_submit=True):
                c1, c2 = st.columns(2)
                with c1:
                    hari = st.text_input("Hari (contoh: 09)")
                    bulan_tahun = st.text_input("Bulan Tahun (contoh: SEP 2026)")
                with c2:
                    tanggal_full = st.text_input("Tanggal Lengkap")
                judul = st.text_input("Judul Agenda")
                deskripsi = st.text_area("Deskripsi")
                
                if st.form_submit_button("💾 Simpan", type="primary"):
                    create_agenda(hari, bulan_tahun, tanggal_full, judul, deskripsi)
                    st.success("Agenda ditambahkan!")
                    st.rerun()
        
        for item in get_all_agenda():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{item['judul']}** — {item.get('tanggal_full', '')}")
                st.caption(item.get("deskripsi", ""))
            with col2:
                if st.button("🗑️", key=f"del_agenda_{item['id']}"):
                    delete_agenda(item["id"])
                    st.rerun()
            st.divider()
    
    # ============================================
    # TAB GALERI
    # ============================================
    with tab3:
        st.subheader("Kelola Galeri")
        
        with st.expander("➕ Upload Foto Galeri"):
            with st.form("form_galeri", clear_on_submit=True):
                gtitle = st.text_input("Judul Foto")
                gfile = st.file_uploader("Pilih Foto", type=["jpg", "jpeg", "png", "webp"])
                
                if st.form_submit_button("💾 Upload", type="primary"):
                    if gfile and gtitle:
                        with st.spinner("Upload..."):
                            url = upload_image(gfile, folder="galeri")
                        create_galeri(gtitle, url)
                        st.success("Foto ditambahkan!")
                        st.rerun()
        
        # Grid galeri
        galeri_list = get_all_galeri()
        cols = st.columns(3)
        for i, item in enumerate(galeri_list):
            with cols[i % 3]:
                st.image(item["image_url"], caption=item["title"], use_column_width=True)
                if st.button("🗑️ Hapus", key=f"del_gal_{item['id']}"):
                    delete_galeri(item["id"])
                    st.rerun()
    
    # ============================================
    # TAB RUNNING TEXT
    # ============================================
    with tab4:
        st.subheader("Kelola Running Text")
        
        with st.form("form_running", clear_on_submit=True):
            content = st.text_area("Isi Running Text")
            if st.form_submit_button("💾 Tambah", type="primary"):
                if content:
                    create_running_text(content)
                    st.success("Ditambahkan!")
                    st.rerun()
        
        for item in get_running_text_active():
            col1, col2 = st.columns([5, 1])
            with col1:
                st.info(item["content"])
            with col2:
                if st.button("🗑️", key=f"del_rt_{item['id']}"):
                    delete_running_text(item["id"])
                    st.rerun()
    
    # ============================================
    # TAB PENGADUAN
    # ============================================
    with tab5:
        st.subheader("Pengaduan Masuk")
        pengaduan_list = get_all_pengaduan()
        
        if not pengaduan_list:
            st.info("Belum ada pengaduan")
        else:
            for p in pengaduan_list:
                with st.expander(f"🎫 {p['tiket']} — {p['nama']} ({p.get('status', 'Baru')})"):
                    st.write(f"**Kategori:** {p['kategori']}")
                    st.write(f"**Prioritas:** {p['prioritas']}")
                    st.write(f"**Lokasi:** {p.get('lokasi', '-')}")
                    st.write(f"**Isi:** {p['isi']}")
                    
                    new_status = st.selectbox(
                        "Update Status",
                        ["Baru", "Diproses", "Selesai", "Ditolak"],
                        index=["Baru", "Diproses", "Selesai", "Ditolak"].index(p.get("status", "Baru")),
                        key=f"status_{p['id']}"
                    )
                    if st.button("Update Status", key=f"upd_{p['id']}"):
                        update_status_pengaduan(p["id"], new_status)
                        st.success("Status diupdate!")
                        st.rerun()
    
    # ============================================
    # TAB PENGATURAN
    # ============================================
    with tab6:
        st.subheader("Pengaturan")
        if st.button("🚪 Logout", type="primary"):
            st.session_state.admin_logged_in = False
            st.session_state.admin_user = None
            st.rerun()

# =========================================================
# MAIN ADMIN APP
# =========================================================
def render_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
    
    if not st.session_state.admin_logged_in:
        admin_login()
    else:
        admin_dashboard()

if __name__ == "__main__":
    render_admin()
