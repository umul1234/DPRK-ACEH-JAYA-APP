import streamlit as st
from datetime import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="DPRK Aceh Jaya - Portal Resmi",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS STYLING LENGKAP
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #0F2C4A;
        --navy-light: #1A4B7C;
        --green: #15803D;
        --green-dark: #166534;
        --green-light: #DCFCE7;
        --gold: #D97706;
        --bg: #F8FAFC;
        --surface: #FFFFFF;
        --text: #0F172A;
        --text-muted: #64748B;
        --border: #E2E8F0;
    }

    * { font-family: 'Plus Jakarta Sans', sans-serif; box-sizing: border-box; }
    
    /* Hide default Streamlit clutter */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stApp > header { display: none; }
    
    .stApp { background: var(--bg) !important; color: var(--text) !important; }

    /* Top Alert Banner */
    .alert-banner {
        background: linear-gradient(90deg, #FEF3C7 0%, #FDE68A 100%);
        border-bottom: 1px solid #F59E0B;
        color: #92400E;
        padding: 10px 24px;
        font-size: 13px;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    /* Navigation Bar */
    .navbar {
        background: var(--surface);
        border-bottom: 3px solid var(--green);
        padding: 16px 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .nav-logo { 
        font-size: 22px; 
        font-weight: 800; 
        color: var(--navy); 
        display: flex; 
        align-items: center; 
        gap: 10px;
        text-decoration: none;
    }
    .nav-logo span { color: var(--green); }
    
    /* NAV BUTTONS - TERLIHAT JELAS (HIJAU GRADASI) */
    .stButton > button {
        background: linear-gradient(135deg, var(--green) 0%, var(--green-dark) 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 6px rgba(21, 128, 61, 0.3) !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--green-dark) 0%, var(--navy) 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(21, 128, 61, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Main Container */
    .main-content { max-width: 1200px; margin: 0 auto; padding: 32px 24px; }

    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%);
        border-radius: 20px;
        padding: 60px 48px;
        color: white;
        position: relative;
        overflow: hidden;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(15, 44, 74, 0.2);
    }
    .hero::after {
        content: '';
        position: absolute;
        right: -50px;
        top: -50px;
        width: 300px;
        height: 300px;
        background: rgba(255,255,255,0.05);
        border-radius: 50%;
    }
    .hero h1 { font-size: 36px; font-weight: 800; margin: 0 0 16px 0; line-height: 1.2; }
    .hero p { font-size: 16px; opacity: 0.9; max-width: 600px; line-height: 1.6; margin: 0; }
    .hero-btn {
        display: inline-block;
        background: var(--green);
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 700;
        margin-top: 24px;
        text-decoration: none;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .hero-btn:hover { 
        transform: translateY(-2px); 
        background: var(--green-dark);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }

    /* Section Titles */
    .section-title {
        font-size: 22px;
        font-weight: 800;
        color: var(--navy);
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .section-title::before {
        content: '';
        width: 4px;
        height: 24px;
        background: var(--green);
        border-radius: 2px;
    }

    /* Service Cards */
    .service-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 48px; }
    .service-card {
        background: var(--surface);
        border: 2px solid var(--border);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(15, 44, 74, 0.1);
        border-color: var(--green);
    }
    .service-icon {
        width: 56px;
        height: 56px;
        background: var(--green-light);
        color: var(--green);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        margin: 0 auto 16px;
    }
    .service-title { font-weight: 700; color: var(--navy); margin-bottom: 8px; font-size: 15px; }
    .service-desc { font-size: 13px; color: var(--text-muted); line-height: 1.5; }

    /* News Cards */
    .news-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
    .news-card {
        background: var(--surface);
        border: 2px solid var(--border);
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .news-card:hover { 
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-color: var(--green);
    }
    .news-img { 
        height: 180px; 
        background: linear-gradient(135deg, var(--navy-light), var(--green));
        display: flex; 
        align-items: center; 
        justify-content: center; 
        color: white; 
        font-size: 48px;
    }
    .news-content { padding: 20px; }
    .news-tag {
        display: inline-block;
        background: var(--navy);
        color: white;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    .news-title { font-size: 17px; font-weight: 700; color: var(--navy); margin: 0 0 8px 0; line-height: 1.4; }
    .news-date { font-size: 12px; color: var(--text-muted); display: flex; align-items: center; gap: 6px; }

    /* Profile Card */
    .profile-card {
        background: var(--surface);
        border: 2px solid var(--border);
        border-radius: 16px;
        padding: 32px 24px;
        text-align: center;
        transition: all 0.3s;
    }
    .profile-card:hover {
        border-color: var(--green);
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
    }
    .profile-avatar {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, var(--navy), var(--green));
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        font-weight: 700;
        margin: 0 auto 16px;
    }

    /* Footer */
    .footer {
        background: var(--navy);
        color: white;
        padding: 48px 40px;
        margin-top: 60px;
        border-radius: 20px 20px 0 0;
        border-top: 4px solid var(--green);
    }
    .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto; }
    .footer h4 { font-size: 16px; font-weight: 700; margin: 0 0 16px 0; color: var(--gold); }
    .footer p, .footer a { font-size: 14px; color: rgba(255,255,255,0.85); line-height: 1.8; text-decoration: none; display: block; }
    .footer a:hover { color: white; text-decoration: underline; }
    .footer-bottom {
        max-width: 1200px;
        margin: 40px auto 0;
        padding-top: 24px;
        border-top: 1px solid rgba(255,255,255,0.15);
        text-align: center;
        font-size: 13px;
        color: rgba(255,255,255,0.6);
    }

    /* Form Styling */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea, 
    .stSelectbox > div > div > select {
        border-radius: 8px !important;
        border: 2px solid var(--border) !important;
        background: var(--surface) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .stTextInput > div > div > input:focus, 
    .stTextArea > div > div > textarea:focus {
        border-color: var(--green) !important;
        box-shadow: 0 0 0 3px var(--green-light) !important;
    }
    
    /* Success Message */
    .success-box {
        background: var(--green-light);
        border-left: 4px solid var(--green);
        padding: 16px;
        border-radius: 8px;
        margin-top: 16px;
        color: var(--green-dark);
        font-weight: 600;
    }
    
    /* Error Message */
    .error-box {
        background: #FEE2E2;
        border-left: 4px solid #DC2626;
        padding: 16px;
        border-radius: 8px;
        margin-top: 16px;
        color: #991B1B;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# STATE MANAGEMENT
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

pages = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Berita": "Berita & Agenda",
    "Layanan": "Layanan & Pengaduan",
    "JDIH": "JDIH & Transparansi",
    "Kontak": "Hubungi Kami"
}

# ==========================================
# TOP ALERT BANNER
# ==========================================
st.markdown("""
<div class="alert-banner">
    <span>🚨</span>
    <span>Layanan Khusus Tanggap Banjir Aktif: Prioritas pengaduan dampak bencana dipercepat 1x24 jam.</span>
</div>
""", unsafe_allow_html=True)

# ==========================================
# NAVIGATION BAR
# ==========================================
nav_cols = st.columns([1, 4, 1])

with nav_cols[0]:
    st.markdown('<a href="#" class="nav-logo" style="text-decoration: none;">🏛️ DPRK <span>ACEH JAYA</span></a>', unsafe_allow_html=True)

with nav_cols[1]:
    nav_container = st.container()
    with nav_container:
        cols = st.columns(len(pages))
        for i, (key, label) in enumerate(pages.items()):
            with cols[i]:
                if st.button(label, key=f"nav_{key}", use_container_width=True):
                    st.session_state.page = label
                    st.rerun()

with nav_cols[2]:
    st.markdown('<div style="text-align: right; font-size: 13px; color: var(--text-muted); padding-top: 12px; font-weight: 600;">🇮🇩 ID</div>', unsafe_allow_html=True)

# ==========================================
# MAIN CONTENT
# ==========================================
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HALAMAN BERANDA
if st.session_state.page == "Beranda":
    st.markdown("""
    <div class="hero">
        <div style="position: relative; z-index: 2;">
            <div style="background: rgba(255,255,255,0.15); display: inline-block; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px; backdrop-filter: blur(4px); border: 1px solid rgba(255,255,255,0.2);">
                PORTAL RESMI LEGISLATIF
            </div>
            <h1>Melayani, Mengawasi,<br>& Mengayomi Masyarakat Aceh Jaya</h1>
            <p>Akses informasi kinerja dewan, produk hukum daerah (JDIH), agenda rapat, dan layanan aspirasi publik dalam satu platform terintegrasi.</p>
            <a href="#" class="hero-btn" onclick="document.querySelector('[key=\'nav_Layanan\']').click()">Sampaikan Aspirasi Anda →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick Services
    st.markdown('<div class="section-title">Layanan Publik Cepat</div>', unsafe_allow_html=True)
    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi atau laporan, termasuk tanggap banjir.", "Layanan"),
        ("", "JDIH & Qanun", "Akses dokumen hukum daerah dan APBK secara transparan.", "JDIH"),
        ("", "Agenda Rapat", "Jadwal sidang paripurna, RDPU, dan kegiatan komisi.", "Berita"),
        ("📄", "Permohonan Informasi", "Layanan PPID untuk keterbukaan informasi publik.", "Layanan")
    ]
    
    svc_cols = st.columns(4)
    for i, (icon, title, desc, target) in enumerate(services):
        with svc_cols[i]:
            st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Akses {title} →", key=f"btn_{target}", use_container_width=True):
                st.session_state.page = pages[target]
                st.rerun()

    # Latest News
    st.markdown('<div class="section-title" style="margin-top: 48px;">Berita & Kegiatan Terkini</div>', unsafe_allow_html=True)
    news_data = [
        ("PARIPURNA", "15 Sep 2026", "Pembahasan KUA-PPAS 2027", "Rapat paripurna membahas kebijakan umum anggaran dan prioritas plafon anggaran sementara tahun 2027."),
        ("RESES", "10 Sep 2026", "Penjaringan Aspirasi Daerah Terpencil", "Anggota DPRK turun langsung menampung keluhan masyarakat terkait infrastruktur pascabanjir di wilayah pesisir."),
        ("LEGISLASI", "02 Sep 2026", "RDPU Penyempurnaan Qanun Ketertiban", "Mendengarkan masukan akademisi dan tokoh masyarakat atas draf qanun terbaru tentang ketertiban umum.")
    ]
    
    news_cols = st.columns(3)
    for i, (tag, date, title, desc) in enumerate(news_data):
        with news_cols[i]:
            st.markdown(f"""
            <div class="news-card">
                <div class="news-img">📷</div>
                <div class="news-content">
                    <span class="news-tag">{tag}</span>
                    <h3 class="news-title">{title}</h3>
                    <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;">{desc}</p>
                    <div class="news-date">🕒 {date}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# HALAMAN PROFIL
elif st.session_state.page == "Profil & Pimpinan":
    st.markdown('<div class="section-title">Profil & Pimpinan DPRK</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: var(--text-muted); margin-bottom: 32px; font-size: 15px;">Masa Jabatan 2024 - 2029 | Kabupaten Aceh Jaya</p>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    pimpinan = [
        ("Ketua DPRK", "H. Muhammad Yusuf, S.H.", "Memimpin sidang paripurna dan koordinasi antar alat kelengkapan dewan."),
        ("Wakil Ketua I", "Drs. H. Ahmad Fauzi, M.M.", "Bidang Legislasi dan Anggaran."),
        ("Wakil Ketua II", "Siti Rahmah, S.IP.", "Bidang Pengawasan dan Hubungan Masyarakat.")
    ]
    
    for i, (jabatan, nama, desc) in enumerate(pimpinan):
        with cols[i]:
            st.markdown(f"""
            <div class="profile-card">
                <div class="profile-avatar">{nama.split()[0][0]}</div>
                <div style="font-size: 12px; color: var(--green); font-weight: 700; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">{jabatan}</div>
                <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0 0 12px 0;">{nama}</h3>
                <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 48px; padding: 32px; background: var(--green-light); border-radius: 16px; border-left: 4px solid var(--green);">', unsafe_allow_html=True)
    st.markdown("### 🏛️ Visi DPRK Aceh Jaya", unsafe_allow_html=True)
    st.markdown('**"Terwujudnya DPRK Aceh Jaya yang Profesional, Aspiratif, dan Berintegritas dalam Mewujudkan Masyarakat Aceh Jaya yang Sejahtera, Mandiri, dan Berakhlak Mulia."**', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
# SESUDAH (Fixed):
st.markdown('<div style="margin-top: 48px; padding: 32px; background: var(--green-light); border-radius: 16px; border-left: 4px solid var(--green);">', unsafe_allow_html=True)
st.markdown("### 🏛️ Visi DPRK Aceh Jaya", unsafe_allow_html=True)
st.markdown('**"Terwujudnya DPRK Aceh Jaya yang Profesional, Aspiratif, dan Berintegritas dalam Mewujudkan Masyarakat Aceh Jaya yang Sejahtera, Mandiri, dan Berakhlak Mulia."**', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
# HALAMAN BERITA
elif st.session_state.page == "Berita & Agenda":
    st.markdown('<div class="section-title">Berita & Agenda Kegiatan</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: var(--text-muted); margin-bottom: 32px;">Informasi terbaru seputar kegiatan DPRK Aceh Jaya</p>', unsafe_allow_html=True)
    
    news_data = [
        ("PARIPURNA", "15 Sep 2026", "Pembahasan KUA-PPAS 2027", "Rapat paripurna membahas kebijakan umum anggaran dan prioritas plafon anggaran sementara tahun 2027. Pembahasan ini melibatkan seluruh anggota dewan dan pemerintah daerah."),
        ("RESES", "10 Sep 2026", "Penjaringan Aspirasi Daerah Terpencil", "Anggota DPRK turun langsung menampung keluhan masyarakat terkait infrastruktur pascabanjir di wilayah pesisir. Fokus pada perbaikan jalan dan jembatan."),
        ("LEGISLASI", "02 Sep 2026", "RDPU Penyempurnaan Qanun Ketertiban", "Mendengarkan masukan akademisi dan tokoh masyarakat atas draf qanun terbaru tentang ketertiban umum dan ketenteraman masyarakat."),
        ("PENGAWASAN", "28 Agu 2026", "Monitoring Program Bantuan Sosial", "Tim komisi melakukan monitoring distribusi bantuan sosial untuk memastikan tepat sasaran dan transparan."),
        ("KERJASAMA", "25 Agu 2026", "Studi Banding ke DPRK Aceh Besar", "Delegasi DPRK Aceh Jaya melakukan studi banding terkait pengelolaan JDIH dan sistem informasi dewan."),
        ("SOSIALISASI", "20 Agu 2026", "Sosialisasi Qanun APBK 2026", "Sosialisasi kepada masyarakat tentang Anggaran Pendapatan dan Belanja Kabupaten tahun 2026.")
    ]
    
    for i in range(0, len(news_data), 2):
        cols = st.columns(2)
        for j in range(2):
            if i+j < len(news_data):
                tag, date, title, desc = news_data[i+j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="news-card">
                        <div class="news-img">📰</div>
                        <div class="news-content">
                            <span class="news-tag">{tag}</span>
                            <h3 class="news-title">{title}</h3>
                            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 12px;">{desc}</p>
                            <div class="news-date"> {date}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

# HALAMAN LAYANAN
elif st.session_state.page == "Layanan & Pengaduan":
    st.markdown('<div class="section-title">Layanan Aspirasi & Pengaduan</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); border-left: 4px solid #F59E0B; padding: 20px; border-radius: 12px; margin-bottom: 32px;">
        <h4 style="margin: 0 0 8px 0; color: #92400E;">🚨 Layanan Tanggap Darurat Banjir</h4>
        <p style="margin: 0; color: #92400E; font-size: 14px;">Prioritas pengaduan dampak bencana akan diproses dalam 1x24 jam. Silakan pilih kategori "Bantuan Dampak Banjir" pada formulir di bawah.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("##### Formulir Pengaduan Masyarakat")
        with st.form("form_aduan", clear_on_submit=False):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Sesuai KTP")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit untuk verifikasi")
                email = st.text_input("Email/WhatsApp *", placeholder="Untuk konfirmasi")
            with c2:
                kategori = st.selectbox("Kategori Pengaduan *", [
                    " Bantuan Dampak Banjir (Prioritas)", 
                    "🛣️ Infrastruktur & Jalan", 
                    "🏥 Pelayanan Publik", 
                    "📜 Legislasi & Qanun", 
                    "💡 Lainnya"
                ])
                prioritas = st.selectbox("Tingkat Prioritas", ["Normal", "Penting", "Segera"])
            
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan detail lokasi, kronologi, atau aspirasi Anda secara jelas dan lengkap...")
            
            submitted = st.form_submit_button("📤 Kirim Laporan", type="primary", use_container_width=True)
            
            if submitted:
                if nama and email and isi:
                    st.markdown("""
                    <div class="success-box">
                        ✅ <strong>Laporan berhasil dikirim!</strong><br>
                        Nomor tiket: #ADU-2026-0917<br>
                        Petugas kami akan menindaklanjuti dalam 1x24 jam (Prioritas Banjir) atau 3x24 jam (Normal).
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="error-box">
                        ⚠️ Mohon lengkapi field yang wajib diisi (Nama, Email/WhatsApp, dan Isi Laporan).
                    </div>
                    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="profile-card" style="background: var(--green-light); border-color: var(--green); text-align: left;">
            <h4 style="color: var(--green); margin-top: 0; font-size: 16px; display: flex; align-items: center; gap: 8px;">
                <span></span> Kontak Cepat
            </h4>
            <div style="margin-bottom: 16px;">
                <p style="font-size: 13px; color: var(--text); margin-bottom: 4px;"><strong>WhatsApp Pengaduan:</strong></p>
                <p style="font-size: 14px; color: var(--navy); font-weight: 700; margin: 0;">+62 812-3456-7890</p>
            </div>
            <div style="margin-bottom: 16px;">
                <p style="font-size: 13px; color: var(--text); margin-bottom: 4px;"><strong>Email:</strong></p>
                <p style="font-size: 13px; color: var(--navy); margin: 0;">pengaduan@dprk.acehjaya.go.id</p>
            </div>
            <div>
                <p style="font-size: 13px; color: var(--text); margin-bottom: 4px;"><strong>Jam Operasional:</strong></p>
                <p style="font-size: 13px; color: var(--navy); margin: 0;">Senin - Jumat<br>08.00 - 16.00 WIB</p>
            </div>
        </div>
        
        <div class="profile-card" style="margin-top: 16px; background: var(--navy); color: white; text-align: left;">
            <h4 style="color: var(--gold); margin-top: 0; font-size: 16px;">📍 Lokasi Kantor</h4>
            <p style="font-size: 13px; color: rgba(255,255,255,0.9); margin: 0; line-height: 1.6;">
                Jl. Merdeka No. 01<br>
                Calang, Aceh Jaya<br>
                Kode Pos 23654
            </p>
        </div>
        """, unsafe_allow_html=True)

# HALAMAN JDIH
elif st.session_state.page == "JDIH & Transparansi":
    st.markdown('<div class="section-title">Jaringan Dokumentasi & Informasi Hukum (JDIH)</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: var(--text-muted); margin-bottom: 32px;">Dokumen hukum daerah dan informasi anggaran Kabupaten Aceh Jaya</p>', unsafe_allow_html=True)
    
    # Search
    search = st.text_input("🔍 Cari Dokumen", placeholder="Masukkan kata kunci (nomor qanun, tahun, atau judul)")
    
    # Filter
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_type = st.selectbox("Tipe Dokumen", ["Semua", "Qanun", "Perbup", "Perwa", "SK"])
    with col2:
        filter_year = st.selectbox("Tahun", ["Semua", "2026", "2025", "2024", "2023"])
    with col3:
        filter_status = st.selectbox("Status", ["Semua", "Berlaku", "Dicabut", "Dalam Proses"])
    
    # Mock Data
    st.markdown('<div style="margin-top: 24px;">', unsafe_allow_html=True)
    
    documents = [
        {"no": "Qanun No. 5/2025", "judul": "Ketertiban Umum dan Ketenteraman Masyarakat", "tahun": "2025", "status": "Berlaku", "unduh": "📄 PDF (2.4 MB)"},
        {"no": "Perbup No. 12/2026", "judul": "Penjabaran APBK Aceh Jaya 2026", "tahun": "2026", "status": "Berlaku", "unduh": "📄 PDF (5.1 MB)"},
        {"no": "Qanun No. 2/2024", "judul": "Perlindungan Korban Bencana Alam", "tahun": "2024", "status": "Berlaku", "unduh": "📄 PDF (1.8 MB)"},
        {"no": "Perwa No. 08/2026", "judul": "Tata Tertib DPRK Aceh Jaya", "tahun": "2026", "status": "Berlaku", "unduh": "📄 PDF (980 KB)"},
        {"no": "SK No. 15/2026", "judul": "Pembentukan Panitia Khusus PORA XV", "tahun": "2026", "status": "Berlaku", "unduh": "📄 PDF (450 KB)"},
    ]
    
    for doc in documents:
        st.markdown(f"""
        <div style="background: white; border: 2px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; transition: all 0.2s;">
            <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                    <span style="background: var(--navy); color: white; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">{doc['no']}</span>
                    <span style="background: var(--green-light); color: var(--green); padding: 4px 12px; border-radius: 6px; font-size: 11px; font-weight: 600;">{doc['status']}</span>
                    <span style="color: var(--text-muted); font-size: 13px;">📅 {doc['tahun']}</span>
                </div>
                <h4 style="margin: 0; color: var(--navy); font-size: 15px;">{doc['judul']}</h4>
            </div>
            <div style="margin-left: 20px;">
                <button style="background: var(--green); color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; font-size: 13px;">{doc['unduh']}</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# HALAMAN KONTAK
elif st.session_state.page == "Hubungi Kami":
    st.markdown('<div class="section-title">Hubungi Kami</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📩 Kirim Pesan")
        with st.form("form_kontak"):
            nama = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            subjek = st.text_input("Subjek")
            pesan = st.text_area("Pesan", height=150)
            
            if st.form_submit_button("Kirim Pesan", type="primary", use_container_width=True):
                st.success("Pesan berhasil dikirim! Kami akan membalas dalam 1x24 jam.")
    
    with col2:
        st.markdown("""
        <div class="profile-card" style="text-align: left;">
            <h4 style="color: var(--navy); margin-top: 0;">📍 Informasi Kontak</h4>
            
            <div style="margin-bottom: 20px; padding: 16px; background: var(--bg); border-radius: 8px;">
                <p style="margin: 0 0 4px 0; font-weight: 700; color: var(--navy); font-size: 14px;">🏢 Sekretariat DPRK</p>
                <p style="margin: 0; color: var(--text-muted); font-size: 13px; line-height: 1.6;">
                    Jl. Merdeka No. 01<br>
                    Calang, Kabupaten Aceh Jaya<br>
                    Aceh 23654
                </p>
            </div>
            
            <div style="margin-bottom: 20px; padding: 16px; background: var(--bg); border-radius: 8px;">
                <p style="margin: 0 0 4px 0; font-weight: 700; color: var(--navy); font-size: 14px;"> Telepon</p>
                <p style="margin: 0; color: var(--text-muted); font-size: 13px;">(0655) 12345</p>
            </div>
            
            <div style="margin-bottom: 20px; padding: 16px; background: var(--bg); border-radius: 8px;">
                <p style="margin: 0 0 4px 0; font-weight: 700; color: var(--navy); font-size: 14px;">✉️ Email</p>
                <p style="margin: 0; color: var(--text-muted); font-size: 13px;">sekretariat@dprk.acehjaya.go.id</p>
            </div>
            
            <div style="padding: 16px; background: var(--bg); border-radius: 8px;">
                <p style="margin: 0 0 4px 0; font-weight: 700; color: var(--navy); font-size: 14px;">🕐 Jam Operasional</p>
                <p style="margin: 0; color: var(--text-muted); font-size: 13px;">
                    Senin - Jumat: 08.00 - 16.00 WIB<br>
                    Sabtu - Minggu: Tutup
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# HALAMAN LAIN (Placeholder)
else:
    st.markdown(f'<div class="section-title">{st.session_state.page}</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="profile-card" style="text-align: center; padding: 60px 20px;">
        <div style="font-size: 64px; margin-bottom: 16px;">🚧</div>
        <h3 style="color: var(--navy); margin-bottom: 12px; font-size: 24px;">Halaman Dalam Pengembangan</h3>
        <p style="color: var(--text-muted); max-width: 500px; margin: 0 auto; line-height: 1.6; font-size: 14px;">
            Konten untuk halaman ini sedang dalam proses penyusunan dan sinkronisasi data dengan sistem internal Sekretariat DPRK Aceh Jaya. Harap cek kembali dalam waktu dekat.
        </p>
        <button style="margin-top: 24px; background: var(--green); color: white; border: none; padding: 12px 32px; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 14px;">← Kembali ke Beranda</button>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div>
            <h4>🏛️ DPRK ACEH JAYA</h4>
            <p style="line-height: 1.8;">
                Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya.<br>
                Mewujudkan pemerintahan yang transparan, akuntabel, dan melayani masyarakat Aceh Jaya.
            </p>
        </div>
        <div>
            <h4>🔗 Tautan Terkait</h4>
            <a href="#">Pemerintah Kab. Aceh Jaya</a>
            <a href="#">JDIH Nasional</a>
            <a href="#">LAPOR! (Pengaduan Nasional)</a>
            <a href="#">Badan Pusat Statistik</a>
            <a href="#">Kemendagri RI</a>
        </div>
        <div>
            <h4>📞 Hubungi Kami</h4>
            <p>📍 Jl. Merdeka No. 01, Calang, Aceh Jaya 23654</p>
            <p>📞 (0655) 12345</p>
            <p>✉️ sekretariat@dprk.acehjaya.go.id</p>
            <p>🕐 Senin - Jumat: 08.00 - 16.00 WIB</p>
        </div>
    </div>
    <div class="footer-bottom">
        © 2026 Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Hak Cipta Dilindungi.<br>
        Developed with ❤️ for Aceh Jaya
    </div>
</div>
""", unsafe_allow_html=True)
