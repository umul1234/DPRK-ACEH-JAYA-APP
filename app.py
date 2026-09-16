import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DATA GLOBAL
# ============================================================
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

# ============================================================
# CSS STYLING
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
    --navy:#0B3C5D;
    --navy2:#08324d;
    --green:#1D7A46;
    --gold:#D9A05B;
    --orange:#E67E22;
    --bg:#F6F8FA;
    --text:#212529;
    --muted:#68737D;
    --line:#E5E9ED;
}

*{font-family:'Inter',sans-serif}
.stApp{background:var(--bg)!important;color:var(--text)!important}
#MainMenu,footer{visibility:hidden}
header[data-testid="stHeader"]{background:transparent!important}

.block-container{
    max-width:1280px;
    padding:0 1.5rem 4rem;
}

.gov-strip{
    background:var(--navy);
    color:#fff;
    font-size:11px;
    padding:8px 0;
}
.gov-inner{
    max-width:1280px;
    margin:auto;
    padding:0 24px;
    display:flex;
    justify-content:space-between;
    gap:15px;
}
.gov-right{opacity:.85}

.site-header{
    background:#fff;
    border-bottom:1px solid var(--line);
}
.brand-row{
    max-width:1280px;
    margin:auto;
    padding:18px 24px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:25px;
}
.brand{
    display:flex;
    align-items:center;
    gap:13px;
}
.logo{
    width:55px;height:55px;
    border-radius:14px;
    background:linear-gradient(135deg,var(--navy),var(--green));
    display:flex;align-items:center;justify-content:center;
    color:#fff;font-size:28px;
    box-shadow:0 7px 18px rgba(11,60,93,.15);
}
.brand-name{
    color:var(--navy);
    font-weight:800;
    font-size:18px;
    line-height:1.15;
}
.brand-small{
    color:var(--muted);
    font-size:10px;
    margin-top:4px;
    letter-spacing:.3px;
}

.nav-wrap{
    background:#fff;
    border-top:1px solid #F0F2F4;
}
.nav-inner{
    max-width:1280px;
    margin:auto;
    padding:0 24px;
    display:flex;
    align-items:center;
    gap:5px;
}

.nav-inner .stButton{margin:0!important}
.nav-inner .stButton>button{
    background:transparent!important;
    color:#4D5861!important;
    border:0!important;
    border-radius:0!important;
    padding:12px 9px!important;
    font-size:12px!important;
    font-weight:600!important;
}
.nav-inner .stButton>button:hover{
    color:var(--navy)!important;
    background:#F5F8FA!important;
}

.hero{
    margin-top:22px;
    min-height:330px;
    border-radius:24px;
    overflow:hidden;
    position:relative;
    background:
      linear-gradient(90deg,rgba(5,35,54,.95),rgba(11,60,93,.78),rgba(11,60,93,.30)),
      linear-gradient(135deg,var(--navy),var(--green));
    display:flex;
    align-items:center;
    padding:42px;
    box-shadow:0 12px 35px rgba(11,60,93,.14);
}
.hero-content{max-width:650px;color:white}
.hero-kicker{
    color:#F2D09B;
    font-size:11px;
    font-weight:800;
    letter-spacing:1.3px;
    text-transform:uppercase;
}
.hero h1{
    font-size:38px;
    line-height:1.12;
    margin:10px 0;
    font-weight:800;
}
.hero p{
    font-size:14px;
    line-height:1.7;
    color:rgba(255,255,255,.86);
}
.hero-badge{
    display:inline-block;
    margin-top:12px;
    background:var(--orange);
    color:#fff;
    padding:9px 15px;
    border-radius:9px;
    font-size:11px;
    font-weight:800;
}

.section{margin-top:35px}
.section-head{
    display:flex;
    justify-content:space-between;
    align-items:end;
    margin-bottom:15px;
}
.section-title{color:var(--navy);font-size:23px;font-weight:800}
.section-desc{color:var(--muted);font-size:12px}

.service-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:17px;
    padding:19px;
    min-height:150px;
    box-shadow:0 3px 15px rgba(33,37,41,.035);
}
.service-icon{
    width:42px;height:42px;
    border-radius:12px;
    background:#EAF3F8;
    display:flex;align-items:center;justify-content:center;
    font-size:21px;
    margin-bottom:13px;
}
.service-title{color:var(--navy);font-weight:800;font-size:13px}
.service-text{color:var(--muted);font-size:11px;line-height:1.55;margin-top:5px}

