# =========================================================
# CSS — MODERN GOVERNMENT PORTAL
# =========================================================
st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
    --primary: #075e54;
    --primary-dark: #043f38;
    --primary-light: #e9f7f3;

    --gold: #d9ad32;
    --gold-light: #f7edc9;

    --text: #183b35;
    --text-dark: #12352f;
    --muted: #71827e;

    --bg: #f4f7f6;
    --white: #ffffff;

    --border: #e1e9e6;

    --shadow-sm: 0 4px 15px rgba(7,94,84,.06);
    --shadow-md: 0 12px 35px rgba(7,94,84,.10);
    --shadow-lg: 0 20px 55px rgba(7,94,84,.14);
}

/* =========================
   GLOBAL
========================= */

* {
    box-sizing: border-box;
}

html,
body,
[class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(7,94,84,.035),
            transparent 30%
        ),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 100% !important;
    padding: 0 !important;
}

#MainMenu,
footer,
header {
    visibility: hidden;
    height: 0;
}

section[data-testid="stSidebar"] {
    display: none;
}

button {
    font-family: 'Inter', sans-serif !important;
}

/* =========================
   GOVERNMENT BAR
========================= */

.govbar {
    min-height: 38px;
    padding: 0 6%;
    background:
        linear-gradient(
            90deg,
            #033a32,
            #075e54,
            #033a32
        );
    color: rgba(255,255,255,.82);

    display: flex;
    align-items: center;
    justify-content: space-between;

    font-size: 11px;
    letter-spacing: .1px;
}

.govbar-left,
.govbar-right {
    display: flex;
    align-items: center;
    gap: 18px;
}

.govbar strong {
    color: #fff;
    font-weight: 700;
}

.govbar-right span {
    cursor: pointer;
    transition: .2s ease;
}

.govbar-right span:hover {
    color: #f5d875;
}

/* =========================
   BRAND
========================= */

.brand-wrap {
    background: rgba(255,255,255,.97);
    border-bottom: 1px solid var(--border);
    padding: 20px 6%;
}

.brand-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 16px;
}

.brand-logo {
    width: 62px;
    height: 62px;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            #0a725f,
            #043e36
        );

    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 29px;

    box-shadow:
        0 8px 20px rgba(7,94,84,.18);

    position: relative;
}

.brand-logo::after {
    content: "";
    position: absolute;

    inset: 4px;

    border: 1px solid rgba(255,255,255,.22);
    border-radius: 12px;
}

.brand-title {
    color: var(--text-dark);

    font-family:
        'Plus Jakarta Sans',
        sans-serif;

    font-size: 18px;
    line-height: 1.25;
    font-weight: 800;

    text-transform: uppercase;
}

.brand-subtitle {
    margin-top: 6px;

    color: #7a8985;

    font-size: 10px;

    letter-spacing: 1.2px;

    font-weight: 600;
}

.brand-location {
    text-align: right;

    color: #71817d;

    font-size: 11px;

    line-height: 1.7;
}

/* =========================
   NAVBAR
========================= */

.nav-wrap {
    background: #fff;

    border-bottom:
        1px solid var(--border);

    padding: 0 6%;

    position: sticky;
    top: 0;

    z-index: 99;
}

.nav-inner {
    min-height: 57px;

    display: flex;
    align-items: center;

    gap: 2px;
}

.nav-button .stButton > button {
    background: transparent !important;

    border: none !important;

    color: #667672 !important;

    font-size: 12px !important;

    font-weight: 700 !important;

    border-radius: 0 !important;

    min-height: 50px !important;

    padding:
        10px 12px !important;

    transition: .2s ease !important;
}

.nav-button .stButton > button:hover {
    background: var(--primary-light) !important;

    color: var(--primary) !important;
}

.nav-button-active .stButton > button {
    color: var(--primary) !important;

    background: #f3f8f6 !important;

    border-bottom:
        3px solid var(--gold) !important;
}

