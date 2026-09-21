import streamlit as st
from datetime import datetime
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Informasi Publik",
    page_icon="https://i.imgur.com/bTNXnLF.png",
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

# WARTA DPRK - Berita Utama (DIKOREKSI: Kabupaten, bukan Kota)
WARTA_DPRK = [
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "date": "Jumat, 14 Agustus 2026",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna Ke-IX Masa Persidangan II Tahun Sidang membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna ke-VIII Masa Persidangan II, Bahas Pertanggungjawaban APBK 2025",
        "date": "Kamis, 30 Juli 2026",
        "desc": "Rapat Paripurna ke-VIII Masa Persidangan II membahas pertanggungjawaban APBK 2025 dan Perubahan Anggaran Kas Daerah Kabupaten Aceh Jaya.",
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
        "desc": "Dalam amanatnya, Yuswardi menekankan pentingnya kedisiplinan dan komitmen dalam menjalankan tugas sebagai ASN di lingkungan Sekretariat DPRK.",
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
        "judul": "Rapat Pleno DPRK Aceh Jaya",
        "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran 2027.",
    },
    {
        "tanggal": "07 September 2026",
        "judul": "Rapat Komisi III DPRK Aceh Jaya",
        "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR.",
    },
    {
        "tanggal": "01 September 2026",
        "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya",
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
# CSS STYLE (DITINGKATKAN: Lebih Modern, Halus, dan Premium)
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #0c4a3e;
    --primary-2: #0f6b58;
    --primary-3: #e9f5f1;
    --gold: #d5a52b;
    --gold-soft: #f7efd4;
    --dark: #0b2e26;
    --text: #1f2d2a;
    --muted: #6b7f7a;
    --bg: #f4f7f6;
    --white: #ffffff;
    --border: #dce6e3;
    --shadow-sm: 0 2px 8px rgba(12, 74, 62, 0.04);
    --shadow: 0 8px 24px rgba(12, 74, 62, 0.08);
    --shadow-lg: 0 16px 40px rgba(12, 74, 62, 0.12);
}

