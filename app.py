import streamlit as st
from datetime import datetime
import pandas as pd

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
# LOGO URL
# =========================================================
LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# =========================================================
# DATA
# =========================================================
PAGES = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Berita": "Berita & Agenda",
    "Galeri": "Galeri Foto & Video",
    "Layanan": "Layanan & Pengaduan",
    "JDIH": "JDIH & Transparansi",
    "Kontak": "Hubungi Kami",
}

# WARTA DPRK - Berita Utama
WARTA_DPRK = [
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "date": "Jumat, 14 Agustus 2026",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna Ke-IX Masa Persidangan II Tahun Sidang membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna ke-VIII Masa Persidangan II, Bahas Pertanggungjawaban APBK 2025 dan Perubahan AKD",
        "date": "Kamis, 30 Juli 2026",
        "desc": "Rapat Paripurna ke-VIII Masa Persidangan II membahas pertanggungjawaban APBK 2025 dan Perubahan Anggaran Kas Daerah.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Ketua DPRK Aceh Jaya Dukung Pelestarian Mangrove, Dorong Penguatan Ekosistem Pesisir",
        "date": "Minggu, 26 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya Musliadi Z, S.E menyampaikan dukungan terhadap kegiatan Penanaman Mangrove Serentak dalam rangka memperingati Hari Mangrove.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Ketua DPRK Aceh Jaya Apresiasi Kejari Aceh Jaya Berhasil Pulihkan Keuangan Negara Rp2,05 Miliar",
        "date": "Rabu, 22 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya menghadiri kegiatan Press Release Capaian Pemulihan Keuangan Negara yang diselenggarakan oleh Kejaksaan Negeri Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=800&q=80",
    },
]

# KESEKRETARIATAN
KESEKRETARIATAN = [
    {
        "title": "Apel Pagi Rutin, ASN DPRK Aceh Jaya Diingatkan Disiplin dan Komitmen Kerja",
        "date": "Senin, 06 April 2026",
        "desc": "Dalam amanatnya, Yuswardi menekankan pentingnya kedisiplinan dan komitmen dalam menjalankan tugas sebagai ASN.",
    },
    {
        "title": "Sekretaris DPRK Aceh Jaya Ikuti Vidcon Entry Meeting Pemeriksaan Laporan Keuangan 2025",
        "date": "Kamis, 02 April 2026",
        "desc": "Sekretaris DPRK Aceh Jaya, Abu Bakar, S.Pd.I., MH mengikuti video conference Entry Meeting Pemeriksaan Laporan Keuangan 2025.",
    },
]

# AGENDA TERKINI
AGENDA_TERKINI = [
    {
        "tanggal": "09 September 2026",
        "judul": "Rapat Pleno DPRK Aceh Jaya - 09 September 2026",
        "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran",
    },
    {
        "tanggal": "07 September 2026",
        "judul": "Rapat Komisi III DPRK Aceh Jaya - 07 September 2026",
        "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR.",
    },
    {
        "tanggal": "01 September 2026",
        "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya - 01 September 2026",
        "desc": "Rapat Badan Musyawarah tentang Penetapan Jadwal Rapat Paripurna DPRK Aceh Jaya.",
    },
]

