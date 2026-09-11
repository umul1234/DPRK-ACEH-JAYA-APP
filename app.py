import streamlit as st
import streamlit.components.v1 as components

# ==========================================================================================
# 1. KONFIGURASI HALAMAN
# ==========================================================================================
st.set_page_config(
    page_title="Sekretariat DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================================================
# 2. CUSTOM CSS SUPER PREMIUM
# ==========================================================================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        * { font-family: 'Plus Jakarta Sans', sans-serif; }
        
        /* Hide default Streamlit elements for a cleaner look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Premium Card Styling */
        .premium-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(226, 232, 240, 0.8);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .premium-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.1);
            border-color: #059669;
        }
        
        /* Hero Section */
        .hero-banner {
            background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #10b981 100%);
            border-radius: 24px;
            padding: 60px 40px;
            color: white;
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(4, 120, 87, 0.4);
        }
        .hero-banner::after {
            content: "🏛️";
            position: absolute;
            right: 40px;
            bottom: -20px;
            font-size: 180px;
            opacity: 0.08;
            transform: rotate(-15deg);
        }
        
        /* Premium Navigation Pills */
        .stRadio > div {
            background: #f1f5f9;
            padding: 6px;
            border-radius: 14px;
            display: flex;
            gap: 4px;
            border: 1px solid #e2e8f0;
        }
        .stRadio label {
            background: transparent;
            border-radius: 10px;
            padding: 10px 18px;
            font-weight: 600;
            font-size: 14px;
            color: #475569;
            transition: all 0.25s ease;
            margin: 0;
            border: none;
        }
        .stRadio input:checked + label {
            background: #059669 !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
            animation: fadeInUp 0.8s ease-out forwards;
        }
        
        /* Custom Metrics */
        .metric-value { font-size: 32px; font-weight: 800; color: #059669; margin: 8px 0; }
        .metric-label { font-size: 13px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
        
        /* Badge */
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .badge-new { background: #fef3c7; color: #92400e; }
        .badge-info { background: #dbeafe; color: #1e40af; }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# 3. HEADER & WEATHER WIDGET
# ==========================================================================================
col_logo, col_spacer, col_weather = st.columns([4, 1, 2])

with col_logo:
    st.markdown('<h1 style="font-size: 28px; font-weight: 800; color: #064e3b; margin: 0;">Sekretariat DPRK</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 15px; font-weight: 500; color: #64748b; margin-top: 4px;">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</p>', unsafe_allow_html=True)

with col_weather:
    st.markdown("""
        <div style="background: rgba(255,255,255,0.9); padding: 12px 20px; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 15px; border: 1px solid #e2e8f0;">
            <div style="font-size: 28px;">⛅</div>
            <div>
                <div style="font-size: 13px; color: #64748b; font-weight: 600;">Aceh Jaya, Aceh</div>
                <div style="font-size: 22px; font-weight: 800; color: #0f172a; line-height: 1;">26°C</div>
                <div style="font-size: 11px; color: #059669; font-weight: 600;">Cerah Berawan • BMKG</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ==========================================================================================
# 4. NAVIGASI PREMIUM
# ==========================================================================================
menu_items = [
    "🏠 BERANDA", "🏛️ PROFIL", "📰 INFORMASI", "📸 GALERI",
    "🛎️ LAYANAN", "📂 INFO PUBLIK", "📞 KONTAK", "🏆 PORA 2026"
]

selected_menu = st.radio("", menu_items, horizontal=True, label_visibility="collapsed")

st.markdown(
    '<div style="text-align: center; font-size: 14px; color: #64748b; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; padding: 12px 0; margin: 20px 0; font-style: italic; font-weight: 500;">Mewujudkan Kabupaten Aceh Jaya yang Transparan, Aspiratif, dan Sejahtera</div>',
    unsafe_allow_html=True
)

# ==========================================================================================
# 5. KONTEN DINAMIS BERDASARKAN MENU
# ==========================================================================================

if selected_menu == "🏠 BERANDA":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    
    # Hero Banner
    st.markdown("""
        <div class="hero-banner">
            <h2 style="font-size: 36px; font-weight: 800; margin-bottom: 16px;">Selamat Datang di Portal Resmi</h2>
            <p style="font-size: 18px; opacity: 0.9; max-width: 600px; line-height: 1.6;">
                Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. 
                Mitra strategis pemerintah dalam mewujudkan tata kelola pemerintahan yang baik dan pelayanan publik yang prima.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        {"value": "15+", "label": "Perda Disusun", "icon": "📜"},
        {"value": "250+", "label": "Aspirasi Masyarakat", "icon": "🗣️"},
        {"value": "4", "label": "Komisi Aktif", "icon": "🏛️"},
        {"value": "98%", "label": "Indeks Kepuasan", "icon": "⭐"}
    ]
    
    for i, col in enumerate([col1, col2, col3, col4]):
        with col:
            st.markdown(f"""
                <div class="premium-card metric-card">
                    <div style="font-size: 28px; margin-bottom: 8px;">{metrics[i]['icon']}</div>
                    <div class="metric-value">{metrics[i]['value']}</div>
                    <div class="metric-label">{metrics[i]['label']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "🏛️ PROFIL":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Profil DPRK Aceh Jaya")
    st.markdown("Lembaga legislatif yang bertugas dalam penyusunan peraturan daerah, pengawasan pelaksanaan pemerintahan daerah, dan penyampaian aspirasi masyarakat Kabupaten Aceh Jaya.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="premium-card">
                <h3 style="color: #064e3b; margin-top: 0;">🎯 Visi</h3>
                <p>Terwujudnya DPRK Aceh Jaya yang profesional, aspiratif, dan berintegritas dalam mendukung pembangunan daerah yang berkeadilan.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="premium-card">
                <h3 style="color: #064e3b; margin-top: 0;">🚀 Misi</h3>
                <ul style="color: #475569; line-height: 1.8;">
                    <li>Meningkatkan kualitas penyusunan Peraturan Daerah.</li>
                    <li>Memperkuat fungsi pengawasan terhadap eksekutif.</li>
                    <li>Memfasilitasi aspirasi masyarakat secara transparan.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.subheader("Struktur Organisasi")
    st.info("👑 **Ketua DPRK** | 👑 **Wakil Ketua** | 📁 **Sekretariat** | 🏛️ **4 Komisi**", icon="ℹ️")
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "📰 INFORMASI":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Agenda & Informasi Terkini")
    
    news_items = [
        {"date": "15 Sep 2026", "tag": "RAPAT PARIPURNA", "title": "Rapat Paripurna Pembahasan KUA-PPAS Tahun 2027", "desc": "Pembahasan bersama antara DPRK dan Pemkab Aceh Jaya terkait prioritas anggaran."},
        {"date": "10 Sep 2026", "tag": "MUSRENBANG", "title": "Pelaksanaan Musyawarah Rencana Pembangunan Daerah", "desc": "Penjaringan aspirasi masyarakat untuk rencana pembangunan tahun depan."},
        {"date": "01 Sep 2026", "tag": "SOSIALISASI", "title": "Sosialisasi Peraturan Daerah Baru kepada Masyarakat", "desc": "Kunjungan reses anggota dewan ke kecamatan-kecamatan di Aceh Jaya."}
    ]
    
    for news in news_items:
        st.markdown(f"""
            <div class="premium-card" style="margin-bottom: 16px; display: flex; gap: 20px; align-items: start;">
                <div style="min-width: 80px; text-align: center; background: #f0fdf4; padding: 10px; border-radius: 12px; border: 1px solid #bbf7d0;">
                    <div style="font-size: 12px; font-weight: 700; color: #059669;">{news['date'].split()[0]}</div>
                    <div style="font-size: 18px; font-weight: 800; color: #064e3b;">{news['date'].split()[1]}</div>
                </div>
                <div>
                    <span class="badge badge-info">{news['tag']}</span>
                    <h3 style="margin: 8px 0 4px 0; color: #0f172a; font-size: 18px;">{news['title']}</h3>
                    <p style="color: #64748b; font-size: 14px; margin: 0;">{news['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "📸 GALERI":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Galeri Kegiatan DPRK")
    st.markdown("Dokumentasi visual dari berbagai aktivitas legislatif dan kemasyarakatan.")
    
    col1, col2, col3 = st.columns(3)
    images = [
        ("https://images.unsplash.com/photo-1541872703-74c5963631df?auto=format&fit=crop&w=600&q=80", "Rapat Koordinasi Komisi"),
        ("https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=600&q=80", "Kunjungan Kerja ke Kecamatan"),
        ("https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=600&q=80", "Musyawarah Perencanaan Pembangunan")
    ]
    
    for col, (url, caption) in zip([col1, col2, col3], images):
        with col:
            st.image(url, use_column_width=True, caption=caption)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "🛎️ LAYANAN":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Layanan Publik")
    st.markdown("Kami menyediakan berbagai layanan untuk memudahkan masyarakat berinteraksi dengan DPRK Aceh Jaya.")
    
    col1, col2 = st.columns(2)
    services = [
        {"icon": "📢", "title": "Pengaduan Masyarakat", "desc": "Sampaikan aspirasi, keluhan, atau saran Anda secara langsung dan transparan."},
        {"icon": "📄", "title": "Permohonan Data Informasi", "desc": "Ajukan permohonan akses informasi publik sesuai dengan ketentuan yang berlaku."},
        {"icon": "🗓️", "title": "Jadwal Reses Anggota", "desc": "Lihat jadwal pertemuan anggota dewan dengan konstituen di daerah pemilihan."},
        {"icon": "⚖️", "title": "Layanan Persidangan", "desc": "Informasi terkait agenda rapat dengar pendapat dan paripurna yang terbuka untuk umum."}
    ]
    
    for i, col in enumerate([col1, col2]):
        with col:
            st.markdown(f"""
                <div class="premium-card" style="cursor: pointer; text-align: center; height: 100%;">
                    <div style="font-size: 40px; margin-bottom: 15px;">{services[i]['icon']}</div>
                    <h3 style="margin: 0 0 10px 0; color: #0f172a; font-size: 18px;">{services[i]['title']}</h3>
                    <p style="color: #64748b; font-size: 14px; margin: 0; line-height: 1.6;">{services[i]['desc']}</p>
                    <button style="margin-top: 15px; background: #059669; color: white; border: none; padding: 8px 20px; border-radius: 8px; font-weight: 600; cursor: pointer;">Akses Layanan</button>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "📂 INFO PUBLIK":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Informasi & Dokumen Publik")
    st.markdown("Transparansi adalah kunci. Unduh dokumen resmi DPRK Aceh Jaya di bawah ini.")
    
    docs = [
        ("Laporan Keterangan Pertanggungjawaban (LKPJ) 2025", "PDF", "2.4 MB"),
        ("Nota Keuangan APBD Kabupaten Aceh Jaya 2026", "PDF", "5.1 MB"),
        ("Peraturan DPRK Nomor 3 Tahun 2025", "PDF", "1.2 MB"),
        ("Laporan Tahunan Sekretariat DPRK 2025", "PDF", "3.8 MB")
    ]
    
    for doc_name, doc_type, size in docs:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown(f"**{doc_name}**")
        with col2:
            st.markdown(f"<span class='badge badge-new'>{doc_type}</span>", unsafe_allow_html=True)
        with col3:
            st.download_button(
                label=f"📥 Unduh ({size})",
                data=f"Mock data untuk {doc_name}",
                file_name=f"{doc_name.replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        st.markdown("<hr style='margin: 10px 0; border-color: #e2e8f0;'>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "📞 KONTAK":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Hubungi Kami")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
            <div class="premium-card" style="height: 100%;">
                <h3 style="color: #064e3b; margin-top: 0;">Informasi Kontak</h3>
                <p style="color: #475569; line-height: 1.8;">
                    📍 <strong>Alamat:</strong><br>
                    Jl. Merdeka No.1, Kecamatan Setia,<br>Kabupaten Aceh Jaya, Aceh<br><br>
                    📞 <strong>Telepon:</strong> (0650) 123456<br>
                    ✉️ <strong>Email:</strong> sekretariat.dprk@acehjaya.go.id<br>
                    🕒 <strong>Jam Operasional:</strong><br>
                    Senin - Jumat: 08.00 - 16.00 WIB
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### Kirim Pesan")
        with st.form("contact_form"):
            c1, c2 = st.columns(2)
            with c1: nama = st.text_input("Nama Lengkap")
            with c2: email = st.text_input("Alamat Email")
            pesan = st.text_area("Pesan atau Aspirasi Anda", height=120)
            submitted = st.form_submit_button("Kirim Pesan", use_container_width=True, type="primary")
            
            if submitted:
                if nama and email and pesan:
                    st.success("✅ Pesan Anda berhasil dikirim! Kami akan segera menindaklanjutinya.")
                else:
                    st.error("⚠️ Mohon lengkapi semua bidang.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    # Embedded Map Placeholder
    st.components.v1.html(
        '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127637.898456!2d95.5!3d4.8!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403b0000000001%3A0x0!2sAceh+Jaya!5e0!3m2!1sid!2sid!4v1600000000000" width="100%" height="300" style="border:0; border-radius: 16px;" allowfullscreen="" loading="lazy"></iframe>',
        height=300
    )
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "🏆 PORA 2026":
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    
    # Special PORA Header
    st.markdown("""
        <div class="hero-banner" style="background: linear-gradient(135deg, #78350f 0%, #b45309 50%, #d97706 100%); box-shadow: 0 25px 50px -12px rgba(180, 83, 9, 0.4);">
            <h2 style="font-size: 36px; font-weight: 800; margin-bottom: 16px;">🏆 PORA ACEH 2026</h2>
            <p style="font-size: 18px; opacity: 0.9; max-width: 600px; line-height: 1.6;">
                Pekan Olahraga Aceh (PORA) merupakan ajang olahraga terbesar di provinsi Aceh. 
                DPRK Aceh Jaya mendukung penuh persiapan dan kesuksesan acara ini.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    # Countdown Timer
    st.markdown("<h3 style='text-align: center; color: #064e3b; font-weight: 700;'>Menuju Pembukaan Resmi</h3>", unsafe_allow_html=True)
    
    countdown_html = """
    <style>
      .countdown-container { display: flex; justify-content: center; gap: 15px; margin: 20px 0; flex-wrap: wrap; }
      .countdown-box {
        background: linear-gradient(135deg, #064e3b, #059669);
        border-radius: 16px; padding: 20px; min-width: 90px; text-align: center; color: white;
        box-shadow: 0 10px 20px rgba(5, 150, 105, 0.2);
      }
      .countdown-value { font-size: 36px; font-weight: 800; display: block; line-height: 1; }
      .countdown-label { font-size: 12px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; margin-top: 5px; display: block;}
    </style>
    <div class="countdown-container" id="countdown">
      <div class="countdown-box"><span class="countdown-value" id="days">00</span><span class="countdown-label">Hari</span></div>
      <div class="countdown-box"><span class="countdown-value" id="hours">00</span><span class="countdown-label">Jam</span></div>
      <div class="countdown-box"><span class="countdown-value" id="minutes">00</span><span class="countdown-label">Menit</span></div>
      <div class="countdown-box"><span class="countdown-value" id="seconds">00</span><span class="countdown-label">Detik</span></div>
    </div>
    <script>
      const countDownDate = new Date("Oct 15, 2026 08:00:00").getTime();
      const x = setInterval(function() {
        const now = new Date().getTime();
        const distance = countDownDate - now;
        document.getElementById("days").innerText = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("hours").innerText = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        document.getElementById("minutes").innerText = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        document.getElementById("seconds").innerText = Math.floor((distance % (1000 * 60)) / 1000);
        if (distance < 0) {
          clearInterval(x);
          document.getElementById("countdown").innerHTML = "<div style='font-size:24px; font-weight:800; color:#059669; text-align:center; width:100%;'>🎉 PORA ACEH 2026 SEDANG BERLANGSUNG!</div>";
        }
      }, 1000);
    </script>
    """
    components.html(countdown_html, height=180)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.subheader("📅 Agenda Penting Persiapan")
    st.dataframe({
        "Tanggal": ["10 Jan 2026", "15 Mar 2026", "01 Jun 2026", "15 Okt 2026"],
        "Kegiatan": ["Rapat Koordinasi Panitia", "Finalisasi Anggaran Pendampingan", "Monitoring Pembangunan Venue", "Upacara Pembukaan"],
        "Status": ["✅ Selesai", "✅ Selesai", "🔄 Berjalan", "⏳ Mendatang"]
    }, use_container_width=True, hide_index=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================================================
# 6. FOOTER
# ==========================================================================================
st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 14px; padding: 20px 0; line-height: 1.6;">
    © 2026 <strong>Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</strong>.<br>
    Dibangun dengan ❤️ untuk transparansi, akuntabilitas, dan pelayanan publik yang lebih baik.
</div>
""", unsafe_allow_html=True)
