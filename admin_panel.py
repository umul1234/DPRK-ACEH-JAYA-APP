# admin_panel.py
import streamlit as st
from datetime import datetime
from database import (
    login_admin, change_password, create_admin, get_all_admins, delete_admin,
    get_all_berita, create_berita, update_berita, delete_berita, upload_image,
    get_all_agenda, create_agenda, update_agenda, delete_agenda,
    get_all_galeri, create_galeri, delete_galeri,
    get_running_text_active, create_running_text, delete_running_text,
    get_all_kesekretariatan, create_kesekretariatan, delete_kesekretariatan,
    get_all_pengaduan, update_status_pengaduan, delete_pengaduan,
    get_all_pimpinan, create_pimpinan, update_pimpinan, delete_pimpinan,
    get_all_pejabat, create_pejabat, delete_pejabat,
    get_all_jdih, create_jdih, delete_jdih,
)

# =========================================================
# CSS ADMIN
# =========================================================
ADMIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #f8faf9; }
.block-container { padding-top: 2rem !important; max-width: 1300px; }

.admin-header {
    background: linear-gradient(135deg, #062b1b, #0d5e3a);
    color: white;
    padding: 24px 32px;
    border-radius: 16px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 10px 30px rgba(13,94,58,0.2);
}
.admin-header h1 { margin: 0; font-size: 24px; font-weight: 800; }
.admin-header p { margin: 4px 0 0; opacity: 0.85; font-size: 13px; }
.admin-badge {
    background: rgba(230,196,88,0.2);
    color: #e6c458;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid rgba(230,196,88,0.4);
}
.stat-box {
    background: white;
    border-radius: 12px;
    padding: 16px;
    border-left: 4px solid #0d5e3a;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.stat-box .label { color: #4a5a55; font-size: 11px; font-weight: 700; text-transform: uppercase; }
.stat-box .value { color: #083d26; font-size: 26px; font-weight: 900; margin-top: 4px; }

.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #14734a, #c9a227) !important;
    transform: translateY(-1px);
}
div[data-testid="stForm"] {
    background: white;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #e5ebe7;
}
.stTabs [data-baseweb="tab-list"] { gap: 4px; }
.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 10px 10px 0 0;
    padding: 12px 20px;
    font-weight: 700;
    font-size: 13px;
    color: #4a5a55;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(180deg, #e8f5ef, white) !important;
    color: #0d5e3a !important;
    border-bottom: 3px solid #0d5e3a;
}
</style>
"""

# =========================================================
# LOGIN
# =========================================================
def admin_login():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding: 40px 0 20px;">
            <div style="font-size: 64px; margin-bottom: 12px;">🏛️</div>
            <h1 style="color: #083d26; margin: 0; font-size: 24px; font-weight: 800;">ADMIN PANEL</h1>
            <p style="color: #4a5a55; margin-top: 6px; font-size: 13px;">DPRK Kabupaten Aceh Jaya</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username", placeholder="Masukkan username")
            password = st.text_input("🔒 Password", type="password", placeholder="Masukkan password")
            submit = st.form_submit_button("🔐 Login", use_container_width=True, type="primary")
            
            if submit:
                if not username or not password:
                    st.error("Username dan password wajib diisi")
                else:
                    user = login_admin(username, password)
                    if user:
                        st.session_state.admin_logged_in = True
                        st.session_state.admin_user = user
                        st.success("✅ Login berhasil!")
                        st.rerun()
                    else:
                        st.error("❌ Username atau password salah")

# =========================================================
# DASHBOARD
# =========================================================
def admin_dashboard():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    
    user = st.session_state.admin_user
    
    # HEADER
    col_h1, col_h2 = st.columns([4, 1])
    with col_h1:
        st.markdown(f"""
        <div class="admin-header">
            <div>
                <h1>🏛️ Admin Panel DPRK</h1>
                <p>Selamat datang, <b>{user['username']}</b> · Kelola konten website</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.admin_logged_in = False
            st.session_state.admin_user = None
            st.rerun()
        if st.button("🌐 Lihat Website", use_container_width=True):
            st.markdown('<meta http-equiv="refresh" content="0; url=./">', unsafe_allow_html=True)
    
    # STATS
    berita_count = len(get_all_berita())
    pengaduan_count = len(get_all_pengaduan())
    galeri_count = len(get_all_galeri())
    agenda_count = len(get_all_agenda())
    
    s1, s2, s3, s4 = st.columns(4)
    for col, label, value, icon in [
        (s1, "Berita", berita_count, "📰"),
        (s2, "Pengaduan", pengaduan_count, "📥"),
        (s3, "Galeri", galeri_count, "🖼️"),
        (s4, "Agenda", agenda_count, "📅"),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <div class="label">{icon} {label}</div>
                <div class="value">{value}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    
    # TABS
    tabs = st.tabs([
        "📰 Berita", "📅 Agenda", "🖼️ Galeri", "📢 Running Text",
        "📋 Kesekretariatan", "📥 Pengaduan", "👥 Pimpinan",
        "🏢 Pejabat", "📜 JDIH", "👤 Admin", "⚙️ Pengaturan"
    ])
    
    with tabs[0]: render_berita_tab()
    with tabs[1]: render_agenda_tab()
    with tabs[2]: render_galeri_tab()
    with tabs[3]: render_running_text_tab()
    with tabs[4]: render_kesekretariatan_tab()
    with tabs[5]: render_pengaduan_tab()
    with tabs[6]: render_pimpinan_tab()
    with tabs[7]: render_pejabat_tab()
    with tabs[8]: render_jdih_tab()
    with tabs[9]: render_admin_users_tab()
    with tabs[10]: render_pengaturan_tab()

# =========================================================
# TAB: BERITA
# =========================================================
def render_berita_tab():
    st.subheader("📰 Kelola Berita")
    
    with st.expander("➕ **Tambah Berita Baru**", expanded=False):
        with st.form("form_tambah_berita", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                title = st.text_input("Judul Berita *", placeholder="Judul berita...")
                date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
            with c2:
                kategori = st.selectbox("Kategori", ["Paripurna", "Lingkungan", "Hukum", "Legislasi", "Kunjungan", "Sosial", "Ekonomi", "Lainnya"])
                prioritas = st.selectbox("Prioritas", ["Normal", "Penting", "Utama"])
            
            desc_text = st.text_area("Deskripsi Berita *", height=100, placeholder="Isi berita...")
            
            st.markdown("**📷 Foto Berita**")
            up_method = st.radio("Sumber Foto", ["Upload File", "URL Manual"], horizontal=True, key="foto_berita_method")
            
            uploaded = None
            image_url_manual = ""
            if up_method == "Upload File":
                uploaded = st.file_uploader("Pilih foto", type=["jpg", "jpeg", "png", "webp"], key="berita_file")
            else:
                image_url_manual = st.text_input("URL Foto", placeholder="https://...")
            
            if st.form_submit_button("💾 Simpan Berita", type="primary", use_container_width=True):
                if not title or not desc_text:
                    st.error("⚠️ Judul dan deskripsi wajib diisi")
                else:
                    image_url = image_url_manual
                    if uploaded:
                        with st.spinner("Mengunggah foto..."):
                            image_url = upload_image(uploaded, folder="berita")
                    
                    create_berita(title, date, desc_text, image_url, kategori)
                    st.success("✅ Berita berhasil ditambahkan!")
                    st.balloons()
                    st.rerun()
    
    st.markdown("### 📋 Daftar Berita")
    berita_list = get_all_berita()
    
    if not berita_list:
        st.info("Belum ada berita. Tambahkan berita baru di atas.")
        return
    
    for item in berita_list:
        with st.container():
            c_img, c_info, c_act = st.columns([1, 4, 2])
            with c_img:
                if item.get("image_url"):
                    try: st.image(item["image_url"], width=100)
                    except: st.write("🖼️")
            with c_info:
                st.markdown(f"**{item['title']}**")
                st.caption(f"📅 {item.get('date', '-')} | 🏷️ {item.get('kategori', '-')} | 👁️ {item.get('views', 0)} views")
            with c_act:
                ca, cb = st.columns(2)
                with ca:
                    with st.popover("✏️ Edit", use_container_width=True):
                        with st.form(f"edit_berita_{item['id']}"):
                            nt = st.text_input("Judul", value=item["title"])
                            nd = st.text_input("Tanggal", value=item.get("date", ""))
                            nk = st.text_input("Kategori", value=item.get("kategori", ""))
                            ndesc = st.text_area("Deskripsi", value=item.get("desc_text", ""), height=100)
                            
                            st.markdown("**Ganti Foto (opsional)**")
                            nup = st.file_uploader("Upload Foto Baru", type=["jpg", "png", "jpeg", "webp"], key=f"up_{item['id']}")
                            nurl = st.text_input("Atau URL Baru", value=item.get("image_url", ""), key=f"url_{item['id']}")
                            
                            if st.form_submit_button("✅ Update", use_container_width=True):
                                new_img = nurl
                                if nup:
                                    new_img = upload_image(nup, folder="berita")
                                update_berita(item["id"], title=nt, date=nd, desc_text=ndesc, kategori=nk, image_url=new_img)
                                st.success("Berhasil diupdate!")
                                st.rerun()
                with cb:
                    if st.button("🗑️ Hapus", key=f"del_b_{item['id']}", use_container_width=True):
                        st.session_state[f"confirm_del_b_{item['id']}"] = True
                    
                    if st.session_state.get(f"confirm_del_b_{item['id']}"):
                        st.warning("Yakin hapus?")
                        cc, cd = st.columns(2)
                        with cc:
                            if st.button("Ya", key=f"yes_b_{item['id']}", use_container_width=True):
                                delete_berita(item["id"])
                                st.session_state[f"confirm_del_b_{item['id']}"] = False
                                st.rerun()
                        with cd:
                            if st.button("Batal", key=f"no_b_{item['id']}", use_container_width=True):
                                st.session_state[f"confirm_del_b_{item['id']}"] = False
                                st.rerun()
            st.divider()

# =========================================================
# TAB: AGENDA
# =========================================================
def render_agenda_tab():
    st.subheader("📅 Kelola Agenda")
    
    with st.expander("➕ **Tambah Agenda**", expanded=False):
        with st.form("form_agenda", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                hari = st.text_input("Hari (contoh: 09)", max_chars=2)
                bulan_tahun = st.text_input("Bulan Tahun (contoh: SEP 2026)")
            with c2:
                tanggal_full = st.text_input("Tanggal Lengkap", value=datetime.now().strftime("%A, %d %B %Y"))
            judul = st.text_input("Judul Agenda *")
            deskripsi = st.text_area("Deskripsi", height=80)
            
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not judul:
                    st.error("Judul wajib diisi")
                else:
                    create_agenda(hari, bulan_tahun, tanggal_full, judul, deskripsi)
                    st.success("✅ Agenda ditambahkan!")
                    st.rerun()
    
    st.markdown("### 📋 Daftar Agenda")
    agenda_list = get_all_agenda()
    if not agenda_list:
        st.info("Belum ada agenda.")
        return
    
    for item in agenda_list:
        c1, c2 = st.columns([5, 1])
        with c1:
            st.markdown(f"**📅 {item.get('hari', '')} {item.get('bulan_tahun', '')}** — {item['judul']}")
            st.caption(f"{item.get('tanggal_full', '')} · {item.get('deskripsi', '')}")
        with c2:
            if st.button("🗑️", key=f"del_ag_{item['id']}", use_container_width=True):
                delete_agenda(item["id"])
                st.rerun()
        st.divider()

# =========================================================
# TAB: GALERI
# =========================================================
def render_galeri_tab():
    st.subheader("🖼️ Kelola Galeri")
    
    with st.expander("➕ **Upload Foto Galeri**", expanded=False):
        with st.form("form_galeri", clear_on_submit=True):
            gtitle = st.text_input("Judul Foto *", placeholder="Contoh: Rapat Paripurna")
            gfile = st.file_uploader("Pilih Foto *", type=["jpg", "jpeg", "png", "webp"])
            
            if st.form_submit_button("💾 Upload", type="primary", use_container_width=True):
                if not gfile or not gtitle:
                    st.error("Judul dan file wajib diisi")
                else:
                    with st.spinner("Mengunggah..."):
                        url = upload_image(gfile, folder="galeri")
                    if url:
                        create_galeri(gtitle, url)
                        st.success("✅ Foto ditambahkan!")
                        st.rerun()
    
    st.markdown("### 📋 Galeri Foto")
    galeri_list = get_all_galeri()
    if not galeri_list:
        st.info("Belum ada foto galeri.")
        return
    
    cols = st.columns(3)
    for i, item in enumerate(galeri_list):
        with cols[i % 3]:
            try: st.image(item["image_url"], caption=item["title"], use_column_width=True)
            except: st.write("🖼️")
            if st.button("🗑️ Hapus", key=f"del_g_{item['id']}", use_container_width=True):
                delete_galeri(item["id"])
                st.rerun()

# =========================================================
# TAB: RUNNING TEXT
# =========================================================
def render_running_text_tab():
    st.subheader("📢 Kelola Running Text")
    
    with st.form("form_rt", clear_on_submit=True):
        content = st.text_area("Isi Running Text *", height=80, placeholder="Teks yang akan berjalan...")
        if st.form_submit_button("💾 Tambah", type="primary", use_container_width=True):
            if content.strip():
                create_running_text(content.strip())
                st.success("✅ Ditambahkan!")
                st.rerun()
            else:
                st.error("Isi tidak boleh kosong")
    
    st.markdown("### 📋 Daftar Running Text Aktif")
    items = get_running_text_active()
    if not items:
        st.info("Belum ada running text.")
        return
    
    for item in items:
        c1, c2 = st.columns([6, 1])
        with c1:
            st.info(item["content"])
        with c2:
            if st.button("🗑️", key=f"del_rt_{item['id']}", use_container_width=True):
                delete_running_text(item["id"])
                st.rerun()

# =========================================================
# TAB: KESEKRETARIATAN
# =========================================================
def render_kesekretariatan_tab():
    st.subheader("📋 Kelola Kesekretariatan")
    
    with st.form("form_kes", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            title = st.text_input("Judul *")
        with c2:
            date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
        
        if st.form_submit_button("💾 Tambah", type="primary", use_container_width=True):
            if title:
                create_kesekretariatan(title, date)
                st.success("✅ Ditambahkan!")
                st.rerun()
    
    st.markdown("### 📋 Daftar")
    for item in get_all_kesekretariatan():
        c1, c2 = st.columns([6, 1])
        with c1:
            st.markdown(f"**{item['title']}**")
            st.caption(f"📅 {item.get('date', '')}")
        with c2:
            if st.button("🗑️", key=f"del_kes_{item['id']}", use_container_width=True):
                delete_kesekretariatan(item["id"])
                st.rerun()
        st.divider()

# =========================================================
# TAB: PENGADUAN
# =========================================================
def render_pengaduan_tab():
    st.subheader("📥 Pengaduan Masyarakat")
    
    pengaduan_list = get_all_pengaduan()
    if not pengaduan_list:
        st.info("Belum ada pengaduan masuk.")
        return
    
    status_filter = st.selectbox("Filter Status", ["Semua", "Baru", "Diproses", "Selesai", "Ditolak"])
    if status_filter != "Semua":
        pengaduan_list = [p for p in pengaduan_list if p.get("status") == status_filter]
    
    for p in pengaduan_list:
        status = p.get("status", "Baru")
        emoji = {"Baru": "🆕", "Diproses": "⏳", "Selesai": "✅", "Ditolak": "❌"}.get(status, "📌")
        
        with st.expander(f"{emoji} **{p['tiket']}** — {p['nama']} ({status})"):
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"**Kategori:** {p['kategori']}")
                st.write(f"**Prioritas:** {p['prioritas']}")
                st.write(f"**Lokasi:** {p.get('lokasi', '-')}")
                st.write(f"**NIK:** {p.get('nik', '-')}")
            with c2:
                st.write(f"**Tanggal:** {p.get('created_at', '')[:10]}")
                st.write(f"**Status:** {status}")
            
            st.markdown("**Isi Laporan:**")
            st.info(p["isi"])
            
            c3, c4 = st.columns(2)
            with c3:
                new_status = st.selectbox(
                    "Update Status",
                    ["Baru", "Diproses", "Selesai", "Ditolak"],
                    index=["Baru", "Diproses", "Selesai", "Ditolak"].index(status),
                    key=f"st_{p['id']}"
                )
                if st.button("✅ Update Status", key=f"upd_p_{p['id']}", use_container_width=True):
                    update_status_pengaduan(p["id"], new_status)
                    st.success("Status diupdate!")
                    st.rerun()
            with c4:
                st.write("")
                st.write("")
                if st.button("🗑️ Hapus Pengaduan", key=f"del_p_{p['id']}", use_container_width=True):
                    delete_pengaduan(p["id"])
                    st.rerun()

# =========================================================
# TAB: PIMPINAN
# =========================================================
def render_pimpinan_tab():
    st.subheader("👥 Pimpinan & Anggota DPRK")
    
    with st.expander("➕ **Tambah Pimpinan/Angg