# PIMPINAN DAN ANGGOTA DPRK
PIMPINAN_DAN_ANGGOTA = [
    ("MUSLIADI Z, S.E", "KETUA DPRK"),
    ("IRWANTO. NP", "WAKIL KETUA I DPRK"),
    ("TEUKU ASRIZAL, S.H", "WAKIL KETUA II DPRK"),
    ("ISKANDAR IBRAHIM", "ANGGOTA DPRK / KETUA KOMISI I"),
    ("H. DASRIL ARAHMAN. IB, S.E", "ANGGOTA DPRK / WAKIL KETUA KOMISI I"),
    ("WANTI CAHYA", "ANGGOTA DPRK / SEKRETARIS KOMISI I"),
    ("MUSLIM", "ANGGOTA DPRK / ANGGOTA KOMISI I"),
    ("Ir. FAUZI YAHYA", "ANGGOTA DPRK / KETUA KOMISI II"),
    ("AZHAR", "ANGGOTA DPRK / WAKIL KETUA KOMISI II"),
    ("FITRA AKHYAR, ST", "ANGGOTA DPRK / SEKRETARIS KOMISI II"),
    ("SAFRIYANTONI", "ANGGOTA DPRK / ANGGOTA KOMISI II"),
    ("AYUDI ILHAM, S.E", "ANGGOTA DPRK / ANGGOTA KOMISI II"),
    ("SUDIRMAN, S.P", "ANGGOTA DPRK / KETUA KOMISI III"),
    ("ABDUL MUTHALLEB", "ANGGOTA DPRK / WAKIL KETUA KOMISI III"),
    ("Drs. H. T. IRFAN TB., M.Si", "ANGGOTA DPRK / SEKRETARIS KOMISI III"),
    ("MUHAMMAD DIAH, S.E", "ANGGOTA DPRK / ANGGOTA KOMISI III"),
    ("HAZAMI, S.Pd", "ANGGOTA DPRK / KETUA KOMISI IV"),
    ("MUHAMMAD JAMIN", "ANGGOTA DPRK / WAKIL KETUA KOMISI IV"),
    ("HJ. FITRI MAYA LISA, S.Sos", "ANGGOTA DPRK / SEKRETARIS KOMISI IV"),
    ("USMAN. ID", "ANGGOTA DPRK / ANGGOTA KOMISI IV"),
]

# PEJABAT SEKRETARIAT
PEJABAT_SEKRETARIAT = [
    ("ABU BAKAR, S.Pd.I., M.H", "Sekretaris DPRK Aceh Jaya"),
    ("IRMA HANUM, SH", "Staf Ahli Bidang Pemerintahan, Hukum dan Politik"),
    ("HIDAYAT, SE., M.Si", "Kepala Bagian Umum dan Keuangan"),
    ("YUSWARDI, S.Kom", "Kepala Bagian Persidangan dan Perundang-Undangan"),
    ("NELLI FAUZIANA, SH., MH", "Kepala Bagian Fasilitasi Penganggaran dan Pengawasan"),
    ("IHSAN SALIM, S.A.P", "Kepala Sub Bagian Tata Usaha dan Kepegawaian"),
]

# JDIH DATA
JDIH_DATA = [
    ["1", "Qanun No. 5/2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku"],
    ["2", "Perbup No. 12/2026", "Penjabaran APBK Aceh Jaya 2026", "Berlaku"],
    ["3", "Qanun No. 2/2024", "Perlindungan Korban Bencana Alam", "Berlaku"],
]

# =========================================================
# CSS STYLE - NAVBAR SUPER PREMIUM
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #064e3b;
    --primary-dark: #022c22;
    --primary-2: #0f6b58;
    --primary-3: #e9f5f1;
    --gold: #d5a52b;
    --gold-light: #fcd34d;
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

