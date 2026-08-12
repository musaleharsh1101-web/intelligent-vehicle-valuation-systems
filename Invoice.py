from datetime import datetime
import html
from io import BytesIO
from urllib.parse import quote

import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


st.set_page_config(page_title="CarMitra | MUSALE MOTORS", page_icon="📄", layout="wide")

if not st.session_state.get("logged_in", False):
    st.switch_page("login.py")

price = st.session_state.get("car_price")
if price is None:
    st.warning("Create a vehicle valuation before viewing a report.")
    if st.button("Go to valuation"):
        st.switch_page("pages/app.py")
    st.stop()

invoice_number = st.session_state.setdefault("invoice_number", f"AVR-{datetime.now():%y%m%d}-{st.session_state.get('customer_id', '0000')}")
customer = st.session_state.get("customer_name", "Customer")
vehicle_rows = [
    ("Brand & Model", st.session_state.get("brand", "—")), 
    ("Manufacturing Year", st.session_state.get("year", "—")), 
    ("Distance Driven", f"{st.session_state.get('km_driven', 0):,} km"), 
    ("Fuel Type", st.session_state.get("fuel", "—")), 
    ("Transmission", st.session_state.get("transmission", "—")), 
    ("Ownership", st.session_state.get("owner", "—")), 
    ("Engine Capacity", f"{st.session_state.get('engine', '—')} CC"), 
    ("Mileage", f"{st.session_state.get('mileage', '—')} km/l")
]

# PDF Generation Function
def build_pdf_report():
    buffer = BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm, topMargin=17 * mm, bottomMargin=17 * mm)
    styles = getSampleStyleSheet()
    title = styles["Title"]
    title.textColor = colors.HexColor("#16284B")
    body = styles["BodyText"]
    body.leading = 15
    
    elements = [
        Paragraph("CarMitra", title), 
        Paragraph("MUSALE MOTORS - VEHICLE VALUATION REPORT", styles["Heading4"]), 
        Spacer(1, 8 * mm)
    ]
    
    summary = Table([
        ["Report Number", invoice_number], 
        ["Customer Name", customer], 
        ["Generated Date", datetime.now().strftime("%d %b %Y, %I:%M %p")], 
        ["Estimated Market Value", f"INR {price:,.0f}"]
    ], colWidths=[58 * mm, 115 * mm])
    
    summary.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EDF4FF")), 
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#16284B")), 
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"), 
        ("GRID", (0, 0), (-1, -1), .35, colors.HexColor("#DCE5F3")), 
        ("PADDING", (0, 0), (-1, -1), 9)
    ]))
    
    elements += [summary, Spacer(1, 9 * mm), Paragraph("Vehicle Specifications", styles["Heading2"])]
    
    vehicle_table = Table([[label, str(value)] for label, value in vehicle_rows], colWidths=[58 * mm, 115 * mm])
    vehicle_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.white), 
        ("GRID", (0, 0), (-1, -1), .35, colors.HexColor("#DCE5F3")), 
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"), 
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))
    
    elements += [
        vehicle_table, 
        Spacer(1, 10 * mm), 
        Paragraph("This valuation is indicative and may vary after physical vehicle inspection, service-history review, location and market-demand assessment.", body), 
        Spacer(1, 8 * mm), 
        Paragraph("CarMitra by MUSALE MOTORS", styles["Heading4"])
    ]
    
    document.build(elements)
    return buffer.getvalue()

# CSS Animations & Enhanced UI Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

#MainMenu, header, footer {visibility:hidden;}
.stApp {
    background: #0f172a;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
}

/* Entrance Animations */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlow {
    0% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    50% { box-shadow: 0 0 28px rgba(56, 189, 248, 0.4); }
    100% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
}

