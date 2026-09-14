import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya • Gemini Portal",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# GEMINI ULTRA DARK THEME (CUSTOM CSS)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto:wght@300;400;500;700&display=swap');

* {
    font-family: 'Google Sans', 'Roboto', sans-serif;
}

/* Base Background & Text */
.stApp {
    background-color: #131314 !important;
    color: #e3e3e3 !important;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 1050px;
    padding-top: 1.5rem;
    padding-bottom: 6rem;
}

/* Sidebar Customisation */
[data-testid="stSidebar"] {
    background-color: #1e1f20 !important;
    border-right: 1px solid #2d2f31 !important;
}

[data-testid="stSidebar"] .stRadio label {
    background: transparent !important;
    color: #c4c7c5 !important;
    border-radius: 28px !important;
    padding: 12px 20px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    margin-bottom: 4px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background-color: #2a2b2d !important;
    color: #e3e3e3 !important;
}

[data-testid="stSidebar"] .stRadio input:checked + label {
    background: #004a77 !important;
    color: #c2e7ff !important;
}

/* Gemini Title Gradient */
.gemini-title {
    font-size: 38px;
    font-weight: 500;
    background: linear-gradient(74deg, #4285f4 0%, #9b72cb 15%, #d96570 30%, #d96570 40%, #9b72cb 60%, #4285f4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
    letter-spacing: -0.5px;
}

.gemini-subtitle {
    font-size: 22px;
    color: #8e918f;
    font-weight: 400;
    margin-bottom: 25px;
}

/* Gemini Card UI */
.g-card {
    background-color: #1e1f20;
    border-radius: 20px;
    padding: 22px;
    border: 1px solid #2d2f31;
    margin-bottom: 16px;
    transition: all 0.25s ease;
}

.g-card:hover {
    background-color: #28292a;
    border-color: #444746;
}

.g-card-title {
    color: #a8c7fa;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.g-card-body {
    color: #c4c7c5;
    font-size: 13.5px;
    line-height: 1.6;
}

/* Quick Prompt Suggestions */
.suggestion-card {
    background-color: #1e1f20;
    border-radius: 16px;
    padding: 16px;
    height: 120px;
    border: 1px solid #2d2f31;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
}

.suggestion-card:hover {
    background-color: #2a2b2d;
    border-color: #5e6063;
}

.suggestion-text {
    color: #e3e3e3;
    font-size: 13px;
    line-height: 1.4;
}

.suggestion-icon {
    align-self: flex-end;
    background: #131314;
    border-radius: 50%;
    padding: 6px 10px;
    font-size: 12px;
}

/* Chat Input Floating Box */
.stChatInput > div {
    border-radius: 28px !important;
    background-color: #1e1f20 !important;
    border: 1px solid #444746 !important;
}

/* Metrics & Stats Gemini Style */
.gemini-metric {
    background: #1e1f20;
    border: 1px solid #2d2f31;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
}

.gemini-metric-val {
    font-size: 32px;
    font-weight: 700;
    color: #a8c7fa;
}

.gemini-metric-lbl {
    font-size: 11px;
    color: #8e918f;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
with st.sidebar:
    st.markdown("""
        <div style='padding: 10px 5px 20px 5px; display: flex; align-items: center; gap: 12px;'>
            <span style='font-size: 28px;'>🏛️</span>
            <div>
                <div style='font-weight: 700; color: #e3e3e3; font-size: 16px;'>DPRK ACEH JAYA</div>
                <div style='font-size: 11px; color: #8e918f;'>Gemini Portal v2.6</div>
            </div>
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
    
    st.markdown("<br><hr style='border-color: #2d2f31;'><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='padding: 0 10px; font-size: 11px; color: #8e918f; line-height: 1.5;'>
             Sekretariat DPRK Aceh Jaya<br>
            Jl. Merdeka No. 1, Calang, Aceh Jaya<br>
            Email: sekretariat@dprk.acehjaya.go.id
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# 1. GEMINI AI ASSISTANT (CHAT INTERFACE)
# ============================================================
if menu == "✨ Gemini AI Assistant":
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if len(st.session_state.messages) == 0:
        st.markdown('<div class="gemini-title">Halo, Warga Aceh Jaya</div>', unsafe_allow_html=True)
        st.markdown('<div class="gemini-subtitle">Apa yang ingin Anda ketahui tentang DPRK hari ini?</div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Apa saja fungsi utama DPRK Aceh Jaya?</div>
                <div class="suggestion-icon">📜</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Bagaimana alur penyampaian aspirasi publik?</div>
                <div class="suggestion-icon">📢</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Bagaimana kesiapan Aceh Jaya untuk PORA XV 2026?</div>
                <div class="suggestion-icon">🏆</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Di mana bisa mengunduh dokumen PERDA & APBK?</div>
                <div class="suggestion-icon">📂</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Tanyakan seputar legislasi, pengaduan, anggaran, atau kegiatan dewan..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Respon Asisten Interaktif
        response = f"Mengenai **'{user_input}'**, Sekretariat DPRK Aceh Jaya berkomitmen memberikan pelayanan transparan. Anda dapat mengecek menu navigasi di samping untuk informasi lebih mendalam atau mengajukan aduan resmi via portal ini."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# ============================================================
# 2. PROFIL & KELENGKAPAN DEWAN
# ============================================================
elif menu == "🏛️ Profil & Kelengkapan":
    st.markdown('<div class="gemini-title">Profil & Struktur DPRK</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">🏛️ Tentang DPRK Aceh Jaya</div>
        <div class="g-card-body">
            DPRK Aceh Jaya adalah lembaga perwakilan rakyat daerah yang berkedudukan sebagai unsur penyelenggara pemerintahan daerah di Kabupaten Aceh Jaya. DPRK memiliki peran strategis dalam menyalurkan aspirasi masyarakat serta mengawasi pelaksanaan roda pemerintahan.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#a8c7fa; margin-top:20px;'>Unsur Pimpinan DPRK</h4>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="g-card" style="text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">👑</div>
            <div style="color:#e3e3e3; font-weight:700;">Ketua DPRK</div>
            <div style="color:#8e918f; font-size:12px; margin-top:4px;">Pimpinan Politik & Lembaga</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="g-card" style="text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">🤝</div>
            <div style="color:#e3e3e3; font-weight:700;">Wakil Ketua I</div>
            <div style="color:#8e918f; font-size:12px; margin-top:4px;">Koor. Bidang Anggaran & Otonomi</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="g-card" style="text-align:center;">
            <div style="font-size:36px; margin-bottom:10px;">🤝</div>
            <div style="color:#e3e3e3; font-weight:700;">Wakil Ketua II</div>
            <div style="color:#8e918f; font-size:12px; margin-top:4px;">Koor. Bidang Pengawasan & Pembangunan</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h4 style='color:#a8c7fa; margin-top:20px;'>Alat Kelengkapan Dewan (AKD)</h4>", unsafe_allow_html=True)
    akd1, akd2, akd3, akd4 = st.columns(4)
    akd1.markdown('<div class="gemini-metric"><div class="gemini-metric-val">4</div><div class="gemini-metric-lbl">Komisi Tetap</div></div>', unsafe_allow_html=True)
    akd2.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">Badan Anggaran</div></div>', unsafe_allow_html=True)
    akd3.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">BAMUS</div></div>', unsafe_allow_html=True)
    akd4.markdown('<div class="gemini-metric"><div class="gemini-metric-val">1</div><div class="gemini-metric-lbl">Badan Pembentukan Qanun</div></div>', unsafe_allow_html=True)

# ============================================================
# 3. FUNGSI & KOMISI DEWAN
# ============================================================
elif menu == "📜 Fungsi & Komisi Dewan":
    st.markdown('<div class="gemini-title">3 Tiga Fungsi Utama</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Tugas Pokok & Bidang Kerja Komisi</div>', unsafe_allow_html=True)
    
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">📝 Legislasi / Qanun</div>
            <div class="g-card-body">Membahas dan menyusun Qanun Daerah bersama Bupati Aceh Jaya untuk kepastian hukum.</div>
        </div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">💰 Penganggaran</div>
            <div class="g-card-body">Membahas dan memberikan persetujuan rancangan APBK demi pembangunan daerah yang adil.</div>
        </div>
        """, unsafe_allow_html=True)
    with f3:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">🔍 Pengawasan</div>
            <div class="g-card-body">Mengawasi pelaksanaan Qanun, APBK, serta kebijakan Pemkab Aceh Jaya secara berkala.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h4 style='color:#a8c7fa; margin-top:20px;'>Pembagian Bidang Komisi</h4>", unsafe_allow_html=True)
    
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
    st.markdown('<div class="gemini-title">Kabar & Agenda Terbaru</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Publikasi Resmi Kegiatan DPRD & DPRK</div>', unsafe_allow_html=True)
    
    news_data = [
        ("Pembahasan Rancangan KUA-PPAS 2027", "15 September 2026", "PARIPURNA", "DPRK Aceh Jaya menggelar Rapat Paripurna pembahasan Kebijakan Umum Anggaran dan Prioritas Plafon Anggaran Sementara bersama Pemerintah Daerah."),
        ("Penjaringan Aspirasi Masyarakat Melalui Reses", "10 September 2026", "RESES", "Seluruh anggota DPRK Aceh Jaya turun ke Dapil masing-masing untuk menampung ide dan keluhan warga di tingkat gampong."),
        ("Rapat Dengar Pendapat Umum (RDPU) Qanun Ketertiban", "02 September 2026", "LEGISLASI", "DPRK mengundang tokoh masyarakat dan akademisi dalam penyempurnaan rancangan Qanun Daerah.")
    ]
    
    for title, date, tag, desc in news_data:
        st.markdown(f"""
        <div class="g-card">
            <div style="display:flex; justify-shadow:space-between; align-items:center; margin-bottom:8px;">
                <span style="background:#004a77; color:#c2e7ff; padding:3px 10px; border-radius:12px; font-size:10px; font-weight:700;">{tag}</span>
                <span style="color:#8e918f; font-size:12px;">{date}</span>
            </div>
            <div style="color:#e3e3e3; font-size:16px; font-weight:700; margin-bottom:6px;">{title}</div>
            <div class="g-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 5. JDIH & TRANSPARANSI DOKUMEN
# ============================================================
elif menu == "📂 JDIH & Transparansi":
    st.markdown('<div class="gemini-title">JDIH & Transparansi</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Jaringan Dokumentasi & Informasi Hukum / Produk Anggaran</div>', unsafe_allow_html=True)
    
    docs = [
        ("Qanun Kabupaten Aceh Jaya tentang APBK 2026", "PDF • 4.8 MB", "Hukum / Anggaran"),
        ("Rencana Kerja (Renja) Sekretariat DPRK 2026", "PDF • 2.1 MB", "Perencanaan"),
        ("Qanun Tata Ruang Wilayah (RTRW) Kabupaten", "PDF • 8.5 MB", "Qanun Daerah"),
        ("Laporan Kinerja Instansi Pemerintah (LKjIP)", "PDF • 3.2 MB", "Akuntabilitas")
    ]
    
    for doc_title, doc_info, doc_cat in docs:
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"""
            <div class="g-card" style="margin-bottom:0px; padding:15px;">
                <div style="color:#e3e3e3; font-weight:500;">📄 {doc_title}</div>
                <div style="color:#8e918f; font-size:11px; margin-top:4px;">{doc_cat} • {doc_info}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("<div style='height:4px;'></div>", unsafe_allow_html=True)
            st.button("Unduh", key=doc_title, use_container_width=True)
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ============================================================
# 6. LAYANAN & PENGADUAN
# ============================================================
elif menu == "🛎️ Layanan & Pengaduan":
    st.markdown('<div class="gemini-title">Layanan Aspirasi Publik</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Sampaikan saran, keluhan, atau permohonan informasi</div>', unsafe_allow_html=True)
    
    with st.form("form_pengaduan"):
        st.markdown("<h4 style='color:#a8c7fa; margin-top:0;'>Formulir Pengaduan / Aspirasi Online</h4>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            nama = st.text_input("Nama Lengkap (Sesuai KTP)")
            nik = st.text_input("NIK / Nomor Identitas")
        with col_b:
            email = st.text_input("Email / Nomor WhatsApp")
            kategori = st.selectbox("Kategori Aspirasi", ["Infrastruktur", "Pelayanan Publik", "Kesehatan & Pendidikan", "Ekonomi & UMKM", "Lainnya"])
            
        subjek = st.text_input("Subjek Pengaduan")
        detail = st.text_area("Detail Aspirasi / Keluhan", height=120)
        
        submitted = st.form_submit_button("Kirim Aspirasi", type="primary", use_container_width=True)
        
        if submitted:
            if nama and detail:
                st.success("✅ Terima kasih. Aspirasi Anda telah diterima oleh Sekretariat DPRK Aceh Jaya untuk ditindaklanjuti.")
            else:
                st.error("⚠️ Mohon lengkapi formulir terlebih dahulu.")

# ============================================================
# 7. TUAN RUMAH PORA XV 2026
# ============================================================
elif menu == "🏆 Tuan Rumah PORA 2026":
    st.markdown('<div class="gemini-title">PORA XV 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Aceh Jaya Tuan Rumah Pekan Olahraga Rakyat Aceh</div>', unsafe_allow_html=True)
    
    target_date = datetime(2026, 11, 1)
    now = datetime.now()
    days_left = max(0, (target_date - now).days)
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #004a77, #1e1f20); padding:30px; border-radius:24px; text-align:center; border:1px solid #4285f4; margin-bottom:20px;">
        <div style="color:#c2e7ff; font-size:12px; font-weight:700; letter-spacing:1px; margin-bottom:10px;">HITUNG MUNDUR ACARA</div>
        <div style="font-size:56px; font-weight:700; color:#ffffff; line-height:1;">{days_left} HARI</div>
        <div style="color:#e3e3e3; font-size:14px; margin-top:10px;">Menuju Penyelenggaraan PORA XV 2026 di Kabupaten Aceh Jaya</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">🏟️ Dukungan Sarana & Prasarana</div>
            <div class="g-card-body">DPRK Aceh Jaya memberikan dukungan penuh dalam pengalokasian anggaran pembenahan venue pertandingan, wisma atlet, dan jalur transportasi.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_y:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-title">🤝 Pengawasan Kesiapan</div>
            <div class="g-card-body">Komisi terkait terus memantau progres fisik lapangan dan kesiapan Panitia Pelaksana agar ajang berjalan sukses.</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 8. KONTAK & PETA LOKASI
# ============================================================
elif menu == "📞 Kontak & Peta Lokasi":
    st.markdown('<div class="gemini-title">Lokasi & Kontak</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Kantor Sekretariat DPRK Aceh Jaya</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">📍 Sekretariat DPRK Aceh Jaya</div>
        <div class="g-card-body">
            <strong>Alamat:</strong> Jl. Merdeka No. 01, Komplek Perkantoran Pemkab, Calang, Kabupaten Aceh Jaya, Provinsi Aceh.<br>
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
        height="320"
        style="border:0; border-radius:20px;"
        allowfullscreen=""
        loading="lazy">
    </iframe>
    """, height=330)