html { scroll-behavior: smooth; }
* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
body, .stApp { background: var(--bg); color: var(--text); }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* Top Bar */
.govbar { 
    background: linear-gradient(90deg, #083b32 0%, #0a4a3f 100%); 
    color: rgba(255,255,255,.85); 
    min-height: 40px; 
    padding: 0 6%; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 12px; 
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.govbar-left, .govbar-right { display: flex; gap: 20px; align-items: center; }
.govbar strong { color: #fff; font-weight: 700; letter-spacing: 0.5px; }
.govbar-right a { color: rgba(255,255,255,.85); text-decoration: none; transition: all .2s ease; }
.govbar-right a:hover { color: var(--gold); }

/* Brand */
.brand-wrap { 
    background: var(--white); 
    border-bottom: 1px solid var(--border); 
    padding: 20px 6%; 
    box-shadow: var(--shadow-sm);
}
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 16px; }
.brand-logo { 
    width: 72px; height: 72px; border-radius: 10px; background: var(--white); 
    display: flex; align-items: center; justify-content: center; 
    box-shadow: 0 4px 12px rgba(12,74,62,.1); overflow: hidden; border: 1px solid var(--border);
}
.brand-logo img { width: 100%; height: 100%; object-fit: contain; padding: 4px; }
.brand-title { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20px; line-height: 1.2; font-weight: 800; text-transform: uppercase; letter-spacing: -0.5px; }
.brand-subtitle { margin-top: 4px; color: var(--muted); font-size: 11px; letter-spacing: 1px; font-weight: 600; }

/* Navigation */
.nav-wrap { 
    background: var(--primary); 
    border-bottom: 3px solid var(--gold); 
    padding: 0 6%; 
    position: sticky; top: 0; z-index: 100;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.nav-inner { min-height: 56px; display: flex; align-items: center; gap: 4px; }
.nav-button .stButton > button, .nav-button-active .stButton > button {
    background: transparent !important; border: none !important; color: rgba(255,255,255,0.85) !important;
    font-size: 13px !important; font-weight: 600 !important; border-radius: 6px 6px 0 0 !important;
    padding: 16px 18px !important; min-height: 56px !important; transition: all .25s ease !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.nav-button .stButton > button:hover { color: #fff !important; background: rgba(255,255,255,0.1) !important; }
.nav-button-active .stButton > button { 
    color: var(--gold) !important; font-weight: 700 !important; 
    background: rgba(255,255,255,0.08) !important; 
    border-bottom: 3px solid var(--gold) !important;
}

/* Running Text */
.running-text-wrap { 
    background: linear-gradient(90deg, var(--gold) 0%, #e0b43a 100%); 
    color: var(--dark); 
    padding: 10px 0; 
    overflow: hidden; 
    white-space: nowrap; 
    border-bottom: 1px solid rgba(0,0,0,0.05);
}
.running-text { display: inline-block; padding-left: 100%; animation: marquee 40s linear infinite; font-size: 13px; font-weight: 600; }
@keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

/* Alert */
.alert { 
    background: #fffdf5; border-bottom: 1px solid #f0dfad; border-left: 4px solid var(--gold); 
    color: #725719; padding: 12px 6%; font-size: 13px; display: flex; align-items: center; gap: 12px; 
}
.alert-badge { 
    width: 22px; height: 22px; border-radius: 50%; background: var(--gold); color: #fff; 
    display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; flex-shrink: 0; 
}

/* Hero */
.hero { 
    position: relative; min-height: 480px; display: flex; align-items: center; overflow: hidden; 
    background: linear-gradient(135deg, rgba(8, 59, 50, 0.96) 0%, rgba(12, 74, 62, 0.88) 50%, rgba(15, 107, 88, 0.75) 100%), 
    url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat; 
}
.hero::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 20% 50%, rgba(213, 165, 43, 0.1) 0%, transparent 50%);
}
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 80px 0; color: white; position: relative; z-index: 2; }
.hero-kicker { 
    display: inline-block; color: var(--gold); font-size: 12px; font-weight: 800; 
    letter-spacing: 2px; margin-bottom: 16px; background: rgba(213, 165, 43, 0.15); 
    padding: 6px 12px; border-radius: 4px; border: 1px solid rgba(213, 165, 43, 0.3);
}
.hero h1 { max-width: 750px; font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(36px, 5vw, 56px); line-height: 1.1; margin: 0 0 24px; font-weight: 800; letter-spacing: -1px; }
.hero p { max-width: 600px; color: rgba(255,255,255,.85); font-size: 17px; line-height: 1.7; margin-bottom: 32px; font-weight: 400; }
.hero-buttons { display: flex; flex-wrap: wrap; gap: 14px; }
.hero-btn { 
    display: inline-flex; align-items: center; gap: 8px; padding: 14px 24px; border-radius: 6px; 
    background: var(--gold); color: var(--dark) !important; text-decoration: none; font-weight: 700; 
    font-size: 14px; transition: all .25s ease; border: 1px solid transparent;
}
.hero-btn:hover { background: #e0b43a; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(213, 165, 43, 0.3); }
.hero-btn.secondary { 
    background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); color: #fff !important; 
    backdrop-filter: blur(4px);
}
.hero-btn.secondary:hover { background: rgba(255,255,255,0.2); border-color: rgba(255,255,255,0.5); }

/* Content */
.content { width: 88%; max-width: 1250px; margin: 0 auto; }
.section { padding: 56px 0; }
.section-head { display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 32px; }
.section-kicker { color: var(--primary-2); font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; }
.section-title { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 800; margin: 0; letter-spacing: -0.5px; }
.section-desc { color: var(--muted); font-size: 14px; line-height: 1.7; margin-top: 8px; max-width: 600px; }

/* Service Box */
.service-box { 
    background: var(--white); border: 1px solid var(--border); min-height: 170px; padding: 28px 20px; 
    text-align: center; transition: all .3s cubic-bezier(0.4, 0, 0.2, 1); border-radius: 10px; 
    position: relative; overflow: hidden;
}
.service-box::before {
    content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 3px; background: var(--primary); transform: scaleX(0); transition: transform .3s ease;
}
a:hover .service-box, .service-box:hover { 
    transform: translateY(-6px); border-color: transparent; box-shadow: var(--shadow-lg); 
}
a:hover .service-box::before, .service-box:hover::before { transform: scaleX(1); }
.service-icon { 
    width: 56px; height: 56px; margin: 0 auto 16px; border-radius: 12px; background: var(--primary-3); 
    color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 26px; 
    transition: all .3s ease;
}
.service-box:hover .service-icon { transform: scale(1.1) rotate(-5deg); background: var(--primary); color: white; }
.service-icon.accent-gold { background: var(--gold-soft); color: #a97e1c; }
.service-box:hover .service-icon.accent-gold { background: var(--gold); color: white; }
.service-icon.accent-blue { background: #e7eef7; color: #2f5f8f; }
.service-box:hover .service-icon.accent-blue { background: #2f5f8f; color: white; }
.service-title { color: var(--dark); font-size: 15px; font-weight: 700; margin-bottom: 8px; font-family: 'Plus Jakarta Sans', sans-serif; }
.service-desc { color: var(--muted); font-size: 12px; line-height: 1.6; }

/* News Grid */
.news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }
.news-card { 
    background: var(--white); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; 
    transition: all .3s ease; height: 100%; display: flex; flex-direction: column; 
}
.news-card:hover { box-shadow: var(--shadow-lg); border-color: transparent; transform: translateY(-4px); }
.news-card-img { width: 100%; height: 190px; object-fit: cover; transition: transform .5s ease; }
.news-card:hover .news-card-img { transform: scale(1.05); }
.news-card-img-wrap { overflow: hidden; position: relative; }
.news-card-img-wrap::after {
    content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 40px; background: linear-gradient(to top, rgba(0,0,0,0.3), transparent);
}
.news-card-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
.news-card h3 { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; line-height: 1.4; margin: 0 0 10px; font-weight: 700; flex: 1; transition: color .2s; }
.news-card:hover h3 { color: var(--primary-2); }
.news-card p { color: var(--muted); font-size: 13px; line-height: 1.6; margin: 0 0 14px; }
.news-date { color: var(--primary-2); font-size: 11px; font-weight: 700; display: flex; align-items: center; gap: 6px; text-transform: uppercase; letter-spacing: 0.5px; }

/* Warta DPRK List */
.warta-list { display: flex; flex-direction: column; gap: 18px; }
.warta-item { 
    background: var(--white); border: 1px solid var(--border); border-radius: 10px; padding: 24px; 
    transition: all .3s ease; display: flex; gap: 24px; align-items: flex-start;
}
.warta-item:hover { box-shadow: var(--shadow); border-color: #b9d6ce; transform: translateX(4px); }
.warta-item-content { flex: 1; }
.warta-item h3 { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; margin: 0 0 10px; font-weight: 700; line-height: 1.4; }
.warta-item .date { color: var(--gold); font-size: 12px; font-weight: 700; margin-bottom: 10px; display: inline-block; background: var(--gold-soft); padding: 4px 10px; border-radius: 4px; }
.warta-item p { color: var(--muted); font-size: 13px; line-height: 1.7; margin: 0; }

/* Agenda */
.agenda-wrap { background: var(--white); border: 1px solid var(--border); border-radius: 10px; padding: 28px; box-shadow: var(--shadow-sm); }
.agenda-item { margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px dashed var(--border); }
.agenda-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.agenda-date-badge { 
    display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: white; 
    padding: 6px 14px; border-radius: 6px; font-size: 11px; font-weight: 700; margin-bottom: 12px; 
    letter-spacing: 0.5px;
}
.agenda-title { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 16px; margin-bottom: 8px; }
.agenda-desc { color: var(--muted); font-size: 13px; line-height: 1.6; }

/* Info Strip */
.info-strip { 
    background: linear-gradient(135deg, var(--primary) 0%, var(--dark) 100%); 
    color: white; padding: 40px 6%; margin: 40px 0;
}
.info-inner { width: 88%; max-width: 1250px; margin: auto; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; }
.info-item { text-align: center; padding: 10px 20px; position: relative; }
.info-item.has-divider::after { content: ''; position: absolute; right: 0; top: 10px; bottom: 10px; width: 1px; background: rgba(255,255,255,.15); }
.info-number { color: var(--gold); font-size: 32px; font-weight: 800; font-family: 'Plus Jakarta Sans', sans-serif; }
.info-label { color: rgba(255,255,255,.7); font-size: 12px; margin-top: 6px; font-weight: 500; letter-spacing: 0.5px; }

/* Profile Card */
.profile-card { 
    background: var(--white); border: 1px solid var(--border); border-radius: 10px; padding: 32px 20px; 
    text-align: center; height: 100%; transition: all .3s ease; position: relative; overflow: hidden;
}
.profile-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); border-color: transparent; }
.profile-photo { 
    width: 96px; height: 96px; border-radius: 50%; margin: auto; display: flex; align-items: center; justify-content: center; 
    background: linear-gradient(145deg, var(--primary-2), var(--primary)); color: #fff; font-size: 32px; font-weight: 800; 
    border: 3px solid var(--white); box-shadow: 0 4px 12px rgba(12,74,62,0.2);
}
.profile-role { color: var(--gold); font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-top: 18px; background: var(--gold-soft); display: inline-block; padding: 4px 10px; border-radius: 4px; }
.profile-name { color: var(--dark); font-size: 17px; font-weight: 800; margin: 12px 0 6px; font-family: 'Plus Jakarta Sans', sans-serif; }
.profile-desc { color: var(--muted); font-size: 12px; line-height: 1.5; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; background: transparent; border-bottom: 2px solid var(--border); }
.stTabs [data-baseweb="tab"] { 
    background: transparent; border-radius: 8px 8px 0 0; padding: 12px 28px; color: var(--muted); 
    font-weight: 600; font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s ease; font-size: 14px;
}
.stTabs [aria-selected="true"] { background: var(--primary-3) !important; color: var(--primary) !important; border-bottom: 2px solid var(--primary); }
.stTabs [data-baseweb="tab"]:hover { background: #f2f7f5 !important; color: var(--primary) !important; }

/* Form Styling Override */
div[data-testid="stForm"] { 
    background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 32px !important; 
    box-shadow: var(--shadow-sm);
}
.stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div { 
    background: #f8faf9 !important; border: 1px solid #d1e0dc !important; border-radius: 8px !important; 
    font-size: 14px !important; color: var(--dark) !important; transition: all .2s !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { 
    border-color: var(--primary) !important; box-shadow: 0 0 0 3px rgba(12, 74, 62, 0.1) !important; 
}
.stButton > button[kind="primary"] { 
    background: var(--primary) !important; border: none !important; color: white !important; 
    border-radius: 8px !important; font-weight: 700 !important; padding: 12px 24px !important;
    transition: all .2s ease !important; font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.stButton > button[kind="primary"]:hover { 
    background: var(--primary-2) !important; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(12, 74, 62, 0.2) !important; 
}

/* Footer */
.footer { 
    background: linear-gradient(180deg, #0d4438 0%, #082722 100%); 
    color: rgba(255,255,255,.7); margin-top: 80px; padding: 64px 6% 0; 
    border-top: 4px solid var(--gold);
}
.footer-container { width: 88%; max-width: 1250px; margin: 0 auto; }
.footer-grid { display: grid; grid-template-columns: 1.8fr 1fr 1fr 1.2fr; gap: 48px; padding-bottom: 48px; }
.footer-column h4 { color: #fff; font-size: 14px; font-weight: 800; margin: 0 0 20px; letter-spacing: 0.5px; font-family: 'Plus Jakarta Sans', sans-serif; }
.footer-column a { display: block; color: rgba(255,255,255,.6); font-size: 13px; line-height: 2.2; text-decoration: none; transition: all .2s ease; }
.footer-column a:hover { color: var(--gold); padding-left: 4px; }
.footer-column p { color: rgba(255,255,255,.6); font-size: 13px; line-height: 1.8; margin: 0 0 10px; }
.footer-brand { display: flex; align-items: center; gap: 14px; margin-bottom: 20px; }
.footer-logo { width: 54px; height: 54px; border-radius: 8px; flex-shrink: 0; background: #fff; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }
.footer-logo img { width: 100%; height: 100%; object-fit: contain; padding: 4px; }
.footer-brand-name { color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 800; letter-spacing: 0.5px; }
.footer-brand-subtitle { color: rgba(255,255,255,.5); font-size: 10px; letter-spacing: 1px; margin-top: 2px; font-weight: 600; }
.footer-description { color: rgba(255,255,255,.5); font-size: 13px; line-height: 1.8; max-width: 320px; margin: 0 0 24px; }
.footer-social { display: flex; gap: 12px; }
.footer-social-item { 
    width: 36px; height: 36px; border-radius: 8px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.1); 
    color: rgba(255,255,255,.8); display: flex; align-items: center; justify-content: center; font-size: 14px; 
    transition: all .2s ease; text-decoration: none; font-weight: 700;
}
.footer-social-item:hover { background: var(--gold); border-color: var(--gold); color: var(--dark); transform: translateY(-2px); }
.footer-divider { border-top: 1px solid rgba(255,255,255,.08); }
.footer-bottom { padding: 24px 0 32px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; color: rgba(255,255,255,.35); font-size: 12px; }

@media (max-width: 900px) {
    .footer-grid { grid-template-columns: 1fr 1fr; row-gap: 40px; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .news-grid { grid-template-columns: 1fr; }
    .warta-item { flex-direction: column; }
    .info-item.has-divider::after { display: none; }
    .hero h1 { font-size: 32px; }
}
@media (max-width: 600px) {
    .footer-grid { grid-template-columns: 1fr; }
    .brand-inner { flex-direction: column; text-align: center; }
    .nav-inner { overflow-x: auto; padding-bottom: 4px; }
    .nav-button .stButton > button, .nav-button-active .stButton > button { white-space: nowrap; }
}
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
        # Clear query param safely
        try:
            del st.query_params["page"]
        except Exception:
            st.query_params.clear()
        st.rerun()

# =========================================================
# TOP BAR & BRAND
# =========================================================
st.markdown(
    """
<div class="govbar">
    <div class="govbar-left">
        <span>🇮🇩 Portal Informasi Pemerintahan Daerah</span>
        <span style="opacity:0.5">|</span>
        <strong>KABUPATEN ACEH JAYA</strong>
    </div>
    <div class="govbar-right">
        <a href="?page=kontak">Hubungi Kami</a>
        <span style="opacity:0.5">|</span>
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
# NAVIGATION
# =========================================================
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns([1.1, 1.2, 1.2, 1.2, 1.3, 1.3, 1.2, 1.0])
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
        🤝 Mari wujudkan transparansi dan akuntabilitas pemerintahan daerah bersama DPRK Aceh Jaya.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="alert">
    <span class="alert-badge">i</span>
    <div>
        <strong>Informasi Publik:</strong> Portal DPRK Aceh Jaya menyediakan akses informasi kelembagaan, produk hukum, agenda persidangan, dan saluran penyampaian aspirasi masyarakat.
    </div>
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
            <p>Akses informasi kegiatan dewan, produk hukum, agenda persidangan, layanan publik, serta sampaikan aspirasi Anda melalui satu portal terpadu yang transparan dan akuntabel.</p>
            <div class="hero-buttons">
                <a class="hero-btn" href="?page=layanan">📢 Sampaikan Aspirasi</a>
                <a class="hero-btn secondary" href="?page=berita">📰 Lihat Berita Terbaru</a>
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
                <div class="section-desc">Akses berbagai layanan dan informasi DPRK Aceh Jaya secara mudah dan terintegrasi.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi, keluhan, dan laporan masyarakat.", "layanan"),
        ("⚖️", "JDIH", "Akses produk hukum dan dokumen peraturan daerah.", "jdih"),
        ("📅", "Agenda DPRK", "Lihat agenda rapat, sidang, dan kegiatan dewan.", "berita"),
        ("📊", "Transparansi", "Informasi publik dan dokumen penyelenggaraan pemerintahan.", "jdih"),
        ("📁", "Dokumen Publik", "Dokumen yang dapat diakses secara terbuka oleh masyarakat.", "jdih"),
        ("🔗", "E-LHKPN", "Pelaporan harta kekayaan penyelenggara negara (KPK).", "https://elhpkpn.kpk.go.id/"),
    ]

    service_cols = st.columns(6)
    icon_accents = ["", "accent-gold", "accent-blue", "", "accent-gold", "accent-blue"]
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
    stats = [("2024–2029", "Masa Jabatan"), ("3", "Pimpinan DPRK"), ("4", "Komisi / AKD"), ("24/7", "Akses Informasi")]
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
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
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
                <div style="flex: 0 0 120px; border-radius: 8px; overflow: hidden; height: 90px; flex-shrink: 0;">
                    <img src="{item['image']}" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="warta-item-content">
                    <h3>{item['title']}</h3>
                    <span class="date">{item['date']}</span>
                    <p>{item['desc']}</p>
                </div>
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
            <div style="font-family:'Plus Jakarta Sans';font-size:18px;font-weight:800;color:var(--dark);margin-bottom:20px;">AGENDA TERKINI</div>
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-item">
                <div class="agenda-date-badge">📅 {item['tanggal']}</div>
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
    <section class="section" style="background: var(--white); border-top: 1px solid var(--border);">
        <div class="content">
            <div class="section-kicker" style="margin-bottom: 15px;">KESEKRETARIATAN</div>
            <div class="warta-list">
    """,
        unsafe_allow_html=True,
    )
    for item in KESEKRETARIATAN:
        st.markdown(
            f"""
        <div class="warta-item" style="padding: 20px;">
            <div class="warta-item-content">
                <h3 style="font-size: 15px;">{item['title']}</h3>
                <span class="date">{item['date']}</span>
                <p>{item['desc']}</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div></section></div>", unsafe_allow_html=True)

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

    tab1, tab2 = st.tabs(["🏛️ Pimpinan dan Anggota DPRK", "👔 Pejabat Sekretariat DPRK"])
    
    with tab1:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; margin-top: 24px;">', unsafe_allow_html=True)
        for nama, jabatan in PIMPINAN_DAN_ANGGOTA:
            st.markdown(
                f"""
            <div class="profile-card">
                <div class="profile-photo">{nama[0]}</div>
                <div class="profile-role">{jabatan}</div>
                <div class="profile-name">{nama}</div>
                <div class="profile-desc">Anggota Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 24px;">', unsafe_allow_html=True)
        for nama, jabatan in PEJABAT_SEKRETARIAT:
            st.markdown(
                f"""
            <div class="profile-card" style="padding: 24px 20px;">
                <div class="profile-role" style="margin-top:0; margin-bottom: 12px;">{jabatan}</div>
                <div class="profile-name" style="font-size: 16px;">{nama}</div>
                <div class="profile-desc">Sekretariat DPRK Aceh Jaya</div>
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
        <div class="warta-item">
            <div style="flex: 0 0 280px; border-radius: 10px; overflow: hidden; height: 180px; flex-shrink: 0;">
                <img src="{item['image']}" style="width: 100%; height: 100%; object-fit: cover; transition: transform .4s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>
            <div class="warta-item-content">
                <h3 style="font-size: 19px;">{item['title']}</h3>
                <span class="date">{item['date']}</span>
                <p style="font-size: 14px; line-height: 1.7;">{item['desc']}</p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <section class="section">
        <div class="section-kicker" style="margin-top: 20px;">Agenda</div>
        <h2 class="section-title" style="font-size:24px;margin-bottom:24px;">AGENDA TERKINI</h2>
        <div class="agenda-wrap">
    """,
        unsafe_allow_html=True,
    )
    for item in AGENDA_TERKINI:
        st.markdown(
            f"""
        <div class="agenda-item">
            <div class="agenda-date-badge">📅 {item['tanggal']}</div>
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
                <h3 style="margin: 0; font-size: 17px;">{title}</h3>
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
        <p class="section-desc">Sampaikan aspirasi, laporan, atau pengaduan kepada DPRK Aceh Jaya secara langsung dan aman.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.8, 1])

    with col1:
        st.markdown(
            """
        <div class="section-kicker">Formulir</div>
        <h3 style="color:var(--dark);font-family:'Plus Jakarta Sans';font-size:22px;margin-bottom:20px;font-weight:700;">Sampaikan Aspirasi Anda</h3>
        """,
            unsafe_allow_html=True,
        )

        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Masukkan nama lengkap Anda")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit NIK")
            with c2:
                kategori = st.selectbox(
                    "Kategori Pengaduan *",
                    ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"],
                )
            lokasi = st.text_input("Lokasi Kejadian (Opsional)", placeholder="Desa / Kecamatan / Lokasi spesifik")
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan aspirasi atau laporan Anda secara rinci dan jelas...")

            submitted = st.form_submit_button("Kirim Aspirasi", type="primary", use_container_width=True)

            if submitted:
                if nama.strip() and isi.strip():
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ **Laporan berhasil dicatat!**\n\nNomor tiket Anda: **ADU-{nomor}**")
                    st.info("💡 Simpan nomor tiket tersebut untuk keperluan pengecekan tindak lanjut.")
                else:
                    st.error("⚠️ Mohon lengkapi **Nama Lengkap** dan **Isi Laporan**.")

    with col2:
        st.markdown(
            """
        <div class="agenda-wrap" style="position: sticky; top: 100px;">
            <div class="section-kicker">Kontak</div>
            <h3 style="color:var(--dark);font-family:'Plus Jakarta Sans';font-size:20px;margin-top:0;font-weight:700;">Hubungi Kami</h3>
            <p style="font-size:13px;color:var(--muted);line-height:1.8;margin-bottom:16px;">
                <strong>📞 Telepon</strong><br>(0655) 12345
            </p>
            <p style="font-size:13px;color:var(--muted);line-height:1.8;margin-bottom:16px;">
                <strong>✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
            </p>
            <p style="font-size:13px;color:var(--muted);line-height:1.8;margin-bottom:16px;">
                <strong>📍 Alamat</strong><br>Jl. Merdeka No. 01, Calang, Aceh Jaya
            </p>
            <hr style="border:none;border-top:1px dashed var(--border);margin:20px 0;">
            <p style="font-size:12px;color:var(--muted);line-height:1.6;">
                <strong>Jam layanan:</strong><br>Senin–Jumat, 08.00–16.00 WIB
            </p>
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
        <p class="section-desc">Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya secara terbuka.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    info_cols = st.columns(4)
    cards = [
        ("⚖️", "Produk Hukum", "Qanun dan dokumen hukum daerah."),
        ("📊", "Transparansi", "Informasi penyelenggaraan pemerintahan."),
        ("📁", "Dokumen Publik", "Dokumen yang dapat diakses masyarakat."),
        ("📑", "Informasi Berkala", "Informasi yang diterbitkan secara berkala."),
    ]

    icon_accents = ["", "accent-gold", "accent-blue", "accent-gold"]
    for i, (icon, title, desc) in enumerate(cards):
        with info_cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="text-align:left; min-height: 150px;">
                <div class="service-icon {icon_accents[i]}" style="margin:0 0 13px;">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:48px;">
        <div class="section-kicker">Database</div>
        <h2 class="section-title" style="font-size:24px;margin-bottom:24px;">Produk Hukum Daerah</h2>
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
            "Tentang": st.column_config.TextColumn("Tentang", width="large"),
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
                <div class="service-desc" style="font-size:13px; font-weight: 500;">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:40px;background:var(--white);border:1px solid var(--border);border-radius:12px;padding:32px;box-shadow:var(--shadow-sm);">
        <div class="section-kicker">Lokasi Kantor</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:var(--dark);font-size:22px;margin-bottom:20px;font-weight:700;">Peta & Lokasi</h3>
        <div style="width:100%;height:350px;border-radius:10px;overflow:hidden;border:1px solid var(--border);">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p style="font-size:13px;color:var(--muted);line-height:1.8;margin-top:20px;">
            <strong>📍 Alamat Lengkap:</strong> Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya, Aceh.
        </p>
        <hr style="border:none;border-top:1px dashed var(--border);margin:24px 0;">
        <div class="section-kicker">Sekretariat</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:var(--dark);font-size:20px;margin-bottom:12px;font-weight:700;">Jam Pelayanan</h3>
        <p style="font-size:13px;color:var(--muted);line-height:1.8;">
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
