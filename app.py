import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# DATA GLOBAL
news_list = [
    ("📝", "PARIPURNA", "15 September 2026", "Pembahasan Rancangan KUA-PPAS 2027",
     "Rapat paripurna pembahasan kebijakan umum anggaran dan prioritas plafon anggaran sementara tahun anggaran 2027."),
    ("📢", "RESES", "10 September 2026", "Penjaringan Aspirasi Masyarakat Melalui Reses",
     "Anggota DPRK turun ke daerah pemilihan untuk menampung aspirasi masyarakat terkait infrastruktur dan bantuan banjir."),
    ("⚖️", "LEGISLASI", "02 September 2026", "RDPU Qanun Ketertiban Umum",
     "Rapat dengar pendapat umum untuk penyempurnaan rancangan Qanun Daerah tentang ketertiban umum dan ketenteraman masyarakat.")
]

pages = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Dewan": "Fungsi & Komisi",
    "Berita": "Berita & Agenda",
    "JDIH": "JDIH & Transparansi",
    "Aspirasi": "Layanan & Pengaduan",
    "PORA": "PORA XV 2026",
    "Kontak": "Kontak & Peta"
}

# CSS STYLING (Clean, Organized, Consistent)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B3C5D;
    --navy-light: #164E75;
    --green: #1D7A46;
    --green-light: #EAF6EF;
    --gold: #D9A05B;
    --bg: #F8FAFC;
    --text: #1E293B;
    --muted: #64748B;
    --line: #E2E8F0;
}

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }
.stApp { background: var(--bg) !important; color: var(--text) !important; }

/* Sidebar Elegan & Bersih */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid var(--line) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Tombol Sidebar */
.stButton > button {
    background-color: transparent !important;
    color: var(--text) !important;
    border: 1px solid transparent !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 10px 16px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    transition: all 0.2s ease-in-out !important;
}

.stButton > button:hover {
    background-color: var(--green-light) !important;
    color: var(--green) !important;
}

/* Tombol Aktif */
[data-testid="stSidebar"] .stButton > button[kind="secondary"]:active,
[data-testid="stSidebar"] .stButton > button.active {
    background-color: var(--green-light) !important;
    color: var(--green) !important;
    border-left: 3px solid var(--green) !important;
    font-weight: 600 !important;
}

.block-container {
    max-width: 1200px;
    padding: 2rem 2rem 4rem;
}

/* Header Strip */
.gov-strip {
    background: var(--navy);
    color: #fff;
    font-size: 12px;
    padding: 12px 24px;
    border-radius: 12px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 6px -1px rgba(11, 60, 93, 0.1);
}

/* Hero Section */
.hero {
    min-height: 240px;
    border-radius: 20px;
    background: linear-gradient(135deg, var(--navy) 0%, var(--green) 100%);
    display: flex;
    align-items: center;
    padding: 40px;
    color: white;
    box-shadow: 0 10px 25px rgba(11, 60, 93, 0.15);
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}
.hero h1 { font-size: 34px; font-weight: 800; margin: 12px 0; line-height: 1.2; }
.hero p { font-size: 16px; opacity: 0.9; max-width: 600px; line-height: 1.6; }

/* Service Cards */
.service-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 24px;
    height: 100%;
    transition: all 0.25s ease-in-out;
    cursor: pointer;
}
.service-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.06);
    border-color: var(--green);
}
.service-icon { 
    width: 48px; 
    height: 48px; 
    background: var(--green-light); 
    color: var(--green);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px; 
    margin-bottom: 16px; 
}
.service-title { color: var(--navy); font-weight: 700; font-size: 16px; margin-bottom: 6px; }
.service-text { color: var(--muted); font-size: 13px; line-height: 1.5; }

