import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Sekretariat DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide"
)

# Custom CSS untuk styling
st.markdown("""
    <style>
        /* Header */
        .header-title {
            font-size: 28px;
            font-weight: 900;
            color: #14532d;
            margin: 0;
        }
        .header-subtitle {
            font-size: 16px;
            font-weight: 500;
            color: #4b5563;
            margin-top: 2px;
        }
        /* Weather Box */
        .weather-box {
            font-size: 16px;
            color: #065f46;
            text-align: right;
        }
        /* Slogan */
        .slogan {
            font-size: 14px;
            color: #6b7280;
            border-top: 1px solid #d1d5db;
            border-bottom: 1px solid #d1d5db;
            padding: 10px 0;
            margin: 20px 0;
            text-align: center;
            font-style: italic;
        }
        /* Banner Styling */
        .banner-box {
            background: linear-gradient(135deg, #22c55e, #14532d);
            color: white;
            padding: 52px 20px;
            border-radius: 12px;
            text-align: center;
            font-size: 32px;
            font-weight: 900;
            box-shadow: 0 6px 12px rgba(20, 83, 45, 0.4);
            user-select: none;
        }
        /* Navigation Radio Buttons */
        .css-1offfwp, .stRadio > div {
            justify-content: center;
        }
        /* Content Container */
        .content-box {
            background-color: #f9fafb;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout Header dan Cuaca
col_logo, col_weather = st.columns([3, 1])

with col_logo:
    st.markdown('<h1 class="header-title">Sekretariat DPRK</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</p>', unsafe_allow_html=True)

with col_weather:
    st.markdown("""
        <div class="weather-box">
            📍 <b>Aceh Jaya</b><br>
            ☁️ 26 °C &nbsp;&nbsp;|&nbsp;&nbsp; Sumber: BMKG
        </div>
    """, unsafe_allow_html=True)

# Navigasi dengan tombol radio horizontal (dipusatkan)
menu_items = [
    "BERANDA", "PROFIL", "INFORMASI", "GALERI",
    "LAYANAN", "INFORMASI PUBLIK", "KONTAK", "PORA ACEH 2026"
]

selected_menu = st.radio("", menu_items, horizontal=True)

# Slogan di bawah navigasi
st.markdown(
    '<div class="slogan">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya | Menuju Kabupaten Aceh Jaya yang lebih baik</div>',
    unsafe_allow_html=True
)

# Konten Berdasarkan Pilihan Menu
if selected_menu == "BERANDA":
    col_welcome, col_banner = st.columns([1, 2])

    with col_welcome:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("SELAMAT DATANG")
        st.write("Di Website Resmi")
        st.header("Sekretariat DPRK\nKabupaten Aceh Jaya")
        st.markdown("""
            Selamat datang di situs resmi Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. 
            Kami berkomitmen memberikan informasi transparan dan akurat untuk masyarakat.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_banner:
        st.markdown(
            '<div class="banner-box">Pemerintah<br>Kabupaten Aceh Jaya</div>',
            unsafe_allow_html=True
        )

elif selected_menu == "PROFIL":
    st.title("Profil DPRK Aceh Jaya")
    st.markdown("""
    DPRK Aceh Jaya adalah lembaga legislatif di Kabupaten Aceh Jaya yang bertugas dalam penyusunan peraturan daerah, pengawasan pelaksanaan pemerintahan daerah, dan penyampaian aspirasi masyarakat.  
    """)
    st.markdown("""### Struktur Organisasi
    - Ketua DPRK  
    - Wakil Ketua  
    - Sekretariat  
    - Komisi-Komisi  
    """)
    st.info("Profil lengkap pimpinan dan anggota dapat diakses melalui halaman resmi atau kantor DPRK.")

elif selected_menu == "INFORMASI":
    st.title("Informasi Publik")
    st.markdown("""
    Berikut adalah pengumuman dan berita terkini yang berkaitan dengan agenda DPRK Aceh Jaya:
    """)
    st.write("- Rapat Paripurna DPRK tanggal 15 September 2026") 
    st.write("- Pelaksanaan Musyawarah Rencana Pembangunan Daerah (Musrenbang) 2026")
    st.write("- Penyusunan Anggaran Tahun 2027")
    st.success("Informasi selalu diperbarui secara berkala.")

elif selected_menu == "GALERI":
    st.title("Galeri Foto Kegiatan")
    st.write("Foto-foto dokumentasi kegiatan DPRK Aceh Jaya akan ditampilkan di sini.")
    st.info("Sementara ini dalam tahap pengembangan.")

elif selected_menu == "LAYANAN":
    st.title("Layanan DPRK Aceh Jaya")
    st.write("Informasi mengenai layanan publik dan mekanisme pengaduan masyarakat.")
    st.info("Fitur dalam pengembangan.")

elif selected_menu == "INFORMASI PUBLIK":
    st.title("Informasi Publik")
    st.write("Data dan informasi yang dapat diakses oleh masyarakat secara transparan.")
    st.info("Segera hadir.")

elif selected_menu == "KONTAK":
    st.title("Kontak DPRK Aceh Jaya")
    st.markdown("""
    **Alamat:**  
    Jl. Merdeka No.1, Kecamatan Setia, Kabupaten Aceh Jaya  
    **Telepon:** (0650) 123456  
    **Email:** sekretariat.dprk@acehjaya.go.id  
    """)
    st.write("Anda juga dapat mengirim pesan melalui form berikut:")
    message = st.text_area("Tulis Pesan Anda")
    if st.button("Kirim"):
        if message.strip():
            st.success("Terima kasih atas pesan Anda. Kami akan menindaklanjutinya.")
        else:
            st.error("Pesan tidak boleh kosong.")

elif selected_menu == "PORA ACEH 2026":
    st.title("PORA Aceh 2026")
    st.write("""
    Pekan Olahraga Aceh (PORA) merupakan ajang olahraga terbesar di provinsi Aceh.  
    Informasi terkait persiapan dan jadwal kegiatan PORA Aceh 2026 akan disajikan di sini.
    """)
    st.info("Segera hadir.")

else:
    st.title("Halaman dalam Pengembangan")
    st.write("Mohon maaf, konten untuk menu ini sedang dalam proses pengembangan.")