.news-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:17px;
    overflow:hidden;
    box-shadow:0 3px 15px rgba(33,37,41,.035);
}
.news-image{
    height:135px;
    background:linear-gradient(135deg,var(--navy),var(--green));
    display:flex;align-items:center;justify-content:center;
    font-size:45px;
}
.news-body{padding:17px}
.tag{
    color:var(--green);
    background:#EAF6EF;
    border-radius:20px;
    padding:5px 9px;
    font-size:9px;
    font-weight:800;
}
.news-date{color:#8A949D;font-size:10px}
.news-title{color:var(--navy);font-weight:800;font-size:14px;line-height:1.4;margin:10px 0 5px}
.news-desc{color:var(--muted);font-size:11px;line-height:1.6}

.card{
    background:white;
    border:1px solid var(--line);
    border-radius:18px;
    padding:22px;
    margin-bottom:15px;
}
.card-title{color:var(--navy);font-weight:800;font-size:16px;margin-bottom:8px}
.card-text{color:#59646D;font-size:13px;line-height:1.7}

.footer{
    margin-top:45px;
    background:var(--navy2);
    color:#fff;
    padding:35px 25px;
    border-radius:22px;
}
.footer-title{font-weight:800;font-size:15px}
.footer-text{color:rgba(255,255,255,.7);font-size:11px;line-height:1.8;margin-top:8px}

@media(max-width:800px){
    .gov-right{display:none}
    .brand-row{padding:15px}
    .nav-inner{overflow-x:auto;padding:0 10px}
    .hero{padding:28px;min-height:290px}
    .hero h1{font-size:28px}
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION & HEADER
# ============================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

st.markdown("""
<div class="gov-strip">
  <div class="gov-inner">
    <div>PEMERINTAH KABUPATEN ACEH JAYA • INFORMASI PUBLIK</div>
    <div class="gov-right">Portal Resmi DPRK Aceh Jaya</div>
  </div>
</div>
<div class="site-header">
  <div class="brand-row">
    <div class="brand">
      <div class="logo">🏛️</div>
      <div>
        <div class="brand-name">DPRK ACEH JAYA</div>
        <div class="brand-small">DEWAN PERWAKILAN RAKYAT KABUPATEN ACEH JAYA</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
cols = st.columns(len(pages))
for col, (label, target) in zip(cols, pages.items()):
    with col:
        if st.button(label, key="nav_"+label, use_container_width=True):
            st.session_state.page = target
            st.rerun()
st.markdown('</div></div>', unsafe_allow_html=True)

# ============================================================
# CONTENT ROUTING
# ============================================================
if st.session_state.page == "Beranda":
    st.markdown("""
    <div class="hero">
      <div class="hero-content">
        <div class="hero-kicker">Portal Resmi DPRK Aceh Jaya</div>
        <h1>Informasi, Aspirasi, dan Transparansi untuk Aceh Jaya</h1>
        <p>
          Akses informasi kelembagaan DPRK, kegiatan dewan, dokumen publik,
          layanan aspirasi masyarakat, serta agenda daerah melalui satu portal.
        </p>
        <div class="hero-badge">Layanan Publik Digital</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
      <div class="section-head">
        <div>
          <div class="section-title">Layanan Utama</div>
          <div class="section-desc">Akses cepat informasi dan layanan DPRK Aceh Jaya</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    services = [
        ("🏛️","Profil DPRK","Informasi kelembagaan, pimpinan, dan alat kelengkapan dewan.","Profil"),
        ("📜","Fungsi & Komisi","Informasi fungsi legislasi, anggaran, pengawasan, dan komisi.","Dewan"),
        ("📂","JDIH","Dokumen Qanun, APBK, perencanaan, dan informasi publik.","JDIH"),
        ("📢","Aspirasi Publik","Sampaikan saran, keluhan, dan aspirasi masyarakat.","Aspirasi"),
        ("📰","Berita & Agenda","Kabar terbaru, rapat paripurna, reses, dan kegiatan DPRK.","Berita"),
        ("🏆","PORA XV 2026","Informasi Aceh Jaya sebagai tuan rumah PORA XV 2026.","PORA"),
    ]

    cols = st.columns(3)
    for i, (icon,title,desc,target) in enumerate(services):
        with cols[i%3]:
            st.markdown(f"""
            <div class="service-card">
              <div class="service-icon">{icon}</div>
              <div class="service-title">{title}</div>
              <div class="service-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Lihat informasi", key="service_"+target, use_container_width=True):
                st.session_state.page = pages[target]
                st.rerun()

    st.markdown("""
    <div class="section">
      <div class="section-head">
        <div>
          <div class="section-title">Berita & Informasi Terkini</div>
          <div class="section-desc">Informasi kegiatan DPRK Aceh Jaya</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for col,(icon,tag,date,title,desc) in zip(cols, news_list):
        with col:
            st.markdown(f"""
            <div class="news-card">
              <div class="news-image">{icon}</div>
              <div class="news-body">
                <span class="tag">{tag}</span>
                <span class="news-date" style="float:right">{date}</span>
                <div class="news-title">{title}</div>
                <div class="news-desc">{desc}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "Profil & Kelengkapan":
    st.markdown('<div class="section"><div class="section-title">Profil DPRK</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div><div class="card-text">Lembaga perwakilan rakyat daerah unsur penyelenggara pemerintahan daerah di Kabupaten Aceh Jaya.</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "Berita & Rapat":
    st.markdown('<div class="section"><div class="section-title">Berita & Agenda</div></div>', unsafe_allow_html=True)
    for icon,tag,date,title,desc in news_list:
        st.markdown(f'<div class="card"><span class="tag">{tag}</span> <span class="news-date">{date}</span><div class="card-title" style="margin-top:10px">{icon} {title}</div><div class="card-text">{desc}</div></div>', unsafe_allow_html=True)

else:
    st.markdown(f'<div class="section"><div class="section-title">{st.session_state.page}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-text">Halaman sedang dalam pembaruan informasi.</div></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  <div class="footer-title">DPRK ACEH JAYA</div>
  <div class="footer-text">
    Sekretariat DPRK Aceh Jaya • Jl. Merdeka No. 01, Calang<br>
    © 2026 DPRK Aceh Jaya. Portal Informasi Publik.
  </div>
</div>
""", unsafe_allow_html=True)