/* News Cards */
.news-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: all 0.2s ease;
}
.news-card:hover {
    box-shadow: 0 8px 16px rgba(0,0,0,0.04);
}
.news-tag { 
    display: inline-block;
    background: var(--green-light); 
    color: var(--green); 
    padding: 4px 12px; 
    border-radius: 20px; 
    font-size: 11px; 
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    width: fit-content;
    margin-bottom: 12px;
}
.news-date { color: var(--muted); font-size: 12px; font-weight: 500; }
.news-title { color: var(--navy); font-weight: 700; font-size: 17px; margin: 8px 0; line-height: 1.4; }
.news-desc { color: var(--muted); font-size: 13px; line-height: 1.6; flex-grow: 1; }

/* Profile Card */
.profile-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 30px;
    text-align: center;
}
.profile-avatar {
    width: 80px;
    height: 80px;
    background: var(--navy-light);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: 0 auto 16px;
    font-weight: 700;
}

/* Footer */
.footer {
    margin-top: 60px;
    background: var(--navy);
    color: #fff;
    padding: 40px;
    border-radius: 20px;
    font-size: 13px;
    line-height: 1.8;
}
.footer a { color: var(--gold); text-decoration: none; }
.footer a:hover { text-decoration: underline; }

/* Form Styling Override */
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    border-radius: 8px !important;
    border: 1px solid var(--line) !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 2px var(--green-light) !important;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<div style='padding: 10px 0 20px 0;'>", unsafe_allow_html=True)
    st.markdown("## 🏛️ DPRK ACEH JAYA")
    st.caption("Dewan Perwakilan Rakyat Kabupaten")
    st.markdown("---")
    
    for label, target in pages.items():
        is_active = (st.session_state.page == target)
        # Menggunakan class 'active' untuk styling CSS
        btn_class = "active" if is_active else ""
        
        if st.button(f"{label}", key=f"side_nav_{label}", use_container_width=True, type="secondary"):
            st.session_state.page = target
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: var(--muted); font-size: 11px; margin-top: 20px;">
        © 2026 Layanan Digital DPRK<br>
        Kabupaten Aceh Jaya
    </div>
    """, unsafe_allow_html=True)

# KONTEN UTAMA
st.markdown("""
<div class="gov-strip">
  <div style="font-weight: 600;">🏛️ PEMERINTAH KABUPATEN ACEH JAYA</div>
  <div style="opacity: 0.8;">Portal Resmi Transparansi & Aspirasi</div>
</div>
""", unsafe_allow_html=True)

# ================= HALAMAN BERANDA =================
if st.session_state.page == "Beranda":
    st.markdown("""
    <div class="hero">
      <div style="position: relative; z-index: 2;">
        <span style="background: rgba(255,255,255,0.2); color:#fff; padding: 4px 12px; border-radius: 20px; font-size:11px; font-weight:700; letter-spacing:1px;">PORTAL RESMI</span>
        <h1>Informasi, Aspirasi, &<br>Transparansi Publik</h1>
        <p>Akses informasi kelembagaan, agenda rapat, dokumen JDIH, serta layanan pengaduan masyarakat Kabupaten Aceh Jaya dalam satu platform.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:var(--navy); margin-top:40px; margin-bottom: 20px; font-weight: 700;'>Layanan Utama</h3>", unsafe_allow_html=True)
    
    services = [
        ("🏛️", "Profil DPRK", "Informasi kelembagaan, sejarah, dan struktur organisasi.", "Profil"),
        ("📜", "Fungsi & Komisi", "Tugas legislasi, anggaran, dan pengawasan per komisi.", "Dewan"),
        ("📂", "JDIH", "Dokumen Qanun, Peraturan Bupati, dan APBK.", "JDIH"),
        ("📢", "Aspirasi Publik", "Layanan pengaduan dan penjaringan aspirasi masyarakat.", "Aspirasi"),
        ("📰", "Berita & Agenda", "Kabar terbaru kegiatan rapat dan reses anggota.", "Berita"),
        ("🏆", "PORA XV 2026", "Informasi dukungan dan anggaran tuan rumah PORA 2026.", "PORA"),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc, target) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="service-card" onclick="document.getElementById('btn_{target}').click()">
              <div class="service-icon">{icon}</div>
              <div class="service-title">{title}</div>
              <div class="service-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            # Tombol tersembunyi secara visual tapi fungsional untuk routing, 
            # atau kita buat tombol yang rapi di bawahnya.
            if st.button("Akses Layanan →", key=f"btn_{target}", use_container_width=True, type="secondary"):
                st.session_state.page = pages[target]
                st.rerun()

