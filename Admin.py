import pandas as pd
import streamlit as st

from storage import get_valuations


st.set_page_config(page_title="CarMitra | Business Dashboard", page_icon="A", layout="wide")
if not st.session_state.get("logged_in", False):
    st.switch_page("login.py")

st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden}.stApp{background:#f6f8fc}.block-container{max-width:1180px;padding-top:2.3rem}.hero{background:radial-gradient(circle at 80% 0,#2c74f5 0,transparent 30%),linear-gradient(115deg,#101d37,#1b376c);border-radius:22px;color:white;padding:2rem;margin-bottom:1.4rem}.hero h1{margin:.3rem 0}.card{background:#fff;border:1px solid #e7ebf2;border-radius:16px;padding:1rem}.stButton>button{background:#1769e0;color:#fff;border:0;border-radius:10px;font-weight:700}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='hero'><div style='font-size:.78rem;font-weight:700;letter-spacing:.1em;color:#a8c5ff'>MUSALE MOTORS</div><h1>Business dashboard</h1><p>Track customer interest and valuation activity across CarMitra.</p></div>", unsafe_allow_html=True)

valuations = get_valuations()
total = len(valuations)
average_price = valuations["estimated_price"].mean() if total else 0
top_brand = valuations["brand"].mode().iloc[0] if total else "-"
today = pd.Timestamp.now().date().isoformat()
today_count = int(valuations["created_at"].str.startswith(today).sum()) if total else 0

metrics = st.columns(4)
metrics[0].metric("Total valuations", total)
metrics[1].metric("Today", today_count)
metrics[2].metric("Average estimate", f"INR {average_price:,.0f}")
metrics[3].metric("Most valued brand", top_brand)

if total:
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Valuations by brand")
        st.bar_chart(valuations.groupby("brand").size().sort_values(ascending=False).head(8))
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Recent customer enquiries")
        recent = valuations[["customer_name", "brand", "customer_city", "estimated_price"]].head(6).rename(columns={"customer_name": "Customer", "brand": "Brand", "customer_city": "City", "estimated_price": "Estimate"})
        recent["Estimate"] = recent["Estimate"].map(lambda value: f"INR {value:,.0f}")
        st.dataframe(recent, hide_index=True, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Analytics will appear after the first valuation is created.")

if st.button("Open saved valuations"):
    st.switch_page("pages/History.py")
