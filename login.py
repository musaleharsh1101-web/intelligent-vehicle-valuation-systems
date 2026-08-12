import streamlit as st


st.set_page_config(
    page_title="Login | CarMitra by Musale Group",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    #MainMenu, header, footer { visibility: hidden; }
    
    /* Charcoal Emerald Background */
    .stApp { 
        background: radial-gradient(circle at 10% 20%, #064e3b 0%, #022c22 60%, #011710 100%);
        color: #f8fafc;
    }
    
    .block-container { max-width: 1160px; padding-top: 7vh; }
    
    /* 3D Wave Keyframes */
    @keyframes wave3D {
        0% {
            transform: perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px);
            text-shadow: 
                1px 1px 0 #16a34a,
                2px 2px 0 #15803d,
                3px 3px 0 #166534,
                4px 4px 10px rgba(0,0,0,0.5);
        }
        50% {
            transform: perspective(1000px) rotateX(8deg) rotateY(-4deg) translateZ(8px);
            text-shadow: 
                1px 1px 0 #4ade80,
                2px 2px 0 #22c55e,
                3px 3px 0 #16a34a,
                4px 4px 0 #15803d,
                6px 6px 15px rgba(34, 197, 94, 0.4);
        }
        100% {
            transform: perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px);
            text-shadow: 
                1px 1px 0 #16a34a,
                2px 2px 0 #15803d,
                3px 3px 0 #166534,
                4px 4px 10px rgba(0,0,0,0.5);
        }
    }

    /* Title Styling */
    .title-3d-advanced {
        font-size: 3.1rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        line-height: 1.2;
        margin-bottom: 1rem;
        display: inline-block;
        background: linear-gradient(135deg, #ffffff 10%, #4ade80 60%, #22c55e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: wave3D 4s ease-in-out infinite;
        transition: all 0.3s ease;
    }

    .title-3d-advanced:hover {
        transform: scale(1.02) perspective(1000px) rotateX(0deg) rotateY(0deg);
        filter: drop-shadow(0 0 15px rgba(74, 222, 128, 0.6));
    }
    
    .subtitle-badge {
        display: inline-block;
        background: rgba(74, 222, 128, 0.15);
        border: 1px solid rgba(74, 222, 128, 0.35);
        color: #4ade80;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .tagline { 
        color: #cbd5e1; 
        font-size: 1.05rem; 
        line-height: 1.6; 
        max-width: 520px; 
        margin-bottom: 1.8rem;
    }
    
    .feature-card { 
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        color: #f1f5f9; 
        margin: 0.6rem 0; 
        font-weight: 600; 
        font-size: 0.95rem;
    }
    
    /* Login Glass Panel */
    .login-panel { 
        background: rgba(6, 30, 22, 0.75); 
        border-radius: 24px; 
        padding: 2.5rem; 
        border: 1px solid rgba(74, 222, 128, 0.2);
        backdrop-filter: blur(20px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5); 
    }
    
    .login-panel h2 { color: #f8fafc; margin-bottom: .25rem; font-weight: 800; }
    .login-panel p { color: #94a3b8; margin-bottom: 1.5rem; }

    /* --- Username & Password Label Effect --- */
    .stTextInput label {
        color: #f8fafc !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        letter-spacing: 0.5px !important;
        text-shadow: 0 0 8px rgba(74, 222, 128, 0.5) !important;
    }

    /* Input Fields Styling */
    .stTextInput > div > div > input {
        background-color: rgba(2, 20, 15, 0.8) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #115e59 !important;
        height: 50px !important;
        font-size: 0.95rem !important;
    }

    /* Placeholder text visibility */
    .stTextInput > div > div > input::placeholder {
        color: #64748b !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #4ade80 !important;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.4) !important;
    }

    /* Green Button */
    .stButton > button { 
        background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); 
        color: white; 
        border: 0; 
        border-radius: 12px; 
        font-weight: 700; 
        min-height: 50px; 
        font-size: 1rem;
        box-shadow: 0 8px 20px rgba(22, 163, 74, 0.35);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(34, 197, 94, 0.5);
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

left, right = st.columns([1.2, 0.8], gap="large")

with left:
    st.markdown("<div class='subtitle-badge'>Vehicle Valuation Portal</div>", unsafe_allow_html=True)
    st.markdown("<div class='title-3d-advanced'>Welcome CarMitra by Musale Group</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>A streamlined workspace for used-car valuation, customer details, financing estimates, and shareable valuation reports.</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='feature-card'>✓ Data-informed vehicle valuation</div>", unsafe_allow_html=True)
    st.markdown("<div class='feature-card'>✓ Clear financing estimates</div>", unsafe_allow_html=True)
    st.markdown("<div class='feature-card'>✓ Professional customer-ready reports</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='login-panel'><h2>Welcome back</h2><p>Sign in to begin a new valuation.</p>", unsafe_allow_html=True)
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submitted = st.form_submit_button("Sign in to Workspace", use_container_width=True)
    
    if submitted:
        if username == "Harsh" and password == "Harsh@1101":
            st.session_state.logged_in = True
            st.switch_page("pages/Customer.py")
        else:
            st.error("Incorrect username or password.")
            
    st.caption("🔒 Secure Access · CarMitra by MUSALE GROUP")
    st.markdown("</div>", unsafe_allow_html=True)