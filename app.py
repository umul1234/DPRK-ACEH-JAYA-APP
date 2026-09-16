import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# 1. Buka sidebar secara default
st.set_page_config(
    page_title="DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded", # Mengaktifkan Sidebar
)

# DATA GLOBAL
news_list = [
    ("📝", "PARIPURNA", "15 September 2026", "Pembahasan Rancangan KUA-PPAS 2027",
     "Rapat paripurna pembahasan kebijakan umum anggaran dan prioritas plafon anggaran sementara."),
    ("📢", "RESES", "10 September 2026", "Penjaringan Aspirasi Masyarakat Melalui Reses",
     "Anggota DPRK turun ke daerah pemilihan untuk menampung aspirasi masyarakat."),
    ("⚖️", "LEGISLASI", "02 September 2026", "RDPU Qanun Ketertiban",
     "Rapat dengar pendapat umum untuk penyempurnaan rancangan Qanun Daerah.")
]

pages = {
    "Beranda": "Beranda",
    "Profil": "Profil & Kelengkapan",
    "Dewan": "Fungsi & Komisi",
    "Berita": "Berita & Rapat",
    "JDIH": "JDIH & Transparansi",
    "Aspirasi": "Layanan & Pengaduan",
    "PORA": "PORA XV 2026",
    "Kontak": "Kontak & Peta"
}

# CSS STYLING (Dioptimalkan untuk Sidebar & Kontras Tombol)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B3C5D;
    --navy2: #08324d;
    --green: #1D7A46;
    --gold: #D9A05B;
    --orange: #E67E22;
    --bg: #F6F8FA;
    --text: #212529;
    --muted: #68737D;
    --line: #E5E9ED;
}

* { font-family: 'Inter', sans-serif; }
.stApp { background: var(--bg) !important; color: var(--text) !important; }

/* Menampilkan & Mewarnai Sidebar Kiri */
[data-testid="stSidebar"] {
    background-color: var(--navy) !important;
    border-right: 1px solid var(--navy2);
}
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Styling Tombol Navigasi di Sidebar (Kontras Tinggi & Jelas) */
[data-testid="stSidebar"] .stButton > button {
    background-color: rgba(255, 255, 255, 0.08) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 10px 15px !important;
    margin-bottom: 4px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: var(--green) !important;
    color: #FFFFFF !important;
    border-color: var(--green) !important;
    transform: translateX(3px);
}

.block-container {
    max-width: 1280px;
    padding: 2rem 2rem 4rem;
}

.gov-strip {
    background: var(--navy);
    color: #fff;
    font-size: 11px;
    padding: 8px 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    display: flex;
    justify-content: space-between;
}

.hero {
    min-height: 280px;
    border-radius: 20px;
    background: linear-gradient(135deg, var(--navy), var(--green));
    display: flex;
    align-items: center;
    padding: 35px;
    color: white;
}
.hero h1 { font-size: 32px; font-weight: 800; margin: 10px 0; }

.service-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 18px;
    min-height: 140px;
    margin-bottom: 10px;
}
.service-icon { font-size: 24px; margin-bottom: 8px; }
.service-title { color: var(--navy); font-weight: 800; font-size: 14px; }
.service-text { color: var(--muted); font-size: 12px; margin-top: 4px; }

.card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
}
.card-title { color: var(--navy); font-weight: 800; font-size: 16px; }

.footer {
    margin-top: 40px;
    background: var(--navy2);
    color: #fff;
    padding: 25px;
    border-radius: 15px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# ============================================================
# SIDEBAR NAVIGATION (Terlihat Jelas)
# ============================================================
with st.sidebar:
    st.markdown("### 🏛️ DPRK ACEH JAYA")
    st.caption("Dewan Perwakilan Rakyat Kabupaten")
    st.markdown("---")
    st.markdown("**MENU UTAMA**")
    
    # Tombol Menu Navigasi Sidebar
    for label, target in pages.items():
        is_active = (st.session_state.page == target)
        btn_label = f"› {label}" if not is_active else f"• {label}"
        if st.button(btn_label, key="side_nav_"+label, use_container_width=True):
            st.session_state.page = target
            st.rerun()

    st.markdown("---")
    st.caption("© 2026 Layanan Digital DPRK")

# ============================================================
# KONTEN UTAMA
# ============================================================
st.markdown("""
<div class="gov-strip">
  <div>PEMERINTAH KABUPATEN ACEH JAYA • INFORMASI PUBLIK</div>
  <div>Portal Resmi DPRK Aceh Jaya</div>
</div>
""", unsafe_allow_html=True)

if st.session_state.page == "Beranda":
    st.markdown("""
    <div class="hero">
      <div>
        <span style="color:#F2D09B; font-size:11px; font-weight:800; letter-spacing:1px;">PORTAL RESMI</span>
        <h1>Informasi, Aspirasi, & Transparansi</h1>
        <p>Akses informasi kelembagaan DPRK, kegiatan dewan, dokumen JDIH, serta layanan pengaduan masyarakat.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:var(--navy); margin-top:25px;'>Layanan Utama</h3>", unsafe_allow_html=True)
    
    services = [
        ("🏛️","Profil DPRK","Informasi kelembagaan & pimpinan.","Profil"),
        ("📜","Fungsi & Komisi","Informasi komisi & tugas legislasi.","Dewan"),
        ("📂","JDIH","Dokumen Qanun & APBK.","JDIH"),
        ("📢","Aspirasi Publik","Layanan pengaduan masyarakat.","Aspirasi"),
        ("📰","Berita & Agenda","Kabar terbaru kegiatan dewan.","Berita"),
        ("🏆","PORA XV 2026","Informasi tuan rumah PORA 2026.","PORA"),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc, target) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="service-card">
              <div class="service-icon">{icon}</div>
              <div class="service-title">{title}</div>
              <div class="service-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Buka Halaman", key="srv_"+target, use_container_width=True):
                st.session_state.page = pages[target]
                st.rerun()

elif st.session_state.page == "Berita & Rapat":
    st.markdown("<h3 style='color:var(--navy);'>Berita & Informasi Terkini</h3>", unsafe_allow_html=True)
    for icon, tag, date, title, desc in news_list:
        st.markdown(f"""
        <div class="card">
          <span style="background:#EAF6EF; color:var(--green); padding:3px 8px; border-radius:10px; font-size:10px; font-weight:700;">{tag}</span>
          <span style="color:#8A949D; font-size:11px; float:right;">{date}</span>
          <div class="card-title" style="margin-top:8px;">{icon} {title}</div>
          <div style="color:var(--muted); font-size:13px; margin-top:5px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown(f"<h3 style='color:var(--navy);'>{st.session_state.page}</h3>", unsafe_allow_html=True)
    st.markdown('<div class="card"><div style="color:var(--muted);">Halaman ini siap diisi dengan informasi detail.</div></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  <b>DPRK ACEH JAYA</b><br>
  Sekretariat DPRK Aceh Jaya • Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya.<br>
  Email: sekretariat@dprk.acehjaya.go.id
</div>
""", unsafe_allow_html=True)
