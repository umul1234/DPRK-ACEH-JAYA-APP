import streamlit as st
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# GEMINI STYLED CUSTOM CSS
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap');

* {
    font-family: 'Google Sans', sans-serif;
}

/* Background & Main Layout */
.stApp {
    background-color: #131314;
    color: #e3e3e3;
}

/* Hide Default Streamlit Elements */
#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 7rem;
}

/* Sidebar Custom Styling */
[data-testid="stSidebar"] {
    background-color: #1e1f20;
    border-right: 1px solid #2d2f31;
    padding-top: 1rem;
}

[data-testid="stSidebar"] .stRadio label {
    background: transparent !important;
    color: #c4c7c5 !important;
    border-radius: 20px !important;
    padding: 10px 16px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    border: none !important;
    margin-bottom: 4px;
}

[data-testid="stSidebar"] .stRadio input:checked + label {
    background: #004a77 !important;
    color: #c2e7ff !important;
}

/* Gemini Title Gradient */
.gemini-title {
    font-size: 40px;
    font-weight: 500;
    background: linear-gradient(74deg, #4285f4 0%, #9b72cb 9%, #d96570 20%, #d96570 24%, #9b72cb 35%, #4285f4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

.gemini-subtitle {
    font-size: 28px;
    color: #444746;
    font-weight: 500;
    margin-bottom: 30px;
}

/* Prompt Card Suggestions */
.suggestion-card {
    background-color: #1e1f20;
    border-radius: 16px;
    padding: 18px;
    height: 140px;
    border: 1px solid transparent;
    transition: all 0.2s ease;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.suggestion-card:hover {
    background-color: #2a2b2d;
    border-color: #444746;
}

.suggestion-text {
    color: #e3e3e3;
    font-size: 14px;
    line-height: 1.4;
}

.suggestion-icon {
    align-self: flex-end;
    background: #131314;
    border-radius: 50%;
    padding: 8px;
    font-size: 14px;
}

/* Chat Messages */
.stChatMessage {
    background-color: transparent !important;
    border: none !important;
}

[data-testid="stChatMessageContent"] {
    background-color: #1e1f20 !important;
    border-radius: 18px !important;
    padding: 14px 18px !important;
    color: #e3e3e3 !important;
}

/* Floating Input Box Area */
.stChatInput {
    border-radius: 28px !important;
    background-color: #1e1f20 !important;
    border: 1px solid #444746 !important;
}

.stChatInput:focus-within {
    border-color: #a8c7fa !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION (GEMINI MENU STYLE)
# ============================================================
with st.sidebar:
    st.markdown("<h3 style='color: #e3e3e3; padding-left: 10px;'>🏛️ DPRK Jaya</h3>", unsafe_allow_html=True)
    
    menu = st.radio(
        "",
        [
            "✨ Chat Asisten",
            "📰 Berita Terkini",
            "📊 Data & Dokumen",
            "🏆 PORA XV 2026",
            "📞 Kontak Layanan"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
        <div style='padding: 10px; font-size: 12px; color: #8e918f;'>
            Portal Resmi Aspirasi & Informasi<br>
            Sekretariat DPRK Aceh Jaya
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# MENU: CHAT ASISTEN (GEMINI MAIN CLONE)
# ============================================================
if menu == "✨ Chat Asisten":
    
    # State untuk riwayat percakapan
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Jika percakapan masih kosong, tampilkan Landing Page ala Gemini
    if len(st.session_state.messages) == 0:
        st.markdown('<div class="gemini-title">Halo, Masyarakat Aceh Jaya</div>', unsafe_allow_html=True)
        st.markdown('<div class="gemini-subtitle">Ada yang bisa saya bantu tentang DPRK hari ini?</div>', unsafe_allow_html=True)
        
        # Grid Kartu Saran Pertanyaan
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Bagaimana cara menyampaikan aspirasi masyarakat?</div>
                <div class="suggestion-icon">📢</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Lihat agenda rapat dan kegiatan DPRK terdekat</div>
                <div class="suggestion-icon">🗓️</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Informasi kesiapan Aceh Jaya sebagai tuan rumah PORA 2026</div>
                <div class="suggestion-icon">🏆</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown("""
            <div class="suggestion-card">
                <div class="suggestion-text">Unduh dokumen transparansi anggaran & PERDA</div>
                <div class="suggestion-icon">📂</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)

    # Tampilkan percakapan yang sudah ada
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat Input melayang di bawah
    if user_input := st.chat_input("Tanyakan sesuatu seputar DPRK Aceh Jaya..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Respon Asisten (Simulasi)
        bot_response = f"Terima kasih. Terkait **'{user_input}'**, Sekretariat DPRK Aceh Jaya senantiasa terbuka menerima aspirasi dan memberikan informasi publik secara transparan."
        
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()

# ============================================================
# MENU: BERITA TERKINI
# ============================================================
elif menu == "📰 Berita Terkini":
    st.markdown('<div class="gemini-title">Informasi & Berita</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Kabar terbaru kegiatan legislatif</div>', unsafe_allow_html=True)
    
    news_list = [
        ("Pembahasan KUA-PPAS 2027", "15 SEP", "DPRK dan Pemkab Aceh Jaya menggelar rapat paripurna pembahasan prioritas anggaran."),
        ("Musrenbang Kabupaten", "10 SEP", "Penjaringan aspirasi masyarakat untuk perencanaan pembangunan daerah tahun mendatang."),
        ("Sosialisasi PERDA Baru", "01 SEP", "Penyampaian informasi peraturan daerah terbaru terkait tata kelola lingkungan.")
    ]
    
    for title, date, desc in news_list:
        with st.container():
            st.markdown(f"""
            <div style="background:#1e1f20; padding:20px; border-radius:16px; margin-bottom:15px; border:1px solid #2d2f31;">
                <span style="color:#a8c7fa; font-size:12px; font-weight:bold;">{date}</span>
                <h3 style="color:#e3e3e3; margin: 5px 0 10px 0;">{title}</h3>
                <p style="color:#c4c7c5; font-size:14px; margin:0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# MENU: DATA & DOKUMEN
# ============================================================
elif menu == "📊 Data & Dokumen":
    st.markdown('<div class="gemini-title">Dokumen Publik</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Transparansi Informasi Hukum & Anggaran</div>', unsafe_allow_html=True)
    
    docs = [
        "LKPJ Kabupaten Aceh Jaya Tahun 2025",
        "Nota Keuangan APBD Kabupaten Aceh Jaya 2026",
        "Peraturan DPRK Nomor 3 Tahun 2025"
    ]
    
    for doc in docs:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div style="background:#1e1f20; padding:15px; border-radius:12px; margin-bottom:10px;">
                📄 <strong style="color:#e3e3e3;">{doc}</strong>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.button("Unduh PDF", key=doc)

# ============================================================
# MENU: PORA XV 2026
# ============================================================
elif menu == "🏆 PORA XV 2026":
    st.markdown('<div class="gemini-title">PORA XV 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Aceh Jaya Tuan Rumah Pekan Olahraga Rakyat Aceh</div>', unsafe_allow_html=True)
    
    target_date = datetime(2026, 11, 1)
    now = datetime.now()
    delta = target_date - now
    days_left = max(0, delta.days)
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1e1f20, #004a77); padding:30px; border-radius:24px; text-align:center;">
        <h2 style="color:#c2e7ff; margin-bottom:10px;">Hitung Mundur Pelaksanaan</h2>
        <h1 style="font-size:64px; color:#ffffff; margin:0;">{days_left} HARI</h1>
        <p style="color:#e3e3e3; margin-top:10px;">Menuju PORA XV 2026 di Kabupaten Aceh Jaya</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# MENU: KONTAK LAYANAN
# ============================================================
elif menu == "📞 Kontak Layanan":
    st.markdown('<div class="gemini-title">Hubungi Kami</div>', unsafe_allow_html=True)
    st.markdown('<div class="gemini-subtitle">Kantor Sekretariat DPRK Aceh Jaya</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#1e1f20; padding:25px; border-radius:20px; line-height:1.8;">
        <p>📍 <strong>Alamat:</strong> Jl. Merdeka No. 1, Setia, Kabupaten Aceh Jaya, Aceh</p>
        <p>📞 <strong>Telepon:</strong> (0650) 123456</p>
        <p>✉️ <strong>Email:</strong> sekretariat.dprk@acehjaya.go.id</p>
        <p>🕒 <strong>Jam Operasional:</strong> Senin – Jumat | 08.00 – 16.00 WIB</p>
    </div>
    """, unsafe_allow_html=True)
