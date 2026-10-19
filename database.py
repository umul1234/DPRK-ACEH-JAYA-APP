CREATE TABLE IF NOT EXISTS berita (
    id BIGSERIAL PRIMARY KEY, title TEXT, date TEXT, desc_text TEXT,
    image_url TEXT, kategori TEXT, views INT DEFAULT 0, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS agenda (
    id BIGSERIAL PRIMARY KEY, hari TEXT, bulan_tahun TEXT, tanggal_full TEXT,
    judul TEXT, deskripsi TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS galeri (
    id BIGSERIAL PRIMARY KEY, title TEXT, image_url TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS anggota (
    id BIGSERIAL PRIMARY KEY, nama TEXT, jabatan TEXT, komisi TEXT,
    dapil TEXT, fraksi TEXT, urutan INT DEFAULT 1, foto_url TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS jdih (
    id BIGSERIAL PRIMARY KEY, nomor TEXT, tentang TEXT, status TEXT, file_url TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS admin_users (
    id BIGSERIAL PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS pengaduan (
    id BIGSERIAL PRIMARY KEY, nama TEXT, nik TEXT, kategori TEXT, prioritas TEXT,
    lokasi TEXT, isi TEXT, tiket TEXT, status TEXT, created_at TIMESTAMPTZ DEFAULT NOW()
);
-- Tambahan tabel pendukung
CREATE TABLE IF NOT EXISTS running_text (id BIGSERIAL PRIMARY KEY, content TEXT, is_active BOOLEAN DEFAULT TRUE, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS kesekretariatan (id BIGSERIAL PRIMARY KEY, title TEXT, date TEXT, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS pimpinan (id BIGSERIAL PRIMARY KEY, nama TEXT, jabatan TEXT, urutan INT, foto_url TEXT, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS pejabat_sekretariat (id BIGSERIAL PRIMARY KEY, nama TEXT, jabatan TEXT, urutan INT, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS fraksi (id BIGSERIAL PRIMARY KEY, nama TEXT, ketua TEXT, jumlah_anggota INT, urutan INT, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS komisi (id BIGSERIAL PRIMARY KEY, nama TEXT, ketua TEXT, bidang TEXT, urutan INT, created_at TIMESTAMPTZ DEFAULT NOW());
CREATE TABLE IF NOT EXISTS faq (id BIGSERIAL PRIMARY KEY, pertanyaan TEXT, jawaban TEXT, urutan INT, created_at TIMESTAMPTZ DEFAULT NOW());

-- Muat ulang schema cache
NOTIFY pgrst, 'reload schema';