/* =========================
   ALERT
========================= */

.alert {
    min-height: 40px;

    padding:
        9px 6%;

    background:
        linear-gradient(
            90deg,
            #fffaf0,
            #fffdf8
        );

    border-bottom:
        1px solid #f1e1b2;

    color: #735c22;

    display: flex;

    align-items: center;

    gap: 8px;

    font-size: 11px;
}

.alert strong {
    color: #604b16;
}

/* =========================
   HERO
========================= */

.hero {
    position: relative;

    min-height: 500px;

    display: flex;

    align-items: center;

    overflow: hidden;

    background:
        linear-gradient(
            90deg,
            rgba(2,38,33,.96) 0%,
            rgba(4,73,62,.86) 42%,
            rgba(4,73,62,.48) 75%,
            rgba(4,73,62,.22) 100%
        ),
        url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=2000&q=90')
        center/cover no-repeat;
}

.hero::after {
    content: "";

    position: absolute;

    width: 500px;
    height: 500px;

    right: -180px;
    bottom: -250px;

    border-radius: 50%;

    background:
        rgba(217,173,50,.12);

    filter: blur(3px);
}

.hero-content {
    width: 88%;
    max-width: 1250px;

    margin: 0 auto;

    padding: 85px 0;

    color: white;

    position: relative;

    z-index: 2;
}

.hero-kicker {
    display: inline-flex;

    align-items: center;

    gap: 8px;

    color: #f8df87;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 2px;

    margin-bottom: 17px;
}

.hero-kicker::before {
    content: "";

    width: 30px;
    height: 2px;

    background: var(--gold);
}

.hero h1 {
    max-width: 720px;

    font-family:
        'Plus Jakarta Sans',
        sans-serif;

    font-size:
        clamp(38px, 5vw, 62px);

    line-height: 1.08;

    margin: 0 0 22px;

    font-weight: 800;

    letter-spacing: -1.7px;
}

.hero p {
    max-width: 650px;

    color:
        rgba(255,255,255,.84);

    font-size: 15px;

    line-height: 1.8;

    margin-bottom: 30px;
}

.hero-buttons {
    display: flex;

    flex-wrap: wrap;

    gap: 12px;
}

.hero-btn {
    display: inline-flex;

    align-items: center;

    justify-content: center;

    padding:
        13px 22px;

    border-radius: 7px;

    background:
        linear-gradient(
            135deg,
            #e1b83c,
            #c99b22
        );

    color: white !important;

    text-decoration: none;

    font-weight: 800;

    font-size: 12px;

    box-shadow:
        0 8px 22px rgba(0,0,0,.12);

    transition: .25s ease;
}

.hero-btn:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(0,0,0,.18);
}

.hero-btn.secondary {
    background:
        rgba(255,255,255,.10);

    border:
        1px solid rgba(255,255,255,.45);

    backdrop-filter: blur(8px);
}

/* =========================
   CONTENT
========================= */

.content {
    width: 88%;
    max-width: 1250px;

    margin: 0 auto;
}

.section {
    padding: 55px 0;
}

.section-head {
    display: flex;

    justify-content: space-between;

    align-items: end;

    gap: 20px;

    margin-bottom: 27px;
}

.section-kicker {
    color: var(--primary);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.8px;

    text-transform: uppercase;

    margin-bottom: 7px;
}

.section-title {
    color: var(--text);

    font-family:
        'Plus Jakarta Sans',
        sans-serif;

    font-size: 28px;

    font-weight: 800;

    margin: 0;

    letter-spacing: -.5px;
}

.section-desc {
    color: var(--muted);

    font-size: 12px;

    line-height: 1.7;

    margin-top: 8px;
}

/* =========================
   SERVICE
========================= */

.service-box {
    background: #fff;

    border:
        1px solid var(--border);

    min-height: 175px;

    padding: 27px 18px;

    text-align: center;

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

    border-radius: 12px;

    box-shadow:
        0 2px 8px rgba(0,0,0,.015);
}

