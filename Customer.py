import streamlit as st


st.set_page_config(
    page_title="Customer Details | CarMitra",
    page_icon="👤",
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
    
    .stApp { 
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 50%, #cbd5e1 100%);
        color: #0f172a;
    }
    
    .block-container { max-width: 950px; padding-top: 3vh; padding-bottom: 5vh; }

    /* Keyframe Animations */
    @keyframes textShimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulseGlow {
        0% { text-shadow: 0 0 5px rgba(37, 99, 235, 0.2); }
        50% { text-shadow: 0 0 18px rgba(37, 99, 235, 0.6); }
        100% { text-shadow: 0 0 5px rgba(37, 99, 235, 0.2); }
    }

    /* 3D Glass Header Box */
    .header-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
        animation: fadeInUp 0.8s ease-out;
    }

    /* Animated Gradient Title */
    .page-title {
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        background: linear-gradient(270deg, #38bdf8, #818cf8, #c084fc, #38bdf8);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        animation: textShimmer 6s ease infinite;
    }

    /* Animated Subtitle */
    .page-subtitle {
        color: #94a3b8;
        margin-top: 8px;
        font-size: 1rem;
        font-weight: 600;
        animation: fadeInUp 1s ease-out;
    }

    /* Section Cards */
    .form-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        animation: fadeInUp 1s ease-out;
    }

    /* Animated Bold Section Headers */
    .section-header {
        font-size: 1.2rem;
        font-weight: 800;
        color: #2563eb;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 1.2rem;
        letter-spacing: 0.3px;
        animation: pulseGlow 3s infinite;
    }

    /* Bold Animated Labels */
    .stTextInput label, .stSelectbox label, .stRadio label {
        color: #1e293b !important;
        font-weight: 800 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.8px !important;
        text-transform: uppercase !important;
        margin-bottom: 8px !important;
        display: inline-block !important;
    }

    .stTextInput > div > div > input, div[data-baseweb="select"] > div {
        background: #f8fafc !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        border-radius: 14px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 0.6rem 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .stTextInput > div > div > input:focus, div[data-baseweb="select"] > div:focus-within {
        border-color: #2563eb !important;
        box-shadow: 0 0 12px rgba(37, 99, 235, 0.2) !important;
        transform: translateY(-1px);
    }

    /* Animated Submit Button Text & Background */
    .stButton > button { 
        background: linear-gradient(270deg, #2563eb, #1d4ed8, #4f46e5, #2563eb) !important; 
        background-size: 300% 300% !important;
        color: #ffffff !important; 
        border: none !important; 
        border-radius: 16px !important; 
        font-weight: 900 !important; 
        min-height: 56px !important; 
        font-size: 1.15rem !important;
        letter-spacing: 1px !important;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3) !important;
        transition: all 0.3s ease !important;
        animation: textShimmer 4s ease infinite !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Animated Header Section
st.markdown(
    """
    <div class='header-box'>
        <div class='page-title'>👤 Customer Information</div>
        <div class='page-subtitle'>Fill in the details below to generate a verified vehicle valuation report.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("customer_form"):
    
    # Card 1: Name & Contact
    st.markdown("<div class='form-card'><div class='section-header'>📞 Contact Details</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    with col1:
        customer_name = st.text_input("Full Name", placeholder="e.g. Ramesh Patil")
        mobile = st.text_input("Mobile Number", placeholder="e.g. 9876543210")
    with col2:
        email = st.text_input("Email Address", placeholder="e.g. ramesh@gmail.com")
    st.markdown("</div>", unsafe_allow_html=True)

    # Card 2: Location
    st.markdown("<div class='form-card'><div class='section-header'>📍 Location Details</div>", unsafe_allow_html=True)
    col3, col4 = st.columns(2, gap="large")
    with col3:
        city = st.text_input("City / District", placeholder="e.g. Kolhapur")
    with col4:
        pincode = st.text_input("Pincode", placeholder="e.g. 416001")
    st.markdown("</div>", unsafe_allow_html=True)

    # Card 3: Preferences
    st.markdown("<div class='form-card'><div class='section-header'>⚙️ Preferences & Type</div>", unsafe_allow_html=True)
    col5, col6 = st.columns(2, gap="large")
    with col5:
        preferred_time = st.selectbox(
            "Preferred Contact Time", 
            ["Morning (9 AM - 12 PM)", "Afternoon (12 PM - 4 PM)", "Evening (4 PM - 8 PM)"]
        )
    with col6:
        customer_type = st.radio("Customer Type", ["Individual (वैयक्तिक)", "Business (व्यवसाय)"], horizontal=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("PROCEED TO VALUATION ➔", use_container_width=True)

if submitted:
    if customer_name and mobile:
        st.session_state["customer_name"] = customer_name
        st.session_state["mobile"] = mobile
        st.session_state["email"] = email
        st.session_state["city"] = city
        st.session_state["pincode"] = pincode
        st.session_state["preferred_time"] = preferred_time
        st.session_state["customer_type"] = customer_type
        
        st.success("Customer details saved successfully!")
        st.switch_page("pages/app.py")
    else:
        st.error("Please fill in at least Full Name and Mobile Number.")