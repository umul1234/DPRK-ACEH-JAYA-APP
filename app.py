import streamlit as st
from datetime import datetime
import pandas as pd
import re

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Informasi Publik",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATA (DIPISAHKAN UNTUK KEMUDAHAN PEMELIHARAAN)
# =========================================================
PAGES = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Berita": "Berita & Agenda",
    "Layanan": "Layanan & Pengaduan",
    "JDIH": "JDIH & Transparansi",
    "Kontak": "Hubungi Kami",
}

NEWS = [
    {
        "tag": "WARTA DPRK",
        "date": "14 Agustus 2026",
        "title": "Ketua DPRK Aceh Jaya Apresiasi Kejari Berhasil Pulihkan Keuangan Negara Rp2,05 Miliar",
        "desc": "Ketua DPRK Aceh Jaya menghadiri kegiatan Press Release Capaian Pemulihan Keuangan Negara yang diselenggarakan oleh Kejaksaan Negeri Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "tag": "RAPAT PARIPURNA",
        "date": "10 Agustus 2026",
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna untuk membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=900&q=80",
    },
    {
        "tag": "PENDIDIKAN",
        "date": "14 Juli 2026",
        "title": "Ketua DPRK Aceh Jaya Dukung Penuh Pembangunan SLB sebagai Wujud Pemerataan Layanan Pendidikan",
        "desc": "Penandatanganan Naskah Perjanjian Hibah Daerah (NPHD) Hibah Tanah untuk Pembangunan Sekolah Luar Biasa (SLB) di Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=900&q=80",
    },
]

AGENDA = [
    ("18", "SEP", "Rapat Paripurna", "Pembahasan kebijakan dan agenda pembangunan daerah."),
    ("20", "SEP", "Rapat Komisi", "Evaluasi program dan pelaksanaan kegiatan pemerintahan daerah."),
    ("24", "SEP", "Rapat Dengar Pendapat", "Penyerapan aspirasi dan masukan masyarakat."),
]

PIMPINAN = [
    ("Ketua DPRK", "Musliadi Z, S.E", "Memimpin sidang paripurna dan koordinasi alat kelengkapan dewan."),
    ("Wakil Ketua I", "Irwanto. NP", "Koordinasi bidang legislasi dan anggaran."),
    ("Wakil Ketua II", "Teuku Asrizal, S.H", "Koordinasi bidang pengawasan dan hubungan masyarakat."),
]

ANGGOTA_DPRK = {
    "Komisi I": [("Iskandar Ibrahim", "Ketua"), ("H. Dasril Arahman. IB, S.E", "Wakil Ketua"), ("Wanti Cahya", "Sekretaris"), ("Muslim", "Anggota")],
    "Komisi II": [("Ir. Fauzi Yahya", "Ketua"), ("Azhar", "Wakil Ketua"), ("Fitra Akhyar, ST", "Sekretaris"), ("Safriyantoni", "Anggota"), ("Ayudi Ilham, S.E", "Anggota")],
    "Komisi III": [("Sudirman, S.P", "Ketua"), ("Abdul Muthalleb", "Wakil Ketua"), ("Drs. H. T. Irfan TB., M.Si", "Sekretaris"), ("Muhammad Diah, S.E", "Anggota")],
    "Komisi IV": [("Hazami, S.Pd", "Ketua"), ("Muhammad Jamin", "Wakil Ketua"), ("Hj. Fitri Maya Lisa, S.Sos", "Sekretaris"), ("Usman. ID", "Anggota")],
}

SEKRETARIAT = [
    ("Abu Bakar, S.Pd.I., M.H", "Sekretaris DPRK"),
    ("Irma Hanum, SH", "Staf Ahli Bidang Pemerintahan, Hukum dan Politik"),
    ("Hidayat, SE., M.Si", "Kepala Bagian Umum dan Keuangan"),
    ("Yuswardi, S.Kom", "Kepala Bagian Persidangan dan Perundang-Undangan"),
    ("Nelli Fauziana, SH., MH", "Kepala Bagian Fasilitasi Penganggaran dan Pengawasan"),
    ("Ihsan Salim, S.A.P", "Kepala Sub Bagian Tata Usaha dan Kepegawaian"),
]