.service-box:hover {
    transform:
        translateY(-6px);

    border-color:
        #b5d7ce;

    box-shadow:
        var(--shadow-md);
}

.service-icon {
    width: 55px;
    height: 55px;

    margin:
        0 auto 15px;

    border-radius: 14px;

    background:
        linear-gradient(
            145deg,
            #edf9f5,
            #dff1eb
        );

    color: var(--primary);

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 23px;
}

.service-title {
    color: var(--text);

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 8px;
}

.service-desc {
    color: #7a8884;

    font-size: 10px;

    line-height: 1.6;
}

/* =========================
   STATISTICS
========================= */

.info-strip {
    background:
        linear-gradient(
            135deg,
            #043d35,
            #075e54 55%,
            #06483f
        );

    color: white;

    padding: 38px 6%;

    position: relative;

    overflow: hidden;
}

.info-strip::before {
    content: "";

    position: absolute;

    width: 350px;
    height: 350px;

    right: -100px;
    top: -230px;

    border-radius: 50%;

    border:
        1px solid rgba(255,255,255,.09);
}

.info-inner {
    width: 88%;
    max-width: 1250px;

    margin: auto;

    position: relative;
    z-index: 2;
}

.info-item {
    text-align: center;

    padding:
        7px 15px;

    border-right:
        1px solid rgba(255,255,255,.12);
}

.info-item:last-child {
    border-right: none;
}

.info-number {
    color: #f4d873;

    font-size: 30px;

    font-weight: 800;

    font-family:
        'Plus Jakarta Sans',
        sans-serif;
}

.info-label {
    color:
        rgba(255,255,255,.70);

    font-size: 10px;

    margin-top: 3px;

    letter-spacing: .4px;
}

/* =========================
   NEWS
========================= */

.news-main {
    background: #fff;

    border:
        1px solid var(--border);

    overflow: hidden;

    border-radius: 12px;

    height: 100%;

    box-shadow:
        var(--shadow-sm);

    transition: .25s ease;
}

.news-main:hover {
    transform: translateY(-3px);

    box-shadow:
        var(--shadow-md);
}

.news-main-img {
    width: 100%;

    height: 270px;

    object-fit: cover;

    display: block;
}

.news-main-body {
    padding: 22px;
}

.news-tag {
    display: inline-block;

    color: var(--primary);

    background: var(--primary-light);

    padding:
        5px 9px;

    border-radius: 5px;

    font-size: 8px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 10px;
}

.news-main h3 {
    color: var(--text);

    font-family:
        'Plus Jakarta Sans',
        sans-serif;

    font-size: 20px;

    line-height: 1.35;

    margin: 0 0 9px;
}

.news-date {
    color: #929f9b;

    font-size: 10px;
}

.news-side {
    display: flex;

    gap: 15px;

    background: #fff;

    border:
        1px solid var(--border);

    padding: 13px;

    margin-bottom: 12px;

    border-radius: 10px;

    transition: .2s ease;
}

.news-side:hover {
    border-color:
        #bdd8d0;

    box-shadow:
        var(--shadow-sm);

    transform:
        translateX(3px);
}

.news-side-img {
    width: 145px;

    height: 105px;

    object-fit: cover;

    border-radius: 7px;

    flex-shrink: 0;
}

.news-side h4 {
    color: var(--text);

    font-size: 13px;

    line-height: 1.4;

    margin: 5px 0 7px;
}

.news-side p {
    color: #7a8884;

    font-size: 10px;

    line-height: 1.5;

    margin: 0;
}

/* =========================
   AGENDA
========================= */

.agenda-wrap {
    background: #fff;

    border:
        1px solid var(--border);

    border-radius: 12px;

    padding: 23px;

    box-shadow:
        var(--shadow-sm);
}

.agenda-row {
    display: flex;

    gap: 15px;

    padding: 16px 0;

    border-bottom:
        1px solid #edf1ef;
}