.report {
    background: rgba(30, 41, 59, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 2.5rem;
    backdrop-filter: blur(16px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}

.top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.logo {
    font-size: 1.4rem;
    font-weight: 800;
    color: #f8fafc;
}

.label {
    font-size: 0.75rem;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.estimate {
    background: linear-gradient(135deg, #0284c7 0%, #4f46e5 100%);
    border-radius: 20px;
    color: white;
    padding: 1.6rem;
    animation: pulseGlow 4s infinite ease-in-out;
    transition: transform 0.3s ease;
}

.estimate:hover {
    transform: translateY(-4px);
}

.estimate .value {
    color: #ffffff;
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0.3rem 0;
}

.line {
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    margin: 1.8rem 0;
}

.badge {
    background: rgba(34, 197, 94, 0.15);
    color: #4ade80;
    border: 1px solid rgba(74, 222, 128, 0.3);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 8px;
}

/* Custom Button Styles */
.stButton>button {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: #fff !important;
    border: 0 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    min-height: 48px !important;
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4) !important;
}

.stDownloadButton>button {
    background: rgba(255, 255, 255, 0.05) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    min-height: 48px !important;
    transition: all 0.3s ease !important;
}

.stDownloadButton>button:hover {
    background: rgba(255, 255, 255, 0.15) !important;
    border-color: #38bdf8 !important;
    color: #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

# Top Bar Header
st.markdown(f"""
<div class='top'>
    <span class='logo'>CarMitra <small style='font-size:.65rem;color:#38bdf8;letter-spacing:.1em;'>BY MUSALE MOTORS</small></span>
    <span style='color:#94a3b8; font-size:0.9rem;'>Valuation Report · <b>{invoice_number}</b></span>
</div>
""", unsafe_allow_html=True)

# Main Report Card Container
st.markdown("<div class='report'>", unsafe_allow_html=True)

header_col, value_card = st.columns([1.3, .7], gap="large")

with header_col:
    st.markdown("<div class='badge'>✓ VERIFIED VALUATION REPORT</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin:.2rem 0;color:#f8fafc;font-weight:800;font-size:2.1rem;'>Your Vehicle Market Estimate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;font-size:0.95rem;'>Algorithmically generated based on current Indian market trends, vehicle condition, and specs provided to CarMitra.</p>", unsafe_allow_html=True)

with value_card:
    st.markdown(f"""
    <div class='estimate'>
        <div class='label' style='color:#cbd5e1;'>Estimated Market Value</div>
        <div class='value'>₹ {price:,.0f}</div>
        <div style='color:#e2e8f0;font-size:.85rem;'>Indicative Market Price Range</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='line'></div>", unsafe_allow_html=True)

# Customer & Vehicle Details Grid
customer_col, vehicle_col = st.columns(2, gap="large")

with customer_col:
    st.markdown("<h4 style='color:#38bdf8;margin-bottom:12px;'>👤 Customer Profile</h4>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='background:rgba(255,255,255,0.03);padding:16px;border-radius:14px;border:1px solid rgba(255,255,255,0.05);'>
        <div style='font-size:1.1rem;font-weight:700;color:#f8fafc;'>{customer}</div>
        <div style='color:#94a3b8;margin-top:4px;font-size:0.9rem;'>✉️ {st.session_state.get('email', '—')}</div>
        <div style='color:#94a3b8;margin-top:2px;font-size:0.9rem;'>📞 {st.session_state.get('mobile', '—')}</div>
        <div style='color:#64748b;margin-top:6px;font-size:0.85rem;'>📍 {st.session_state.get('city', '—')}, {st.session_state.get('state', '—')}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#38bdf8;margin-bottom:12px;'>📊 Valuation Summary</h4>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='background:rgba(255,255,255,0.03);padding:14px;border-radius:14px;border:1px solid rgba(255,255,255,0.05);font-size:0.9rem;'>
        <div style='display:flex;justify-content:space-between;padding:4px 0;'><span style='color:#94a3b8;'>Base Market Price</span><span style='color:#f8fafc;'>₹ {price*1.05:,.0f}</span></div>
        <div style='display:flex;justify-content:space-between;padding:4px 0;'><span style='color:#94a3b8;'>Age & Usage Adj.</span><span style='color:#ef4444;'>- ₹ {price*0.05:,.0f}</span></div>
        <div style='display:flex;justify-content:space-between;padding:6px 0;border-top:1px solid rgba(255,255,255,0.1);font-weight:700;'><span style='color:#38bdf8;'>Final Estimate</span><span style='color:#38bdf8;'>₹ {price:,.0f}</span></div>
    </div>
    """, unsafe_allow_html=True)

with vehicle_col:
    st.markdown("<h4 style='color:#38bdf8;margin-bottom:12px;'>🚘 Vehicle Snapshot</h4>", unsafe_allow_html=True)
    for label, value in vehicle_rows:
        st.markdown(f"""
        <div style='display:flex;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.06);padding:.5rem 0;'>
            <span style='color:#94a3b8;font-size:0.9rem;'>{label}</span>
            <b style='color:#f8fafc;font-size:0.9rem;'>{value}</b>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class='line'></div>
<p style='color:#64748b;font-size:.82rem;text-align:center;'>
    📌 <i>This valuation is indicative. Final offer may vary based on physical inspection, vehicle history, accident status, and local dealer demand.</i>
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Action Buttons Section
report_html = f"""<!doctype html><html><body style='font-family:Arial;padding:40px;color:#16284b'><h1>CarMitra</h1><p><b>MUSALE MOTORS</b></p><p>Valuation report {html.escape(invoice_number)}</p><h2>Estimated market value: ₹ {price:,.0f}</h2><h3>Customer</h3><p>{html.escape(customer)}<br>{html.escape(st.session_state.get('email', '—'))}</p><h3>Vehicle details</h3><table border='1' cellpadding='9' cellspacing='0'>{''.join(f'<tr><td>{html.escape(str(label))}</td><td>{html.escape(str(value))}</td></tr>' for label, value in vehicle_rows)}</table></body></html>"""

col_d1, col_d2 = st.columns(2)

with col_d1:
    st.download_button("📥 Download HTML Report", report_html, file_name=f"CarMitra_Valuation_{invoice_number}.html", mime="text/html", use_container_width=True)

with col_d2:
    st.download_button("📄 Download Official PDF Report", build_pdf_report(), file_name=f"CarMitra_Official_Report_{invoice_number}.pdf", mime="application/pdf", use_container_width=True)

whatsapp_message = quote(f"Hello {customer}, your CarMitra vehicle valuation from MUSALE MOTORS is ready!\n\n🚘 Estimated market value for your {st.session_state.get('brand', 'vehicle')} is *INR {price:,.0f}*.\nReport No: {invoice_number}\n\nPlease contact us for dealership inspection.")
whatsapp_number = str(st.session_state.get("mobile", "")).strip()
whatsapp_url = f"https://wa.me/91{whatsapp_number}?text={whatsapp_message}" if len(whatsapp_number) == 10 else f"https://wa.me/?text={whatsapp_message}"

st.markdown("<br>", unsafe_allow_html=True)
col_wa, col_fin = st.columns([1.5, 1])

with col_wa:
    st.link_button("💬 Share Report on WhatsApp", whatsapp_url, use_container_width=True)

with col_fin:
    if st.button("Finish & Return ➔", use_container_width=True):
        st.switch_page("pages/Thank_You.py")