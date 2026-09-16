from pathlib import Path

code = r'''import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya • Portal Informasi",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# MODERN GOVERNMENT THEME — NAVY / GREEN / GOLD
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B3C5D;
    --navy-dark: #082E47;
    --green: #1D7A46;
    --gold: #D9A05B;
    --orange: #E67E22;
    --bg: #F8F9FA;
    --white: #FFFFFF;
    --text: #212529;
    --muted: #6C757D;
    --border: #E3E7EA;
    --soft-blue: #EAF3F8;
    --soft-green: #EAF6EF;
    --soft-gold: #FBF3E7;
}

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}

#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: rgba(248,249,250,0.92) !important;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

/* ========================= SIDEBAR ========================= */
[data-testid="stSidebar"] {
    background: var(--white) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

[data-testid="stSidebar"] .stRadio label {
    color: #46515A !important;
    border-radius: 12px !important;
    padding: 11px 14px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    margin-bottom: 4px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: var(--soft-blue) !important;
    color: var(--navy) !important;
}

[data-testid="stSidebar"] .stRadio input:checked + label {
    background: var(--navy) !important;
    color: white !important;
    box-shadow: 0 5px 15px rgba(11,60,93,0.18);
}

/* ========================= BRAND ========================= */
.brand-box {
    background: linear-gradient(135deg, var(--navy), #14577F);
    border-radius: 18px;
    padding: 18px;
    color: white;
    margin-bottom: 18px;
    box-shadow: 0 8px 25px rgba(11,60,93,0.16);
}

.brand-icon {
    width: 46px;
    height: 46px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    margin-bottom: 12px;
}

.brand-title {
    font-size: 16px;
    font-weight: 800;
    letter-spacing: .2px;
}

.brand-subtitle {
    font-size: 10px;
    opacity: .78;
    margin-top: 4px;
}

.sidebar-footer {
    padding: 14px;
    background: var(--bg);
    border-radius: 12px;
    color: var(--muted);
    font-size: 10px;
    line-height: 1.6;
}

/* ========================= PAGE HEADER ========================= */
.page-header {
    margin-bottom: 24px;
}

.page-title {
    color: var(--navy);
    font-size: 34px;
    line-height: 1.15;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 6px;
}

.page-subtitle {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.6;
}

/* ========================= HERO ========================= */
.hero {
    background: linear-gradient(135deg, var(--navy) 0%, #14577F 68%, var(--green) 100%);
    border-radius: 24px;
    padding: 34px;
    color: white;
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 35px rgba(11,60,93,0.16);
}

.hero:after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    right: -70px;
    top: -90px;
    border: 35px solid rgba(217,160,91,.16);
}

.hero-kicker {
    color: #F6D49E;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 9px;
}

.hero-text {
    max-width: 720px;
    color: rgba(255,255,255,.84);
    font-size: 14px;
    line-height: 1.7;
}

/* ========================= CARDS ========================= */
.g-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 21px;
    margin-bottom: 15px;
    box-shadow: 0 3px 14px rgba(33,37,41,.035);
    transition: all .2s ease;
}

.g-card:hover {
    transform: translateY(-2px);
    border-color: #C9D6DE;
    box-shadow: 0 8px 24px rgba(33,37,41,.07);
}

.g-card-title {
    color: var(--navy);
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 9px;
}

.g-card-body {
    color: #56616A;
    font-size: 13px;
    line-height: 1.7;
}

/* ========================= METRICS ========================= */
.gemini-metric {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 3px 14px rgba(33,37,41,.035);
}

.gemini-metric-val {
    font-size: 29px;
    font-weight: 800;
    color: var(--navy);
}

.gemini-metric-lbl {
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .7px;
    margin-top: 4px;
}

/* ========================= FEATURE / QUICK MENU ========================= */
.feature-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 19px;
    min-height: 145px;
    box-shadow: 0 3px 14px rgba(33,37,41,.035);
}

.feature-icon {
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 11px;
    background: var(--soft-blue);
    margin-bottom: 13px;
    font-size: 19px;
}

.feature-title {
    color: var(--navy);
    font-weight: 800;
    font-size: 13px;
    margin-bottom: 5px;
}

.feature-text {
    color: var(--muted);
    font-size: 11px;
    line-height: 1.55;
}

/* ========================= NEWS ========================= */
.news-tag {
    display: inline-block;
    background: var(--soft-green);
    color: var(--green);
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: .4px;
}

.news-date {
    color: var(--muted);
    font-size: 11px;
}

.news-title {
    color: var(--navy);
    font-size: 16px;
    font-weight: 800;
    margin: 9px 0 6px;
}

/* ========================= BUTTONS / INPUTS ========================= */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 700 !important;
    border: 1px solid var(--border) !important;
    min-height: 42px !important;
}

.stButton > button[kind="primary"],
button[data-testid="baseButton-primary"] {
    background: var(--orange) !important;
    color: white !important;
    border-color: var(--orange) !important;
}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #D7DEE3 !important;
    background: white !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: var(--navy) !important;
    box-shadow: 0 0 0 1px var(--navy) !important;
}

/* Chat */
.stChatInput > div {
    background: white !important;
    border: 1px solid #CBD5DB !important;
    border-radius: 18px !important;
}

/* ========================= STATUS ========================= */
.status-pill {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 800;
}

.status-green {
    background: var(--soft-green);
    color: var(--green);
}

/* ========================= DIVIDER ========================= */
.section-label {
    color: var(--navy);
    font-size: 16px;
    font-weight: 800;
    margin: 23px 0 12px;
}

/* ========================= MOBILE ========================= */
@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem;
    }

    .page-title {
        font-size: 27px;
    }

    .hero-title {
        font-size: 25px;
    }

    .hero {
        padding: 25px;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
with st.sidebar:
    st.markdown("""
    <div class="brand-box">
        <div class="brand-icon">🏛️</div>
        <div class="brand-title">DPRK ACEH JAYA</div>
        <div class="brand-subtitle">PORTAL INFORMASI & PELAYANAN PUBLIK</div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "",
        [
            "✨ Gemini AI Assistant",
            "🏛️ Profil & Kelengkapan",
            "📜 Fungsi & Komisi Dewan",
            "📰 Berita & Rapat Paripurna",
            "📂 JDIH & Transparansi",
            "🛎️ Layanan & Pengaduan",
            "🏆 Tuan Rumah PORA 2026",
            "📞 Kontak & Peta Lokasi"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-footer">
        <b>Sekretariat DPRK Aceh Jaya</b><br>
        Jl. Merdeka No. 1, Calang, Aceh Jaya<br>
        sekretariat@dprk.acehjaya.go.id
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# 1. GEMINI AI ASSISTANT
# ============================================================
if menu == "✨ Gemini AI Assistant":

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div class="hero">
            <div class="hero-kicker">Portal Informasi DPRK Aceh Jaya</div>
            <div class="hero-title">Halo, Warga Aceh Jaya 👋</div>
            <div class="hero-text">
                Temukan informasi seputar fungsi DPRK, kegiatan dewan, dokumen hukum,
                layanan aspirasi, serta agenda daerah dalam satu portal.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-label">Pertanyaan cepat</div>', unsafe_allow_html=True)

        cols = st.columns(4)
        suggestions = [
            ("📜", "Fungsi utama DPRK", "Apa saja fungsi utama DPRK Aceh Jaya?"),
            ("📢", "Aspirasi publik", "Bagaimana alur penyampaian aspirasi publik?"),
            ("🏆", "PORA XV 2026", "Bagaimana kesiapan Aceh Jaya untuk PORA XV 2026?"),
            ("📂", "Dokumen publik", "Di mana bisa mengunduh dokumen PERDA & APBK?")
        ]

        for col, (icon, title, text) in zip(cols, suggestions):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input(
        "Tanyakan tentang legislasi, pengaduan, anggaran, atau kegiatan dewan..."
    ):
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        response = (
            f"Mengenai **'{user_input}'**, Sekretariat DPRK Aceh Jaya "
            "berkomitmen memberikan pelayanan transparan. Anda dapat mengecek "
            "menu navigasi di samping untuk informasi lebih mendalam atau "
            "mengajukan aduan resmi melalui portal ini."
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()

# ============================================================
# 2. PROFIL & KELENGKAPAN DEWAN
# ============================================================
elif menu == "🏛️ Profil & Kelengkapan":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">Profil & Struktur DPRK</div>
        <div class="page-subtitle">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">🏛️ Tentang DPRK Aceh Jaya</div>
        <div class="g-card-body">
            DPRK Aceh Jaya adalah lembaga perwakilan rakyat daerah yang berkedudukan
            sebagai unsur penyelenggara pemerintahan daerah di Kabupaten Aceh Jaya.
            DPRK memiliki peran strategis dalam menyalurkan aspirasi masyarakat
            serta mengawasi pelaksanaan roda pemerintahan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Unsur Pimpinan DPRK</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    leadership = [
        (c1, "👑", "Ketua DPRK", "Pimpinan Politik & Lembaga"),
        (c2, "🤝", "Wakil Ketua I", "Koor. Bidang Anggaran & Otonomi"),
        (c3, "🤝", "Wakil Ketua II", "Koor. Bidang Pengawasan & Pembangunan")
    ]

    for col, icon, title, desc in leadership:
        with col:
            st.markdown(f"""
            <div class="g-card" style="text-align:center; min-height:125px;">
                <div style="font-size:30px; margin-bottom:8px;">{icon}</div>
                <div style="color:#0B3C5D; font-weight:800;">{title}</div>
                <div style="color:#6C757D; font-size:11px; margin-top:5px;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Alat Kelengkapan Dewan (AKD)</div>', unsafe_allow_html=True)

    akd1, akd2, akd3, akd4 = st.columns(4)
    akd1.markdown('<div class="gemini-metric"><div class="gemini-metric-val">4</div><div class="gemini-metric-lbl">Komisi Tetap</div></div>', unsafe_allow_html=True)
    akd2.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">Badan Anggaran</div></div>', unsafe_allow_html=True)
    akd3.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">BAMUS</div></div>', unsafe_allow_html=True)
    akd4.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">Badan Pembentukan Qanun</div></div>', unsafe_allow_html=True)

# ============================================================
# 3. FUNGSI & KOMISI DEWAN
# ============================================================
elif menu == "📜 Fungsi & Komisi Dewan":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">Fungsi & Komisi Dewan</div>
        <div class="page-subtitle">Tiga fungsi utama dan pembagian bidang kerja komisi</div>
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    functions = [
        (f1, "📝", "Legislasi / Qanun", "Membahas dan menyusun Qanun Daerah bersama Bupati Aceh Jaya untuk kepastian hukum."),
        (f2, "💰", "Penganggaran", "Membahas dan memberikan persetujuan rancangan APBK demi pembangunan daerah yang adil."),
        (f3, "🔍", "Pengawasan", "Mengawasi pelaksanaan Qanun, APBK, serta kebijakan Pemkab Aceh Jaya secara berkala.")
    ]

    for col, icon, title, desc in functions:
        with col:
            st.markdown(f"""
            <div class="g-card" style="min-height:170px;">
                <div class="g-card-title">{icon} {title}</div>
                <div class="g-card-body">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Pembagian Bidang Komisi</div>', unsafe_allow_html=True)

    komisis = [
        ("Komisi A - Pemerintahan & Hukum", "Mencakup Tata Pemerintahan, Kepegawaian, Hukum/Qanun, Pertanahan, dan Ketertiban Umum."),
        ("Komisi B - Perekonomian & Keuangan", "Mencakup Pertanian, Perikanan, Perdagangan, UMKM, Pariwisata, dan Pendapatan Daerah."),
        ("Komisi C - Pembangunan & Infrastruktur", "Mencakup Pekerjaan Umum, Perumahan Rakyat, Perhubungan, Lingkungan Hidup, dan Bencana."),
        ("Komisi D - Kesejahteraan Rakyat", "Mencakup Pendidikan, Kesehatan, Syariat Islam, Sosial, Budaya, dan Olahraga.")
    ]

    for title, desc in komisis:
        st.markdown(f"""
        <div class="g-card">
            <div class="g-card-title">{title}</div>
            <div class="g-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 4. BERITA & RAPAT PARIPURNA
# ============================================================
elif menu == "📰 Berita & Rapat Paripurna":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">Kabar & Agenda Terbaru</div>
        <div class="page-subtitle">Publikasi kegiatan DPRK dan rapat paripurna</div>
    </div>
    """, unsafe_allow_html=True)

    news_data = [
        ("Pembahasan Rancangan KUA-PPAS 2027", "15 September 2026", "PARIPURNA",
         "DPRK Aceh Jaya menggelar Rapat Paripurna pembahasan Kebijakan Umum Anggaran dan Prioritas Plafon Anggaran Sementara bersama Pemerintah Daerah."),
        ("Penjaringan Aspirasi Masyarakat Melalui Reses", "10 September 2026", "RESES",
         "Seluruh anggota DPRK Aceh Jaya turun ke Dapil masing-masing untuk menampung ide dan keluhan warga di tingkat gampong."),
        ("Rapat Dengar Pendapat Umum (RDPU) Qanun Ketertiban", "02 September 2026", "LEGISLASI",
         "DPRK mengundang tokoh masyarakat dan akademisi dalam penyempurnaan rancangan Qanun Daerah.")
    ]

    for title, date, tag, desc in news_data:
        st.markdown(f"""
        <div class="g-card">
            <div style="display:flex; justify-content:space-between; align-items:center; gap:10px;">
                <span class="news-tag">{tag}</span>
                <span class="news-date">{date}</span>
            </div>
            <div class="news-title">{title}</div>
            <div class="g-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 5. JDIH & TRANSPARANSI
# ============================================================
elif menu == "📂 JDIH & Transparansi":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">JDIH & Transparansi</div>
        <div class="page-subtitle">Jaringan Dokumentasi dan Informasi Hukum / Produk Anggaran</div>
    </div>
    """, unsafe_allow_html=True)

    docs = [
        ("Qanun Kabupaten Aceh Jaya tentang APBK 2026", "PDF • 4.8 MB", "Hukum / Anggaran"),
        ("Rencana Kerja (Renja) Sekretariat DPRK 2026", "PDF • 2.1 MB", "Perencanaan"),
        ("Qanun Tata Ruang Wilayah (RTRW) Kabupaten", "PDF • 8.5 MB", "Qanun Daerah"),
        ("Laporan Kinerja Instansi Pemerintah (LKjIP)", "PDF • 3.2 MB", "Akuntabilitas")
    ]

    for doc_title, doc_info, doc_cat in docs:
        c1, c2 = st.columns([5, 1])

        with c1:
            st.markdown(f"""
            <div class="g-card" style="margin-bottom:8px;">
                <div class="g-card-title">📄 {doc_title}</div>
                <div class="g-card-body">{doc_cat} • {doc_info}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            st.button("Unduh", key=doc_title, use_container_width=True)

# ============================================================
# 6. LAYANAN & PENGADUAN
# ============================================================
elif menu == "🛎️ Layanan & Pengaduan":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">Layanan Aspirasi Publik</div>
        <div class="page-subtitle">Sampaikan saran, keluhan, atau permohonan informasi</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="g-card" style="border-left:4px solid #E67E22;">
        <div class="g-card-title">📢 Formulir Pengaduan / Aspirasi Online</div>
        <div class="g-card-body">
            Isi formulir secara lengkap agar aspirasi dapat diterima dan diproses
            oleh Sekretariat DPRK Aceh Jaya.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_pengaduan"):
        col_a, col_b = st.columns(2)

        with col_a:
            nama = st.text_input("Nama Lengkap (Sesuai KTP)")
            nik = st.text_input("NIK / Nomor Identitas")

        with col_b:
            email = st.text_input("Email / Nomor WhatsApp")
            kategori = st.selectbox(
                "Kategori Aspirasi",
                ["Infrastruktur", "Pelayanan Publik", "Kesehatan & Pendidikan", "Ekonomi & UMKM", "Lainnya"]
            )

        subjek = st.text_input("Subjek Pengaduan")
        detail = st.text_area("Detail Aspirasi / Keluhan", height=130)

        submitted = st.form_submit_button(
            "Kirim Aspirasi",
            type="primary",
            use_container_width=True
        )

        if submitted:
            if nama and detail:
                st.success(
                    "✅ Terima kasih. Aspirasi Anda telah diterima oleh Sekretariat DPRK Aceh Jaya untuk ditindaklanjuti."
                )
            else:
                st.error("⚠️ Mohon lengkapi formulir terlebih dahulu.")

# ============================================================
# 7. TUAN RUMAH PORA XV 2026
# ============================================================
elif menu == "🏆 Tuan Rumah PORA 2026":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">PORA XV 2026</div>
        <div class="page-subtitle">Aceh Jaya Tuan Rumah Pekan Olahraga Rakyat Aceh</div>
    </div>
    """, unsafe_allow_html=True)

    target_date = datetime(2026, 11, 1)
    now = datetime.now()
    days_left = max(0, (target_date - now).days)

    st.markdown(f"""
    <div class="hero" style="text-align:center;">
        <div class="hero-kicker">Hitung Mundur Acara</div>
        <div style="font-size:58px; font-weight:800; line-height:1;">{days_left}</div>
        <div style="font-size:14px; margin-top:8px; color:rgba(255,255,255,.82);">
            HARI MENUJU PENYELENGGARAAN PORA XV 2026
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_x, col_y = st.columns(2)

    with col_x:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">🏟️ Dukungan Sarana & Prasarana</div>
            <div class="g-card-body">
                DPRK Aceh Jaya memberikan dukungan penuh dalam pengalokasian anggaran
                pembenahan venue pertandingan, wisma atlet, dan jalur transportasi.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_y:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">🤝 Pengawasan Kesiapan</div>
            <div class="g-card-body">
                Komisi terkait terus memantau progres fisik lapangan dan kesiapan
                Panitia Pelaksana agar ajang berjalan sukses.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 8. KONTAK & PETA LOKASI
# ============================================================
elif menu == "📞 Kontak & Peta Lokasi":

    st.markdown("""
    <div class="page-header">
        <div class="page-title">Lokasi & Kontak</div>
        <div class="page-subtitle">Kantor Sekretariat DPRK Aceh Jaya</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">📍 Sekretariat DPRK Aceh Jaya</div>
        <div class="g-card-body">
            <strong>Alamat:</strong> Jl. Merdeka No. 01, Komplek Perkantoran Pemkab,
            Calang, Kabupaten Aceh Jaya, Provinsi Aceh.<br><br>
            <strong>Jam Pelayanan:</strong> Senin - Jumat | 08.00 - 16.30 WIB<br>
            <strong>Telepon/Fax:</strong> (0654) 221001<br>
            <strong>Email Resmi:</strong> sekretariat@dprk.acehjaya.go.id
        </div>
    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127637.898456!2d95.5!3d4.8!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403b0000000001%3A0x0!2sAceh+Jaya!5e0!3m2!1sid!2sid!4v1600000000000"
        width="100%"
        height="360"
        style="border:0; border-radius:18px;"
        allowfullscreen=""
        loading="lazy">
    </iframe>
    """, height=370)
'''

path = Path("/mnt/data/dprk_aceh_jaya_modern.py")
path.write_text(code, encoding="utf-8")

print(f"File berhasil dibuat: {path}")