.agenda-row:last-child {
    border-bottom: none;
}

.agenda-date {
    width: 62px;
    height: 65px;

    background:
        linear-gradient(
            145deg,
            #075e54,
            #043e36
        );

    color: white;

    border-radius: 8px;

    text-align: center;

    padding-top: 8px;

    flex-shrink: 0;

    box-shadow:
        0 6px 14px rgba(7,94,84,.14);
}

.agenda-date strong {
    display: block;

    font-size: 23px;

    line-height: 1;

    font-weight: 800;
}

.agenda-date span {
    font-size: 8px;

    letter-spacing: 1.2px;

    color:
        rgba(255,255,255,.75);
}

.agenda-title {
    color: var(--text);

    font-weight: 800;

    font-size: 13px;

    margin-bottom: 5px;
}

.agenda-desc {
    color: #7a8884;

    font-size: 10px;

    line-height: 1.55;
}

/* =========================
   PROFILE
========================= */

.profile-card {
    background: white;

    border:
        1px solid var(--border);

    border-radius: 14px;

    padding: 30px 20px;

    text-align: center;

    height: 100%;

    box-shadow:
        var(--shadow-sm);

    transition: .25s ease;
}

.profile-card:hover {
    transform:
        translateY(-5px);

    box-shadow:
        var(--shadow-md);

    border-color:
        #bcd8d1;
}

.profile-photo {
    width: 94px;
    height: 94px;

    border-radius: 50%;

    margin: auto;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        linear-gradient(
            145deg,
            #0b705e,
            #063e37
        );

    color: white;

    font-size: 28px;

    font-weight: 800;

    box-shadow:
        0 7px 20px rgba(7,94,84,.18);

    border:
        4px solid #eef7f4;
}

.profile-role {
    color: var(--primary);

    font-size: 9px;

    font-weight: 800;

    text-transform: uppercase;

    letter-spacing: 1px;

    margin-top: 17px;
}

.profile-name {
    color: var(--text);

    font-size: 16px;

    font-weight: 800;

    margin: 6px 0;
}

.profile-desc {
    color: #7a8884;

    font-size: 10px;

    line-height: 1.6;
}

/* =========================
   FORMS
========================= */

div[data-testid="stForm"] {
    background: white;

    border:
        1px solid var(--border);

    border-radius: 12px;

    padding: 27px !important;

    box-shadow:
        var(--shadow-sm);
}

