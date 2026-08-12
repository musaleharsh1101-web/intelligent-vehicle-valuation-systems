import streamlit as st
import urllib.parse

st.set_page_config(page_title="CarMitra | MUSALE MOTORS", page_icon="✓", layout="wide")

customer = st.session_state.get("customer_name", "Customer")
price = st.session_state.get("car_price", 0)
brand = st.session_state.get("brand", "your vehicle")

st.markdown("""
<style>
#MainMenu, header, footer { visibility:hidden; }
.stApp { background:#f6f8fc; }
.block-container { max-width:920px; padding-top:3vh; }

/* Cards Styling */
.complete { background:white; padding:2.5rem; border-radius:26px; text-align:center; box-shadow:0 16px 42px rgba(23,41,76,.09); border:1px solid #e8edf5; }
.check { width:70px; height:70px; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; background:#e6f7ee; color:#087b50; font-size:2rem; font-weight:800; }
.complete h1 { color:#17233b; margin:.9rem 0 .45rem; }
.complete p { color:#6f7c93; }
.amount { background:#f2f7ff; color:#1769e0; padding:1.15rem; border-radius:14px; font-weight:800; font-size:1.65rem; margin:1.2rem 0; }

.card-box {
    background: white;
    padding: 1.8rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(23,41,76,.06);
    border: 1px solid #e8edf5;
    margin-top: 1.2rem;
}

/* Referral Banner Styling */
.referral-card {
    background: linear-gradient(135deg, #1769e0 0%, #0c4bb7 100%);
    color: white;
    padding: 1.8rem;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(23, 105, 224, 0.25);
    margin-top: 1.2rem;
}
.referral-code-box {
    background: rgba(255, 255, 255, 0.15);
    border: 2px dashed rgba(255, 255, 255, 0.5);
    padding: 0.8rem 1.2rem;
    border-radius: 12px;
    font-size: 1.3rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-align: center;
    color: #ffffff;
    margin: 1rem 0;
}

.stButton>button { background:#1769e0; color:#fff; border:0; border-radius:10px; font-weight:700; min-height:46px; }
</style>
""", unsafe_allow_html=True)

# 1. Main Valuation Banner
st.markdown(f"""
<div class='complete'>
    <div class='check'>✓</div>
    <h1>Your valuation is ready, {customer}.</h1>
    <p>Your report for <b>{brand}</b> has been generated successfully.</p>
    <div class='amount'>Estimated value · ₹ {price:,.0f}</div>
    <p style='font-size:.9rem'>Keep this estimate handy while comparing offers. Actual value can vary after an in-person inspection.</p>
</div>
""", unsafe_allow_html=True)

# 2. 🚗 Fast-Track Doorstep Inspection Section
st.markdown("<div class='card-box'>", unsafe_allow_html=True)
st.markdown("### ⚡ Fast-Track Doorstep Inspection Request")
st.markdown("<p style='color:#6f7c93; font-size:0.95rem; margin-bottom: 1.2rem;'>Want a physical inspection? Book a free doorstep evaluation slot below and our expert mechanic from <b>MUSALE MOTORS</b> will visit you.</p>", unsafe_allow_html=True)

