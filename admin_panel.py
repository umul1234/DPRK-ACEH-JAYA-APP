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
# CSS ADMIN — MODERN
# =========================================================
ADMIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #f4f7f5; }
.block-container { padding-top: 1.5rem !important; max-width: 1400px; }

/* LOGIN PAGE */
.login-wrap {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 90vh;
    background: white;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 30px 80px rgba(0,0,0,0.08);
    margin-top: 1rem;
}
.login-left {
    background: linear-gradient(135deg, #fef2f2 0%, #fff5f5 50%, #ffffff 100%);
    padding: 60px 50px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}
.login-left::before {
    content: '';
    position: absolute;
    top: -100px; right: -100px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(220,38,38,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.login-left-logo {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 90px; height: 90px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(220,38,38,0.15);
    border: 2px solid #fee2e2;
    margin-bottom: 28px;
    font-size: 44px;
}
.login-left h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #991b1b;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 1px;
    margin: 0 0 12px;
    line-height: 1.1;
}
.login-left-sub {
    color: #0f172a;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 20px;
}
.login-left-desc {
    color: #64748b;
    font-size: 14px;
    line-height: 1.7;
    max-width: 400px;
}
.login-left-footer {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #94a3b8;
    font-size: 12px;
    font-weight: 600;
    padding-top: 20px;
    border-top: 1px solid #f1f5f9;
}

.login-right {
    padding: 60px 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: white;
}
.login-right h2 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0f172a;
    font-size: 28px;
    font-weight: 800;
    margin: 0 0 8px;
}
.login-right-sub {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 32px;
}

/* Form styling untuk login */
.login-right div[data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}
.login-right label {
    font-size: 12px !important;
    font-weight: 800 !important;
    color: #dc2626 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    margin-bottom: 6px !important;
}
.login-right input {
    background: #f8fafc !important;
    border: 2px solid #e2e8f0 !important;
    border-radius: 10px !important;
    padding: 12px 14px !important;
    font-size: 14px !important;
    color: #0f172a !important;
}
.login-right input:focus {
    border-color: #dc2626 !important;
    box-shadow: 0 0 0 3px rgba(220,38,38,0.1) !important;
}
.login-right .stButton > button {
    background: linear-gradient(135deg, #dc2626, #991b1b) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    box-shadow: 0 10px 25px rgba(220,38,38,0.3) !important;
    transition: all 0.3s !important;
    margin-top: 8px !important;
}
.login-right .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 35px rgba(220,38,38,0.4) !important;
}

/* DASHBOARD */
.admin-header {
    background: linear-gradient(135deg, #062b1b 0%, #0d5e3a 100%);
    color: white;
    padding: 26px 32px;
    border-radius: 18px;
    margin-bottom: 24px;
    box-shadow: 0 12px 40px rgba(13,94,58,0.25);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
}
.admin-header h1 { margin: 0; font-size: 24px; font-weight: 800; color: white !important; }
.admin-header p { margin: 6px 0 0; opacity: 0.9; font-size: 13px; color: white !important; }

.stat-box {
    background: white;
    border-radius: 14px;
    padding: 20px;
    border-left: 4px solid #0d5e3a;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}
.stat-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(13,94,58,0.12);
}
.stat-box .label {
    color: #4a5a55; font-size: 11px; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.8px;
    display: flex; align-items: center; gap: 6px;
}
.stat-box .value {
    color: #083d26; font-size: 32px; font-weight: 900;
    margin-top: 8px; line-height: 1;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
.stat-box .sub {
    color: #94a3b8; font-size: 11px;
    margin-top: 4px; font-weight: 600;
}

/* Tab */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: white;
    padding: 6px;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    margin-bottom: 20px;
    flex-wrap: wrap;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 700;
    font-size: 12.5px;
    color: #64748b;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: white !important;
}

/* Form */
div[data-testid="stForm"] {
    background: white;
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #e5ebe7;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 10px 16px !important;
    transition: all 0.25s !important;
    box-shadow: 0 4px 12px rgba(13,94,58,0.15) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #14734a, #c9a227) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(13,94,58,0.25) !important;
}

/* Card item untuk list CRUD */
.crud-card {
    background: white;
    border-radius: 14px;
    padding: 16px 20px;
    border: 1px solid #e5ebe7;
    margin-bottom: 12px;
    display: flex;
    gap: 16px;
    align-items: center;
    transition: all 0.25s;
}
.crud-card:hover {
    border-color: #0d5e3a;
    box-shadow: 0 8px 24px rgba(13,94,58,0.1);
    transform: translateX(4px);
}
.crud-thumb {
    width: 72px; height: 72px;
    border-radius: 12px;
    object-fit: cover;
    flex-shrink: 0;
    background: #f1f5f9;
}
.crud-content { flex: 1; min-width: 0; }
.crud-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px; font-weight: 800;
    color: #083d26; margin: 0 0 4px;
    line-height: 1.4;
}
.crud-meta {
    font-size: 11.5px; color: #64748b;
    font-weight: 600;
    display: flex; gap: 10px; flex-wrap: wrap;
    margin-top: 4px;
}
.crud-badge {
    display: inline-block;
    background: #f0fdf4;
    color: #166534;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}
.crud-badge-gold { background: #fef9c3; color: #854d0e; }
.crud-badge-red { background: #fee2e2; color: #991b1b; }
.crud-badge-blue { background: #dbeafe; color: #1e40af; }

/* Section header */
.section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #083d26;
    font-size: 20px;
    font-weight: 800;
    margin: 24px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title::before {
    content: '';
    width: 4px; height: 22px;
    background: linear-gradient(180deg, #0d5e3a, #c9a227);
    border-radius: 4px;
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: 48px 20px;
    background: white;
    border-radius: 16px;
    border: 2px dashed #e5ebe7;
}
.empty-state-icon { font-size: 48px; margin-bottom: 12px; opacity: 0.5; }
.empty-state-text { color: #94a3b8; font-size: 14px; font-weight: 600; }

/* Login error */
.login-error {
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #991b1b;
    padding: 12px 16px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 700;
    margin-top: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Sidebar nav */
.admin-nav {
    background: white;
    border-radius: 14px;
    padding: 8px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    display: flex;
    gap: 6px;
    overflow-x: auto;
    flex-wrap: wrap;
}
.admin-nav-item {
    padding: 10px 16px;
    border-radius: 10px;
    font-size: 12.5px;
    font-weight: 700;
    color: #64748b;
    text-decoration: none;
    white-space: nowrap;
    transition: all 0.2s;
    cursor: pointer;
    border: none;
    background: transparent;
}
.admin-nav-item:hover {
    background: #f0fdf4;
    color: #0d5e3a;
}
.admin-nav-item.active {
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: white;
}

@media (max-width: 768px) {
    .login-wrap { grid-template-columns: 1fr; min-height: auto; }
    .login-left { padding: 40px 30px; }
    .login-right { padding: 40px 30px; }
    .login-left h1 { font-size: 26px; }
    .stat-box .value { font-size: 26px; }
    .crud-card { flex-direction: column; align-items: flex-start; }
}
</style>
"""

# =========================================================
# LOGIN PAGE
# =========================================================
def admin_login():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    # KIRI — branding
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fef2f2 0%, #fff5f5 50%, #ffffff 100%);
                    padding: 50px 40px; border-radius: 24px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.06);
                    min-height: 500px;
                    display: flex; flex-direction: column; justify-content: space-between;
                    border: 1px solid #fee2e2;">
            <div>
                <div style="display: inline-flex; align-items: center; justify-content: center;
                            width: 90px; height: 90px; background: white;
                            border-radius: 20px; box-shadow: 0 10px 30px rgba(220,38,38,0.15);
                            border: 2px solid #fee2e2; margin-bottom: 28px;
                            font-size: 44px;">
                    🏛️
                </div>
                <h1 style="font-family: 'Plus Jakarta Sans', sans-serif;
                          color: #991b1b; font-size: 34px; font-weight: 900;
                          letter-spacing: 1px; margin: 0 0 12px; line-height: 1.1;">
                    DPRK ACEH JAYA
                </h1>
                <div style="color: #0f172a; font-size: 15px; font-weight: 700; margin-bottom: 20px;">
                    Dewan Perwakilan Rakyat Kabupaten
                </div>
                <div style="color: #64748b; font-size: 14px; line-height: 1.7; max-width: 400px;">
                    Panel admin untuk mengelola konten website DPRK Aceh Jaya — berita, agenda, galeri, pengaduan, dan lainnya.
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;
                        color: #94a3b8; font-size: 12px; font-weight: 600;
                        padding-top: 20px; border-top: 1px solid #fecaca;">
                🔒 Sistem Autentikasi Aman & Terenkripsi
            </div>
        </div>
        """, unsafe_allow_html=True)

    # KANAN — form login
    with col2:
        st.markdown("""
        <div style="padding: 50px 20px 20px;">
            <h2 style="font-family: 'Plus Jakarta Sans', sans-serif;
                       color: #0f172a; font-size: 28px; font-weight: 800;
                       margin: 0 0 8px;">
                Login Administrator
            </h2>
            <div style="color: #64748b; font-size: 14px; margin-bottom: 32px;">
                Masukkan kredensial akun Anda untuk melanjutkan.
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("USERNAME", placeholder="Masukkan username", key="login_username")
            password = st.text_input("PASSWORD", type="password", placeholder="Masukkan password", key="login_password")
            submit = st.form_submit_button("Masuk ke Panel  →", use_container_width=True, type="primary")

            if submit:
                if not username or not password:
                    st.markdown("""
                    <div class="login-error">⚠️ Username dan password wajib diisi</div>
                    """, unsafe_allow_html=True)
                else:
                    user = login_admin(username, password)
                    if user:
                        st.session_state.admin_logged_in = True
                        st.session_state.admin_user = user
                        st.success("✅ Login berhasil! Mengalihkan...")
                        st.rerun()
                    else:
                        st.markdown("""
                        <div class="login-error">❌ Username atau password salah</div>
                        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center; padding: 20px;
                    color: #94a3b8; font-size: 12px;">
            <a href="/" style="color: #64748b; text-decoration: none; font-weight: 700;">
                ← Kembali ke Website Utama
            </a>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================
def admin_dashboard():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    user = st.session_state.admin_user

    # Header
    col_h1, col_h2 = st.columns([4, 1])
    with col_h1:
        st.markdown(f"""
        <div class="admin-header">
            <div>
                <h1>🏛️ Admin Panel DPRK</h1>
                <p>Selamat datang, <b>{user['username']}</b> · Kelola konten website DPRK Aceh Jaya</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        if st.button("🌐 Lihat Website", use_container_width=True):
            st.markdown('<meta http-equiv="refresh" content="0; url=./">', unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.admin_logged_in = False
            st.session_state.admin_user = None
            st.rerun()

    # Statistik
    berita_count = len(get_all_berita())
    pengaduan_list = get_all_pengaduan()
    pengaduan_baru = len([p for p in pengaduan_list if p.get("status") == "Baru"])
    galeri_count = len(get_all_galeri())
    agenda_count = len(get_all_agenda())

    s1, s2, s3, s4 = st.columns(4)
    stats = [
        (s1, "Berita", berita_count, "📰", "Total artikel dipublikasikan", "#0d5e3a"),
        (s2, "Pengaduan", pengaduan_list.__len__(), "📥", f"{pengaduan_baru} baru masuk", "#dc2626"),
        (s3, "Galeri", galeri_count, "🖼️", "Foto dokumentasi", "#c9a227"),
        (s4, "Agenda", agenda_count, "📅", "Jadwal rapat", "#14734a"),
    ]
    for col, label, value, icon, sub, color in stats:
        with col:
            st.markdown(f"""
            <div class="stat-box" style="border-left-color: {color};">
                <div class="label">{icon} {label}</div>
                <div class="value">{value}</div>
                <div class="sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

    # Tabs
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
# HELPER — Empty State
# =========================================================
def show_empty_state(icon, text):
    st.markdown(f"""
    <div class="empty-state">
        <div class="empty-state-icon">{icon}</div>
        <div class="empty-state-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TAB: BERITA
# =========================================================
def render_berita_tab():
    st.markdown('<div class="section-title">📰 Kelola Berita</div>', unsafe_allow_html=True)

    with st.expander("➕ **Tambah Berita Baru**", expanded=False):
        with st.form("form_tambah_berita", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                title = st.text_input("Judul Berita *", placeholder="Judul berita...")
                date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
            with c2:
                kategori = st.selectbox("Kategori", ["Paripurna", "Lingkungan", "Hukum", "Legislasi", "Kunjungan", "Sosial", "Ekonomi", "Lainnya"])

            desc_text = st.text_area("Deskripsi Berita *", height=100, placeholder="Isi berita...")

            st.markdown("**📷 Foto Berita**")
            up_method = st.radio("Sumber Foto", ["Upload File", "URL Manual"], horizontal=True, key="foto_berita_method")

            uploaded = None
            image_url_manual = ""
            if up_method == "Upload File":
                uploaded = st.file_uploader("Pilih foto", type=["jpg", "jpeg", "png", "webp"], key="berita_file")
                if uploaded:
                    st.image(uploaded, caption="Preview", width=200)
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

    st.markdown('<div class="section-title">📋 Daftar Berita</div>', unsafe_allow_html=True)

    # Search
    search = st.text_input("🔎 Cari berita", placeholder="Ketik judul...", key="search_berita")

    berita_list = get_all_berita()
    if search:
        berita_list = [b for b in berita_list if search.lower() in b.get("title", "").lower()]

    if not berita_list:
        show_empty_state("📰", "Belum ada berita. Tambahkan berita baru di atas.")
        return

    for item in berita_list:
        c_img, c_info, c_act = st.columns([1, 5, 2])
        with c_img:
            if item.get("image_url"):
                try: st.image(item["image_url"], width=80)
                except: st.write("🖼️")
            else:
                st.markdown('<div style="width:80px;height:80px;background:#f1f5f9;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:32px;">🖼️</div>', unsafe_allow_html=True)
        with c_info:
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">{item['title']}</div>
                <div class="crud-meta">
                    <span>📅 {item.get('date', '-')}</span>
                    <span class="crud-badge">{item.get('kategori', '-')}</span>
                    <span>👁️ {item.get('views', 0)} views</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
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
                key_del = f"del_b_{item['id']}"
                if st.button("🗑️ Hapus", key=key_del, use_container_width=True):
                    st.session_state[f"confirm_{key_del}"] = True
                if st.session_state.get(f"confirm_{key_del}"):
                    st.warning("Yakin hapus?")
                    cc, cd = st.columns(2)
                    with cc:
                        if st.button("Ya", key=f"yes_{key_del}", use_container_width=True):
                            delete_berita(item["id"])
                            st.session_state[f"confirm_{key_del}"] = False
                            st.rerun()
                    with cd:
                        if st.button("Batal", key=f"no_{key_del}", use_container_width=True):
                            st.session_state[f"confirm_{key_del}"] = False
                            st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: AGENDA
# =========================================================
def render_agenda_tab():
    st.markdown('<div class="section-title">📅 Kelola Agenda</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-title">📋 Daftar Agenda</div>', unsafe_allow_html=True)
    agenda_list = get_all_agenda()
    if not agenda_list:
        show_empty_state("📅", "Belum ada agenda.")
        return

    for item in agenda_list:
        c1, c2 = st.columns([6, 1])
        with c1:
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">📅 {item.get('hari', '')} {item.get('bulan_tahun', '')} — {item['judul']}</div>
                <div class="crud-meta">
                    <span>{item.get('tanggal_full', '')}</span>
                    <span>{(item.get('deskripsi', '') or '')[:80]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            if st.button("🗑️", key=f"del_ag_{item['id']}", use_container_width=True):
                delete_agenda(item["id"])
                st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: GALERI
# =========================================================
def render_galeri_tab():
    st.markdown('<div class="section-title">🖼️ Kelola Galeri</div>', unsafe_allow_html=True)

    with st.expander("➕ **Upload Foto Galeri**", expanded=False):
        with st.form("form_galeri", clear_on_submit=True):
            gtitle = st.text_input("Judul Foto *", placeholder="Contoh: Rapat Paripurna")
            gfile = st.file_uploader("Pilih Foto *", type=["jpg", "jpeg", "png", "webp"])
            if gfile:
                st.image(gfile, caption="Preview", width=200)
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

    st.markdown('<div class="section-title">📋 Galeri Foto</div>', unsafe_allow_html=True)
    galeri_list = get_all_galeri()
    if not galeri_list:
        show_empty_state("🖼️", "Belum ada foto galeri.")
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
    st.markdown('<div class="section-title">📢 Kelola Running Text</div>', unsafe_allow_html=True)

    with st.form("form_rt", clear_on_submit=True):
        content = st.text_area("Isi Running Text *", height=80, placeholder="Teks yang akan berjalan...")
        if st.form_submit_button("💾 Tambah", type="primary", use_container_width=True):
            if content.strip():
                create_running_text(content.strip())
                st.success("✅ Ditambahkan!")
                st.rerun()
            else:
                st.error("Isi tidak boleh kosong")

    st.markdown('<div class="section-title">📋 Daftar Running Text Aktif</div>', unsafe_allow_html=True)
    items = get_running_text_active()
    if not items:
        show_empty_state("📢", "Belum ada running text.")
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
    st.markdown('<div class="section-title">📋 Kelola Kesekretariatan</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-title">📋 Daftar</div>', unsafe_allow_html=True)
    items = get_all_kesekretariatan()
    if not items:
        show_empty_state("📋", "Belum ada data.")
        return
    for item in items:
        c1, c2 = st.columns([6, 1])
        with c1:
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">{item['title']}</div>
                <div class="crud-meta"><span>📅 {item.get('date', '')}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            if st.button("🗑️", key=f"del_kes_{item['id']}", use_container_width=True):
                delete_kesekretariatan(item["id"])
                st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: PENGADUAN
# =========================================================
def render_pengaduan_tab():
    st.markdown('<div class="section-title">📥 Pengaduan Masyarakat</div>', unsafe_allow_html=True)

    pengaduan_list = get_all_pengaduan()
    if not pengaduan_list:
        show_empty_state("📥", "Belum ada pengaduan masuk.")
        return

    # Stats
    col1, col2, col3, col4 = st.columns(4)
    counts = {
        "Baru": len([p for p in pengaduan_list if p.get("status") == "Baru"]),
        "Diproses": len([p for p in pengaduan_list if p.get("status") == "Diproses"]),
        "Selesai": len([p for p in pengaduan_list if p.get("status") == "Selesai"]),
        "Ditolak": len([p for p in pengaduan_list if p.get("status") == "Ditolak"]),
    }
    for col, (status, count) in zip([col1, col2, col3, col4], counts.items()):
        with col:
            color = {"Baru": "#0d5e3a", "Diproses": "#c9a227", "Selesai": "#16a34a", "Ditolak": "#dc2626"}[status]
            st.markdown(f"""
            <div class="stat-box" style="border-left-color: {color};">
                <div class="label">{status}</div>
                <div class="value">{count}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    status_filter = st.selectbox("Filter Status", ["Semua", "Baru", "Diproses", "Selesai", "Ditolak"], key="filter_pengaduan")
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
                new_status = st.selectbox("Update Status", ["Baru", "Diproses", "Selesai", "Ditolak"],
                    index=["Baru", "Diproses", "Selesai", "Ditolak"].index(status), key=f"st_{p['id']}")
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
    st.markdown('<div class="section-title">👥 Pimpinan & Anggota DPRK</div>', unsafe_allow_html=True)

    with st.expander("➕ **Tambah Pimpinan/Anggota**", expanded=False):
        with st.form("form_pimpinan", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *")
                urutan = st.number_input("Urutan", min_value=1, value=1)
            with c2:
                jabatan = st.text_input("Jabatan *", placeholder="Contoh: KETUA DPRK")
                foto = st.file_uploader("Foto (opsional)", type=["jpg", "png", "jpeg"])
                if foto:
                    st.image(foto, width=100)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nama and jabatan:
                    foto_url = upload_image(foto, folder="pimpinan") if foto else None
                    create_pimpinan(nama, jabatan, urutan, foto_url)
                    st.success("✅ Ditambahkan!")
                    st.rerun()

    st.markdown('<div class="section-title">📋 Daftar</div>', unsafe_allow_html=True)
    items = get_all_pimpinan()
    if not items:
        show_empty_state("👥", "Belum ada data pimpinan.")
        return
    for item in items:
        c1, c2, c3 = st.columns([1, 5, 1])
        with c1:
            if item.get("foto_url"):
                try: st.image(item["foto_url"], width=60)
                except: st.write("👤")
            else:
                st.markdown('<div style="width:60px;height:60px;background:#f1f5f9;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;">👤</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">{item['nama']}</div>
                <div class="crud-meta"><span class="crud-badge crud-badge-gold">{item['jabatan']}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            if st.button("🗑️", key=f"del_pim_{item['id']}", use_container_width=True):
                delete_pimpinan(item["id"])
                st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: PEJABAT
# =========================================================
def render_pejabat_tab():
    st.markdown('<div class="section-title">🏢 Pejabat Sekretariat</div>', unsafe_allow_html=True)

    with st.form("form_pejabat", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nama = st.text_input("Nama *")
        with c2:
            jabatan = st.text_input("Jabatan *")
        urutan = st.number_input("Urutan", min_value=1, value=1)
        if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
            if nama and jabatan:
                create_pejabat(nama, jabatan, urutan)
                st.success("✅ Ditambahkan!")
                st.rerun()

    st.markdown('<div class="section-title">📋 Daftar</div>', unsafe_allow_html=True)
    items = get_all_pejabat()
    if not items:
        show_empty_state("🏢", "Belum ada data pejabat.")
        return
    for item in items:
        c1, c2 = st.columns([6, 1])
        with c1:
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">{item['nama']}</div>
                <div class="crud-meta"><span class="crud-badge crud-badge-blue">{item['jabatan']}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            if st.button("🗑️", key=f"del_pej_{item['id']}", use_container_width=True):
                delete_pejabat(item["id"])
                st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: JDIH
# =========================================================
def render_jdih_tab():
    st.markdown('<div class="section-title">📜 Kelola Produk Hukum (JDIH)</div>', unsafe_allow_html=True)

    with st.expander("➕ **Tambah Produk Hukum**", expanded=False):
        with st.form("form_jdih", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                nomor = st.text_input("Nomor & Tahun *", placeholder="Qanun No. 5/2025")
                status = st.selectbox("Status", ["Berlaku", "Dicabut", "Diubah"])
            with c2:
                tentang = st.text_input("Tentang *")
            file_up = st.file_uploader("Upload PDF (opsional)", type=["pdf"])
            file_url_manual = st.text_input("Atau URL File (opsional)")
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nomor and tentang:
                    file_url = file_url_manual
                    if file_up:
                        with st.spinner("Upload..."):
                            file_url = upload_image(file_up, folder="jdih")
                    create_jdih(nomor, tentang, status, file_url)
                    st.success("✅ Ditambahkan!")
                    st.rerun()

    st.markdown('<div class="section-title">📋 Daftar Produk Hukum</div>', unsafe_allow_html=True)
    items = get_all_jdih()
    if not items:
        show_empty_state("📜", "Belum ada produk hukum.")
        return
    for item in items:
        c1, c2 = st.columns([6, 1])
        with c1:
            status = item.get('status', '-')
            badge_class = "crud-badge" if status == "Berlaku" else "crud-badge crud-badge-red"
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">{item['nomor']} — {item['tentang']}</div>
                <div class="crud-meta"><span class="{badge_class}">{status}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            if st.button("🗑️", key=f"del_jdih_{item['id']}", use_container_width=True):
                delete_jdih(item["id"])
                st.rerun()
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: ADMIN USERS
# =========================================================
def render_admin_users_tab():
    st.markdown('<div class="section-title">👤 Manajemen Admin</div>', unsafe_allow_html=True)

    with st.form("form_add_admin", clear_on_submit=True):
        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            new_user = st.text_input("Username Baru")
        with c2:
            new_pass = st.text_input("Password", type="password")
        with c3:
            st.write("")
            st.write("")
            submit = st.form_submit_button("➕ Tambah", use_container_width=True)
        if submit:
            if new_user and new_pass:
                try:
                    create_admin(new_user, new_pass)
                    st.success("✅ Admin ditambahkan!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Gagal: {e}")
            else:
                st.error("Isi semua field")

    st.markdown('<div class="section-title">📋 Daftar Admin</div>', unsafe_allow_html=True)
    current = st.session_state.admin_user
    for adm in get_all_admins():
        c1, c2 = st.columns([5, 1])
        with c1:
            is_me = adm["id"] == current["id"]
            badge = '<span class="crud-badge">ANDA</span>' if is_me else ''
            st.markdown(f"""
            <div class="crud-content" style="padding: 8px 0;">
                <div class="crud-title">👤 {adm['username']} {badge}</div>
                <div class="crud-meta"><span>Dibuat: {adm.get('created_at', '')[:10]}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            if adm["id"] != current["id"]:
                if st.button("🗑️", key=f"del_adm_{adm['id']}", use_container_width=True):
                    delete_admin(adm["id"])
                    st.rerun()
            else:
                st.caption("—")
        st.markdown('<div style="height:1px;background:#e5ebe7;margin:10px 0;"></div>', unsafe_allow_html=True)

# =========================================================
# TAB: PENGATURAN
# =========================================================
def render_pengaturan_tab():
    st.markdown('<div class="section-title">⚙️ Pengaturan</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🔒 Ganti Password")
        with st.form("form_ganti_password"):
            p1 = st.text_input("Password Lama", type="password")
            p2 = st.text_input("Password Baru", type="password")
            p3 = st.text_input("Konfirmasi Password Baru", type="password")
            if st.form_submit_button("💾 Ganti Password", type="primary", use_container_width=True):
                user = login_admin(st.session_state.admin_user["username"], p1)
                if not user:
                    st.error("Password lama salah")
                elif p2 != p3:
                    st.error("Password baru tidak sama")
                elif len(p2) < 6:
                    st.error("Password minimal 6 karakter")
                else:
                    change_password(st.session_state.admin_user["id"], p2)
                    st.success("✅ Password berhasil diubah!")
                    st.balloons()

    with col2:
        st.markdown("### ℹ️ Info Sistem")
        st.markdown(f"""
        <div style="background:white;border-radius:14px;padding:20px;border:1px solid #e5ebe7;">
            <div style="margin-bottom:12px;">
                <div style="color:#94a3b8;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:0.8px;">User Login</div>
                <div style="color:#083d26;font-size:15px;font-weight:800;margin-top:4px;">👤 {st.session_state.admin_user['username']}</div>
            </div>
            <div style="margin-bottom:12px;">
                <div style="color:#94a3b8;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:0.8px;">Waktu Server</div>
                <div style="color:#083d26;font-size:14px;font-weight:700;margin-top:4px;">🕐 {datetime.now().strftime('%A, %d %B %Y · %H:%M:%S')}</div>
            </div>
            <div style="margin-bottom:12px;">
                <div style="color:#94a3b8;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:0.8px;">Database</div>
                <div style="color:#083d26;font-size:14px;font-weight:700;margin-top:4px;">🗄️ Supabase Cloud</div>
            </div>
            <div>
                <div style="color:#94a3b8;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:0.8px;">Storage</div>
                <div style="color:#083d26;font-size:14px;font-weight:700;margin-top:4px;">📦 Supabase Storage (<code>dprk-images</code>)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================
def render_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
    if not st.session_state.admin_logged_in:
        admin_login()
    else:
        admin_dashboard()
