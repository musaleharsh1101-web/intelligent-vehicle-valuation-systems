import streamlit as st


from storage import get_valuations


st.set_page_config(page_title="CarMitra | Saved Valuations", page_icon="H", layout="wide")
if not st.session_state.get("logged_in", False):
    st.switch_page("login.py")

st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden}.stApp{background:#f6f8fc}.block-container{max-width:1120px;padding-top:2.3rem}.hero{background:linear-gradient(115deg,#15284d,#2466cf);border-radius:22px;color:white;padding:1.9rem;margin-bottom:1.4rem}.hero h1{margin:.3rem 0}.stButton>button{background:#1769e0;color:#fff;border:0;border-radius:10px;font-weight:700}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='hero'><div style='font-size:.78rem;font-weight:700;letter-spacing:.1em'>CARMITRA BY MUSALE MOTORS</div><h1>Saved valuations</h1><p>Review previous vehicle estimates and customer enquiries in one place.</p></div>", unsafe_allow_html=True)

valuations = get_valuations()
if valuations.empty:
    st.info("No valuations have been saved yet. Generate a valuation to see it here.")
else:
    search = st.text_input("Search by customer, brand, city or mobile number")
    if search:
        match = valuations.astype(str).apply(lambda column: column.str.contains(search, case=False, na=False))
        valuations = valuations[match.any(axis=1)]
    st.metric("Saved valuations", len(valuations))
    display = valuations.rename(columns={"created_at": "Created", "customer_name": "Customer", "customer_mobile": "Mobile", "customer_city": "City", "brand": "Brand", "year": "Year", "km_driven": "KM driven", "fuel": "Fuel", "transmission": "Transmission", "estimated_price": "Estimated price"})
    display["Estimated price"] = display["Estimated price"].map(lambda value: f"INR {value:,.0f}")
    st.dataframe(display.drop(columns=["id"]), use_container_width=True, hide_index=True)

if st.button("Back to valuation"):
    st.switch_page("pages/app.py")
