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
# DATA
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
        "tag": "PARIPURNA",
        "date": "15 September 2026",
        "title": "Pembahasan KUA-PPAS 2027",
        "desc": "Rapat paripurna membahas kebijakan umum anggaran dan prioritas plafon anggaran sementara.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "tag": "RESES",
        "date": "10 September 2026",
        "title": "Penjaringan Aspirasi Masyarakat",
        "desc": "Anggota DPRK melakukan kegiatan penjaringan aspirasi masyarakat dan mendengarkan kebutuhan pembangunan daerah.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=900&q=80",
    },
    {
        "tag": "LEGISLASI",
        "date": "02 September 2026",
        "title": "RDPU Penyempurnaan Qanun",
        "desc": "DPRK mendengarkan masukan akademisi, tokoh masyarakat, dan pemangku kepentingan terhadap rancangan qanun.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=900&q=80",
    },
]

AGENDA = [
    ("18", "SEP", "Rapat Paripurna", "Pembahasan kebijakan dan agenda pembangunan daerah."),
    ("20", "SEP", "Rapat Komisi", "Evaluasi program dan pelaksanaan kegiatan pemerintahan daerah."),
    ("24", "SEP", "Rapat Dengar Pendapat", "Penyerapan aspirasi dan masukan masyarakat."),
]

PIMPINAN = [
    ("Ketua DPRK", "H. Muhammad Yusuf, S.H.", "Memimpin sidang paripurna dan koordinasi alat kelengkapan dewan."),
    ("Wakil Ketua I", "Drs. H. Ahmad Fauzi, M.M.", "Koordinasi bidang legislasi dan anggaran."),
    ("Wakil Ketua II", "Siti Rahmah, S.IP.", "Koordinasi bidang pengawasan dan hubungan masyarakat."),
]

JDIH_DATA = [
    ["1", "Qanun No. 5/2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku"],
    ["2", "Perbup No. 12/2026", "Penjabaran APBK Aceh Jaya 2026", "Berlaku"],
    ["3", "Qanun No. 2/2024", "Perlindungan Korban Bencana Alam", "Berlaku"],
]

/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    background: #eaf4f1;
    color: #4f6963;
    margin-top: 50px;
    padding: 52px 6% 0;
    border-top: 1px solid #d3e3df;
}

.footer-container {
    width: 88%;
    max-width: 1250px;
    margin: 0 auto;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 45px;
    padding-bottom: 42px;
}

.footer-brand {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 18px;
}

.footer-logo {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background: #d7ebe5;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    color: #0c4a3e;
    border: 1px solid #c4ded6;
}

.footer-brand-name {
    color: #0c4a3e;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 800;
    line-height: 1.25;
}

.footer-brand-subtitle {
    color: #78908a;
    font-size: 10px;
    letter-spacing: .8px;
    margin-top: 4px;
}

.footer-column h4 {
    color: #0c4a3e;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 800;
    margin: 4px 0 16px;
}

.footer-column p {
    color: #607771;
    font-size: 11px;
    line-height: 1.8;
    margin: 0 0 7px;
}

.footer-column a {
    display: block;
    color: #607771;
    font-size: 11px;
    line-height: 1.8;
    text-decoration: none;
    margin-bottom: 5px;
    transition: .2s ease;
}

.footer-column a:hover {
    color: #0c6b58;
    padding-left: 4px;
}

.footer-description {
    max-width: 390px;
    color: #607771;
    font-size: 11px;
    line-height: 1.8;
}

.footer-social {
    display: flex;
    gap: 8px;
    margin-top: 17px;
}

.footer-social-item {
    width: 34px;
    height: 34px;
    border: 1px solid #c6dcd6;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0c4a3e;
    background: #f5faf8;
    font-size: 14px;
}

.footer-social-item:hover {
    background: #dceee9;
}

.footer-divider {
    height: 1px;
    background: #cdded9;
}

.footer-bottom {
    min-height: 65px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    color: #78908a;
    font-size: 10px;
}

.footer-bottom-left {
    line-height: 1.6;
}

.footer-bottom-right {
    text-align: right;
}

@media (max-width: 900px) {

    .footer-grid {
        grid-template-columns: 1fr 1fr;
        gap: 35px;
    }

    .footer-bottom {
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        padding: 18px 0;
    }

    .footer-bottom-right {
        text-align: left;
    }
}

@media (max-width: 600px) {

    .footer {
        padding-left: 5%;
        padding-right: 5%;
    }

    .footer-container {
        width: 94%;
    }

    .footer-grid {
        grid-template-columns: 1fr;
        gap: 28px;
    }
}
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# =========================================================
# TOP BAR
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
        <span>Hubungi Kami</span>
        <span>PPID</span>
        <span>ID</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# BRAND
