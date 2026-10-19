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
    get_all_anggota, create_anggota, update_anggota, delete_anggota,
    get_all_fraksi, create_fraksi, delete_fraksi,
    get_all_komisi, create_komisi, delete_komisi,
    get_all_faq, create_faq, delete_faq,
)

# =========================================================
# KONFIGURASI & LOGO
# =========================================================
LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# =========================================================
# CSS PREMIUM ADMIN (Dikembalikan seperti awal)
# =========================================================
ADMIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');

html, body, [class*="css"], .stApp {
    background: #f4f7f5 !important;
    color: #0f172a !important;
}
* { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1500px; }

.stApp p, .stApp span, .stApp label, .stApp div, .stApp li { color: #0f172a; }
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 { color: #083d26 !important; }

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #062b1b 0%, #0a3d24 100%) !important;
    border-right: none !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.08);
}
section[data-testid="stSidebar"] > div {
    background: transparent !important;
    padding-top: 1rem !important;
}
section[data-testid="stSidebar"] * { color: #e2efe8 !important; }
section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: #e2efe8 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 12px 16px !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    margin-bottom: 4px !important;
    width: 100% !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(201,162,39,0.4) !important;
    transform: translateX(4px) !important;
}
section[data-testid="stSidebar"] .stButton > button p,
section[data-testid="stSidebar"] .stButton > button span,
section[data-testid="stSidebar"] .stButton > button div {
    color: #e2efe8 !important;
    text-align: left !important;
    font-weight: 600 !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #c9a227 0%, #e0b93a 100%) !important;
    border-color: transparent !important;
    color: #062b1b !important;
    box-shadow: 0 6px 18px rgba(201,162,39,0.35) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"] p,
section[data-testid="stSidebar"] .stButton > button[kind="primary"] span,
section[data-testid="stSidebar"] .stButton > button[kind="primary"] div {
    color: #062b1b !important;
    font-weight: 800 !important;
}

/* Sidebar Brand */
.sidebar-brand {
    display: flex; align-items: center; gap: 12px;
    padding: 14px 16px; margin-bottom: 8px;
    background: rgba(255,255,255,0.04);
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.06);
}
.sidebar-brand-logo {
    width: 42px; height: 42px; border-radius: 12px;
    background: white; padding: 6px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.sidebar-brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.sidebar-brand-text { line-height: 1.2; }
.sidebar-brand-title {
    color: #ffffff !important; font-weight: 900 !important;
    font-size: 13px !important; letter-spacing: 0.5px;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.sidebar-brand-sub { color: #8fb8a3 !important; font-size: 10.5px !important; font-weight: 600 !important; margin-top: 2px; }

/* Sidebar Label & User */
.sidebar-label { color: #6f9a83 !important; font-size: 10px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; padding: 16px 16px 6px !important; margin: 0 !important; }
.sidebar-user { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 12px 14px; margin: 8px 0; }
.sidebar-user-name { color: #ffffff !important; font-weight: 800 !important; font-size: 13px !important; }
.sidebar-user-role { color: #8fb8a3 !important; font-size: 11px !important; font-weight: 600 !important; margin-top: 2px; }

/* ===== LOGIN ===== */
.login-brand { background: linear-gradient(135deg, #f0fdf4 0%, #f7fef9 50%, #ffffff 100%); padding: 50px 40px; border-radius: 24px; box-shadow: 0 20px 60px rgba(0,0,0,0.06); min-height: 520px; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid #d1fae5; }
.login-brand-logo { display: inline-flex; align-items: center; justify-content: center; width: 90px; height: 90px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(13,94,58,0.15); border: 2px solid #d1fae5; margin-bottom: 28px; overflow: hidden; padding: 10px; }
.login-brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.login-brand h1 { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #0d5e3a !important; font-size: 34px !important; font-weight: 900 !important; letter-spacing: 1px !important; margin: 0 0 12px !important; line-height: 1.1 !important; }
.login-brand-sub { color: #0f172a !important; font-size: 15px !important; font-weight: 700 !important; margin-bottom: 20px !important; }
.login-brand-desc { color: #64748b !important; font-size: 14px !important; line-height: 1.7 !important; max-width: 400px !important; }
.login-brand-footer { display: flex; align-items: center; gap: 10px; color: #94a3b8 !important; font-size: 12px !important; font-weight: 600 !important; padding-top: 20px !important; border-top: 1px solid #bbf7d0 !important; }
.login-title { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #0f172a !important; font-size: 28px !important; font-weight: 800 !important; margin: 0 0 8px !important; }
.login-subtitle { color: #64748b !important; font-size: 14px !important; margin-bottom: 32px !important; }

/* ===== FORMS ===== */
div[data-testid="stForm"] { background: white !important; border-radius: 16px !important; padding: 22px !important; border: 1px solid #e5ebe7 !important; box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important; }
.stApp label { font-size: 11.5px !important; font-weight: 800 !important; color: #0d5e3a !important; text-transform: uppercase !important; letter-spacing: 0.8px !important; margin-bottom: 4px !important; }
.stApp input, .stApp textarea { background: #f8fafc !important; border: 1.5px solid #e2e8f0 !important; border-radius: 10px !important; padding: 11px 13px !important; font-size: 14px !important; color: #0f172a !important; transition: all 0.2s ease !important; }
.stApp input:focus, .stApp textarea:focus { border-color: #0d5e3a !important; box-shadow: 0 0 0 3px rgba(13,94,58,0.1) !important; background: white !important; }
.stApp input::placeholder, .stApp textarea::placeholder { color: #94a3b8 !important; }
div[data-baseweb="select"] > div { background: #f8fafc !important; border: 1.5px solid #e2e8f0 !important; color: #0f172a !important; border-radius: 10px !important; }
div[data-baseweb="select"] * { color: #0f172a !important; }

/* ===== BUTTONS ===== */
.stApp .stButton > button { background: linear-gradient(135deg, #0d5e3a, #14734a) !important; color: #ffffff !important; border: none !important; border-radius: 10px !important; font-weight: 700 !important; padding: 10px 16px !important; box-shadow: 0 4px 12px rgba(13,94,58,0.15) !important; font-size: 14px !important; transition: all 0.2s ease !important; }
.stApp .stButton > button:hover { background: linear-gradient(135deg, #14734a, #c9a227) !important; transform: translateY(-2px) !important; box-shadow: 0 8px 20px rgba(13,94,58,0.25) !important; }
.stApp .stButton > button p, .stApp .stButton > button span, .stApp .stButton > button div { color: #ffffff !important; font-weight: 700 !important; }

/* ===== HEADER ===== */
.admin-header { background: linear-gradient(135deg, #062b1b 0%, #0d5e3a 60%, #14734a 100%); color: white !important; padding: 28px 34px; border-radius: 20px; margin-bottom: 24px; box-shadow: 0 16px 40px rgba(13,94,58,0.25); position: relative; overflow: hidden; }
.admin-header::after { content: ''; position: absolute; right: -40px; top: -40px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(201,162,39,0.25) 0%, transparent 70%); border-radius: 50%; }
.admin-header h1 { margin: 0 !important; font-size: 24px !important; font-weight: 800 !important; color: white !important; position: relative; z-index: 1; }
.admin-header p { margin: 6px 0 0 !important; opacity: 0.95 !important; font-size: 13px !important; color: white !important; position: relative; z-index: 1; }
.admin-header * { color: white !important; }

/* ===== STAT BOXES ===== */
.stat-box { background: white !important; border-radius: 16px; padding: 20px; border-left: 4px solid #0d5e3a; box-shadow: 0 4px 20px rgba(0,0,0,0.04); height: 100%; min-height: 110px; transition: all 0.2s ease; position: relative; overflow: hidden; }
.stat-box:hover { transform: translateY(-2px); box-shadow: 0 10px 28px rgba(0,0,0,0.08); }
.stat-box .label { color: #4a5a55 !important; font-size: 11px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 0.8px !important; }
.stat-box .value { color: #083d26 !important; font-size: 32px !important; font-weight: 900 !important; margin-top: 8px !important; line-height: 1 !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
.stat-box .sub { color: #94a3b8 !important; font-size: 11px !important; margin-top: 4px !important; font-weight: 600 !important; }

/* ===== PANEL CARD ===== */
.panel-card { background: white; border-radius: 20px; padding: 26px 28px; border: 1px solid #e5ebe7; box-shadow: 0 8px 32px rgba(13,94,58,0.06); margin-bottom: 20px; }
.panel-title { font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 17px !important; font-weight: 800 !important; color: #083d26 !important; margin: 0 0 4px !important; display: flex; align-items: center; gap: 8px; }
.panel-sub { color: #64748b !important; font-size: 12.5px !important; font-weight: 600 !important; margin-bottom: 18px !important; }
.panel-divider { height: 1px; background: linear-gradient(90deg, #e5ebe7 0%, transparent 100%); margin: 18px 0; }
.form-badge { display: inline-flex; align-items: center; gap: 6px; background: linear-gradient(135deg, #f0fdf4, #dcfce7); color: #166534 !important; padding: 4px 12px; border-radius: 20px; font-size: 10.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 12px; }

/* ===== SECTION TITLE ===== */
.section-title { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #083d26 !important; font-size: 18px !important; font-weight: 800 !important; margin: 8px 0 16px !important; display: flex !important; align-items: center !important; gap: 10px !important; }
.section-title::before { content: ''; width: 4px; height: 20px; background: linear-gradient(180deg, #0d5e3a, #c9a227); border-radius: 4px; }

/* ===== CRUD LIST ===== */
.crud-item { background: white; border-radius: 14px; padding: 14px 16px; border: 1px solid #e5ebe7; margin-bottom: 10px; transition: all 0.2s ease; }
.crud-item:hover { border-color: #0d5e3a; box-shadow: 0 6px 20px rgba(13,94,58,0.08); transform: translateY(-1px); }
.crud-title { font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 14px !important; font-weight: 800 !important; color: #083d26 !important; margin: 0 0 4px !important; line-height: 1.4 !important; }
.crud-meta { font-size: 11.5px !important; color: #64748b !important; font-weight: 600 !important; display: flex !important; gap: 10px !important; flex-wrap: wrap !important; margin-top: 4px !important; }
.crud-badge { display: inline-block !important; background: #f0fdf4 !important; color: #166534 !important; padding: 3px 10px !important; border-radius: 20px !important; font-size: 10.5px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 0.4px !important; }
.crud-badge-gold { background: #fef9c3 !important; color: #854d0e !important; }
.crud-badge-red { background: #fee2e2 !important; color: #991b1b !important; }
.crud-badge-blue { background: #dbeafe !important; color: #1e40af !important; }

/* ===== EMPTY STATE ===== */
.empty-state { text-align: center; padding: 56px 20px; background: white !important; border-radius: 18px; border: 2px dashed #e5ebe7; }
.empty-state-icon { font-size: 52px; margin-bottom: 14px; opacity: 0.4; }
.empty-state-text { color: #94a3b8 !important; font-size: 14px !important; font-weight: 600 !important; }

/* ===== EXPANDER ===== */
div[data-testid="stExpander"] { background: white !important; border: 1px solid #e5ebe7 !important; border-radius: 14px !important; margin-bottom: 12px !important; overflow: hidden !important; box-shadow: 0 2px 10px rgba(0,0,0,0.02) !important; }
div[data-testid="stExpander"] summary { background: white !important; padding: 14px 18px !important; cursor: pointer !important; }
div[data-testid="stExpander"] summary:hover { background: #f0fdf4 !important; }
div[data-testid="stExpander"] summary p { color: #083d26 !important; font-weight: 800 !important; font-size: 14px !important; margin: 0 !important; }

/* ===== ALERTS ===== */
div[data-testid="stAlert"] { border-radius: 12px !important; padding: 12px 16px !important; }
div[data-testid="stAlert"] p, div[data-testid="stAlert"] span, div[data-testid="stAlert"] div { color: #0f172a !important; font-weight: 600 !important; }

/* ===== POPOVER & FILE UPLOADER ===== */
div[data-testid="stPopover"] > button, div[data-testid="stPopover"] button { background: white !important; border: 1px solid #e5ebe7 !important; color: #083d26 !important; font-weight: 700 !important; }
div[data-testid="stPopover"] button p, div[data-testid="stPopover"] button span { color: #083d26 !important; font-weight: 700 !important; }
div[data-testid="stFileUploader"] { background: #f8fafc !important; border: 2px dashed #cbd5e1 !important; border-radius: 12px !important; padding: 12px !important; }
div[data-testid="stFileUploader"] * { color: #0f172a !important; }
div[data-testid="stFileUploader"] button { background: white !important; border: 1px solid #0d5e3a !important; color: #0d5e3a !important; font-weight: 700 !important; }

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .login-brand { padding: 40px 30px; min-height: auto; }
    .login-brand h1 { font-size: 26px !important; }
    .stat-box .value { font-size: 26px !important; }
    .block-container { padding: 1rem !important; }
}
</style>
"""

# =========================================================
# LOGIN PAGE
# =========================================================
def admin_login():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
        <div class="login-brand">
            <div>
                <div class="login-brand-logo">
                    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya">
                </div>
                <h1>DPRK ACEH JAYA</h1>
                <div class="login-brand-sub">Dewan Perwakilan Rakyat Kabupaten</div>
                <div class="login-brand-desc">
                    Panel admin untuk mengelola konten website DPRK Aceh Jaya — berita, agenda, galeri, pengaduan, dan lainnya.
                </div>
            </div>
            <div class="login-brand-footer">
                🔒 Sistem Autentikasi Aman & Terenkripsi
            </div>
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

        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <span style="color: #64748b; font-weight: 700; font-size: 13px;">
                ← Kembali ke Website Utama (Gunakan URL tanpa ?admin=true)
            </span>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# HELPER
# =========================================================
def show_empty_state(icon, text):
    st.markdown(f"""
    <div class="empty-state">
        <div class="empty-state-icon">{icon}</div>
        <div class="empty-state-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def panel_header(icon, title, subtitle=""):
    st.markdown(f"""
    <div style="margin-bottom: 6px;">
        <span class="form-badge">✨ Form Input</span>
    </div>
    <div class="panel-title">{icon} {title}</div>
    <div class="panel-sub">{subtitle}</div>
    """, unsafe_allow_html=True)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
MENU_ITEMS = [
    ("dashboard", "🏠", "Dashboard"),
    ("berita", "📰", "Berita"),
    ("agenda", "📅", "Agenda"),
    ("galeri", "🖼️", "Galeri"),
    ("anggota", "👥", "Anggota DPRK"),
    ("fraksi", "🏛️", "Fraksi"),
    ("komisi", "📋", "Komisi"),
    ("faq", "❓", "FAQ"),
    ("running_text", "📢", "Running Text"),
    ("kesekretariatan", "📋", "Kesekretariatan"),
    ("pengaduan", "📥", "Pengaduan"),
    ("pimpinan", "👥", "Pimpinan"),
    ("pejabat", "🏢", "Pejabat"),
    ("jdih", "📜", "JDIH"),
    ("admin_users", "👤", "Manajemen Admin"),
    ("pengaturan", "⚙️", "Pengaturan"),
]

def render_sidebar():
    user = st.session_state.admin_user

    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-brand">
            <div class="sidebar-brand-logo">
                <img src="{LOGO_URL}" alt="Logo">
            </div>
            <div class="sidebar-brand-text">
                <div class="sidebar-brand-title">DPRK ACEH JAYA</div>
                <div class="sidebar-brand-sub">Admin Panel</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="sidebar-user">
            <div class="sidebar-user-name">👤 {user['username']}</div>
            <div class="sidebar-user-role">Administrator</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sidebar-label">Menu Utama</div>', unsafe_allow_html=True)

        if "admin_page" not in st.session_state:
            st.session_state.admin_page = "dashboard"

        for key, icon, label in MENU_ITEMS:
            is_active = st.session_state.admin_page == key
            btn_type = "primary" if is_active else "secondary"
            if st.button(
                f"{icon}  {label}",
                key=f"nav_{key}",
                use_container_width=True,
                type=btn_type,
            ):
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

# =========================================================
# DASHBOARD
# =========================================================
def admin_dashboard():
    user = st.session_state.admin_user

    st.markdown(f"""
    <div class="admin-header">
        <h1>🏛️ Admin Panel DPRK</h1>
        <p>Selamat datang, <b>{user['username']}</b> · Kelola konten website DPRK Aceh Jaya</p>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Memuat ringkasan data..."):
        berita_count = len(get_all_berita())
        pengaduan_list = get_all_pengaduan()
        pengaduan_baru = len([p for p in pengaduan_list if p.get("status") == "Baru"])
        galeri_count = len(get_all_galeri())
        agenda_count = len(get_all_agenda())
        anggota_count = len(get_all_anggota())

    s1, s2, s3, s4, s5 = st.columns(5)
    stats = [
        (s1, "Berita", berita_count, "📰", "Total artikel dipublikasikan", "#0d5e3a"),
        (s2, "Pengaduan", len(pengaduan_list), "📥", f"{pengaduan_baru} baru masuk", "#dc2626"),
        (s3, "Galeri", galeri_count, "🖼️", "Foto dokumentasi", "#c9a227"),
        (s4, "Agenda", agenda_count, "📅", "Jadwal rapat", "#14734a"),
        (s5, "Anggota", anggota_count, "👥", "Total anggota DPRK", "#1e40af"),
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

    st.markdown("""
    <div class="panel-card">
        <div class="panel-title">🎯 Panduan Cepat</div>
        <div class="panel-sub">Gunakan menu di sidebar untuk mengelola konten.</div>
        <div class="panel-divider"></div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;">
            <div style="padding:14px;background:#f0fdf4;border-radius:12px;border-left:3px solid #0d5e3a;">
                <div style="font-weight:800;color:#083d26;font-size:13px;">📰 Kelola Berita</div>
                <div style="color:#64748b;font-size:12px;margin-top:4px;">Tambah, edit, hapus artikel berita</div>
            </div>
            <div style="padding:14px;background:#fef9c3;border-radius:12px;border-left:3px solid #c9a227;">
                <div style="font-weight:800;color:#854d0e;font-size:13px;">📥 Cek Pengaduan</div>
                <div style="color:#64748b;font-size:12px;margin-top:4px;">Tanggapi laporan masyarakat</div>
            </div>
            <div style="padding:14px;background:#dbeafe;border-radius:12px;border-left:3px solid #1e40af;">
                <div style="font-weight:800;color:#1e40af;font-size:13px;">🖼️ Upload Galeri</div>
                <div style="color:#64748b;font-size:12px;margin-top:4px;">Dokumentasi kegiatan DPRK</div>
            </div>
            <div style="padding:14px;background:#f3e8ff;border-radius:12px;border-left:3px solid #7c3aed;">
                <div style="font-weight:800;color:#6b21a8;font-size:13px;">👥 Kelola Anggota</div>
                <div style="color:#64748b;font-size:12px;margin-top:4px;">Data pimpinan & anggota dewan</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PAGE: BERITA
# =========================================================
def page_berita():
    st.markdown('<div class="section-title">📰 Kelola Berita</div>', unsafe_allow_html=True)

    col_list, col_form = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        panel_header("➕", "Tambah Berita", "Isi form di bawah untuk menambah berita baru.")

        with st.form("form_tambah_berita", clear_on_submit=True):
            title = st.text_input("Judul Berita *", placeholder="Judul berita...")
            date = st.text_input("Tanggal", value=datetime.now().strftime("%A, %d %B %Y"))
            kategori = st.selectbox("Kategori", ["Paripurna", "Lingkungan", "Hukum", "Legislasi", "Kunjungan", "Reses", "Rapat", "Sosial", "Ekonomi", "Lainnya"])
            desc_text = st.text_area("Deskripsi Berita *", height=120, placeholder="Isi berita...")

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

        st.markdown('</div>', unsafe_allow_html=True)

    with col_list:
        c_search, c_refresh = st.columns([4, 1])
        with c_search:
            search = st.text_input("🔎 Cari berita", placeholder="Ketik judul...", key="search_berita")
        with c_refresh:
            st.write("")
            st.write("")
            if st.button("🔄 Refresh", key="refresh_berita", use_container_width=True):
                st.rerun()

        with st.spinner("Memuat berita dari database..."):
            berita_list = get_all_berita()

        st.caption(f"📊 Total berita di database: **{len(berita_list)}**")

        if search:
            berita_list = [b for b in berita_list if search.lower() in b.get("title", "").lower()]

        if not berita_list:
            show_empty_state("📰", "Belum ada berita. Tambahkan berita baru di form sebelah kanan.")
            return

        for item in berita_list:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c_img, c_info = st.columns([1, 6])
            with c_img:
                if item.get("image_url"):
                    try: st.image(item["image_url"], width=70)
                    except: st.write("🖼️")
                else:
                    st.markdown('<div style="width:70px;height:70px;background:#f1f5f9;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:26px;">🖼️</div>', unsafe_allow_html=True)
            with c_info:
                st.markdown(f"""
                <div class="crud-content" style="padding: 4px 0;">
                    <div class="crud-title">{item['title']}</div>
                    <div class="crud-meta">
                        <span>📅 {item.get('date', '-')}</span>
                        <span class="crud-badge">{item.get('kategori', '-')}</span>
                        <span>👁️ {item.get('views', 0)} views</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            ca, cb, _ = st.columns([1, 1, 4])
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
                    delete_berita(item["id"])
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PAGE: AGENDA
# =========================================================
def page_agenda():
    st.markdown('<div class="section-title">📅 Kelola Agenda</div>', unsafe_allow_html=True)

    col_list, col_form = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        panel_header("➕", "Tambah Agenda", "Isi detail agenda kegiatan DPRK.")
        with st.form("form_agenda", clear_on_submit=True):
            hari = st.text_input("Hari (contoh: 09)", max_chars=2)
            bulan_tahun = st.text_input("Bulan Tahun (contoh: SEP 2026)")
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
        st.markdown('</div>', unsafe_allow_html=True)

    with col_list:
        with st.spinner("Memuat agenda..."):
            agenda_list = get_all_agenda()
        if not agenda_list:
            show_empty_state("📅", "Belum ada agenda.")
            return
        for item in agenda_list:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1:
                st.markdown(f"""
                <div class="crud-content" style="padding: 4px 0;">
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
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PAGE: GALERI
# =========================================================
def page_galeri():
    st.markdown('<div class="section-title">🖼️ Kelola Galeri</div>', unsafe_allow_html=True)

    col_list, col_form = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        panel_header("📤", "Upload Foto", "Tambah foto ke galeri dokumentasi.")
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
        st.markdown('</div>', unsafe_allow_html=True)

    with col_list:
        with st.spinner("Memuat galeri..."):
            galeri_list = get_all_galeri()
        if not galeri_list:
            show_empty_state("🖼️", "Belum ada foto galeri.")
            return
        cols = st.columns(2)
        for i, item in enumerate(galeri_list):
            with cols[i % 2]:
                st.markdown('<div class="crud-item">', unsafe_allow_html=True)
                try:
                    st.image(item["image_url"], caption=item["title"], use_container_width=True)
                except Exception:
                    st.write("🖼️")
                if st.button("🗑️ Hapus", key=f"del_g_{item['id']}", use_container_width=True):
                    delete_galeri(item["id"])
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PAGE: ANGGOTA DPRK
# =========================================================
def page_anggota():
    st.markdown('<div class="section-title">👥 Kelola Anggota DPRK</div>', unsafe_allow_html=True)

    col_list, col_form = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        panel_header("➕", "Tambah Anggota", "Data anggota DPRK Aceh Jaya.")
        with st.form("form_anggota", clear_on_submit=True):
            nama = st.text_input("Nama Lengkap *", placeholder="Nama anggota")
            jabatan = st.text_input("Jabatan", value="Anggota")
            komisi = st.selectbox("Komisi", ["Komisi I", "Komisi II", "Komisi III", "Komisi IV", "-"])
            dapil = st.selectbox("Dapil", ["Dapil 1 (Calang)", "Dapil 2 (Teunom)", "Dapil 3 (Jaya)", "Dapil 4 (Krueng Sabee)", "Dapil 5 (Sampoiniet)", "-"])
            fraksi = st.text_input("Fraksi", placeholder="Contoh: Golkar")
            urutan = st.number_input("Urutan", min_value=1, value=1)
            foto = st.file_uploader("Foto (opsional)", type=["jpg", "png", "jpeg"])

            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if not nama:
                    st.error("⚠️ Nama wajib diisi")
                else:
                    foto_url = upload_image(foto, folder="anggota") if foto else None
                    create_anggota(nama, jabatan, komisi, dapil, fraksi, urutan, foto_url)
                    st.success("✅ Anggota ditambahkan!")
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_list:
        search = st.text_input("🔎 Cari anggota", placeholder="Nama...", key="search_anggota")
        with st.spinner("Memuat anggota..."):
            items = get_all_anggota()

        if search:
            items = [a for a in items if search.lower() in a.get("nama", "").lower()]

        if not items:
            show_empty_state("👥", "Belum ada data anggota.")
            return

        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 5, 1.4])
            with c1:
                if item.get("foto_url"):
                    try: st.image(item["foto_url"], width=56)
                    except: st.write("👤")
                else:
                    st.markdown('<div style="width:56px;height:56px;background:#f1f5f9;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:22px;">👤</div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="crud-content" style="padding: 4px 0;">
                    <div class="crud-title">{item.get('nama','-')}</div>
                    <div class="crud-meta">
                        <span class="crud-badge crud-badge-gold">{item.get('jabatan','-')}</span>
                        <span>🏛️ {item.get('komisi','-')}</span>
                        <span>🗳️ {item.get('dapil','-')}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with c3:
                if st.button("🗑️", key=f"del_ang_{item['id']}", use_container_width=True):
                    delete_anggota(item["id"])
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PAGE: JDIH
# =========================================================
def page_jdih():
    st.markdown('<div class="section-title">📜 Kelola Produk Hukum (JDIH)</div>', unsafe_allow_html=True)
    col_list, col_form = st.columns([2, 1], gap="large")
    with col_form:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        panel_header("➕", "Tambah Produk Hukum", "Dokumen hukum & peraturan.")
        with st.form("form_jdih", clear_on_submit=True):
            nomor = st.text_input("Nomor & Tahun *", placeholder="Qanun No. 5/2025")
            tentang = st.text_input("Tentang *")
            status = st.selectbox("Status", ["Berlaku", "Dicabut", "Diubah"])
            if st.form_submit_button("💾 Simpan", type="primary", use_container_width=True):
                if nomor and tentang:
                    create_jdih(nomor, tentang, status)
                    st.success("✅ Ditambahkan!")
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_list:
        with st.spinner("Memuat produk hukum..."):
            items = get_all_jdih()
        if not items:
            show_empty_state("📜", "Belum ada produk hukum.")
            return
        for item in items:
            st.markdown('<div class="crud-item">', unsafe_allow_html=True)
            c1, c2 = st.columns([6, 1])
            with c1:
                st.markdown(f'<div class="crud-title">{item["nomor"]} — {item["tentang"]}</div><div class="crud-meta"><span class="crud-badge">{item.get("status")}</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("🗑️", key=f"del_jdih_{item['id']}", use_container_width=True):
                    delete_jdih(item["id"])
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PAGE: PENGADUAN
# =========================================================
def page_pengaduan():
    st.markdown('<div class="section-title">📥 Pengaduan Masyarakat</div>', unsafe_allow_html=True)
    with st.spinner("Memuat pengaduan..."):
        pengaduan_list = get_all_pengaduan()
    if not pengaduan_list:
        show_empty_state("📥", "Belum ada pengaduan masuk.")
        return
    for p in pengaduan_list:
        with st.expander(f"🎫 {p['tiket']} — {p['nama']}"):
            st.write(f"**Kategori:** {p['kategori']} | **Status:** {p['status']}")
            st.info(p["isi"])
            if st.button("🗑️ Hapus Pengaduan", key=f"del_p_{p['id']}"):
                delete_pengaduan(p["id"])
                st.rerun()

# =========================================================
# PAGE: PIMPINAN & PEJABAT & LAINNYA (Disederhanakan agar tidak error)
# =========================================================
def page_pimpinan():
    st.info("Modul Pimpinan siap dikembangkan.")

def page_pejabat():
    st.info("Modul Pejabat siap dikembangkan.")

def page_fraksi():
    st.info("Modul Fraksi siap dikembangkan.")

def page_komisi():
    st.info("Modul Komisi siap dikembangkan.")

def page_faq():
    st.info("Modul FAQ siap dikembangkan.")

def page_running_text():
    st.info("Modul Running Text siap dikembangkan.")

def page_kesekretariatan():
    st.info("Modul Kesekretariatan siap dikembangkan.")

def page_admin_users():
    st.info("Modul Admin Users siap dikembangkan.")

def page_pengaturan():
    st.info("Modul Pengaturan siap dikembangkan.")

# =========================================================
# ROUTER
# =========================================================
PAGE_ROUTES = {
    "dashboard": admin_dashboard,
    "berita": page_berita,
    "agenda": page_agenda,
    "galeri": page_galeri,
    "anggota": page_anggota,
    "fraksi": page_fraksi,
    "komisi": page_komisi,
    "faq": page_faq,
    "running_text": page_running_text,
    "kesekretariatan": page_kesekretariatan,
    "pengaduan": page_pengaduan,
    "pimpinan": page_pimpinan,
    "pejabat": page_pejabat,
    "jdih": page_jdih,
    "admin_users": page_admin_users,
    "pengaturan": page_pengaturan,
}

def render_admin_dashboard():
    st.markdown(ADMIN_CSS, unsafe_allow_html=True)
    render_sidebar()
    current = st.session_state.get("admin_page", "dashboard")
    route = PAGE_ROUTES.get(current, admin_dashboard)
    route()

# =========================================================
# MAIN
# =========================================================
def render_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
    if "admin_page" not in st.session_state:
        st.session_state.admin_page = "dashboard"

    if not st.session_state.admin_logged_in:
        admin_login()
    else:
        render_admin_dashboard()
