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
    get_all_anggota, create_anggota, update_anggota, delete_anggota,
    get_all_fraksi, create_fraksi, update_fraksi, delete_fraksi,
    get_all_komisi, create_komisi, update_komisi, delete_komisi,
    get_all_faq, create_faq, update_faq, delete_faq,
)

LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

ADMIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
html, body, [class*="css"], .stApp { background: #f4f7f5 !important; color: #0f172a !important; }
* { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1500px; }
.stApp p, .stApp span, .stApp label, .stApp div, .stApp li { color: #0f172a; }
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 { color: #083d26 !important; }

section[data-testid="stSidebar"] { background: linear-gradient(180deg, #062b1b 0%, #0a3d24 100%) !important; border-right: none !important; box-shadow: 4px 0 24px rgba(0,0,0,0.08); }
section[data-testid="stSidebar"] > div { background: transparent !important; padding-top: 1rem !important; }
section[data-testid="stSidebar"] * { color: #e2efe8 !important; }
section[data-testid="stSidebar"] .stButton > button { background: transparent !important; border: 1px solid rgba(255,255,255,0.08) !important; color: #e2efe8 !important; text-align: left !important; justify-content: flex-start !important; padding: 12px 16px !important; border-radius: 10px !important; font-weight: 600 !important; font-size: 13.5px !important; margin-bottom: 4px !important; width: 100% !important; box-shadow: none !important; transition: all 0.2s ease !important; }
section[data-testid="stSidebar"] .stButton > button:hover { background: rgba(255,255,255,0.08) !important; border-color: rgba(201,162,39,0.4) !important; transform: translateX(4px) !important; }
section[data-testid="stSidebar"] .stButton > button p, section[data-testid="stSidebar"] .stButton > button span, section[data-testid="stSidebar"] .stButton > button div { color: #e2efe8 !important; text-align: left !important; font-weight: 600 !important; }
section[data-testid="stSidebar"] .stButton > button[kind="primary"] { background: linear-gradient(135deg, #c9a227 0%, #e0b93a 100%) !important; border-color: transparent !important; color: #062b1b !important; box-shadow: 0 6px 18px rgba(201,162,39,0.35) !important; }
section[data-testid="stSidebar"] .stButton > button[kind="primary"] p, section[data-testid="stSidebar"] .stButton > button[kind="primary"] span, section[data-testid="stSidebar"] .stButton > button[kind="primary"] div { color: #062b1b !important; font-weight: 800 !important; }

.sidebar-brand { display: flex; align-items: center; gap: 12px; padding: 14px 16px; margin-bottom: 8px; background: rgba(255,255,255,0.04); border-radius: 14px; border: 1px solid rgba(255,255,255,0.06); }
.sidebar-brand-logo { width: 42px; height: 42px; border-radius: 12px; background: white; padding: 6px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.sidebar-brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.sidebar-brand-text { line-height: 1.2; }
.sidebar-brand-title { color: #ffffff !important; font-weight: 900 !important; font-size: 13px !important; letter-spacing: 0.5px; font-family: 'Plus Jakarta Sans', sans-serif !important; }
.sidebar-brand-sub { color: #8fb8a3 !important; font-size: 10.5px !important; font-weight: 600 !important; margin-top: 2px; }
.sidebar-label { color: #6f9a83 !important; font-size: 10px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; padding: 16px 16px 6px !important; margin: 0 !important; }
.sidebar-user { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 14px; margin: 8px 0; }
.sidebar-user-name { color: #ffffff !important; font-weight: 800 !important; font-size: 13px !important; }
.sidebar-user-role { color: #8fb8a3 !important; font-size: 11px !important; font-weight: 600 !important; margin-top: 2px; }

.login-brand { background: linear-gradient(135deg, #f0fdf4 0%, #f7fef9 50%, #ffffff 100%); padding: 50px 40px; border-radius: 24px; box-shadow: 0 20px 60px rgba(0,0,0,0.06); min-height: 520px; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid #d1fae5; }
.login-brand-logo { display: inline-flex; align-items: center; justify-content: center; width: 90px; height: 90px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(13,94,58,0.15); border: 2px solid #d1fae5; margin-bottom: 28px; overflow: hidden; padding: 10px; }
.login-brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.login-brand h1 { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #0d5e3a !important; font-size: 34px !important; font-weight: 900 !important; letter-spacing: 1px !important; margin: 0 0 12px !important; line-height: 1.1 !important; }
.login-brand-sub { color: #0f172a !important; font-size: 15px !important; font-weight: 700 !important; margin-bottom: 20px !important; }
.login-brand-desc { color: #64748b !important; font-size: 14px !important; line-height: 1.7 !important; max-width: 400px !important; }
.login-brand-footer { display: flex; align-items: center; gap: 10px; color: #94a3b8 !important; font-size: 12px !important; font-weight: 600 !important; padding-top: 20px !important; border-top: 1px solid #bbf7d0 !important; }
.login-title { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #0f172a !important; font-size: 28px !important; font-weight: 800 !important; margin: 0 0 8px !important; }
.login-subtitle { color: #64748b !important; font-size: 14px !important; margin-bottom: 32px !important; }

div[data-testid="stForm"] { background: white !important; border-radius: 16px !important; padding: 22px !important; border: 1px solid #e5ebe7 !important; box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important; }
.stApp label { font-size: 11.5px !important; font-weight: 800 !important; color: #0d5e3a !important; text-transform: uppercase !important; letter-spacing: 0.8px !important; margin-bottom: 4px !important; }
.stApp input, .stApp textarea { background: #f8fafc !important; border: 1.5px solid #e2e8f0 !important; border-radius: 10px !important; padding: 11px 13px !important; font-size: 14px !important; color: #0f172a !important; transition: all 0.2s ease !important; }
.stApp input:focus, .stApp textarea:focus { border-color: #0d5e3a !important; box-shadow: 0 0 0 3px rgba(13,94,58,0.1) !important; background: white !important; }
div[data-baseweb="select"] > div { background: #f8fafc !important; border: 1.5px solid #e2e8f0 !important; color: #0f172a !important; border-radius: 10px !important; }
div[data-baseweb="select"] * { color: #0f172a !important; }

.stApp .stButton > button { background: linear-gradient(135deg, #0d5e3a, #14734a) !important; color: #ffffff !important; border: none !important; border-radius: 10px !important; font-weight: 700 !important; padding: 10px 16px !important; box-shadow: 0 4px 12px rgba(13,94,58,0.15) !important; font-size: 14px !important; transition: all 0.2s ease !important; }
.stApp .stButton > button:hover { background: linear-gradient(135deg, #14734a, #c9a227) !important; transform: translateY(-2px) !important; box-shadow: 0 8px 20px rgba(13,94,58,0.25) !important; }
.stApp .stButton > button p, .stApp .stButton > button span, .stApp .stButton > button div { color: #ffffff !important; font-weight: 700 !important; }

.admin-header { background: linear-gradient(135deg, #062b1b 0%, #0d5e3a 60%, #14734a 100%); color: white !important; padding: 28px 34px; border-radius: 20px; margin-bottom: 24px; box-shadow: 0 16px 40px rgba(13,94,58,0.25); position: relative; overflow: hidden; }
.admin-header::after { content: ''; position: absolute; right: -40px; top: -40px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(201,162,39,0.25) 0%, transparent 70%); border-radius: 50%; }
.admin-header h1 { margin: 0 !important; font-size: 24px !important; font-weight: 800 !important; color: white !important; position: relative; z-index: 1; }
.admin-header p { margin: 6px 0 0 !important; opacity: 0.95 !important; font-size: 13px !important; color: white !important; position: relative; z-index: 1; }
.admin-header * { color: white !important; }

.stat-box { background: white !important; border-radius: 16px; padding: 20px; border-left: 4px solid #0d5e3a; box-shadow: 0 4px 20px rgba(0,0,0,0.04); height: 100%; min-height: 110px; transition: all 0.2s ease; position: relative; overflow: hidden; }
.stat-box:hover { transform: translateY(-2px); box-shadow: 0 10px 28px rgba(0,0,0,0.08); }
.stat-box .label { color: #4a5a55 !important; font-size: 11px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 0.8px !important; }
.stat-box .value { color: #083d26 !important; font-size: 32px !important; font-weight: 900 !important; margin-top: 8px !important; line-height: 1 !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
.stat-box .sub { color: #94a3b8 !important; font-size: 11px !important; margin-top: 4px !important; font-weight: 600 !important; }

.panel-card { background: white; border-radius: 20px; padding: 26px 28px; border: 1px solid #e5ebe7; box-shadow: 0 8px 32px rgba(13,94,58,0.06); margin-bottom: 20px; }
.panel-title { font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 17px !important; font-weight: 800 !important; color: #083d26 !important; margin: 0 0 4px !important; display: flex; align-items: center; gap: 8px; }
.panel-sub { color: #64748b !important; font-size: 12.5px !important; font-weight: 600 !important; margin-bottom: 18px !important; }
.panel-divider { height: 1px; background: linear-gradient(90deg, #e5ebe7 0%, transparent 100%); margin: 18px 0; }
.form-badge { display: inline-flex; align-items: center; gap: 6px; background: linear-gradient(135deg, #f0fdf4, #dcfce7); color: #166534 !important; padding: 4px 12px; border-radius: 20px; font-size: 10.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 12px; }

.section-title { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #083d26 !important; font-size: 18px !important; font-weight: 800 !important; margin: 8px 0 16px !important; display: flex !important; align-items: center !important; gap: 10px !important; }
.section-title::before { content: ''; width: 4px; height: 20px; background: linear-gradient(180deg, #0d5e3a, #c9a227); border-radius: 4px; }

.crud-item { background: white; border-radius: 14px; padding: 14px 16px; border: 1px solid #e5ebe7; margin-bottom: 10px; transition: all 0.2s ease; }
.crud-item:hover { border-color: #0d5e3a; box-shadow: 0 6px 20px rgba(13,94,58,0.08); transform: translateY(-1px); }
.crud-title { font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 14px !important; font-weight: 800 !important; color: #083d26 !important; margin: 0 0 4px !important; line-height: 1.4 !important; }
.crud-meta { font-size: 11.5px !important; color: #64748b !important; font-weight: 600 !important; display: flex !important; gap: 10px !important; flex-wrap: wrap !important; margin-top: 4px !important; }
.crud-badge { display: inline-block !important; background: #f0fdf4 !important; color: #166534 !important; padding: 3px 10px !important; border-radius: 20px !important; font-size: 10.5px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 0.4px !important; }
.crud-badge-gold { background: #fef9c3 !important; color: #854d0e !important; }
.crud-badge-red { background: #fee2e2 !important; color: #991b1b !important; }
.crud-badge-blue { background: #dbeafe !important; color: #1e40af !important; }

.empty-state { text-align: center; padding: 56px 20px; background: white !important; border-radius: 18px; border: 2px dashed #e5ebe7; }
.empty-state-icon { font-size: 52px; margin-bottom: 14px; opacity: 0.4; }
.empty-state-text { color: #94a3b8 !important; font-size: 14px !important; font-weight: 600 !important; }
div[data-testid="stExpander"] { background: white !important; border: 1px solid #e5ebe7 !important; border-radius: 14px !important; margin-bottom: 12px !important; overflow: hidden !important; box-shadow: 0 2px 10px rgba(0,0,0,0.02) !important; }
div[data-testid="stExpander"] summary { background: white !important; padding: 14px 18px !important; cursor: pointer !important; }
div[data-testid="stExpander"] summary:hover { background: #f0fdf4 !important; }
div[data-testid="stExpander"] summary p { color: #083d26 !important; font-weight: 800 !important; font-size: 14px !important; margin: 0 !important; }
div[data-testid="stAlert"] { border-radius: 12px !important; padding: 12px 16px !important; }
div[data-testid="stAlert"] p, div[data-testid="stAlert"] span, div[data-testid="stAlert"] div { color: #0f172a !important; font-weight: 600 !important; }
div[data-testid="stPopover"] > button, div[data-testid="stPopover"] button { background: white !important; border: 1px solid #e5ebe7 !important; color: #083d26 !important; font-weight: 700 !important; }
div[data-testid="stPopover"] button p, div[data-testid="stPopover"] button span { color: #083d26 !important; font-weight: 700 !important; }
div[data-testid="stFileUploader"] { background: #f8fafc !important; border: 2px dashed #cbd5e1 !important; border-radius: 12px !important; padding: 12px !important; }
div[data-testid="stFileUploader"] * { color: #0f172a !important; }
div[data-testid="stFileUploader"] button { background: white !important; border: 1px solid #0d5e3a !important; color: #0d5e3a !important; font-weight: 700 !important; }
div[data-testid="stFileUploader"] button * { color: #0d5e3a !important; }
@media (max-width: 768px) { .login-brand { padding: 40px 30px; min-height: auto; } .login-brand h1 { font-size: 26px !important; } .stat-box .value { font-size: 26px !important; } .block-container { padding: 1rem !important; } }
</style>
"""

def admin_login():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
        <div class="login-brand">
            <div>
                <div class="login-brand-logo"><img src="{LOGO_URL}" alt="Logo"></div>
                <h1>DPRK ACEH JAYA</h1>
                <div class="login-brand-sub">Dewan Perwakilan Rakyat Kabupaten</div>
                <div class="login-brand-desc">Panel admin untuk mengelola konten website DPRK Aceh Jaya — berita, agenda, galeri, pengaduan, dan lainnya.</div>
            </div>
            <div class="login-brand-footer">🔒 Sistem Autentikasi Aman & Terenkripsi</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="padding: 40px 0 20px;">
            <div class="login-title">Login Administrator</div>
            <div class="login-subtitle">Masukkan kredensial akun Anda untuk melanjutkan.</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("USERNAME", placeholder="Masukkan username", key="login_username")
            password = st.text_input("PASSWORD", type="password", placeholder="Masukkan password", key="login_password")
            submit = st.form_submit_button("Masuk ke Panel  →", use_container_width=True, type="primary")
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

def show_empty_state(icon, text):
    st.markdown(f'<div class="empty-state"><div class="empty-state-icon">{icon}</div><div class="empty-state-text">{text}</div></div>', unsafe_allow_html=True)

def panel_header(icon, title, subtitle=""):
    st.markdown(f'<div style="margin-bottom: 6px;"><span class="form-badge">✨ Form Input</span></div><div class="panel-title">{icon} {title}</div><div class="panel-sub">{subtitle}</div>', unsafe_allow_html=True)

MENU_ITEMS = [
    ("dashboard", "🏠", "Dashboard"), ("berita", "📰", "Berita"), ("agenda", "📅", "Agenda"), ("galeri", "🖼️", "Galeri"),
    ("anggota", "👥", "Anggota DPRK"), ("fraksi", "🏛️", "Fraksi"), ("komisi", "📋", "Komisi"), ("faq", "❓", "FAQ"),
    ("running_text", "📢", "Running Text"), ("kesekretariatan", "📋", "Kesekretariatan"), ("pengaduan", "📥", "Pengaduan"),
    ("pimpinan", "👥", "Pimpinan"), ("pejabat", "🏢", "Pejabat"), ("jdih", "📜", "JDIH"),
    ("admin_users", "👤", "Manajemen Admin"), ("pengaturan", "⚙️", "Pengaturan"),
]

def render_sidebar():
    user = st.session_state.admin_user
    with st.sidebar:
        st.markdown(f'<div class="sidebar-brand"><div class="sidebar-brand-logo"><img src="{LOGO_URL}" alt="Logo"></div><div class="sidebar-brand-text"><div class="sidebar-brand-title">DPRK ACEH JAYA</div><div class="sidebar-brand-sub">Admin Panel</div></div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sidebar-user"><div class="sidebar-user-name">👤 {user["username"]}</div><div class="sidebar-user-role">Administrator</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-label">Menu Utama</div>', unsafe_allow_html=True)
        if "admin_page" not in st.session_state:
            st.session_state.admin_page = "dashboard"
        for key, icon, label in MENU_ITEMS:
            is_active = st.session_state.admin_page == key
            if st.button(f"{icon}  {label}", key=f"nav_{key}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.admin_page = key
                st.rerun()
        st.markdown('<div class="sidebar-label">Aksi</div>', unsafe_allow_html=True)
        if st.button("🌐  Lihat Website", key="nav_website", use_container_width=True):
            st.query_params["page"] = "public"
            st.rerun()
        if st.button("🚪  Logout", key="nav_logout", use_container_width=True):
            st.session_state.admin_logged_in = False
            st.session_state.admin_user = None
            st.session_state.admin_page = "dashboard"
            st.rerun()

def admin_dashboard():
    user = st.session_state.admin_user
    st.markdown(f'<div class="admin-header"><h1>🏛️ Admin Panel DPRK</h1><p>Selamat datang, <b>{user["username"]}</b> · Kelola konten website DPRK Aceh Jaya</p></div>', unsafe_allow_html=True)
    with st.spinner("Memuat ringkasan data..."):
        b_count = len(get_all_berita()); p_count = len(get_all_pengaduan()); g_count = len(get_all_galeri()); a_count = len(get_all_agenda()); ang_count = len(get_all_anggota())
    s1, s2, s3, s4, s5 = st.columns(5)
    stats = [(s1, "Berita", b_count, "📰", "Total artikel", "#0d5e3a"), (s2, "Pengaduan", p_count, "📥", "Total masuk", "#dc2626"), (s3, "Galeri", g_count, "🖼️", "Foto dokumentasi", "#c9a227"), (s4, "Agenda", a_count, "📅", "Jadwal rapat", "#14734a"), (s5, "Anggota", ang_count, "👥", "Total anggota", "#1e40af")]
    for col, label, value, icon, sub, color in stats:
        with col: st.markdown(f'<div class="stat-box" style="border-left-color: {color};"><div class="label">{icon} {label}</div><div class="value">{value}</div><div class="sub">{sub}</div></div>', unsafe_allow_html=True)

def page_berita():
    st.markdown('<div class="section-title">📰 Kelola Berita</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Berita", "Isi form untuk menambah berita.")
        with st.form("form_tambah_berita", clear_on_submit=True):
            title = st.text_input("Judul Berita *"); date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
            kategori = st.selectbox("Kategori", ["Paripurna", "Lingkungan", "Hukum", "Legislasi", "Kunjungan", "Reses", "Rapat", "Sosial", "Ekonomi", "Lainnya"])
            desc_text = st.text_area("Deskripsi Berita *", height=120)
            up_method = st.radio("Sumber Foto", ["Upload File", "URL Manual"], horizontal=True)
            uploaded, image_url_manual = None, ""
            if up_method == "Upload File": uploaded = st.file_uploader("Pilih foto", type=["jpg", "jpeg", "png", "webp"])
            else: image_url_manual = st.text_input("URL Foto", placeholder="https://...")
            if st.form_submit_button("💾 Simpan Berita", type="primary", use_container_width=True):
                if not title or not desc_text: st.error("Judul & deskripsi wajib diisi")
                else:
                    img = image_url_manual
                    if uploaded: img = upload_image(uploaded, folder="berita")
                    create_berita(title, date, desc_text, img, kategori); st.success("✅ Berhasil!"); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        c_search, c_refresh = st.columns([4, 1])
        with c_search: search = st.text_input("🔎 Cari berita", placeholder="Ketik judul...", key="search_berita")
        with c_refresh: st.write(""); st.write(""); st.button("🔄 Refresh", key="refresh_berita", use_container_width=True, on_click=st.rerun)
        with st.spinner("Memuat berita..."): berita_list = get_all_berita()
        st.caption(f"📊 Total berita di database: **{len(berita_list)}**")
        if search: berita_list = [b for b in berita_list if search.lower() in b.get("title", "").lower()]
        if not berita_list: show_empty_state("📰", "Belum ada berita."); return
        for item in berita_list:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c_img, c_info = st.columns([1, 6])
            with c_img:
                if item.get("image_url"): st.image(item["image_url"], width=70)
                else: st.markdown('<div style="width:70px;height:70px;background:#f1f5f9;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:26px;">🖼️</div>', unsafe_allow_html=True)
            with c_info: st.markdown(f'<div class="crud-title">{item["title"]}</div><div class="crud-meta"><span>📅 {item.get("date", "-")}</span><span class="crud-badge">{item.get("kategori", "-")}</span><span>👁️ {item.get("views", 0)}</span></div>', unsafe_allow_html=True)
            ca, cb, _ = st.columns([1, 1, 4])
            with ca:
                with st.popover("✏️ Edit", use_container_width=True):
                    with st.form(f"edit_berita_{item['id']}"):
                        nt = st.text_input("Judul", value=item["title"]); nd = st.text_input("Tanggal", value=item.get("date", ""))
                        nk = st.text_input("Kategori", value=item.get("kategori", "")); ndesc = st.text_area("Deskripsi", value=item.get("desc_text", ""), height=100)
                        nup = st.file_uploader("Upload Foto Baru", type=["jpg", "png", "jpeg", "webp"]); nurl = st.text_input("Atau URL Baru", value=item.get("image_url", ""))
                        if st.form_submit_button("✅ Update", use_container_width=True):
                            new_img = nurl
                            if nup: new_img = upload_image(nup, folder="berita")
                            update_berita(item["id"], title=nt, date=nd, desc_text=ndesc, kategori=nk, image_url=new_img); st.success("Diupdate!"); st.rerun()
            with cb:
                if st.button("🗑️ Hapus", key=f"del_b_{item['id']}", use_container_width=True):
                    delete_berita(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_agenda():
    st.markdown('<div class="section-title">📅 Kelola Agenda</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Agenda", "Detail agenda DPRK.")
        with st.form("form_agenda", clear_on_submit=True):
            hari = st.text_input("Hari", max_chars=2); bulan_tahun = st.text_input("Bulan Tahun")
            tanggal_full = st.text_input("Tanggal Lengkap", value=datetime.now().strftime("%A, %d %B %Y"))
            judul = st.text_input("Judul Agenda *"); deskripsi = st.text_area("Deskripsi", height=80)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not judul: st.error("Judul wajib diisi")
                else: create_agenda(hari, bulan_tahun, tanggal_full, judul, deskripsi); st.success("✅ Berhasil!"); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat agenda..."): items = get_all_agenda()
        if not items: show_empty_state("📅", "Belum ada agenda."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">📅 {item.get("hari", "")} {item.get("bulan_tahun", "")} — {item["judul"]}</div><div class="crud-meta"><span>{item.get("tanggal_full", "")}</span><span>{(item.get("deskripsi", "") or "")[:80]}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_ag_{item['id']}", use_container_width=True): delete_agenda(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_galeri():
    st.markdown('<div class="section-title">🖼️ Kelola Galeri</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("📤", "Upload Foto", "Tambah foto.")
        with st.form("form_galeri", clear_on_submit=True):
            gtitle = st.text_input("Judul Foto *"); gfile = st.file_uploader("Pilih Foto *", type=["jpg", "jpeg", "png", "webp"])
            if st.form_submit_button("💾 Upload", type="primary", use_container_width=True):
                if not gfile or not gtitle: st.error("Wajib diisi")
                else:
                    url = upload_image(gfile, folder="galeri")
                    if url: create_galeri(gtitle, url); st.success("✅ Berhasil!"); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat galeri..."): items = get_all_galeri()
        if not items: show_empty_state("🖼️", "Belum ada foto."); return
        cols = st.columns(2)
        for i, item in enumerate(items):
            with cols[i % 2]:
                st.markdown('<div class="crud-item">', unsafe_allow_html=True)
                st.image(item["image_url"], caption=item["title"], use_container_width=True)
                if st.button("🗑️ Hapus", key=f"del_g_{item['id']}", use_container_width=True): delete_galeri(item["id"]); st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

def page_anggota():
    st.markdown('<div class="section-title">👥 Kelola Anggota DPRK</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Anggota", "Data anggota.")
        with st.form("form_anggota", clear_on_submit=True):
            nama = st.text_input("Nama *"); jabatan = st.text_input("Jabatan", value="Anggota")
            komisi = st.selectbox("Komisi", ["Komisi I", "Komisi II", "Komisi III", "Komisi IV", "-"]); dapil = st.selectbox("Dapil", ["Dapil 1", "Dapil 2", "Dapil 3", "Dapil 4", "Dapil 5", "-"])
            fraksi = st.text_input("Fraksi"); urutan = st.number_input("Urutan", 1, 100, 1); foto = st.file_uploader("Foto", type=["jpg", "png"])
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not nama: st.error("Nama wajib")
                else:
                    f_url = upload_image(foto, folder="anggota") if foto else None
                    create_anggota(nama, jabatan, komisi, dapil, fraksi, urutan, f_url); st.success("✅ Berhasil!"); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat anggota..."): items = get_all_anggota()
        if not items: show_empty_state("👥", "Belum ada anggota."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 5, 1.4])
            with c1:
                if item.get("foto_url"): st.image(item["foto_url"], width=56)
                else: st.markdown('<div style="width:56px;height:56px;background:#f1f5f9;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:22px;">👤</div>', unsafe_allow_html=True)
            with c2: st.markdown(f'<div class="crud-title">{item["nama"]}</div><div class="crud-meta"><span class="crud-badge crud-badge-gold">{item.get("jabatan")}</span><span>{item.get("komisi")}</span><span>{item.get("dapil")}</span></div>', unsafe_allow_html=True)
            with c3:
                ca, cb = st.columns(2)
                with ca:
                    with st.popover("✏️", use_container_width=True):
                        with st.form(f"edit_ang_{item['id']}"):
                            nn = st.text_input("Nama", value=item["nama"]); nj = st.text_input("Jabatan", value=item.get("jabatan")); nk = st.text_input("Komisi", value=item.get("komisi")); nd = st.text_input("Dapil", value=item.get("dapil")); nf = st.text_input("Fraksi", value=item.get("fraksi"))
                            if st.form_submit_button("✅ Update", use_container_width=True): update_anggota(item["id"], nama=nn, jabatan=nj, komisi=nk, dapil=nd, fraksi=nf); st.rerun()
                with cb:
                    if st.button("🗑️", key=f"del_ang_{item['id']}", use_container_width=True): delete_anggota(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_fraksi():
    st.markdown('<div class="section-title">🏛️ Kelola Fraksi</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Fraksi")
        with st.form("form_fraksi", clear_on_submit=True):
            nama = st.text_input("Nama Fraksi *"); ketua = st.text_input("Ketua"); jumlah = st.number_input("Jumlah Anggota", 0, 100, 0)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not nama: st.error("Nama wajib")
                else: create_fraksi(nama, ketua, jumlah); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat fraksi..."): items = get_all_fraksi()
        if not items: show_empty_state("🏛️", "Belum ada fraksi."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">🏛️ {item["nama"]}</div><div class="crud-meta"><span>Ketua: {item.get("ketua")}</span><span class="crud-badge">{item.get("jumlah_anggota")} anggota</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_fr_{item['id']}", use_container_width=True): delete_fraksi(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_komisi():
    st.markdown('<div class="section-title">📋 Kelola Komisi</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Komisi")
        with st.form("form_komisi", clear_on_submit=True):
            nama = st.text_input("Nama Komisi *"); ketua = st.text_input("Ketua"); bidang = st.text_area("Bidang", height=80)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not nama: st.error("Nama wajib")
                else: create_komisi(nama, ketua, bidang); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat komisi..."): items = get_all_komisi()
        if not items: show_empty_state("📋", "Belum ada komisi."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">📋 {item["nama"]}</div><div class="crud-meta"><span>Ketua: {item.get("ketua")}</span><span>{item.get("bidang")}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_kom_{item['id']}", use_container_width=True): delete_komisi(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_faq():
    st.markdown('<div class="section-title">❓ Kelola FAQ</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah FAQ")
        with st.form("form_faq", clear_on_submit=True):
            pertanyaan = st.text_input("Pertanyaan *"); jawaban = st.text_area("Jawaban *", height=100)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not pertanyaan or not jawaban: st.error("Wajib diisi")
                else: create_faq(pertanyaan, jawaban); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat FAQ..."): items = get_all_faq()
        if not items: show_empty_state("❓", "Belum ada FAQ."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">❓ {item["pertanyaan"]}</div><div class="crud-meta"><span>{item.get("jawaban")[:100]}...</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_faq_{item['id']}", use_container_width=True): delete_faq(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_running_text():
    st.markdown('<div class="section-title">📢 Kelola Running Text</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Teks")
        with st.form("form_rt", clear_on_submit=True):
            content = st.text_area("Isi *", height=80)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if content: create_running_text(content); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat teks..."): items = get_running_text_active()
        if not items: show_empty_state("📢", "Belum ada teks."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.info(item["content"])
            with c2:
                if st.button("🗑️", key=f"del_rt_{item['id']}", use_container_width=True): delete_running_text(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_kesekretariatan():
    st.markdown('<div class="section-title">📋 Kelola Kesekretariatan</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Data")
        with st.form("form_kes", clear_on_submit=True):
            title = st.text_input("Judul *"); date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if title: create_kesekretariatan(title, date); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat data..."): items = get_all_kesekretariatan()
        if not items: show_empty_state("📋", "Belum ada data."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">{item["title"]}</div><div class="crud-meta"><span>📅 {item.get("date")}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_kes_{item['id']}", use_container_width=True): delete_kesekretariatan(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_pengaduan():
    st.markdown('<div class="section-title">📥 Pengaduan</div>', unsafe_allow_html=True)
    with st.spinner("Memuat..."): pengaduan_list = get_all_pengaduan()
    if not pengaduan_list: show_empty_state("📥", "Belum ada pengaduan."); return
    status_filter = st.selectbox("Filter", ["Semua", "Baru", "Diproses", "Selesai", "Ditolak"])
    if status_filter != "Semua": pengaduan_list = [p for p in pengaduan_list if p.get("status") == status_filter]
    for p in pengaduan_list:
        with st.expander(f"🎫 {p['tiket']} — {p['nama']} ({p.get('status')})"):
            st.write(f"**Kategori:** {p['kategori']} | **Lokasi:** {p.get('lokasi')} | **NIK:** {p.get('nik')}")
            st.info(p["isi"])
            c3, c4 = st.columns(2)
            with c3:
                new_status = st.selectbox("Update Status", ["Baru", "Diproses", "Selesai", "Ditolak"], index=["Baru", "Diproses", "Selesai", "Ditolak"].index(p.get("status", "Baru")))
                if st.button("✅ Update", key=f"upd_{p['id']}"): update_status_pengaduan(p["id"], new_status); st.rerun()
            with c4:
                if st.button("🗑️ Hapus", key=f"del_p_{p['id']}"): delete_pengaduan(p["id"]); st.rerun()

def page_pimpinan():
    st.markdown('<div class="section-title">👥 Pimpinan</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Pimpinan")
        with st.form("form_pim", clear_on_submit=True):
            nama = st.text_input("Nama *"); jabatan = st.text_input("Jabatan *"); urutan = st.number_input("Urutan", 1); foto = st.file_uploader("Foto", type=["jpg", "png"])
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nama and jabatan:
                    f_url = upload_image(foto, folder="pimpinan") if foto else None
                    create_pimpinan(nama, jabatan, urutan, f_url); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat..."): items = get_all_pimpinan()
        if not items: show_empty_state("👥", "Belum ada data."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 5, 1])
            with c1:
                if item.get("foto_url"): st.image(item["foto_url"], width=56)
            with c2: st.markdown(f'<div class="crud-title">{item["nama"]}</div><div class="crud-meta"><span class="crud-badge crud-badge-gold">{item["jabatan"]}</span></div>', unsafe_allow_html=True)
            with c3:
                if st.button("🗑️", key=f"del_pim_{item['id']}"): delete_pimpinan(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_pejabat():
    st.markdown('<div class="section-title">🏢 Pejabat</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Pejabat")
        with st.form("form_pej", clear_on_submit=True):
            nama = st.text_input("Nama *"); jabatan = st.text_input("Jabatan *"); urutan = st.number_input("Urutan", 1)
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nama and jabatan: create_pejabat(nama, jabatan, urutan); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat..."): items = get_all_pejabat()
        if not items: show_empty_state("🏢", "Belum ada data."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">{item["nama"]}</div><div class="crud-meta"><span class="crud-badge crud-badge-blue">{item["jabatan"]}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_pej_{item['id']}"): delete_pejabat(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_jdih():
    st.markdown('<div class="section-title">📜 JDIH</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Hukum")
        with st.form("form_jdih", clear_on_submit=True):
            nomor = st.text_input("Nomor *"); tentang = st.text_input("Tentang *"); status = st.selectbox("Status", ["Berlaku", "Dicabut", "Diubah"])
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nomor and tentang: create_jdih(nomor, tentang, status); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat..."): items = get_all_jdih()
        if not items: show_empty_state("📜", "Belum ada data."); return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1: st.markdown(f'<div class="crud-title">{item["nomor"]} — {item["tentang"]}</div><div class="crud-meta"><span class="crud-badge">{item.get("status")}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_jdih_{item['id']}"): delete_jdih(item["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_admin_users():
    st.markdown('<div class="section-title">👤 Manajemen Admin</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("➕", "Tambah Admin")
        with st.form("form_adm", clear_on_submit=True):
            nu = st.text_input("Username"); np = st.text_input("Password", type="password")
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nu and np: create_admin(nu, np); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat..."): admins = get_all_admins()
        current = st.session_state.admin_user
        for adm in admins:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([5, 1])
            with c1: st.markdown(f'<div class="crud-title">👤 {adm["username"]} {"(Anda)" if adm["id"]==current["id"] else ""}</div>', unsafe_allow_html=True)
            with c2:
                if adm["id"] != current["id"]:
                    if st.button("🗑️", key=f"del_adm_{adm['id']}"): delete_admin(adm["id"]); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

def page_pengaturan():
    st.markdown('<div class="section-title">⚙️ Pengaturan</div>', unsafe_allow_html=True)
    col1, _ = st.columns([1, 1])
    with col1:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True); panel_header("🔒", "Ganti Password")
        with st.form("form_pass"):
            p1 = st.text_input("Password Lama", type="password"); p2 = st.text_input("Password Baru", type="password"); p3 = st.text_input("Konfirmasi", type="password")
            if st.form_submit_button("💾 Ganti", type="primary"):
                user = login_admin(st.session_state.admin_user["username"], p1)
                if not user: st.error("Password lama salah")
                elif p2 != p3: st.error("Konfirmasi tidak cocok")
                elif len(p2) < 6: st.error("Minimal 6 karakter")
                else: change_password(st.session_state.admin_user["id"], p2); st.success("✅ Berhasil!")
        st.markdown('</div>', unsafe_allow_html=True)

PAGE_ROUTES = {
    "dashboard": admin_dashboard, "berita": page_berita, "agenda": page_agenda, "galeri": page_galeri,
    "anggota": page_anggota, "fraksi": page_fraksi, "komisi": page_komisi, "faq": page_faq,
    "running_text": page_running_text, "kesekretariatan": page_kesekretariatan, "pengaduan": page_pengaduan,
    "pimpinan": page_pimpinan, "pejabat": page_pejabat, "jdih": page_jdih,
    "admin_users": page_admin_users, "pengaturan": page_pengaturan,
}

def render_admin_dashboard():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    render_sidebar()
    current = st.session_state.get("admin_page", "dashboard")
    route = PAGE_ROUTES.get(current, admin_dashboard)
    route()

def render_admin():
    if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False
    if "admin_page" not in st.session_state: st.session_state.admin_page = "dashboard"
    if not st.session_state.admin_logged_in: admin_login()
    else: render_admin_dashboard()