# ================= HALAMAN PROFIL =================
elif st.session_state.page == "Profil & Pimpinan":
    st.markdown("<h2 style='color:var(--navy); font-weight: 700;'>Profil & Pimpinan DPRK</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--muted); margin-bottom: 30px;'>Masa Jabatan 2024 - 2029</p>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    pimpinan = [
        ("Ketua DPRK", "H. Muhammad Yusuf, S.H.", "Komisi A"),
        ("Wakil Ketua I", "Drs. H. Ahmad Fauzi, M.M.", "Komisi B"),
        ("Wakil Ketua II", "Siti Rahmah, S.IP.", "Komisi C")
    ]
    
    for i, (jabatan, nama, komisi) in enumerate(pimpinan):
        with cols[i]:
            st.markdown(f"""
            <div class="profile-card">
                <div class="profile-avatar">{nama.split()[0][0]}</div>
                <div style="font-size: 12px; color: var(--green); font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">{jabatan}</div>
                <div style="font-size: 18px; font-weight: 700; color: var(--navy); margin-bottom: 4px;">{nama}</div>
                <div style="font-size: 13px; color: var(--muted);">{komisi}</div>
            </div>
            """, unsafe_allow_html=True)

# ================= HALAMAN BERITA =================
elif st.session_state.page == "Berita & Agenda":
    st.markdown("<h2 style='color:var(--navy); font-weight: 700;'>Berita & Informasi Terkini</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:var(--muted); margin-bottom: 30px;'>Update terbaru seputar kegiatan dewan dan kebijakan publik.</p>", unsafe_allow_html=True)
    
    # Layout 2 Kolom untuk berita agar lebih rapi
    for i in range(0, len(news_list), 2):
        cols = st.columns(2)
        
        # Item 1
        icon1, tag1, date1, title1, desc1 = news_list[i]
        with cols[0]:
            st.markdown(f"""
            <div class="news-card">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="news-tag">{tag1}</span>
                <span class="news-date">{date1}</span>
              </div>
              <div class="news-title">{icon1} {title1}</div>
              <div class="news-desc">{desc1}</div>
              <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--line);">
                <span style="color: var(--green); font-size: 13px; font-weight: 600; cursor: pointer;">Baca Selengkapnya →</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Item 2 (jika ada)
        if i + 1 < len(news_list):
            icon2, tag2, date2, title2, desc2 = news_list[i+1]
            with cols[1]:
                st.markdown(f"""
                <div class="news-card">
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="news-tag">{tag2}</span>
                    <span class="news-date">{date2}</span>
                  </div>
                  <div class="news-title">{icon2} {title2}</div>
                  <div class="news-desc">{desc2}</div>
                  <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--line);">
                    <span style="color: var(--green); font-size: 13px; font-weight: 600; cursor: pointer;">Baca Selengkapnya →</span>
                  </div>
                </div>
                """, unsafe_allow_html=True)

# ================= HALAMAN ASPIRASI (Dengan Form) =================
elif st.session_state.page == "Layanan & Pengaduan":
    st.markdown("<h2 style='color:var(--navy); font-weight: 700;'>Layanan Aspirasi & Pengaduan</h2>", unsafe_allow_html=True)
    
    # Alert khusus banjir (menyesuaikan konteks user)
    st.markdown("""
    <div style="background: #FEF3C7; border-left: 4px solid #D97706; color: #92400E; padding: 16px; border-radius: 8px; margin-bottom: 24px; font-size: 14px;">
        <strong>⚠️ Layanan Tanggap Darurat Banjir:</strong> Jika Anda melaporkan dampak banjir, silakan pilih kategori "Bantuan Darurat" agar segera diteruskan ke BPBD dan dinas terkait.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("form_aspirasi"):
            st.markdown("##### Formulir Pengaduan Masyarakat")
            nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
            nik = st.text_input("NIK (Opsional)", placeholder="16 digit NIK untuk verifikasi")
            kategori = st.selectbox("Kategori Pengaduan", ["Infrastruktur & Jalan", "Bantuan Banjir", "Pelayanan Publik", "Legislasi & Qanun", "Lainnya"])
            isi = st.text_area("Isi Laporan / Aspirasi", height=150, placeholder="Jelaskan detail laporan atau aspirasi Anda di sini...")
            
            submitted = st.form_submit_button("Kirim Laporan", type="primary", use_container_width=True)
            
            if submitted:
                if nama and isi:
                    st.success("✅ Laporan Anda berhasil dikirim! Nomor tiket: #ADU-2026-089. Kami akan menindaklanjuti dalam 3x24 jam.")
                else:
                    st.error("Mohon lengkapi Nama dan Isi Laporan.")

    with col2:
        st.markdown("""
        <div class="profile-card" style="text-align: left; background: var(--green-light); border-color: var(--green);">
            <h4 style="color: var(--green); margin-top: 0;">📞 Kontak Cepat</h4>
            <p style="font-size: 13px; color: var(--text); margin-bottom: 8px;"><strong>WhatsApp Pengaduan:</strong><br>+62 812-3456-7890</p>
            <p style="font-size: 13px; color: var(--text); margin-bottom: 8px;"><strong>Email:</strong><br>pengaduan@dprk.acehjaya.go.id</p>
            <p style="font-size: 13px; color: var(--text);"><strong>Jam Operasional:</strong><br>Senin - Jumat, 08.00 - 16.00 WIB</p>
        </div>
        """, unsafe_allow_html=True)