/* Top Bar */
.govbar { background: var(--primary-dark); color: rgba(255,255,255,.88); min-height: 38px; padding: 0 6%; display: flex; align-items: center; justify-content: space-between; font-size: 12px; }
.govbar-left, .govbar-right { display: flex; gap: 20px; align-items: center; }
.govbar strong { color: #fff; }
.govbar-right a { color: rgba(255,255,255,.88); text-decoration: none; transition: color .15s ease; }
.govbar-right a:hover { color: var(--gold-light); text-decoration: underline; }

/* Brand */
.brand-wrap { background: #fff; border-bottom: 1px solid #e7ecea; padding: 18px 6%; }
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand-logo { width: 70px; height: 70px; border-radius: 8px; background: #fff; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(12,74,62,.18); overflow: hidden; }
.brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.brand-title { color: #123b33; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; line-height: 1.2; font-weight: 800; text-transform: uppercase; }
.brand-subtitle { margin-top: 4px; color: #788783; font-size: 11px; letter-spacing: .6px; }

/* =========================================
   NAVIGATION - SUPER PREMIUM
   ========================================= */
.nav-wrap { 
    background: linear-gradient(180deg, #065f46 0%, #022c22 100%); 
    border-bottom: 2px solid var(--gold); 
    padding: 0 6%;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2), 0 2px 8px rgba(0,0,0,0.1);
    position: relative;
    z-index: 100;
}

/* Subtle top shine for premium glass effect */
.nav-wrap::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
}

.nav-inner { 
    min-height: 64px; 
    display: flex; 
    align-items: center; 
    gap: 0;
    justify-content: center;
}

/* Navbar Items */
.nav-button, .nav-button-active { 
    position: relative;
    flex: 1;
    margin: 0 4px;
}

.nav-button .stButton > button, 
.nav-button-active .stButton > button {
    background: transparent !important; 
    border: 1px solid transparent !important; 
    color: rgba(255,255,255,0.85) !important;
    font-size: 12.5px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    border-radius: 6px !important;
    padding: 14px 16px !important;
    min-height: 48px !important;
    width: 100% !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}

.nav-button .stButton > button:hover { 
    color: #ffffff !important; 
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(255,255,255,0.15) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.nav-button-active .stButton > button {
    color: #ffffff !important; 
    font-weight: 800 !important; 
    background: linear-gradient(135deg, rgba(213, 165, 43, 0.2) 0%, rgba(213, 165, 43, 0.05) 100%) !important;
    border-color: rgba(213, 165, 43, 0.5) !important;
    box-shadow: 0 0 20px rgba(213, 165, 43, 0.15), inset 0 1px 0 rgba(255,255,255,0.1);
}

/* Active Indicator - Premium Gold Glow */
.nav-button::after, 
.nav-button-active::after {
    content: ''; 
    position: absolute; 
    left: 50%; 
    width: 0;
    bottom: -2px; 
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold-light), var(--gold), var(--gold-light), transparent); 
    border-radius: 2px;
    transform: translateX(-50%);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); 
    box-shadow: 0 0 12px rgba(213, 165, 43, 0.8);
}

.nav-button:hover::after { 
    width: 60%;
}

.nav-button-active::after { 
    width: 60%;
}
/* ========================================= */

/* Running Text */
.running-text-wrap { background: var(--gold); color: var(--dark); padding: 10px 0; overflow: hidden; white-space: nowrap; border-bottom: 2px solid var(--primary); }
.running-text { display: inline-block; padding-left: 100%; animation: marquee 35s linear infinite; font-size: 13px; font-weight: 600; }
@keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

/* Alert */
.alert { background: #fff9e9; border-bottom: 1px solid #f0dfad; border-left: 3px solid var(--gold); color: #725719; padding: 10px 6%; font-size: 12px; display: flex; align-items: center; gap: 10px; }
.alert-badge { width: 20px; height: 20px; border-radius: 50%; background: var(--gold); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 11px; flex-shrink: 0; }

/* Hero */
.hero { position: relative; min-height: 440px; display: flex; align-items: center; overflow: hidden; background: linear-gradient(90deg, rgba(4,43,36,.95) 0%, rgba(8,74,62,.78) 45%, rgba(8,74,62,.35) 100%), url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat; }
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 70px 0; color: white; }
.hero-kicker { display: inline-block; color: #f8df87; font-size: 12px; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 14px; }
.hero h1 { max-width: 720px; font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(34px, 5vw, 60px); line-height: 1.08; margin: 0 0 20px; font-weight: 800; }
.hero p { max-width: 650px; color: rgba(255,255,255,.88); font-size: 16px; line-height: 1.75; margin-bottom: 28px; }
.hero-buttons { display: flex; flex-wrap: wrap; gap: 12px; }
.hero-btn { display: inline-block; padding: 12px 21px; border-radius: 5px; background: var(--gold); color: #fff !important; text-decoration: none; font-weight: 700; font-size: 13px; transition: transform .15s ease, box-shadow .15s ease, background .15s ease; }
.hero-btn:hover { background: #c1961f; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,.2); }
.hero-btn.secondary { background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.55); }
.hero-btn.secondary:hover { background: rgba(255,255,255,.2); }

/* Content */
.content { width: 88%; max-width: 1250px; margin: 0 auto; }
.section { padding: 48px 0; }
.section-head { display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 24px; }
.section-kicker { color: var(--primary-2); font-size: 11px; font-weight: 800; letter-spacing: 1.4px; text-transform: uppercase; margin-bottom: 6px; }
.section-title { color: #183d35; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 27px; font-weight: 800; margin: 0; }
.section-desc { color: var(--muted); font-size: 13px; line-height: 1.6; margin-top: 7px; }

/* Service Box */
.service-box { background: #fff; border: 1px solid var(--border); min-height: 160px; padding: 25px 20px; text-align: center; transition: .25s ease; border-radius: 8px; }
a:hover .service-box { transform: translateY(-4px) !important; border-color: #b9d6ce !important; box-shadow: var(--shadow) !important; }
.service-box:hover { transform: translateY(-4px); border-color: #b9d6ce; box-shadow: var(--shadow); }
.service-icon { width: 54px; height: 54px; margin: 0 auto 14px; border-radius: 50%; background: var(--primary-3); color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 24px; transition: transform .25s ease; }
.service-box:hover .service-icon { transform: scale(1.08); }
.service-icon.accent-gold { background: var(--gold-soft); color: #a97e1c; }
.service-icon.accent-blue { background: #e7eef7; color: #2f5f8f; }
.service-title { color: #183d35; font-size: 14px; font-weight: 800; margin-bottom: 7px; }
.service-desc { color: #7a8884; font-size: 11px; line-height: 1.5; }

/* News Grid */
.news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }
.news-card { background: #fff; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; transition: box-shadow .2s ease, border-color .2s ease; height: 100%; display: flex; flex-direction: column; }
.news-card:hover { box-shadow: var(--shadow); border-color: #b9d6ce; }
.news-card-img { width: 100%; height: 180px; object-fit: cover; transition: transform .4s ease; }
.news-card:hover .news-card-img { transform: scale(1.05); }
.news-card-img-wrap { overflow: hidden; }
.news-card-body { padding: 18px; flex: 1; display: flex; flex-direction: column; }
.news-card h3 { color: #173b33; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; line-height: 1.4; margin: 0 0 8px; font-weight: 700; flex: 1; }
.news-card p { color: #71817d; font-size: 12px; line-height: 1.6; margin: 0 0 12px; }
.news-date { color: var(--primary-2); font-size: 11px; font-weight: 600; display: flex; align-items: center; gap: 5px; }

/* Warta DPRK List */
.warta-list { display: flex; flex-direction: column; gap: 16px; }
.warta-item { background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 20px; transition: box-shadow .2s ease; }
.warta-item:hover { box-shadow: var(--shadow); }
.warta-item h3 { color: var(--primary); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; margin: 0 0 8px; font-weight: 700; line-height: 1.4; }
.warta-item .date { color: var(--gold); font-size: 12px; font-weight: 700; margin-bottom: 8px; display: block; }
.warta-item p { color: var(--muted); font-size: 13px; line-height: 1.6; margin: 0; }

/* Agenda */
.agenda-wrap { background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 22px; }
.agenda-item { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }
.agenda-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.agenda-date-badge { display: inline-block; background: var(--primary); color: white; padding: 6px 12px; border-radius: 4px; font-size: 11px; font-weight: 700; margin-bottom: 10px; }
.agenda-title { color: #1b4138; font-weight: 800; font-size: 15px; margin-bottom: 8px; }
.agenda-desc { color: #7a8884; font-size: 12px; line-height: 1.6; }

/* Info Strip */
.info-strip { background: var(--primary); color: white; padding: 34px 6%; }
.info-inner { width: 88%; max-width: 1250px; margin: auto; }
.info-item { text-align: center; padding: 5px 15px; position: relative; }
.info-item.has-divider::after { content: ''; position: absolute; right: 0; top: 8px; bottom: 8px; width: 1px; background: rgba(255,255,255,.15); }
.info-number { color: #f4d873; font-size: 29px; font-weight: 800; }
.info-label { color: rgba(255,255,255,.78); font-size: 11px; margin-top: 3px; }

/* Profile Card */
.profile-card { background: white; border: 1px solid var(--border); border-radius: 8px; padding: 28px 20px; text-align: center; height: 100%; transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease; }
.profile-card:hover { transform: translateY(-4px); box-shadow: var(--shadow); border-color: #b9d6ce; }
.profile-photo { width: 92px; height: 92px; border-radius: 50%; margin: auto; display: flex; align-items: center; justify-content: center; background: linear-gradient(145deg, #0c5d4d, #0b4037); color: #fff; font-size: 30px; font-weight: 800; }
.profile-role { color: var(--primary-2); font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: .8px; margin-top: 16px; }
.profile-name { color: #183d35; font-size: 17px; font-weight: 800; margin: 6px 0; }
.profile-desc { color: #7a8884; font-size: 11px; line-height: 1.55; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; background: transparent; border-bottom: 1px solid var(--border); }
.stTabs [data-baseweb="tab"] { background: transparent; border-radius: 8px 8px 0 0; padding: 12px 24px; color: var(--muted); font-weight: 600; font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s ease; }
.stTabs [aria-selected="true"] { background: var(--primary-3) !important; color: var(--primary) !important; border-bottom: 2px solid var(--primary); }
.stTabs [data-baseweb="tab"]:hover { background: #f2f7f5 !important; color: var(--primary) !important; }

/* Footer */
.footer { background: radial-gradient(ellipse at top left, #0d4438 0%, #022c22 62%), #022c22; color: rgba(255,255,255,.75); margin-top: 60px; padding: 56px 6% 0; }
.footer-container { width: 88%; max-width: 1250px; margin: 0 auto; }
.footer-grid { display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; }
.footer-column h4 { color: #fff; font-size: 13px; font-weight: 800; margin: 0 0 18px; letter-spacing: .3px; }
.footer-column a { display: block; color: rgba(255,255,255,.62); font-size: 12.5px; line-height: 2.15; text-decoration: none; transition: color .15s ease, padding-left .15s ease; }
.footer-column a:hover { color: var(--gold-light); padding-left: 3px; }
.footer-column p { color: rgba(255,255,255,.62); font-size: 12.5px; line-height: 1.85; margin: 0 0 8px; }
.footer-brand { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; }
.footer-logo { width: 50px; height: 50px; border-radius: 6px; flex-shrink: 0; background: #fff; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.footer-logo img { width: 100%; height: 100%; object-fit: contain; }
.footer-brand-name { color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14.5px; font-weight: 800; letter-spacing: .3px; }
.footer-brand-subtitle { color: rgba(255,255,255,.5); font-size: 10px; letter-spacing: .6px; margin-top: 2px; }
.footer-description { color: rgba(255,255,255,.58); font-size: 12.5px; line-height: 1.85; max-width: 340px; margin: 0 0 22px; }
.footer-social { display: flex; gap: 10px; }
.footer-social-item { width: 34px; height: 34px; border-radius: 50%; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.14); color: rgba(255,255,255,.85); display: flex; align-items: center; justify-content: center; font-size: 13px; transition: background .15s ease, border-color .15s ease; text-decoration: none; }
.footer-social-item:hover { background: var(--gold); border-color: var(--gold); color: var(--primary-dark); }
.footer-divider { border-top: 1px solid rgba(255,255,255,.1); }
.footer-bottom { padding: 18px 0 22px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; color: rgba(255,255,255,.42); font-size: 11px; }

@media (max-width: 850px) {
    .footer-grid { grid-template-columns: 1fr 1fr; row-gap: 32px; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .news-grid { grid-template-columns: 1fr; }
    .nav-inner { flex-wrap: wrap; justify-content: center; }
    .nav-button, .nav-button-active { flex: 0 0 33.333%; margin: 2px; }
    .nav-button .stButton > button, .nav-button-active .stButton > button { 
        padding: 10px 8px !important; 
        font-size: 11px !important; 
        letter-spacing: 0.5px !important;
    }
}

div[data-testid="stForm"] { background: white; border: 1px solid var(--border); border-radius: 8px; padding: 25px !important; }
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { border-radius: 5px !important; border-color: #d8e1de !important; }
.stButton > button[kind="primary"], .stFormSubmitButton > button { background: var(--primary) !important; border: none !important; color: white !important; border-radius: 5px !important; font-weight: 700 !important; transition: background .15s ease !important; }
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover { background: var(--primary-2) !important; }
div[data-testid="stDataFrame"] { border: 1px solid var(--border) !important; border-radius: 8px !important; overflow: hidden; }
a:focus-visible, button:focus-visible, .stButton > button:focus-visible { outline: 2px solid var(--gold) !important; outline-offset: 2px !important; }
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE & NAVIGATION
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

PAGE_URLS = {v: k.lower().replace(" & ", "-").replace(" ", "-") for k, v in PAGES.items()}
URL_TO_PAGE = {v: k for k, v in PAGE_URLS.items()}

query_params = st.query_params
if "page" in query_params:
    target = query_params["page"]
    if target in URL_TO_PAGE:
        st.session_state.page = URL_TO_PAGE[target]
        del st.query_params["page"]
        st.rerun()

# =========================================================
# TOP BAR & BRAND
# =========================================================
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

st.markdown(
    f"""
<div class="brand-wrap">
    <div class="brand-inner">
        <div class="brand">
            <div class="brand-logo">
                <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya" 
                     onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
            </div>
            <div>
                <div class="brand-title">Dewan Perwakilan Rakyat<br>Kabupaten Aceh Jaya</div>
                <div class="brand-subtitle">PORTAL INFORMASI PUBLIK DAN ASPIRASI MASYARAKAT</div>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION - SUPER PREMIUM
# =========================================================
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns(7)
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

# =========================================================
# RUNNING TEXT & ALERT
# =========================================================
st.markdown(
    """
<div class="running-text-wrap">
    <div class="running-text">
        📢 Selamat Datang di Portal Resmi DPRK Aceh Jaya &nbsp;&nbsp;|&nbsp;&nbsp; 
        📅 Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;|&nbsp;&nbsp; 
        📢 Layanan Pengaduan Masyarakat kini dapat diakses melalui menu Layanan & Pengaduan &nbsp;&nbsp;|&nbsp;&nbsp; 
         Mari wujudkan transparansi dan akuntabilitas pemerintahan daerah bersama DPRK Aceh Jaya.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

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
# BERANDA
# =========================================================
if st.session_state.page == "Beranda":
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

    # Layanan Publik
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
    st.markdown("</div></div>", unsafe_allow_html=True)

    # WARTA DPRK & AGENDA
    st.markdown(
        """
    <div class="content">
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Informasi Terbaru</div>
                <h2 class="section-title">WARTA DPRK & Agenda</h2>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_warta, col_agenda = st.columns([2, 1])

    with col_warta:
        st.markdown('<div class="section-kicker" style="margin-bottom: 15px;">WARTA DPRK</div>', unsafe_allow_html=True)
        st.markdown('<div class="warta-list">', unsafe_allow_html=True)
        for item in WARTA_DPRK[:3]:
            st.markdown(
                f"""
            <div class="warta-item">
                <h3>{item['title']}</h3>
                <span class="date">{item['date']}</span>
                <p>{item['desc']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with col_agenda:
        st.markdown(
            """
        <div class="agenda-wrap">
            <div class="section-kicker">Jadwal</div>
            <div style="font-family:'Plus Jakarta Sans';font-size:18px;font-weight:800;color:#183d35;margin-bottom:20px;">AGENDA TERKINI</div>
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-item">
                <div class="agenda-date-badge">{item['tanggal']}</div>
                <div class="agenda-title">{item['judul']}</div>
                <div class="agenda-desc">{item['desc']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)

    # KESEKRETARIATAN
    st.markdown(
        """
    <section class="section" style="background: #fff;">
        <div class="content">
            <div class="section-kicker" style="margin-bottom: 15px;">KESEKRETARIATAN</div>
            <div class="warta-list">
    """,
        unsafe_allow_html=True,
    )
    for item in KESEKRETARIATAN:
        st.markdown(
            f"""
        <div class="warta-item">
            <h3>{item['title']}</h3>
            <span class="date">{item['date']}</span>
            <p>{item['desc']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div></section></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# PROFIL & PIMPINAN
# =========================================================
elif st.session_state.page == "Profil & Pimpinan":
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

    tab1, tab2 = st.tabs(["🏛️ Pimpinan dan Anggota DPRK", "🏢 Pejabat Sekretariat DPRK"])
    
    with tab1:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px; margin-top: 20px;">', unsafe_allow_html=True)
        for nama, jabatan in PIMPINAN_DAN_ANGGOTA:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 16px; text-align: center;">
                <div style="font-weight: 800; color: var(--primary); font-size: 14px; margin-bottom: 5px;">{nama}</div>
                <div style="color: var(--muted); font-size: 11px;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 15px; margin-top: 20px;">', unsafe_allow_html=True)
        for nama, jabatan in PEJABAT_SEKRETARIAT:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid var(--border); border-radius: 8px; padding: 16px; text-align: center;">
                <div style="font-weight: 800; color: var(--primary); font-size: 14px; margin-bottom: 5px;">{nama}</div>
                <div style="color: var(--muted); font-size: 12px;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# BERITA & AGENDA
# =========================================================
elif st.session_state.page == "Berita & Agenda":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Publikasi</div>
        <h2 class="section-title">WARTA DPRK</h2>
        <p class="section-desc">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="warta-list">', unsafe_allow_html=True)
    for item in WARTA_DPRK:
        st.markdown(
            f"""
        <div class="warta-item" style="display: flex; gap: 20px; align-items: flex-start;">
            <div style="flex: 0 0 250px; border-radius: 8px; overflow: hidden;">
                <img src="{item['image']}" style="width: 100%; height: 180px; object-fit: cover;">
            </div>
            <div style="flex: 1;">
                <h3 style="font-size: 18px; margin-bottom: 8px;">{item['title']}</h3>
                <span class="date" style="display: block; margin-bottom: 10px;">{item['date']}</span>
                <p>{item['desc']}</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <section class="section">
        <div class="section-kicker" style="margin-top: 40px;">Agenda</div>
        <h2 class="section-title" style="font-size:23px;margin-bottom:18px;">AGENDA TERKINI</h2>
        <div class="agenda-wrap">
    """,
        unsafe_allow_html=True,
    )
    for item in AGENDA_TERKINI:
        st.markdown(
            f"""
        <div class="agenda-item">
            <div class="agenda-date-badge">{item['tanggal']}</div>
            <div class="agenda-title">{item['judul']}</div>
            <div class="agenda-desc">{item['desc']}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div></section></div>", unsafe_allow_html=True)

# =========================================================
# GALERI
# =========================================================
elif st.session_state.page == "Galeri Foto & Video":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Dokumentasi</div>
        <h2 class="section-title">Galeri Foto & Video</h2>
        <p class="section-desc">Dokumentasi kegiatan, rapat, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )
    
    st.markdown('<div class="news-grid">', unsafe_allow_html=True)
    gallery_items = [
        ("Rapat Paripurna", "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=600&q=80"),
        ("Kunjungan Kerja", "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=600&q=80"),
        ("Sosialisasi Qanun", "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=600&q=80"),
        ("Penanaman Mangrove", "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=600&q=80"),
    ]
    for title, img in gallery_items:
        st.markdown(
            f"""
        <div class="news-card">
            <div class="news-card-img-wrap">
                <img class="news-card-img" src="{img}" style="height: 220px;">
            </div>
            <div class="news-card-body" style="justify-content: center; align-items: center; text-align: center;">
                <h3 style="margin: 0;">{title}</h3>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown('</div></div>', unsafe_allow_html=True)

# =========================================================
# LAYANAN & PENGADUAN
# =========================================================
elif st.session_state.page == "Layanan & Pengaduan":
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
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit")
            with c2:
                kategori = st.selectbox(
                    "Kategori Pengaduan *",
                    ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"],
                )
            lokasi = st.text_input("Lokasi Kejadian (Opsional)", placeholder="Desa / Kecamatan / lokasi")
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan aspirasi atau laporan secara jelas...")

            submitted = st.form_submit_button("Kirim Aspirasi", type="primary", use_container_width=True)

            if submitted:
                if nama.strip() and isi.strip():
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ Laporan berhasil dicatat. Nomor tiket: ADU-{nomor}")
                    st.info("Simpan nomor tiket untuk keperluan pengecekan tindak lanjut.")
                else:
                    st.error("Mohon lengkapi Nama Lengkap dan Isi Laporan.")

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
# JDIH & TRANSPARANSI
# =========================================================
elif st.session_state.page == "JDIH & Transparansi":
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
# KONTAK
# =========================================================
else:
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
# FOOTER
# =========================================================
st.markdown(
f"""
<div class="footer">
<div class="footer-container">
<div class="footer-grid">

<!-- KOLOM 1 -->
<div class="footer-column">
<div class="footer-brand">
<div class="footer-logo">
    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
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
<a href="#" class="footer-social-item">f</a>
<a href="#" class="footer-social-item">𝕏</a>
<a href="#" class="footer-social-item">▶</a>
<a href="#" class="footer-social-item">◎</a>
</div>
</div>

<!-- KOLOM 2 -->
<div class="footer-column">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=profil">Pimpinan DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=galeri">Galeri</a>
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
© {datetime.now().year} DPRK Aceh Jaya. Seluruh hak cipta dilindungi.
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