# =========================================================
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

# =========================================================
# NAVIGATION
# =========================================================
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns([1.05, 1.05, 1.15, 1.2, 1.2, 1.05, 0.85])
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
# ALERT
# =========================================================
st.markdown(
    """
<div class="alert">
    <span>📢</span>
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
                <a class="hero-btn" href="#layanan">Sampaikan Aspirasi</a>
                <a class="hero-btn secondary" href="#berita">Lihat Berita</a>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

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
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi, keluhan, dan laporan masyarakat.", "Layanan"),
        ("📜", "JDIH", "Akses produk hukum dan dokumen peraturan daerah.", "JDIH"),
        ("📅", "Agenda DPRK", "Lihat agenda rapat, sidang, dan kegiatan DPRK.", "Berita"),
        ("📊", "Transparansi", "Informasi publik dan dokumen penyelenggaraan pemerintahan.", "JDIH"),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses oleh masyarakat.", "JDIH"),
        ("ℹ️", "Informasi Publik", "Informasi mengenai layanan dan kelembagaan DPRK.", "Kontak"),
    ]

    service_cols = st.columns(6)
    for i, (icon, title, desc, target) in enumerate(services):
        with service_cols[i]:
            st.markdown(
                f"""
            <div class="service-box">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</section></div>", unsafe_allow_html=True)

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
            st.markdown(
                f"""
            <div class="info-item">
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
            <img class="news-main-img" src="{main_news['image']}">
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
                <img class="news-side-img" src="{item['image']}">
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
# PROFIL
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

    st.markdown(
        """
    <div style="background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:28px;margin-bottom:40px;">
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
            initials = "".join([word[0] for word in name.split()[:2]])
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
        <h2 class="section-title">Berita & Agenda DPRK</h2>
        <p class="section-desc">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    for item in NEWS:
        st.markdown(
            f"""
        <div style="background:#fff;border:1px solid #e1e8e5;border-radius:8px;padding:18px;margin-bottom:18px;display:flex;gap:22px;">
            <img src="{item['image']}" style="width:270px;height:165px;object-fit:cover;border-radius:6px;">
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

    st.markdown(
        """
    <div style="margin-top:45px;" class="section-kicker">Agenda</div>
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

    for i, (icon, title, desc) in enumerate(cards):
        with info_cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="text-align:left;">
                <div class="service-icon" style="margin:0 0 13px;">{icon}</div>
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
        <div class="section-kicker">Sekretariat</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#183d35;font-size:21px;">Jam Pelayanan</h3>
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
"""
<div class="footer">

<div class="footer-container">

<div class="footer-grid">

<!-- KOLOM 1 -->
<div class="footer-column">

<div class="footer-brand">

<div class="footer-logo">
🏛️
</div>

<div>
<div class="footer-brand-name">
DPRK ACEH JAYA
</div>

<div class="footer-brand-subtitle">
PORTAL INFORMASI PUBLIK
</div>
</div>

</div>

<p class="footer-description">
Portal resmi Dewan Perwakilan Rakyat Kabupaten Aceh Jaya
yang menyediakan informasi kelembagaan, berita, agenda,
produk hukum, layanan publik, dan aspirasi masyarakat.
</p>

<div class="footer-social">

<div class="footer-social-item">
f
</div>

<div class="footer-social-item">
𝕏
</div>

<div class="footer-social-item">
▶
</div>

<div class="footer-social-item">
◎
</div>

</div>

</div>


<!-- KOLOM 2 -->
<div class="footer-column">

<h4>
Navigasi
</h4>

<a href="#">
Beranda
</a>

<a href="#">
Profil DPRK
</a>

<a href="#">
Pimpinan DPRK
</a>

<a href="#">
Berita & Agenda
</a>

<a href="#">
Komisi
</a>

</div>


<!-- KOLOM 3 -->
<div class="footer-column">

<h4>
Layanan Publik
</h4>

<a href="#">
Pengaduan Masyarakat
</a>

<a href="#">
Informasi Publik
</a>

<a href="#">
JDIH
</a>

<a href="#">
Transparansi
</a>

<a href="#">
Dokumen Publik
</a>

</div>


<!-- KOLOM 4 -->
<div class="footer-column">

<h4>
Hubungi Kami
</h4>

<p>
📍 Jl. Merdeka No. 01
</p>

<p>
Calang, Kabupaten Aceh Jaya
</p>

<p>
📞 (0655) 12345
</p>

<p>
✉️ sekretariat@dprk.acehjaya.go.id
</p>

<p>
🕐 Senin–Jumat, 08.00–16.00 WIB
</p>

</div>

</div>


<div class="footer-divider">
</div>


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