JDIH_DATA = [
    ["1", "Qanun No. 5 Tahun 2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku"],
    ["2", "Perbup No. 12 Tahun 2026", "Penjabaran APBK Aceh Jaya Tahun 2026", "Berlaku"],
    ["3", "Qanun No. 2 Tahun 2024", "Perlindungan Korban Bencana Alam", "Berlaku"],
]

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def get_initials(name):
    return "".join([word[0] for word in name.split()[:2]]).upper()

def validate_nik(nik):
    return nik == "" or (nik.isdigit() and len(nik) == 16)

# =========================================================
# CSS (DISEDIAKAN SEPERTI ASLINYA, TAPI DENGAN PENYESUAIAN MINOR)
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #0c4a3e;
    --primary-2: #0f6b58;
    --primary-3: #e9f5f1;
    --gold: #d5a52b;
    --gold-soft: #f7efd4;
    --dark: #17322d;
    --text: #273936;
    --muted: #71817d;
    --bg: #f6f8f7;
    --white: #ffffff;
    --border: #e1e8e5;
    --shadow: 0 8px 28px rgba(12, 74, 62, .08);
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* ... (CSS LAINNYA TETAP SAMA) ... */

</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGASI & SESSION STATE
# =========================================================
PAGE_URLS = {
    "Beranda": "beranda",
    "Profil & Pimpinan": "profil",
    "Berita & Agenda": "berita",
    "Layanan & Pengaduan": "layanan",
    "JDIH & Transparansi": "jdih",
    "Hubungi Kami": "kontak",
}
URL_TO_PAGE = {v: k for k, v in PAGE_URLS.items()}

if "page" not in st.session_state:
    st.session_state.page = "Beranda"

query_params = st.query_params.to_dict()
if "page" in query_params:
    target = query_params["page"]
    if target in URL_TO_PAGE:
        st.session_state.page = URL_TO_PAGE[target]
        st.query_params.clear()
        st.rerun()