.stTextInput input,
.stTextArea textarea,
div[data-baseweb="select"] > div {
    border-radius:
        7px !important;

    border-color:
        #d8e3df !important;

    background:
        #fbfcfc !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color:
        var(--primary) !important;

    box-shadow:
        0 0 0 2px rgba(7,94,84,.08) !important;
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button {
    background:
        linear-gradient(
            135deg,
            #075e54,
            #043f38
        ) !important;

    border: none !important;

    color: white !important;

    border-radius:
        7px !important;

    font-weight: 800 !important;

    min-height:
        42px !important;

    transition: .2s ease !important;
}

.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button:hover {
    transform:
        translateY(-1px);

    box-shadow:
        0 8px 18px rgba(7,94,84,.18);
}

/* =========================
   DATAFRAME
========================= */

div[data-testid="stDataFrame"] {
    border-radius: 10px;

    overflow: hidden;

    border:
        1px solid var(--border);

    box-shadow:
        var(--shadow-sm);
}

/* =========================
   FOOTER
========================= */

.footer {
    background:
        linear-gradient(
            145deg,
            #062f29,
            #082f2b
        );

    color:
        rgba(255,255,255,.72);

    margin-top: 60px;

    padding:
        55px 6% 20px;
}

.footer-container {
    width: 88%;

    max-width: 1250px;

    margin: auto;
}

.footer-grid {
    display: grid;

    grid-template-columns:
        1.6fr
        1fr
        1fr
        1.25fr;

    gap: 45px;
}

.footer-column h4 {
    color: white;

    font-size: 13px;

    font-weight: 800;

    margin:
        0 0 17px;
}

.footer-brand {
    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 17px;
}

.footer-logo {
    width: 46px;
    height: 46px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 11px;

    background:
        rgba(255,255,255,.08);

    border:
        1px solid rgba(255,255,255,.12);

    font-size: 20px;
}

.footer-brand-name {
    color: white;

    font-family:
        'Plus Jakarta Sans',
        sans-serif;

    font-size: 14px;

    font-weight: 800;
}

.footer-brand-subtitle {
    color:
        rgba(255,255,255,.40);

    font-size: 8px;

    letter-spacing: 1.3px;

    margin-top: 3px;
}

.footer-description {
    color:
        rgba(255,255,255,.56);

    font-size: 10px;

    line-height: 1.8;

    max-width: 330px;

    margin: 0 0 20px;
}

.footer-column > a {
    display: block;

    color:
        rgba(255,255,255,.58);

    font-size: 10px;

    line-height: 1;

    text-decoration: none;

    margin-bottom: 13px;

    transition: .2s ease;
}

.footer-column > a:hover {
    color: #f4d873;

    transform:
        translateX(3px);
}

.footer-column > p {
    color:
        rgba(255,255,255,.57);

    font-size: 10px;

    line-height: 1.7;

    margin:
        0 0 7px;
}

.footer-social {
    display: flex;

    gap: 8px;
}

.footer-social-item {
    width: 32px;
    height: 32px;

    border-radius: 8px;

    background:
        rgba(255,255,255,.07);

    border:
        1px solid rgba(255,255,255,.10);

    display: flex;

    align-items: center;

    justify-content: center;

    color:
        rgba(255,255,255,.75);

    font-size: 12px;

    transition: .2s ease;
}

.footer-social-item:hover {
    background:
        rgba(217,173,50,.16);

    color:
        #f4d873;

    transform:
        translateY(-2px);
}

.footer-divider {
    margin-top: 42px;

    border-top:
        1px solid rgba(255,255,255,.09);
}

.footer-bottom {
    padding-top: 18px;

    display: flex;

    justify-content: space-between;

    gap: 20px;

    color:
        rgba(255,255,255,.38);

    font-size: 9px;
}

/* =========================
   MOBILE
========================= */

@media (max-width: 900px) {

    .govbar-left {
        display: none;
    }

    .govbar {
        justify-content: flex-end;
    }

    .brand-inner {
        align-items: flex-start;
    }

    .brand-title {
        font-size: 14px;
    }

    .brand-subtitle {
        font-size: 8px;
    }

    .brand-location {
        display: none;
    }

    .hero {
        min-height: 480px;
    }

    .hero h1 {
        font-size: 38px;
    }

    .content,
    .hero-content,
    .info-inner,
    .footer-container {
        width: 92%;
    }

    .nav-wrap {
        padding: 0 4%;

        overflow-x: auto;
    }

    .nav-inner {
        width: max-content;
    }

    .footer-grid {
        grid-template-columns:
            1fr 1fr;

        gap: 35px;
    }

    .footer-bottom {
        flex-direction: column;

        text-align: center;
    }
}

@media (max-width: 600px) {

    .hero h1 {
        font-size: 34px;
    }

    .hero p {
        font-size: 13px;
    }

    .section {
        padding: 40px 0;
    }

    .section-title {
        font-size: 24px;
    }

    .news-side {
        flex-direction: column;
    }

    .news-side-img {
        width: 100%;
        height: 180px;
    }

    .footer-grid {
        grid-template-columns: 1fr;
    }

    .info-item {
        border-right: none;

        border-bottom:
            1px solid rgba(255,255,255,.10);

        padding: 15px;
    }

    .info-item:last-child {
        border-bottom: none;
    }
}

</style>
""",
    unsafe_allow_html=True,
)
