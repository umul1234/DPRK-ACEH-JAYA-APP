from pathlib import Path
import zipfile, textwrap, os

root = Path("/mnt/data/dprk_aceh_jaya_semarang_style")
root.mkdir(exist_ok=True)

app = r'''import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# THEME
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
    --white:#fff;
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

/* top government strip */
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

/* brand/header */
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

/* navigation */
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
.nav-item{
    color:#4D5861;
    font-size:12px;
    font-weight:600;
    padding:13px 11px;
}
.nav-item.active{
    color:var(--navy);
    border-bottom:3px solid var(--green);
}

/* streamlit buttons as nav */
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

/* hero */
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

/* section */
.section{
    margin-top:35px;
}
.section-head{
    display:flex;
    justify-content:space-between;
    align-items:end;
    margin-bottom:15px;
}
.section-title{
    color:var(--navy);
    font-size:23px;
    font-weight:800;
}
.section-desc{
    color:var(--muted);
    font-size:12px;
}

/* service cards */
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

/* news */
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

/* stats */
.stat{
    background:var(--navy);
    color:white;
    border-radius:16px;
    padding:21px;
}
.stat-num{font-size:28px;font-weight:800}
.stat-label{font-size:10px;opacity:.76;margin-top:3px}

/* content cards */
.card{
    background:white;
    border:1px solid var(--line);
    border-radius:18px;
    padding:22px;
    margin-bottom:15px;
}
.card-title{color:var(--navy);font-weight:800;font-size:16px;margin-bottom:8px}
.card-text{color:#59646D;font-size:13px;line-height:1.7}

/* forms */
.stTextInput input,.stTextArea textarea,
.stSelectbox div[data-baseweb="select"]>div{
    background:white!important;
    border:1px solid #D6DDE2!important;
    border-radius:10px!important;
}
.stButton>button{
    border-radius:10px!important;
    font-weight:700!important;
}
button[kind="primary"]{
    background:var(--orange)!important;
    color:white!important;
    border-color:var(--orange)!important;
}

/* footer */
.footer{
    margin-top:45px;
    background:var(--navy2);
    color:#fff;
    padding:35px 25px;
    border-radius:22px;
}
.footer-title{font-weight:800;font-size:15px}
.footer-text{color:rgba(255,255,255,.7);font-size:11px;line-height:1.8;margin-top:8px}

/* mobile */
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
# SESSION
# ============================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

pages = {
    "Beranda":"Beranda",
    "Profil":"Profil & Kelengkapan",
    "Dewan":"Fungsi & Komisi",
    "Berita":"Berita & Rapat",
    "JDIH":"JDIH & Transparansi",
    "Aspirasi":"Layanan & Pengaduan",
    "PORA":"PORA XV 2026",
    "Kontak":"Kontak & Peta"
}

# ============================================================
# HEADER
# ============================================================
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
# BERANDA
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

    news = [
        ("📝","PARIPURNA","15 September 2026","Pembahasan Rancangan KUA-PPAS 2027",
         "Rapat paripurna pembahasan kebijakan umum anggaran dan prioritas plafon anggaran sementara."),
        ("📢","RESES","10 September 2026","Penjaringan Aspirasi Masyarakat Melalui Reses",
         "Anggota DPRK turun ke daerah pemilihan untuk menampung aspirasi masyarakat."),
        ("⚖️","LEGISLASI","02 September 2026","RDPU Qanun Ketertiban",
         "Rapat dengar pendapat umum untuk penyempurnaan rancangan Qanun Daerah.")
    ]

    cols = st.columns(3)
    for col,(icon,tag,date,title,desc) in zip(cols,news):
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

    st.markdown("""
    <div class="section">
      <div class="section-head">
        <div>
          <div class="section-title">Sekilas DPRK Aceh Jaya</div>
          <div class="section-desc">Informasi ringkas kelembagaan</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4=st.columns(4)
    stats=[("4","Komisi Tetap"),("1","Badan Anggaran"),("1","BAMUS"),("1","Badan Pembentukan Qanun")]
    for c,(num,label) in zip([c1,c2,c3,c4],stats):
        with c:
            st.markdown(f'<div class="stat"><div class="stat-num">{num}</div><div class="stat-label">{label}</div></div>',unsafe_allow_html=True)

# ============================================================
# OTHER PAGES
# ============================================================
elif st.session_state.page == "Profil & Kelengkapan":
    st.markdown('<div class="section"><div class="section-title">Profil & Kelengkapan DPRK</div><div class="section-desc">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div></div>',unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="card-title">🏛️ Tentang DPRK Aceh Jaya</div>
      <div class="card-text">
      DPRK Aceh Jaya adalah lembaga perwakilan rakyat daerah yang berkedudukan
      sebagai unsur penyelenggara pemerintahan daerah di Kabupaten Aceh Jaya.
      DPRK memiliki peran dalam menyalurkan aspirasi masyarakat serta mengawasi
      pelaksanaan pemerintahan daerah.
      </div>
    </div>
    """,unsafe_allow_html=True)
    for icon,title,desc in [
        ("👑","Ketua DPRK","Pimpinan lembaga DPRK."),
        ("🤝","Wakil Ketua I","Koordinasi bidang anggaran dan otonomi."),
        ("🤝","Wakil Ketua II","Koordinasi bidang pengawasan dan pembangunan.")
    ]:
        st.markdown(f'<div class="card"><div class="card-title">{icon} {title}</div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)

elif st.session_state.page == "Fungsi & Komisi":
    st.markdown('<div class="section"><div class="section-title">Fungsi & Komisi Dewan</div><div class="section-desc">Tugas pokok dan bidang kerja DPRK</div></div>',unsafe_allow_html=True)
    for icon,title,desc in [
        ("📝","Legislasi / Qanun","Membahas dan menyusun Qanun Daerah bersama Pemerintah Daerah."),
        ("💰","Penganggaran","Membahas dan memberikan persetujuan rancangan APBK."),
        ("🔍","Pengawasan","Mengawasi pelaksanaan Qanun, APBK, dan kebijakan daerah.")
    ]:
        st.markdown(f'<div class="card"><div class="card-title">{icon} {title}</div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)
    for title,desc in [
        ("Komisi A - Pemerintahan & Hukum","Tata pemerintahan, kepegawaian, hukum/Qanun, pertanahan, dan ketertiban umum."),
        ("Komisi B - Perekonomian & Keuangan","Pertanian, perikanan, perdagangan, UMKM, pariwisata, dan pendapatan daerah."),
        ("Komisi C - Pembangunan & Infrastruktur","Pekerjaan umum, perumahan, perhubungan, lingkungan hidup, dan bencana."),
        ("Komisi D - Kesejahteraan Rakyat","Pendidikan, kesehatan, sosial, budaya, syariat Islam, dan olahraga.")
    ]:
        st.markdown(f'<div class="card"><div class="card-title">{title}</div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)

elif st.session_state.page == "Berita & Rapat":
    st.markdown('<div class="section"><div class="section-title">Berita & Rapat Paripurna</div><div class="section-desc">Publikasi kegiatan DPRK Aceh Jaya</div></div>',unsafe_allow_html=True)
    for icon,tag,date,title,desc in news:
        st.markdown(f'<div class="card"><span class="tag">{tag}</span> <span class="news-date">{date}</span><div class="card-title" style="margin-top:10px">{icon} {title}</div><div class="card-text">{desc}</div></div>',unsafe_allow_html=True)

elif st.session_state.page == "JDIH & Transparansi":
    st.markdown('<div class="section"><div class="section-title">JDIH & Transparansi</div><div class="section-desc">Dokumentasi hukum dan informasi publik</div></div>',unsafe_allow_html=True)
    docs=[
        ("Qanun Kabupaten Aceh Jaya tentang APBK 2026","PDF • 4.8 MB","Hukum / Anggaran"),
        ("Rencana Kerja (Renja) Sekretariat DPRK 2026","PDF • 2.1 MB","Perencanaan"),
        ("Qanun Tata Ruang Wilayah Kabupaten","PDF • 8.5 MB","Qanun Daerah"),
        ("Laporan Kinerja Instansi Pemerintah (LKjIP)","PDF • 3.2 MB","Akuntabilitas")
    ]
    for title,info,cat in docs:
        c1,c2=st.columns([5,1])
        with c1:
            st.markdown(f'<div class="card"><div class="card-title">📄 {title}</div><div class="card-text">{cat} • {info}</div></div>',unsafe_allow_html=True)
        with c2:
            st.markdown("<br>",unsafe_allow_html=True)
            st.button("Unduh",key="download_"+title,use_container_width=True)

elif st.session_state.page == "Layanan & Pengaduan":
    st.markdown('<div class="section"><div class="section-title">Layanan Aspirasi Publik</div><div class="section-desc">Sampaikan saran, keluhan, atau permohonan informasi</div></div>',unsafe_allow_html=True)
    with st.form("pengaduan"):
        a,b=st.columns(2)
        with a:
            nama=st.text_input("Nama Lengkap")
            nik=st.text_input("NIK / Nomor Identitas")
        with b:
            kontak=st.text_input("Email / Nomor WhatsApp")
            kategori=st.selectbox("Kategori",["Infrastruktur","Pelayanan Publik","Kesehatan & Pendidikan","Ekonomi & UMKM","Lainnya"])
        subjek=st.text_input("Subjek Pengaduan")
        detail=st.text_area("Detail Aspirasi / Keluhan",height=150)
        submit=st.form_submit_button("Kirim Aspirasi",type="primary",use_container_width=True)
        if submit:
            if nama and detail:
                st.success("Aspirasi Anda telah diterima oleh Sekretariat DPRK Aceh Jaya.")
            else:
                st.error("Mohon lengkapi nama dan detail aspirasi.")

elif st.session_state.page == "PORA XV 2026":
    st.markdown('<div class="section"><div class="section-title">PORA XV 2026</div><div class="section-desc">Aceh Jaya Tuan Rumah Pekan Olahraga Rakyat Aceh</div></div>',unsafe_allow_html=True)
    target=datetime(2026,11,1)
    days=max(0,(target-datetime.now()).days)
    st.markdown(f'<div class="hero" style="justify-content:center;text-align:center"><div class="hero-content"><div class="hero-kicker">Hitung Mundur</div><h1>{days} HARI</h1><p>Menuju penyelenggaraan PORA XV 2026 di Kabupaten Aceh Jaya.</p></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">🏟️ Dukungan Sarana & Prasarana</div><div class="card-text">Dukungan pengalokasian anggaran pembenahan venue pertandingan, wisma atlet, dan jalur transportasi.</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">🤝 Pengawasan Kesiapan</div><div class="card-text">Pemantauan progres fisik lapangan dan kesiapan panitia pelaksana.</div></div>',unsafe_allow_html=True)

elif st.session_state.page == "Kontak & Peta":
    st.markdown('<div class="section"><div class="section-title">Kontak & Peta Lokasi</div><div class="section-desc">Sekretariat DPRK Aceh Jaya</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-title">📍 Sekretariat DPRK Aceh Jaya</div><div class="card-text"><b>Alamat:</b> Jl. Merdeka No. 01, Komplek Perkantoran Pemkab, Calang, Kabupaten Aceh Jaya, Provinsi Aceh.<br><b>Jam:</b> Senin–Jumat, 08.00–16.30 WIB<br><b>Telepon:</b> (0654) 221001<br><b>Email:</b> sekretariat@dprk.acehjaya.go.id</div></div>',unsafe_allow_html=True)
    components.html("""<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127637.898456!2d95.5!3d4.8!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403b0000000001%3A0x0!2sAceh+Jaya!5e0!3m2!1sid!2sid!4v1600000000000" width="100%" height="360" style="border:0;border-radius:18px" allowfullscreen loading="lazy"></iframe>""",height=370)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
  <div class="footer-title">DPRK ACEH JAYA</div>
  <div class="footer-text">
    Sekretariat DPRK Aceh Jaya • Jl. Merdeka No. 01, Komplek Perkantoran Pemkab, Calang<br>
    Email: sekretariat@dprk.acehjaya.go.id • Telepon: (0654) 221001<br><br>
    © 2026 DPRK Aceh Jaya. Portal Informasi dan Pelayanan Publik.
  </div>
</div>
""", unsafe_allow_html=True)
'''

requirements = """streamlit>=1.40,<2.0
"""

readme = """# DPRK Aceh Jaya — Portal Informasi

Portal Streamlit dengan gaya portal pemerintahan modern, terinspirasi pola
informasi/layanan portal pemerintah daerah.

## Menjalankan lokal

```bash
pip install -r requirements.txt
streamlit run app.py
