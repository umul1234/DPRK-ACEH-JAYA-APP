import streamlit as st
from datetime import datetime

# Konfigurasi Halaman
st.set_page_config(
    page_title="DPRK Aceh Jaya - Portal Resmi",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed" # Kita gunakan navigasi atas untuk kesan website publik
)

# ==========================================
# 1. CSS STYLING (Modern, Clean, Consistent)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #0F2C4A;
        --navy-light: #1A4B7C;
        --green: #15803D;
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
        border-bottom: 1px solid var(--border);
        padding: 16px 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .nav-logo { font-size: 20px; font-weight: 800; color: var(--navy); display: flex; align-items: center; gap: 10px; }
    .nav-logo span { color: var(--green); }
    
    /* Nav Buttons */
    .nav-btn {
        background: transparent !important;
        color: var(--text-muted) !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 8px 16px !important;
        border-radius: 6px !important;
        transition: all 0.2s !important;
    }
    .nav-btn:hover { background: var(--green-light) !important; color: var(--green) !important; }
    .nav-btn.active { background: var(--navy) !important; color: white !important; }

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
        transition: transform 0.2s;
    }
    .hero-btn:hover { transform: translateY(-2px); background: #166534; }

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
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(15, 44, 74, 0.08);
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
        border: 1px solid var(--border);
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .news-card:hover { box-shadow: 0 8px 16px rgba(0,0,0,0.06); }
    .news-img { height: 180px; background: #CBD5E1; display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 14px; }
    .news-content { padding: 20px; }
    .news-tag {
        display: inline-block;
        background: var(--navy);
        color: white;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    .news-title { font-size: 17px; font-weight: 700; color: var(--navy); margin: 0 0 8px 0; line-height: 1.4; }
    .news-date { font-size: 12px; color: var(--text-muted); display: flex; align-items: center; gap: 6px; }

    /* Footer */
    .footer {
        background: var(--navy);
        color: white;
        padding: 48px 40px;
        margin-top: 60px;
        border-radius: 20px 20px 0 0;
    }
    .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto; }
    .footer h4 { font-size: 16px; font-weight: 700; margin: 0 0 16px 0; color: #FDE68A; }
    .footer p, .footer a { font-size: 14px; color: rgba(255,255,255,0.8); line-height: 1.8; text-decoration: none; display: block; }
    .footer a:hover { color: white; }
    .footer-bottom {
        max-width: 1200px;
        margin: 40px auto 0;
        padding-top: 24px;
        border-top: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        font-size: 13px;
        color: rgba(255,255,255,0.5);
    }

    /* Form Styling */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > select {
        border-radius: 8px !important;
        border: 1px solid var(--border) !important;
        background: var(--surface) !important;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: var(--green) !important;
        box-shadow: 0 0 0 3px var(--green-light) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. STATE & NAVIGATION
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

# Top Alert Banner (Konteks Bantuan Banjir)
st.markdown("""
<div class="alert-banner">
    <span>🚨</span>
    <span>Layanan Khusus Tanggap Banjir Aktif: Prioritas pengaduan dampak bencana dipercepat 1x24 jam.</span>
</div>
""", unsafe_allow_html=True)

# Navbar
nav_cols = st.columns([1, 3, 1])
with nav_cols[0]:
    st.markdown('<div class="nav-logo">🏛️ DPRK <span>ACEH JAYA</span></div>', unsafe_allow_html=True)

with nav_cols[1]:
    nav_container = st.container()
    with nav_container:
        cols = st.columns(len(pages))
        for i, (key, label) in enumerate(pages.items()):
            is_active = (st.session_state.page == label)
            btn_class = "active" if is_active else ""
            if cols[i].button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
                st.session_state.page = label
                st.rerun()

with nav_cols[2]:
    st.markdown('<div style="text-align: right; font-size: 13px; color: var(--text-muted); padding-top: 10px;">🇮🇩 ID | EN</div>', unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ==========================================
# 3. PAGE CONTENT
# ==========================================

if st.session_state.page == "Beranda":
    # Hero Section
    st.markdown("""
    <div class="hero">
        <div style="position: relative; z-index: 2;">
            <div style="background: rgba(255,255,255,0.15); display: inline-block; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 16px; backdrop-filter: blur(4px);">
                PORTAL RESMI LEGISLATIF
            </div>
            <h1>Melayani, Mengawasi,<br>& Mengayomi Masyarakat Aceh Jaya</h1>
            <p>Akses informasi kinerja dewan, produk hukum daerah (JDIH), agenda rapat, dan layanan aspirasi publik dalam satu platform terintegrasi.</p>
            <a href="#" class="hero-btn" onclick="document.querySelector('[key=\'nav_Layanan\']').click()">Sampaikan Aspirasi Anda</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick Services
    st.markdown('<div class="section-title">Layanan Publik Cepat</div>', unsafe_allow_html=True)
    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi atau laporan, termasuk tanggap banjir.", "Layanan"),
        ("📜", "JDIH & Qanun", "Akses dokumen hukum daerah dan APBK secara transparan.", "JDIH"),
        ("📅", "Agenda Rapat", "Jadwal sidang paripurna, RDPU, dan kegiatan komisi.", "Berita"),
        ("📄", "Permohonan Informasi", "Layanan PPID untuk keterbukaan informasi publik.", "Layanan")
    ]
    
    svc_cols = st.columns(4)
    for i, (icon, title, desc, target) in enumerate(services):
        with svc_cols[i]:
            st.markdown(f"""
            <div class="service-card" onclick="document.querySelector('[key=\'nav_{target}\']').click()">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # Latest News
    st.markdown('<div class="section-title" style="margin-top: 20px;">Berita & Kegiatan Terkini</div>', unsafe_allow_html=True)
    news_data = [
        ("PARIPURNA", "15 Sep 2026", "Pembahasan KUA-PPAS 2027", "Rapat paripurna membahas kebijakan umum anggaran dan prioritas plafon anggaran sementara."),
        ("RESES", "10 Sep 2026", "Penjaringan Aspirasi Daerah Terpencil", "Anggota DPRK turun langsung menampung keluhan masyarakat terkait infrastruktur pascabanjir."),
        ("LEGISLASI", "02 Sep 2026", "RDPU Penyempurnaan Qanun Ketertiban", "Mendengarkan masukan akademisi dan tokoh masyarakat atas draf qanun terbaru.")
    ]
    
    news_cols = st.columns(3)
    for i, (tag, date, title, desc) in enumerate(news_data):
        with news_cols[i]:
            st.markdown(f"""
            <div class="news-card">
                <div class="news-img">📷 Thumbnail Berita</div>
                <div class="news-content">
                    <span class="news-tag">{tag}</span>
                    <h3 class="news-title">{title}</h3>
                    <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;">{desc}</p>
                    <div class="news-date">🕒 {date}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "Profil & Pimpinan":
    st.markdown('<div class="section-title">Profil & Pimpinan DPRK</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: var(--text-muted); margin-bottom: 32px;">Masa Jabatan 2024 - 2029 | Kabupaten Aceh Jaya</p>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    pimpinan = [
        ("Ketua DPRK", "H. Muhammad Yusuf, S.H.", "Memimpin sidang paripurna dan koordinasi antar alat kelengkapan dewan."),
        ("Wakil Ketua I", "Drs. H. Ahmad Fauzi, M.M.", "Bidang Legislasi dan Anggaran."),
        ("Wakil Ketua II", "Siti Rahmah, S.IP.", "Bidang Pengawasan dan Hubungan Masyarakat.")
    ]
    
    for i, (jabatan, nama, desc) in enumerate(pimpinan):
        with cols[i]:
            st.markdown(f"""
            <div class="service-card" style="text-align: center; padding: 32px 24px;">
                <div style="width: 80px; height: 80px; background: var(--navy); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 700; margin: 0 auto 16px;">
                    {nama.split()[0][0]}
                </div>
                <div style="font-size: 12px; color: var(--green); font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">{jabatan}</div>
                <h3 style="font-size: 18px; font-weight: 700; color: var(--navy); margin: 0 0 12px 0;">{nama}</h3>
                <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "Layanan & Pengaduan":
    st.markdown('<div class="section-title">Layanan Aspirasi & Pengaduan</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("##### Formulir Pengaduan Masyarakat")
        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Sesuai KTP")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit untuk verifikasi")
            with c2:
                kategori = st.selectbox("Kategori Pengaduan *", [
                    "🚨 Bantuan Dampak Banjir (Prioritas)", 
                    "Infrastruktur & Jalan", 
                    "Pelayanan Publik", 
                    "Legislasi & Qanun", 
                    "Lainnya"
                ])
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan detail lokasi, kronologi, atau aspirasi Anda secara jelas...")
            
            submitted = st.form_submit_button("Kirim Laporan", type="primary", use_container_width=True)
            if submitted:
                if nama and isi:
                    st.success("✅ Laporan berhasil dikirim! Nomor tiket: #ADU-2026-0917. Petugas kami akan menindaklanjuti dalam 1x24 jam (Prioritas Banjir).")
                else:
                    st.error("Mohon lengkapi Nama dan Isi Laporan.")

    with col2:
        st.markdown("""
        <div class="service-card" style="background: var(--green-light); border-color: var(--green); text-align: left;">
            <h4 style="color: var(--green); margin-top: 0; font-size: 16px;">📞 Kontak Cepat</h4>
            <p style="font-size: 13px; color: var(--text); margin-bottom: 12px;"><strong>WhatsApp Pengaduan:</strong><br>+62 812-3456-7890</p>
            <p style="font-size: 13px; color: var(--text); margin-bottom: 12px;"><strong>Email:</strong><br>pengaduan@dprk.acehjaya.go.id</p>
            <p style="font-size: 13px; color: var(--text);"><strong>Jam Operasional:</strong><br>Senin - Jumat, 08.00 - 16.00 WIB</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "JDIH & Transparansi":
    st.markdown('<div class="section-title">Jaringan Dokumentasi & Informasi Hukum (JDIH)</div>', unsafe_allow_html=True)
    
    # Mock Data Table
    data = {
        "No": ["1", "2", "3"],
        "Nomor & Tahun": ["Qanun No. 5/2025", "Perbup No. 12/2026", "Qanun No. 2/2024"],
        "Tentang": ["Ketertiban Umum dan Ketenteraman Masyarakat", "Penjabaran APBK Aceh Jaya 2026", "Perlindungan Korban Bencana Alam"],
        "Status": ["Berlaku", "Berlaku", "Berlaku"],
        "Unduh": ["📄 PDF", "📄 PDF", "📄 PDF"]
    }
    st.dataframe(data, use_container_width=True, hide_index=True)

else:
    st.markdown(f'<div class="section-title">{st.session_state.page}</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="service-card" style="text-align: center; padding: 60px 20px;">
        <div style="font-size: 48px; margin-bottom: 16px;">🚧</div>
        <h3 style="color: var(--navy); margin-bottom: 8px;">Halaman Dalam Pengembangan</h3>
        <p style="color: var(--text-muted); max-width: 500px; margin: 0 auto;">
            Konten untuk halaman ini sedang dalam proses sinkronisasi data dengan sistem internal Sekretariat DPRK Aceh Jaya.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. FOOTER
# ==========================================
st.markdown('</div>', unsafe_allow_html=True) # Close main-content

st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div>
            <h4>DPRK ACEH JAYA</h4>
            <p>Secretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya.<br>
            Mewujudkan pemerintahan yang transparan, akuntabel, dan melayani.</p>
        </div>
        <div>
            <h4>Tautan Terkait</h4>
            <a href="#">Pemerintah Kab. Aceh Jaya</a>
            <a href="#">JDIH Nasional</a>
            <a href="#">LAPOR! (Pengaduan Nasional)</a>
            <a href="#">Badan Pusat Statistik</a>
        </div>
        <div>
            <h4>Hubungi Kami</h4>
            <p>📍 Jl. Merdeka No. 01, Calang, Aceh Jaya</p>
            <p>📞 (0655) 12345</p>
            <p>✉️ sekretariat@dprk.acehjaya.go.id</p>
        </div>
    </div>
    <div class="footer-bottom">
        © 2026 Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Hak Cipta Dilindungi.
    </div>
</div>
""", unsafe_allow_html=True)