# =========================================================
# KOMPONEN HEADER (TOP BAR, RUNNING TEXT, BRAND, NAV)
# =========================================================
def render_header():
    # Top Bar
    st.markdown(
        """
    <div class="govbar">
        <div class="govbar-left">
            <span>🇮🇩 Portal Informasi Pemerintahan Daerah</span>
            <span>|</span>
            <strong>DPRK ACEH JAYA</strong>
        </div>
        <div class="govbar-right">
            <a href="?page=kontak">Hubungi Kami</a>
            <span>|</span>
            <a href="?page=jdih">PPID</a>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Running Text
    st.markdown(
        """
    <div class="running-text-wrap">
        <div class="running-text">
            📢 Selamat Datang di Portal Resmi DPRK Aceh Jaya &nbsp;&nbsp;|&nbsp;&nbsp; 
            📅 Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;|&nbsp;&nbsp; 
            📢 Layanan Pengaduan Masyarakat kini dapat diakses melalui menu Layanan & Pengaduan &nbsp;&nbsp;|&nbsp;&nbsp; 
            🌐 Mari wujudkan transparansi dan akuntabilitas pemerintahan daerah bersama DPRK Aceh Jaya.
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Brand
    st.markdown(
        """
    <div class="brand-wrap">
        <div class="brand-inner">
            <div class="brand">
                <div class="brand-logo">🏛️</div>
                <div>
                    <div class="brand-title">Dewan Perwakilan Rakyat<br>Kabupaten Aceh Jaya</div>
                    <div class="brand-subtitle">PORTAL INFORMASI PUBLIK DAN ASPIRASI MASYARAKAT</div>
                </div>
            </div>
            <div style="text-align:right;color:#74827e;font-size:11px;line-height:1.7;">
                Kabupaten Aceh Jaya<br>
                Provinsi Aceh
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Navigation
    st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
    nav_cols = st.columns([1.05, 1.05, 1.15, 1.2, 1.2, 1.05])
    nav_keys = list(PAGES.keys())

    for i, key in enumerate(nav_keys):
        with nav_cols[i]:
            active_class = "nav-button-active" if st.session_state.page == PAGES[key] else "nav-button"
            st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
            if st.button(PAGES[key].replace(" & ", " • "), key=f"nav_{key}", use_container_width=True):
                st.session_state.page = PAGES[key]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Alert
    st.markdown(
        """
    <div class="alert">
        <span class="alert-badge">i</span>
        <strong>Informasi:</strong>
        <span>Portal DPRK Aceh Jaya menyediakan akses informasi publik, produk hukum, agenda dewan, dan penyampaian aspirasi masyarakat.</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

# =========================================================
# HALAMAN BERANDA
# =========================================================
def render_beranda():
    st.markdown(
        """
    <section class="hero">
        <div class="hero-content">
            <div class="hero-kicker">PORTAL RESMI DPRK ACEH JAYA</div>
            <h1>Suara Masyarakat,<br>Bagian dari Pembangunan Aceh Jaya</h1>
            <p>Akses informasi kegiatan DPRK, produk hukum, agenda persidangan, layanan publik, serta sampaikan aspirasi masyarakat melalui satu portal informasi yang mudah diakses.</p>
            <div class="hero-buttons">
                <a class="hero-btn" href="?page=layanan">Sampaikan Aspirasi</a>
                <a class="hero-btn secondary" href="?page=berita">Lihat Berita</a>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # ... (SISA KODE BERANDA TETAP SAMA, TAPI DI DALAM FUNGSI INI) ...
    st.markdown('<div class="content" id="layanan">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Akses Cepat</div>
                <h2 class="section-title">Layanan Publik</h2>
                <div class="section-desc">Akses layanan dan informasi DPRK Aceh Jaya secara lebih mudah.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi, keluhan, dan laporan masyarakat.", "layanan"),
        ("📜", "JDIH", "Akses produk hukum dan dokumen peraturan daerah.", "jdih"),
        ("📅", "Agenda DPRK", "Lihat agenda rapat, sidang, dan kegiatan DPRK.", "berita"),
        ("📊", "Transparansi", "Informasi publik dan dokumen penyelenggaraan pemerintahan.", "jdih"),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses oleh masyarakat.", "jdih"),
        ("🔗", "E-LHKPN", "Pelaporan harta kekayaan penyelenggara negara.", "https://elhpkpn.kpk.go.id/"),
    ]

    service_cols = st.columns(6)
    icon_accents = ["", "accent-gold", "accent-blue"]
    for i, (icon, title, desc, target) in enumerate(services):
        with service_cols[i]:
            accent = icon_accents[i % 3]
            is_external = target.startswith("http")
            link_target = 'target="_blank" rel="noopener noreferrer"' if is_external else ""
            href_val = target if is_external else f"?page={target}"
            st.markdown(
                f"""
            <a href="{href_val}" {link_target} style="text-decoration: none; color: inherit; display: block;">
                <div class="service-box">
                    <div class="service-icon {accent}">{icon}</div>
                    <div class="service-title">{title}</div>
                    <div class="service-desc">{desc}</div>
                </div>
            </a>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</section></div>", unsafe_allow_html=True)

    # Info Strip
    st.markdown(
        """
    <div class="info-strip">
        <div class="info-inner">
    """,
        unsafe_allow_html=True,
    )

    stat_cols = st.columns(4)
    stats = [("2024–2029", "Masa Jabatan"), ("3", "Pimpinan DPRK"), ("5", "Komisi / Alat Kelengkapan"), ("24/7", "Akses Informasi")]
    for i, (number, label) in enumerate(stats):
        with stat_cols[i]:
            divider_class = "has-divider" if i < len(stats) - 1 else ""
            st.markdown(
                f"""
            <div class="info-item {divider_class}">
                <div class="info-number">{number}</div>
                <div class="info-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        </div>
    </div>
    <div class="content" id="berita">
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Informasi Terbaru</div>
                <h2 class="section-title">Berita & Agenda</h2>
                <div class="section-desc">Informasi kegiatan dan agenda DPRK Aceh Jaya.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_news, col_agenda = st.columns([1.75, 1])

    with col_news:
        main_news = NEWS[0]
        st.markdown(
            f"""
        <div class="news-main">
            <div class="news-main-img-wrap"><img class="news-main-img" src="{main_news['image']}"></div>
            <div class="news-main-body">
                <div class="news-tag">{main_news['tag']}</div>
                <h3>{main_news['title']}</h3>
                <p style="color:#71817d;font-size:12px;line-height:1.65;">{main_news['desc']}</p>
                <div class="news-date">🕒 {main_news['date']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        for item in NEWS[1:]:
            st.markdown(
                f"""
            <div class="news-side" style="margin-top:18px;">
                <div class="news-side-img-wrap"><img class="news-side-img" src="{item['image']}"></div>
                <div>
                    <div class="news-tag">{item['tag']}</div>
                    <h4>{item['title']}</h4>
                    <p>{item['desc']}</p>
                    <div class="news-date" style="margin-top:7px;">🕒 {item['date']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col_agenda:
        st.markdown('<div class="agenda-wrap">', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="section-kicker">Jadwal</div>
            <div style="font-family:'Plus Jakarta Sans';font-size:20px;font-weight:800;color:#183d35;margin-bottom:5px;">Agenda Terdekat</div>
            """,
            unsafe_allow_html=True,
        )

        for day, month, title, desc in AGENDA:
            st.markdown(
                f"""
            <div class="agenda-row">
                <div class="agenda-date">
                    <strong>{day}</strong>
                    <span>{month}</span>
                </div>
                <div>
                    <div class="agenda-title">{title}</div>
                    <div class="agenda-desc">{desc}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section></div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN PROFIL
# =========================================================
def render_profil():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Tentang DPRK</div>
        <h2 class="section-title">Profil DPRK Aceh Jaya</h2>
        <p class="section-desc">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya sebagai unsur penyelenggara pemerintahan daerah bersama pemerintah daerah menjalankan fungsi legislasi, anggaran, dan pengawasan sesuai ketentuan peraturan perundang-undangan.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(["🏛️ Pimpinan", "👥 Anggota DPRK per Komisi", "🏢 Pejabat Sekretariat"])
    
    with tab1:
        st.markdown(
            """
        <div style="background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:28px;margin-top:20px;margin-bottom:20px;">
            <div class="section-kicker">Pimpinan</div>
            <h2 class="section-title" style="font-size:22px;">Pimpinan DPRK Aceh Jaya</h2>
            <p class="section-desc">Masa Jabatan 2024–2029.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        cols = st.columns(3)
        for i, (role, name, desc) in enumerate(PIMPINAN):
            with cols[i]:
                initials = get_initials(name)
                st.markdown(
                    f"""
                <div class="profile-card">
                    <div class="profile-photo">{initials}</div>
                    <div class="profile-role">{role}</div>
                    <div class="profile-name">{name}</div>
                    <div class="profile-desc">{desc}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    with tab2:
        st.markdown('<div style="margin-top:20px;">', unsafe_allow_html=True)
        for komisi, members in ANGGOTA_DPRK.items():
            with st.expander(f"📂 {komisi}", expanded=False):
                cols = st.columns(2)
                for idx, (nama, jabatan) in enumerate(members):
                    with cols[idx % 2]:
                        initials = get_initials(nama)
                        st.markdown(
                            f"""
                        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:#f6f8f7;border-radius:6px;margin-bottom:8px;border:1px solid #e1e8e5;">
                            <div style="width:40px;height:40px;border-radius:50%;background:var(--primary-3);color:var(--primary);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;flex-shrink:0;">
                                {initials}
                            </div>
                            <div>
                                <div style="font-size:11px;color:var(--primary-2);font-weight:700;text-transform:uppercase;">{jabatan}</div>
                                <div style="font-size:14px;font-weight:600;color:#183d35;">{nama}</div>
                            </div>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div style="margin-top:20px;">', unsafe_allow_html=True)
        cols = st.columns(2)
        for idx, (nama, jabatan) in enumerate(SEKRETARIAT):
            with cols[idx % 2]:
                st.markdown(
                    f"""
                <div style="display:flex;align-items:center;gap:12px;padding:16px;background:#fff;border-radius:8px;margin-bottom:12px;border:1px solid #e1e8e5;box-shadow:0 2px 8px rgba(12,74,62,0.04);">
                    <div style="width:44px;height:44px;border-radius:50%;background:var(--gold-soft);color:#a97e1c;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;flex-shrink:0;">
                        🏢
                    </div>
                    <div>
                        <div style="font-size:11px;color:#71817d;font-weight:600;text-transform:uppercase;">{jabatan}</div>
                        <div style="font-size:15px;font-weight:700;color:#183d35;">{nama}</div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN BERITA & AGENDA
# =========================================================
def render_berita_agenda():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Publikasi</div>
        <h2 class="section-title">Berita & Agenda DPRK</h2>
        <p class="section-desc">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    for item in NEWS:
        st.markdown(
            f"""
        <div class="news-list-card" style="background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:18px;margin-bottom:18px;display:flex;gap:22px;">
            <div style="width:270px;height:165px;border-radius:6px;overflow:hidden;flex-shrink:0;">
                <img src="{item['image']}" style="width:100%;height:100%;object-fit:cover;transition:transform .4s ease;">
            </div>
            <div style="padding:6px 0;">
                <div class="news-tag">{item['tag']}</div>
                <h3 style="color:#183d35;font-family:'Plus Jakarta Sans';font-size:21px;margin:0 0 8px;">{item['title']}</h3>
                <p style="color:#71817d;font-size:12px;line-height:1.7;">{item['desc']}</p>
                <div class="news-date">🕒 {item['date']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Galeri
    st.markdown(
        """
    <div style="margin-top:45px;">
        <div class="section-kicker">Multimedia</div>
        <h2 class="section-title" style="font-size:23px;margin-bottom:18px;">Galeri & Video</h2>
    </div>
    <div style="background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:20px;text-align:center;margin-bottom:40px;">
        <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:6px;">
            <iframe src="https://www.youtube.com/embed/ScMzIvxBSi4" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
        <p style="margin-top:15px;color:#71817d;font-size:13px;">Video Dokumentasi Kegiatan DPRK Aceh Jaya</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Agenda
    st.markdown(
        """
    <div class="section-kicker">Agenda</div>
    <h2 class="section-title" style="font-size:23px;margin-bottom:18px;">Agenda Terdekat</h2>
    """,
        unsafe_allow_html=True,
    )

    agenda_cols = st.columns(3)
    for i, (day, month, title, desc) in enumerate(AGENDA):
        with agenda_cols[i]:
            st.markdown(
                f"""
            <div class="agenda-wrap" style="height:100%;">
                <div class="agenda-date">
                    <strong>{day}</strong><span>{month}</span>
                </div>
                <div style="margin-top:16px;" class="agenda-title">{title}</div>
                <div class="agenda-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN LAYANAN & PENGADUAN
# =========================================================
def render_layanan_pengaduan():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Pelayanan Masyarakat</div>
        <h2 class="section-title">Layanan Aspirasi & Pengaduan</h2>
        <p class="section-desc">Sampaikan aspirasi, laporan, atau pengaduan kepada DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.75, 1])

    with col1:
        st.markdown(
            """
        <div class="section-kicker">Formulir</div>
        <h3 style="color:#183d35;font-family:'Plus Jakarta Sans';font-size:21px;margin-bottom:15px;">Sampaikan Aspirasi Anda</h3>
        """,
            unsafe_allow_html=True,
        )

        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Masukkan nama lengkap")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit", max_chars=16)
            with c2:
                kategori = st.selectbox(
                    "Kategori Pengaduan *",
                    ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"],
                )
            lokasi = st.text_input("Lokasi Kejadian (Opsional)", placeholder="Desa / Kecamatan / lokasi")
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan aspirasi atau laporan secara jelas...")

            submitted = st.form_submit_button("Kirim Aspirasi", type="primary", use_container_width=True)

            if submitted:
                if not nama.strip():
                    st.error("❌ Nama lengkap harus diisi.")
                elif not isi.strip():
                    st.error("❌ Isi laporan harus diisi.")
                elif nik and not validate_nik(nik):
                    st.error("❌ NIK harus terdiri dari 16 digit angka.")
                else:
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ Laporan berhasil dicatat. Nomor tiket: **ADU-{nomor}**")
                    st.info("Simpan nomor tiket untuk keperluan pengecekan tindak lanjut.")

    with col2:
        st.markdown(
            """
        <div class="agenda-wrap">
            <div class="section-kicker">Kontak</div>
            <h3 style="color:#183d35;font-family:'Plus Jakarta Sans';font-size:20px;margin-top:0;">Hubungi Kami</h3>
            <p style="font-size:12px;color:#71817d;line-height:1.8;">
                <strong>📞 Telepon</strong><br>(0655) 12345
            </p>
            <p style="font-size:12px;color:#71817d;line-height:1.8;">
                <strong>✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
            </p>
            <p style="font-size:12px;color:#71817d;line-height:1.8;">
                <strong>📍 Alamat</strong><br>Jl. Merdeka No. 01, Calang, Aceh Jaya
            </p>
            <hr style="border:none;border-top:1px solid #edf1ef;">
            <p style="font-size:11px;color:#71817d;line-height:1.7;">Jam layanan: Senin–Jumat, 08.00–16.00 WIB.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN JDIH & TRANSPARANSI
# =========================================================
def render_jdih_transparansi():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Dokumentasi Hukum</div>
        <h2 class="section-title">JDIH & Transparansi</h2>
        <p class="section-desc">Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    info_cols = st.columns(4)
    cards = [
        ("⚖️", "Produk Hukum", "Qanun dan dokumen hukum daerah."),
        ("📊", "Transparansi", "Informasi penyelenggaraan pemerintahan."),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses masyarakat."),
        ("📑", "Informasi Berkala", "Informasi yang diterbitkan secara berkala."),
    ]

    icon_accents = ["", "accent-gold", "accent-blue", "accent-gold"]
    for i, (icon, title, desc) in enumerate(cards):
        with info_cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="text-align:left;">
                <div class="service-icon {icon_accents[i]}" style="margin:0 0 13px;">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:45px;">
        <div class="section-kicker">Database</div>
        <h2 class="section-title" style="font-size:23px;margin-bottom:18px;">Produk Hukum Daerah</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(JDIH_DATA, columns=["No", "Nomor & Tahun", "Tentang", "Status"])
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "No": st.column_config.TextColumn("No", width="small"),
            "Nomor & Tahun": st.column_config.TextColumn("Nomor & Tahun"),
            "Tentang": st.column_config.TextColumn("Tentang"),
            "Status": st.column_config.TextColumn("Status"),
        },
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN KONTAK
# =========================================================
def render_kontak():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Informasi Kontak</div>
        <h2 class="section-title">Hubungi DPRK Aceh Jaya</h2>
        <p class="section-desc">Gunakan informasi berikut untuk mendapatkan layanan dan informasi dari Sekretariat DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat", "Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya"),
        ("📞", "Telepon", "(0655) 12345"),
        ("✉️", "Email", "sekretariat@dprk.acehjaya.go.id"),
    ]

    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="min-height:180px;">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc" style="font-size:12px;">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:35px;background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:30px;">
        <div class="section-kicker">Lokasi Kantor</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#183d35;font-size:21px;margin-bottom:15px;">Peta & Lokasi</h3>
        <div style="width:100%;height:300px;border-radius:8px;overflow:hidden;border:1px solid #e1e8e5;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p style="font-size:12px;color:#71817d;line-height:1.8;margin-top:15px;">
            <strong>📍 Alamat Lengkap:</strong> Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya, Aceh.
        </p>
        <hr style="border:none;border-top:1px solid #edf1ef;margin:20px 0;">
        <div class="section-kicker">Sekretariat</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#183d35;font-size:21px;margin-bottom:10px;">Jam Pelayanan</h3>
        <p style="font-size:12px;color:#71817d;line-height:1.8;">
            Senin–Kamis: 08.00–16.30 WIB<br>
            Jumat: 08.00–16.30 WIB<br>
            Sabtu–Minggu: Libur
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RENDER HALAMAN SESUAI NAVIGASI
# =========================================================
render_header()

if st.session_state.page == "Beranda":
    render_beranda()
elif st.session_state.page == "Profil & Pimpinan":
    render_profil()
elif st.session_state.page == "Berita & Agenda":
    render_berita_agenda()
elif st.session_state.page == "Layanan & Pengaduan":
    render_layanan_pengaduan()
elif st.session_state.page == "JDIH & Transparansi":
    render_jdih_transparansi()
else:
    render_kontak()

# =========================================================
# FOOTER
# =========================================================
st.markdown(
"""
<div class="footer">
<div class="footer-container">
<div class="footer-grid">

<!-- KOLOM 1 -->
<div class="footer-column">
<div class="footer-brand">
<div class="footer-logo">🏛️</div>
<div>
<div class="footer-brand-name">DPRK ACEH JAYA</div>
<div class="footer-brand-subtitle">PORTAL INFORMASI PUBLIK</div>
</div>
</div>
<p class="footer-description">
Portal resmi Dewan Perwakilan Rakyat Kabupaten Aceh Jaya
yang menyediakan informasi kelembagaan, berita, agenda,
produk hukum, layanan publik, dan aspirasi masyarakat.
</p>
<div class="footer-social">
<div class="footer-social-item">f</div>
<div class="footer-social-item">𝕏</div>
<div class="footer-social-item">▶</div>
<div class="footer-social-item">◎</div>
</div>
</div>

<!-- KOLOM 2 -->
<div class="footer-column">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=profil">Pimpinan DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=berita">Komisi</a>
</div>

<!-- KOLOM 3 -->
<div class="footer-column">
<h4>Layanan Publik</h4>
<a href="?page=layanan">Pengaduan Masyarakat</a>
<a href="?page=kontak">Informasi Publik</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank" rel="noopener noreferrer">E-LHKPN</a>
</div>

<!-- KOLOM 4 -->
<div class="footer-column">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Kabupaten Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
<p>🕐 Senin–Jumat, 08.00–16.00 WIB</p>
</div>

</div>

<div class="footer-divider"></div>

<div class="footer-bottom">
<div class="footer-bottom-left">
© 2026 DPRK Aceh Jaya. Seluruh hak cipta dilindungi.
</div>
<div class="footer-bottom-right">
Portal Informasi Publik • Kabupaten Aceh Jaya
</div>
</div>

</div>
</div>
""",
unsafe_allow_html=True
)