with st.form("doorstep_inspection_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        inspection_date = st.date_input("Preferred Date (पाहणीची तारीख)")
    with col2:
        inspection_time = st.selectbox(
            "Preferred Time Slot (वेळ)",
            [
                "10:00 AM - 12:00 PM",
                "12:00 PM - 02:00 PM",
                "02:00 PM - 04:00 PM",
                "04:00 PM - 06:00 PM"
            ]
        )
        
    address = st.text_area("Doorstep Address (घरचा पत्ता)", placeholder="Enter your full address with landmark...", height=90)
    
    submit_btn = st.form_submit_button("📅 Schedule Free Inspection", use_container_width=True)
    
    if submit_btn:
        if address.strip() != "":
            st.session_state["inspection_booked"] = True
            st.session_state["inspection_date"] = str(inspection_date)
            st.session_state["inspection_time"] = inspection_time
            st.session_state["inspection_address"] = address
            st.success(f"🎉 Inspection requested successfully! Our team will visit your address on {inspection_date} ({inspection_time}).")
        else:
            st.error("Please enter your address before booking.")

st.markdown("</div>", unsafe_allow_html=True)

# 3. 📋 RTO Documents Checklist & 🏢 Nearby Hub Info (2 Columns)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class='card-box'>
        <h4 style='color:#17233b; margin-top:0;'>📋 Required Documents</h4>
        <p style='color:#6f7c93; font-size:0.85rem;'>विक्री/हस्तांतरणासाठी लागणारी कागदपत्रे:</p>
        <ul style='color:#475569; font-size:0.88rem; line-height:1.7; padding-left:1.2rem;'>
            <li>Original RC Book (आरसी बुक)</li>
            <li>Valid Insurance Policy (विमा प्रत)</li>
            <li>PUC Certificate (पीयूसी)</li>
            <li>RTO Form 29 & 30 (स्वाक्षरी केलेले)</li>
            <li>Owner ID & Address Proof</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class='card-box'>
        <h4 style='color:#17233b; margin-top:0;'>🏢 Nearest Musale Motors Hub</h4>
        <p style='color:#6f7c93; font-size:0.85rem;'>तुमच्या जवळचे शोरूम आणि वर्कशॉप:</p>
        <p style='color:#1e293b; font-size:0.9rem; font-weight:600; margin-bottom:2px;'>📍 Kolhapur Main Branch</p>
        <p style='color:#64748b; font-size:0.85rem; margin-bottom:8px;'>Station Road, Near Railway Station, Kolhapur</p>
        <p style='color:#1769e0; font-size:0.88rem; font-weight:700; margin-bottom:0;'>📞 Contact: +91 98765 43210</p>
    </div>
    """, unsafe_allow_html=True)

# 4. 🎁 Refer & Earn Section
ref_code = f"CARMITRA-{customer.upper()[:4] if customer else 'REF'}2026"
share_msg = f"नमस्कार! मी CarMitra (Musale Motors) वापरून माझ्या गाडीचे व्हॅल्युएशन केले. तुम्हीसुद्धा तुमच्या गाडीची योग्य किंमत मोफत जाणून घ्या! माझा रिफरल कोड वापरा: *{ref_code}*"
whatsapp_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(share_msg)}"

st.markdown(f"""
<div class='referral-card'>
    <h3 style='margin:0; color:white;'>🎁 Refer & Earn ₹1,000!</h3>
    <p style='font-size:0.92rem; opacity:0.9; margin-top:5px;'>
        तुमच्या मित्राला <b>CarMitra</b> रिफर करा. त्यांनी पाहणी/विक्री पूर्ण केल्यावर तुम्हाला मिळतील <b>₹1,000 कॅशबॅक!</b>
    </p>
    <div class='referral-code-box'>
        YOUR CODE: {ref_code}
    </div>
</div>
""", unsafe_allow_html=True)

col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    st.link_button("📲 Share on WhatsApp", whatsapp_url, use_container_width=True)
with col_ref2:
    if st.button("📋 Copy Referral Code", use_container_width=True):
        st.toast(f"Referral code {ref_code} copied!", icon="✅")

# 5. ⭐ Customer Rating & Feedback System
st.markdown("<div class='card-box'>", unsafe_allow_html=True)
st.markdown("### ⭐ How was your experience with CarMitra?")
st.markdown("<p style='color:#6f7c93; font-size:0.9rem;'>तुमचा अनुभव कसा राहिला? रेटिंग द्या आणि अभिप्राय नोंदवा.</p>", unsafe_allow_html=True)

rating = st.feedback("stars")

feedback_text = st.text_input("Your Feedback (पर्यायी)", placeholder="उदा. अतिशय जलद आणि अचूक सर्व्हिस...")

if st.button("Submit Feedback", use_container_width=True):
    if rating is not None:
        st.session_state["user_rating"] = rating + 1
        st.session_state["user_feedback"] = feedback_text
        st.success(f"🎉 धन्यवाद! तुमचे {rating + 1} ⭐ रेटिंग आणि अभिप्राय सबमिट झाले आहे.")
    else:
        st.warning("कृपया अभिप्राय सबमिट करण्यापूर्वी स्टार रेटिंग निवडा.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Navigation Action Buttons
left, right = st.columns(2)
with left:
    if st.button("Start a new valuation", use_container_width=True):
        for key in ["car_price", "brand", "year", "km_driven"]:
            st.session_state.pop(key, None)
        st.switch_page("pages/app.py")
with right:
    if st.button("Sign out", use_container_width=True):
        st.session_state.clear()
        st.switch_page("login.py")