# ================= HALAMAN LAINNYA (Placeholder Rapi) =================
else:
    st.markdown(f"<h2 style='color:var(--navy); font-weight: 700;'>{st.session_state.page}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid var(--line); border-radius: 16px; padding: 40px; text-align: center; margin-top: 20px;">
        <div style="font-size: 48px; margin-bottom: 16px;">🚧</div>
        <h3 style="color: var(--navy); margin-bottom: 8px;">Halaman Dalam Pengembangan</h3>
        <p style="color: var(--muted); max-width: 500px; margin: 0 auto;">
            Konten untuk <strong>{st.session_state.page}</strong> sedang dalam proses pembaruan data dan sinkronisasi dengan sistem database internal DPRK Aceh Jaya.
        </p>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px;">
    <div>
      <h4 style="color: #fff; margin-top: 0; margin-bottom: 16px;">DPRK ACEH JAYA</h4>
      <p style="opacity: 0.8; line-height: 1.6;">
        Sekretariat DPRK Aceh Jaya<br>
        Jl. Merdeka No. 01, Calang,<br>
        Kabupaten Aceh Jaya, Aceh 23654
      </p>
    </div>
    <div>
      <h4 style="color: #fff; margin-top: 0; margin-bottom: 16px;">Tautan Cepat</h4>
      <div style="opacity: 0.8; line-height: 2;">
        <a href="#">Portal Pemkab Aceh Jaya</a><br>
        <a href="#">JDIH Nasional</a><br>
        <a href="#">LAPOR! (Pengaduan Nasional)</a>
      </div>
    </div>
    <div>
      <h4 style="color: #fff; margin-top: 0; margin-bottom: 16px;">Hubungi Kami</h4>
      <div style="opacity: 0.8; line-height: 2;">
        📞 (0655) 12345<br>
        ✉️ sekretariat@dprk.acehjaya.go.id
      </div>
    </div>
  </div>
  <div style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 30px; padding-top: 20px; text-align: center; opacity: 0.6; font-size: 12px;">
    © 2026 Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Hak Cipta Dilindungi.
  </div>
</div>
""", unsafe_allow_html=True)
