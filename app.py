import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

from storage import save_valuation


st.set_page_config(
    page_title="CarMitra | MUSALE MOTORS", page_icon="🚗", layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parents[1]

TRANSLATIONS = {
    "English": {
        "workspace_title": "Vehicle Valuation Workspace",
        "hero_heading": "Make your next car decision with confidence.",
        "hero_sub": "Hello, <b>{customer}</b>. Enter the vehicle details below for a data-informed market estimate.",
        "step_1": "1. Customer details",
        "step_2": "2. Vehicle valuation",
        "step_3": "3. Your report",
        "find_car": "📍 <b>Find the right car near you</b><span style='color:#64748b'> · Personalised prices and services for your city</span>",
        "journey_title": "Everything your car journey needs",
        "journey_sub": "Transparent valuation, financing support and a customer-first purchase experience.",
        "offers_title": "🎉 Special Offers & Benefits",
        "offers_sub": "Take advantage of limited-time benefits on car evaluation and purchase.",
        "popular_title": "Popular choices in your city",
        "popular_sub": "A quick look at vehicles frequently explored by CarMitra customers.",
        "supported_brands": "Supported brands",
        "fuel_types": "Fuel types",
        "estimation_time": "Estimation time",
        "report_status": "Report status",
        "instant": "Instant",
        "ready": "Ready",
        "clear_pricing_title": "Clear pricing",
        "clear_pricing_desc": "A transparent estimate range, not a hidden quote.",
        "easy_financing_title": "Easy financing",
        "easy_financing_desc": "Use the EMI planner before you commit.",
        "shareable_report_title": "Shareable report",
        "shareable_report_desc": "Send your complete estimate to family or a dealer.",
        "vehicle_profile_title": "Vehicle profile",
        "vehicle_profile_sub": "Provide accurate specifications for a more meaningful estimate.",
        "choose_brand": "Choose car brand",
        "brand_caption": "The vehicle preview updates when you select a brand.",
        "brand_preview_desc": "Brand card from the selected vehicle reference collection",
        "core_details": "Core details",
        "selected_brand": "Selected brand",
        "mfg_year": "Manufacturing year",
        "dist_driven": "Distance driven (km)",
        "fuel_type": "Fuel type",
        "seller_type": "Seller type",
        "transmission": "Transmission",
        "perf_details": "Performance details",
        "ownership": "Ownership history",
        "mileage": "Mileage (km/l)",
        "engine_cap": "Engine capacity (CC)",
        "max_power": "Maximum power (HP)",
        "seats": "Seats",
        "btn_generate": "Generate valuation",
        "unsupported_msg": "This vehicle profile is not supported by the current valuation model.",
        "est_market_val": "Estimated market value",
        "based_on_details": "Based on the vehicle details provided",
        "exp_range": "Expected range",
        "conf_score": "Confidence score",
        "resale_signal": "Resale signal",
        "high": "High",
        "positive": "Positive",
        "based_on_profile": "Based on complete profile",
        "popular_config": "Popular configuration",
        "financing_snapshot": "Financing snapshot",
        "down_payment": "Down payment (₹)",
        "interest_rate": "Annual interest rate (%)",
        "loan_term": "Loan term",
        "est_monthly_emi": "Estimated monthly EMI",
        "loan_amount": "Loan amount",
        "years": "years",
        "btn_view_report": "View valuation report",
        "footer_note": "CarMitra by MUSALE MOTORS provides an indicative estimate based on historical vehicle data. Final resale value can vary with inspection, condition, and local market demand.",
        "welcome": "Welcome",
        "sidebar_caption": "Complete the vehicle profile to receive an estimated market value.",
        "saved_valuations": "Saved valuations",
        "biz_dashboard": "Business dashboard",
        "logout": "Log out",
        "service_city": "Service city",
        "select_lang": "🌐 Select Language / भाषा निवडा",
        "offer1_badge": "FREE BENEFIT",
        "offer1_title": "🚗 Free Home Doorstep Inspection",
        "offer1_desc": "Book valuation today and get a full 140+ point physical vehicle inspection completely free.",
        "offer2_badge": "EXCHANGE BONUS",
        "offer2_title": "💥 ₹15,000 Exchange Bonus",
        "offer2_desc": "Sell your old car and upgrade to a certified pre-owned car with extra bonus valuation.",
        "offer3_badge": "LOW INTEREST",
        "offer3_title": "📉 Special 8.5% Finance Rate",
        "offer3_desc": "Exclusive pre-approved car loan processing fee waiver for MUSALE MOTORS customers.",
        "srv1_title": "Buy a used car",
        "srv1_desc": "Explore inspected vehicles and compare transparent prices.",
        "srv2_title": "Sell your car",
        "srv2_desc": "Get a data-backed market estimate in minutes.",
        "srv3_title": "Check EMI",
        "srv3_desc": "Plan an affordable monthly payment before you decide.",
        "srv4_title": "Vehicle report",
        "srv4_desc": "Share your CarMitra valuation on WhatsApp or PDF."
    },
    "मराठी": {
        "workspace_title": "गाडी व्हॅल्युएशन वर्कस्पेस",
        "hero_heading": "तुमच्या पुढच्या गाडीचा निर्णय आत्मविश्वासाने घ्या.",
        "hero_sub": "नमस्कार, <b>{customer}</b>. अचूक बाजार किंमत मिळवण्यासाठी खालील डिटेल्स भरा.",
        "step_1": "१. ग्राहकाची माहिती",
        "step_2": "२. गाडीचे व्हॅल्युएशन",
        "step_3": "३. तुमचा रिपोर्ट",
        "find_car": "📍 <b>तुमच्या जवळची योग्य गाडी शोधा</b><span style='color:#64748b'> · तुमच्या शहरासाठी खास दर आणि सेवा</span>",
        "journey_title": "तुमच्या कार प्रवासासाठी सर्व काही",
        "journey_sub": "पारदर्शक व्हॅल्युएशन, आर्थिक मदत आणि सर्वोत्तम अनुभव.",
        "offers_title": "🎉 खास ऑफर्स आणि फायदे",
        "offers_sub": "गाडी तपासणी आणि खरेदीवर मर्यादित कालावधीच्या ऑफरचा लाभ घ्या.",
        "popular_title": "तुमच्या शहरातील लोकप्रिय गाड्या",
        "popular_sub": "CarMitra ग्राहकांनी सर्वाधिक निवडलेल्या गाड्यांवर एक नजर टाका.",
        "supported_brands": "उपलब्ध ब्रँड्स",
        "fuel_types": "इंधनाचे प्रकार",
        "estimation_time": "अंदाज वेळ",
        "report_status": "रिपोर्ट स्थिती",
        "instant": "तात्काळ",
        "ready": "तयार आहे",
        "clear_pricing_title": "पारदर्शक किंमत",
        "clear_pricing_desc": "कोणताही छुपा खर्च नाही, स्पष्ट किंमत श्रेणी.",
        "easy_financing_title": "सोपे कर्जाचे पर्याय",
        "easy_financing_desc": "निर्णय घेण्यापूर्वी EMI कॅल्क्युलेटर वापरा.",
        "shareable_report_title": "शेअर करण्यायोग्य रिपोर्ट",
        "shareable_report_desc": "तुमचा पूर्ण रिपोर्ट कुटुंब किंवा डीलर्ससोबत शेअर करा.",
        "vehicle_profile_title": "गाडीची माहिती",
        "vehicle_profile_sub": "अचूक अंदाजासाठी योग्य तपशील प्रविष्ट करा.",
        "choose_brand": "कारचा ब्रँड निवडा",
        "brand_caption": "तुम्ही ब्रँड निवडल्यावर खालील फोटो बदलेल.",
        "brand_preview_desc": "निवडलेल्या ब्रँडचे प्रीव्ह्यू कार्ड",
        "core_details": "मुख्य तपशील",
        "selected_brand": "निवडलेला ब्रँड",
        "mfg_year": "निर्मितीचे वर्ष (Year)",
        "dist_driven": "गाडी किती किमी चालली (Km)",
        "fuel_type": "इंधनाचा प्रकार (Fuel)",
        "seller_type": "विक्रेत्याचा प्रकार (Seller)",
        "transmission": "गिअरचा प्रकार (Transmission)",
        "perf_details": "परफॉर्मन्स तपशील",
        "ownership": "मालिकी इतिहास (Ownership)",
        "mileage": "मायलेज (km/l)",
        "engine_cap": "इंजिन क्षमता (CC)",
        "max_power": "मॅक्स पॉवर (HP)",
        "seats": "सीट क्षमता",
        "btn_generate": "व्हॅल्युएशन तयार करा",
        "unsupported_msg": "या गाडीची माहिती सध्याच्या व्हॅल्युएशन मॉडेलला सपोर्ट करत नाही.",
        "est_market_val": "अंदाजे बाजार मूल्य (किंमत)",
        "based_on_details": "दिलेल्या गाडीच्या तपशीलावर आधारित",
        "exp_range": "अपेक्षित किंमत श्रेणी",
        "conf_score": "विश्वासार्हता स्कोअर",
        "resale_signal": "रीसेल संकेत",
        "high": "उच्च (High)",
        "positive": "सकारात्मक",
        "based_on_profile": "संपूर्ण प्रोफाईलवर आधारित",
        "popular_config": "लोकप्रिय मॉडेल कॉन्फिगरेशन",
        "financing_snapshot": "कर्ज आणि EMI तपशील",
        "down_payment": "डाऊन पेमेंट (₹)",
        "interest_rate": "वार्षिक व्याज दर (%)",
        "loan_term": "कर्जाचा कालावधी",
        "est_monthly_emi": "अंदाजे मासिक EMI",
        "loan_amount": "कर्ज रक्कम",
        "years": "वर्षे",
        "btn_view_report": "व्हॅल्युएशन रिपोर्ट पहा",
        "footer_note": "MUSALE MOTORS चे CarMitra जुन्या डेटाच्या आधारे अंदाजे किंमत दर्शवते. प्रत्यक्ष तपासणीनुसार अंतिम किंमत बदलू शकते.",
        "welcome": "सुस्वागतम",
        "sidebar_caption": "अंदाजे बाजार मूल्य मिळवण्यासाठी गाडीची माहिती पूर्ण करा.",
        "saved_valuations": "सेव्ह केलेले व्हॅल्युएशन",
        "biz_dashboard": "बिझनेस डॅशबोर्ड",
        "logout": "लॉग आऊट",
        "service_city": "सेवा शहर",
        "select_lang": "🌐 Select Language / भाषा निवडा",
        "offer1_badge": "मोफत फायदा",
        "offer1_title": "🚗 मोफत डोअरस्टेप इन्स्पेक्शन",
        "offer1_desc": "आजच व्हॅल्युएशन बुक करा आणि १४०+ पॉइंट्सची गाडी तपासणी मोफत मिळवा.",
        "offer2_badge": "एक्सचेंज बोनस",
        "offer2_title": "💥 ₹१५,००० एक्सचेंज बोनस",
        "offer2_desc": "जुनी गाडी विका आणि अतिरिक्त बोनससह नवीन प्रमाणित गाडीत अपग्रेड करा.",
        "offer3_badge": "कमी व्याज दर",
        "offer3_title": "📉 खास ८.५% वर फायनान्स",
        "offer3_desc": "MUSALE MOTORS च्या ग्राहकांसाठी प्रोसेसिंग फी वर विशेष सवलत.",
        "srv1_title": "जुनी कार खरेदी करा",
        "srv1_desc": "तपासलेल्या गाड्या आणि पारदर्शक दरांची तुलना करा.",
        "srv2_title": "तुमची कार विका",
        "srv2_desc": "काही मिनिटांत डेटावर आधारित किंमत मिळवा.",
        "srv3_title": "EMI तपासा",
        "srv3_desc": "निर्णय घेण्यापूर्वी परवडणारा मासिक हप्ता आखा.",
        "srv4_title": "व्हॅल्युएशन रिपोर्ट",
        "srv4_desc": "तुमचा रिपोर्ट WhatsApp किंवा PDF द्वारे शेअर करा."
    },
    "हिंदी": {
        "workspace_title": "वाहन मूल्यांकन कार्यस्थान",
        "hero_heading": "अपनी अगली कार का निर्णय आत्मविश्वास से लें।",
        "hero_sub": "नमस्ते, <b>{customer}</b>। सटीक बाजार मूल्य प्राप्त करने के लिए नीचे दिए गए विवरण भरें।",
        "step_1": "1. ग्राहक विवरण",
        "step_2": "2. वाहन मूल्यांकन",
        "step_3": "3. आपकी रिपोर्ट",
        "find_car": "📍 <b>अपने पास सही कार खोजें</b><span style='color:#64748b'> · आपके शहर के लिए विशेष कीमतें और सेवाएं</span>",
        "journey_title": "आपकी कार यात्रा के लिए सब कुछ",
        "journey_sub": "पारदर्शी मूल्यांकन, वित्त सहायता और बेहतरीन ग्राहक अनुभव।",
        "offers_title": "🎉 विशेष ऑफ़र और लाभ",
        "offers_sub": "कार मूल्यांकन और खरीद पर सीमित समय के लाभों का लाभ उठाएं।",
        "popular_title": "आपके शहर में लोकप्रिय विकल्प",
        "popular_sub": "CarMitra ग्राहकों द्वारा अक्सर देखी जाने वाली गाड़ियों पर एक नज़र डालें।",
        "supported_brands": "समर्थित ब्रांड्स",
        "fuel_types": "ईंधन के प्रकार",
        "estimation_time": "अनुमान का समय",
        "report_status": "रिपोर्ट की स्थिति",
        "instant": "तत्काल",
        "ready": "तैयार है",
        "clear_pricing_title": "स्पष्ट मूल्य निर्धारण",
        "clear_pricing_desc": "कोई छिपा हुआ शुल्क नहीं, पारदर्शी मूल्य सीमा।",
        "easy_financing_title": "आसान वित्त पोषण",
        "easy_financing_desc": "निर्णय लेने से पहले ईएमआई कैलकुलेटर का उपयोग करें।",
        "shareable_report_title": "शेयर करने योग्य रिपोर्ट",
        "shareable_report_desc": "अपनी पूरी रिपोर्ट परिवार या डीलर के साथ साझा करें।",
        "vehicle_profile_title": "वाहन प्रोफ़ाइल",
        "vehicle_profile_sub": "अधिक सटीक अनुमान के लिए सही विनिर्देश प्रदान करें।",
        "choose_brand": "कार ब्रांड चुनें",
        "brand_caption": "जब आप ब्रांड चुनते हैं तो पूर्वावलोकन अपडेट होता है।",
        "brand_preview_desc": "चयनित ब्रांड का पूर्वावलोकन कार्ड",
        "core_details": "मुख्य विवरण",
        "selected_brand": "चयनित ब्रांड",
        "mfg_year": "निर्माण वर्ष",
        "dist_driven": "चली गई दूरी (किमी)",
        "fuel_type": "ईंधन का प्रकार",
        "seller_type": "विक्रेता का प्रकार",
        "transmission": "ट्रांसमिशन",
        "perf_details": "प्रदर्शन विवरण",
        "ownership": "स्वामित्व का इतिहास",
        "mileage": "माइलेज (किमी/लीटर)",
        "engine_cap": "इंजन क्षमता (सीसी)",
        "max_power": "अधिकतम पावर (एचपी)",
        "seats": "सीटें",
        "btn_generate": "मूल्यांकन उत्पन्न करें",
        "unsupported_msg": "यह वाहन प्रोफ़ाइल वर्तमान मूल्यांकन मॉडल द्वारा समर्थित नहीं है।",
        "est_market_val": "अनुमानित बाजार मूल्य",
        "based_on_details": "प्रदान किए गए वाहन विवरण के आधार पर",
        "exp_range": "अपेक्षित मूल्य सीमा",
        "conf_score": "विश्वास स्कोर",
        "resale_signal": "पुनर्विक्रय संकेत",
        "high": "उच्च",
        "positive": "सकारात्मक",
        "based_on_profile": "पूर्ण प्रोफ़ाइल पर आधारित",
        "popular_config": "लोकप्रिय कॉन्फ़िगरेशन",
        "financing_snapshot": "वित्त और ईएमआई विवरण",
        "down_payment": "डाउन पेमेंट (₹)",
        "interest_rate": "वार्षिक ब्याज दर (%)",
        "loan_term": "ऋण अवधि",
        "est_monthly_emi": "अनुमानित मासिक ईएमआई",
        "loan_amount": "ऋण राशि",
        "years": "वर्ष",
        "btn_view_report": "मूल्यांकन रिपोर्ट देखें",
        "footer_note": "MUSALE MOTORS द्वारा CarMitra ऐतिहासिक डेटा के आधार पर अनुमानित मूल्य प्रदान करता है। अंतिम मूल्य निरीक्षण और स्थानीय मांग के अनुसार भिन्न हो सकता है।",
        "welcome": "स्वागत है",
        "sidebar_caption": "अनुमानित बाजार मूल्य प्राप्त करने के लिए वाहन प्रोफ़ाइल पूरा करें।",
        "saved_valuations": "सहेजे गए मूल्यांकन",
        "biz_dashboard": "बिजनेस डैशबोर्ड",
        "logout": "लॉग आउट",
        "service_city": "सेवा शहर",
        "select_lang": "🌐 Select Language / भाषा चुनें",
        "offer1_badge": "मुफ़्त लाभ",
        "offer1_title": "🚗 मुफ़्त डोरस्टेप निरीक्षण",
        "offer1_desc": "आज ही मूल्यांकन बुक करें और 140+ बिंदु वाहन निरीक्षण मुफ़्त पाएं।",
        "offer2_badge": "एक्सचेंज बोनस",
        "offer2_title": "💥 ₹15,000 एक्सचेंज बोनस",
        "offer2_desc": "अपनी पुरानी कार बेचें और अतिरिक्त बोनस के साथ अपग्रेड करें।",
        "offer3_badge": "कम ब्याज दर",
        "offer3_title": "📉 विशेष 8.5% वित्त दर",
        "offer3_desc": "MUSALE MOTORS के ग्राहकों के लिए प्रोसेसिंग शुल्क में विशेष छूट।",
        "srv1_title": "पुरानी कार खरीदें",
        "srv1_desc": "जांची गई गाड़ियों और पारदर्शी कीमतों की तुलना करें।",
        "srv2_title": "अपनी कार बेचें",
        "srv2_desc": "मिनटों में डेटा-आधारित बाजार अनुमान प्राप्त करें।",
        "srv3_title": "ईएमआई जांचें",
        "srv3_desc": "निर्णय लेने से पहले किफायती मासिक किश्त की योजना बनाएं।",
        "srv4_title": "वाहन रिपोर्ट",
        "srv4_desc": "अपनी CarMitra रिपोर्ट WhatsApp या PDF के माध्यम से साझा करें।"
    }
}


@st.cache_data(show_spinner=False)
def load_vehicle_data():
    data = pd.read_csv(ROOT_DIR / "Cardetails.csv")
    data["name"] = data["name"].astype(str).str.split().str[0]
    return data


@st.cache_resource(show_spinner=False)
def load_model():
    with open(ROOT_DIR / "model.pkl", "rb") as model_file:
        return pickle.load(model_file)


def money(amount):
    return f"₹ {amount:,.0f}"


BRAND_IMAGE_IDS = {
    "Ambassador": 1,
    "Ashok": 2,
    "Audi": 3,
    "BMW": 4,
    "Chevrolet": 5,
    "Daewoo": 6,
    "Datsun": 7,
    "Fiat": 8,
    "Force": 9,
    "Ford": 10,
    "Honda": 11,
    "Hyundai": 12,
    "Isuzu": 13,
    "Jaguar": 14,
    "Jeep": 15,
    "Kia": 16,
    "Land": 17,
    "Lexus": 18,
    "MG": 19,
    "Mahindra": 20,
    "Maruti": 21,
    "Mercedes-Benz": 22,
    "Mitsubishi": 23,
    "Nissan": 24,
    "Opel": 25,
    "Renault": 27,
    "Skoda": 28,
    "Tata": 29,
    "Toyota": 30,
    "Volkswagen": 31,
    "Volvo": 32,
}


def get_brand_image(brand):
    image_id = BRAND_IMAGE_IDS.get(brand, 99)
    return ROOT_DIR / "assets" / "brand-cards" / f"brand-{image_id:02d}.jpg"


def inject_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        #MainMenu, header, footer { visibility: hidden; }
        
        .stApp { 
            background: linear-gradient(135deg, #eef2f6 0%, #d9e2ec 100%); 
            color: #0f172a; 
        }
        
        [data-testid="stSidebar"] { background: #0f172a; }
        [data-testid="stSidebar"] * { color: #f1f5f9; }
        
        .block-container { max-width: 1250px; padding-top: 2rem; padding-bottom: 2rem; }
        
        .hero { 
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%), radial-gradient(circle at 90% 10%, #2563eb 0%, transparent 40%); 
            border-radius: 20px; 
            padding: 2.5rem; 
            color: white; 
            margin-bottom: 1.5rem; 
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.15);
        }
        .eyebrow { color: #38bdf8; font-size: .8rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 0.5rem; }
        .hero h1 { font-size: 2.4rem; font-weight: 800; margin: 0 0 0.5rem; color: #ffffff; }
        .hero p { color: #94a3b8; font-size: 1.05rem; margin: 0; }
        
        .journey { display:flex; gap:.8rem; align-items:center; background:#ffffff; border:1px solid #cbd5e1; border-radius:14px; padding:.8rem 1.2rem; margin:0 0 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .journey-step { color:#64748b; font-weight:600; font-size:.88rem; white-space:nowrap; }
        .journey-step.active { color:#2563eb; font-weight:700; }
        .journey-divider { color:#cbd5e1; }
        
        .service-card { 
            background:#ffffff; 
            border:1px solid #cbd5e1; 
            border-radius:16px; 
            padding:1.2rem; 
            min-height:135px; 
            transition: all 0.25s ease;
            box-shadow:0 4px 6px -1px rgba(0,0,0,0.02);
        }
        .service-card:hover {
            transform: translateY(-4px);
            border-color: #3b82f6;
            box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.1);
        }
        .service-card h3 { color:#0f172a; font-size:1.05rem; font-weight:700; margin:.5rem 0 .3rem; }
        .service-card p { color:#64748b; font-size:.85rem; margin:0; line-height:1.4; }
        .service-icon { width:36px; height:36px; border-radius:10px; background:#eff6ff; color:#2563eb; display:flex; align-items:center; justify-content:center; font-weight:800; }
        
        .offer-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border: 1px dashed #2563eb;
            border-radius: 16px;
            padding: 1.25rem;
            transition: all 0.25s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
            height: 100%;
        }
        .offer-card:hover {
            transform: translateY(-4px);
            border-style: solid;
            box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.12);
        }
        .offer-badge {
            background: #ef4444;
            color: white;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 3px 9px;
            border-radius: 20px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 0.6rem;
            letter-spacing: 0.05em;
        }
        .offer-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.3rem;
        }
        .offer-desc {
            color: #64748b;
            font-size: 0.85rem;
            margin-bottom: 0.8rem;
            line-height: 1.4;
        }
        .promo-code {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1d4ed8;
            font-weight: 700;
            font-size: 0.8rem;
            padding: 4px 10px;
            border-radius: 8px;
            display: inline-block;
        }

        .city-strip { background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:.6rem 1.2rem; margin:0 0 1.5rem; font-size:0.92rem; }
        .car-card-title { font-weight:700; color:#0f172a; margin:.6rem 0 .1rem; font-size:1rem; }
        .car-card-meta { color:#64748b; font-size:.83rem; }
        
        .section-title { font-size: 1.4rem; font-weight: 800; color: #0f172a; margin: 1rem 0 .2rem; }
        .section-subtitle { color: #64748b; font-size: .92rem; margin: 0 0 1.2rem; }
        
        .brand-preview { background:#0f172a; border-radius:16px; color:white; padding:1.1rem; margin-bottom:1rem; border:1px solid rgba(255,255,255,0.05); }
        .brand-preview p { color:#94a3b8; margin:.25rem 0 0; font-size:.88rem; }
        
        .card { background: white; border: 1px solid #cbd5e1; border-radius: 18px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03); }
        
        .result-card { 
            background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); 
            border-radius: 20px; 
            color: white; 
            padding: 2rem; 
            text-align: center; 
            box-shadow: 0 12px 25px -5px rgba(22, 163, 74, 0.3); 
        }
        .result-card .label { font-size: .8rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; opacity: .9; }
        .result-card .price { font-size: 2.8rem; font-weight: 800; margin: .4rem 0; letter-spacing: -0.5px; }
        
        [data-testid="stMetric"] { background: white; border: 1px solid #cbd5e1; padding: 1rem; border-radius: 14px; }
        
        .stButton > button { 
            background: #2563eb; 
            color: white; 
            border: 0; 
            border-radius: 10px; 
            font-weight: 700; 
            min-height: 48px;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }
        .stButton > button:hover { background: #1d4ed8; color: white; transform: translateY(-1px); }
        </style>
        """,
        unsafe_allow_html=True,
    )


if not st.session_state.get("logged_in", False):
    st.switch_page("login.py")

inject_styles()
data = load_vehicle_data()
model = load_model()
customer = st.session_state.get("customer_name", "Customer")

with st.sidebar:
    st.markdown("## 🚗 CarMitra")
    st.caption("MUSALE MOTORS · VEHICLE VALUATION")
    st.divider()
    
    selected_lang = st.selectbox(
        "🌐 Select Language / भाषा निवडा",
        ["English", "मराठी", "हिंदी"],
        index=0
    )
    t = TRANSLATIONS[selected_lang]
    
    st.divider()
    st.write(f"{t['welcome']}, **{customer}**")
    st.caption(t['sidebar_caption'])
    st.divider()
    st.page_link("pages/History.py", label=t['saved_valuations'])
    st.page_link("pages/Admin.py", label=t['biz_dashboard'])
    st.divider()
    if st.button(t['logout'], use_container_width=True):
        st.session_state.clear()
        st.switch_page("login.py")

hero_sub_text = t['hero_sub'].format(customer=customer)
st.markdown(
    f"""<div class="hero">
        <div class="eyebrow">{t['workspace_title']}</div>
        <h1>{t['hero_heading']}</h1>
        <p>{hero_sub_text}</p>
    </div>""",
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='journey'><span class='journey-step'>{t['step_1']}</span><span class='journey-divider'>›</span><span class='journey-step active'>{t['step_2']}</span><span class='journey-divider'>›</span><span class='journey-step'>{t['step_3']}</span></div>",
    unsafe_allow_html=True,
)

location_left, location_right = st.columns([1.2, 0.8], gap="large")
with location_left:
    st.markdown(
        f"<div class='city-strip'>{t['find_car']}</div>",
        unsafe_allow_html=True,
    )
with location_right:
    selected_city = st.selectbox(
        t['service_city'],
        ["Kolhapur", "Pune", "Mumbai", "Nashik", "Sangli", "Satara"],
        index=0,
        label_visibility="collapsed",
    )
    st.session_state["service_city"] = selected_city

st.markdown(
    f"<div class='section-title'>{t['journey_title']}</div><p class='section-subtitle'>{t['journey_sub']}</p>",
    unsafe_allow_html=True,
)

service_columns = st.columns(4, gap="medium")
service_data = [
    ("01", t['srv1_title'], t['srv1_desc']),
    ("02", t['srv2_title'], t['srv2_desc']),
    ("03", t['srv3_title'], t['srv3_desc']),
    ("04", t['srv4_title'], t['srv4_desc']),
]
for column, (number, title, description) in zip(service_columns, service_data):
    with column:
        st.markdown(
            f"<div class='service-card'><div class='service-icon'>{number}</div><h3>{title}</h3><p>{description}</p></div>",
            unsafe_allow_html=True,
        )

st.markdown(
    f"<br><div class='section-title'>{t['offers_title']}</div><p class='section-subtitle'>{t['offers_sub']}</p>",
    unsafe_allow_html=True,
)
offer_col1, offer_col2, offer_col3 = st.columns(3, gap="medium")

with offer_col1:
    st.markdown(
        f"""
    <div class='offer-card'>
        <span class='offer-badge'>{t['offer1_badge']}</span>
        <div class='offer-title'>{t['offer1_title']}</div>
        <div class='offer-desc'>{t['offer1_desc']}</div>
        <div>Code: <span class='promo-code'>FREEINSPECT</span></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with offer_col2:
    st.markdown(
        f"""
    <div class='offer-card'>
        <span class='offer-badge'>{t['offer2_badge']}</span>
        <div class='offer-title'>{t['offer2_title']}</div>
        <div class='offer-desc'>{t['offer2_desc']}</div>
        <div>Code: <span class='promo-code'>CARUPGRADE</span></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with offer_col3:
    st.markdown(
        f"""
    <div class='offer-card'>
        <span class='offer-badge'>{t['offer3_badge']}</span>
        <div class='offer-title'>{t['offer3_title']}</div>
        <div class='offer-desc'>{t['offer3_desc']}</div>
        <div>Code: <span class='promo-code'>EASYLOAN</span></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"<br><div class='section-title'>{t['popular_title']}</div><p class='section-subtitle'>{t['popular_sub']}</p>",
    unsafe_allow_html=True,
)
popular_cars = [
    ("Maruti", "City-ready hatchback", "From INR 4.5 lakh"),
    ("Hyundai", "Smart family car", "From INR 6.0 lakh"),
    ("Tata", "Built for Indian roads", "From INR 5.5 lakh"),
    ("Mahindra", "Adventure-ready SUV", "From INR 10.0 lakh"),
]
popular_columns = st.columns(4, gap="medium")
for column, (popular_brand, tagline, price_label) in zip(
    popular_columns, popular_cars
):
    with column:
        st.image(get_brand_image(popular_brand), use_container_width=True)
        st.markdown(
            f"<div class='car-card-title'>{popular_brand}</div><div class='car-card-meta'>{tagline} · {price_label}</div>",
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)

metrics = st.columns(4)
metrics[0].metric(t['supported_brands'], f"{data['name'].nunique()}+")
metrics[1].metric(t['fuel_types'], data["fuel"].nunique())
metrics[2].metric(t['estimation_time'], t['instant'])
metrics[3].metric(t['report_status'], t['ready'])

trust_columns = st.columns(3, gap="medium")
trust_items = [
    (t['clear_pricing_title'], t['clear_pricing_desc']),
    (t['easy_financing_title'], t['easy_financing_desc']),
    (t['shareable_report_title'], t['shareable_report_desc']),
]
for column, (title, description) in zip(trust_columns, trust_items):
    with column:
        st.markdown(
            f"<div class='service-card'><h3>{title}</h3><p>{description}</p></div>",
            unsafe_allow_html=True,
        )

st.markdown(
    f"<div class='section-title'>{t['vehicle_profile_title']}</div><p class='section-subtitle'>{t['vehicle_profile_sub']}</p>",
    unsafe_allow_html=True,
)

brand_column, preview_column = st.columns([1, 1.15], gap="large")
with brand_column:
    brand = st.selectbox(
        t['choose_brand'], sorted(data["name"].dropna().unique())
    )
    st.caption(t['brand_caption'])
with preview_column:
    st.markdown(
        f"<div class='brand-preview'><b>{brand} vehicle preview</b><p>{t['brand_preview_desc']}</p></div>",
        unsafe_allow_html=True,
    )
    st.image(get_brand_image(brand), use_container_width=True)

with st.form("valuation_form"):
    primary, secondary = st.columns(2, gap="large")
    with primary:
        st.markdown(f"#### {t['core_details']}")
        st.markdown(f"**{t['selected_brand']}:** {brand}")
        year = st.slider(t['mfg_year'], 1994, 2024, 2018)
        km_driven = st.number_input(
            t['dist_driven'],
            min_value=0,
            max_value=500000,
            value=50000,
            step=1000,
        )
        fuel = st.selectbox(
            t['fuel_type'], sorted(data["fuel"].dropna().unique())
        )
        seller_type = st.selectbox(
            t['seller_type'], sorted(data["seller_type"].dropna().unique())
        )
        transmission = st.selectbox(
            t['transmission'], sorted(data["transmission"].dropna().unique())
        )
    with secondary:
        st.markdown(f"#### {t['perf_details']}")
        owner = st.selectbox(
            t['ownership'], sorted(data["owner"].dropna().unique())
        )
        mileage = st.number_input(
            t['mileage'],
            min_value=1.0,
            max_value=60.0,
            value=18.0,
            step=0.5,
        )
        engine = st.number_input(
            t['engine_cap'],
            min_value=500,
            max_value=8000,
            value=1200,
            step=50,
        )
        max_power = st.number_input(
            t['max_power'],
            min_value=1.0,
            max_value=1000.0,
            value=90.0,
            step=5.0,
        )
        seats = st.selectbox(t['seats'], list(range(2, 11)), index=3)
        submitted = st.form_submit_button(
            t['btn_generate'], use_container_width=True
        )

if submitted:
    input_data = pd.DataFrame(
        [
            [
                brand,
                year,
                km_driven,
                fuel,
                seller_type,
                transmission,
                owner,
                mileage,
                engine,
                max_power,
                seats,
            ]
        ],
        columns=[
            "name",
            "year",
            "km_driven",
            "fuel",
            "seller_type",
            "transmission",
            "owner",
            "mileage",
            "engine",
            "max_power",
            "seats",
        ],
    )
    mappings = {
        "fuel": {"Diesel": 1, "Petrol": 2, "LPG": 3, "CNG": 4},
        "seller_type": {"Individual": 1, "Dealer": 2, "Trustmark Dealer": 3},
        "transmission": {"Manual": 1, "Automatic": 2},
        "owner": {
            "First Owner": 1,
            "Second Owner": 2,
            "Third Owner": 3,
            "Fourth & Above Owner": 4,
            "Test Drive Car": 5,
        },
    }
    brand_mapping = {
        name: index
        for index, name in enumerate(
            [
                "Maruti",
                "Skoda",
                "Honda",
                "Hyundai",
                "Toyota",
                "Ford",
                "Renault",
                "Mahindra",
                "Tata",
                "Chevrolet",
                "Datsun",
                "Jeep",
                "Mercedes-Benz",
                "Mitsubishi",
                "Audi",
                "Volkswagen",
                "BMW",
                "Nissan",
                "Lexus",
                "Jaguar",
                "Land",
                "MG",
                "Volvo",
                "Daewoo",
                "Kia",
                "Fiat",
                "Force",
                "Ambassador",
                "Ashok",
                "Isuzu",
                "Opel",
            ],
            start=1,
        )
    }
    mappings["name"] = brand_mapping
    for column, mapping in mappings.items():
        input_data[column] = input_data[column].map(mapping)

    if input_data.isna().any().any():
        st.error(t['unsupported_msg'])
    else:
        estimate = float(model.predict(input_data)[0])
        estimate = estimate * 10 if estimate < 100000 else estimate
        st.session_state.update(
            {
                "brand": brand,
                "year": year,
                "km_driven": km_driven,
                "fuel": fuel,
                "seller_type": seller_type,
                "transmission": transmission,
                "owner": owner,
                "mileage": mileage,
                "engine": engine,
                "max_power": max_power,
                "seats": seats,
                "car_price": estimate,
            }
        )
        st.session_state["valuation_id"] = save_valuation(
            {
                "customer_name": customer,
                "customer_mobile": st.session_state.get("mobile", ""),
                "customer_city": st.session_state.get("city", ""),
                "brand": brand,
                "year": year,
                "km_driven": km_driven,
                "fuel": fuel,
                "transmission": transmission,
                "estimated_price": estimate,
            }
        )
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='result-card'><div class='label'>{t['est_market_val']}</div><div class='price'>{money(estimate)}</div><div>{t['based_on_details']}</div></div>",
            unsafe_allow_html=True,
        )
            # =========================================================
    # CASH ON DELIVERY OPTION
    # =========================================================
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #dbe3ef;
            border-radius: 18px;
            padding: 1.25rem 1.4rem;
            margin-top: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
        ">
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                margin-bottom:6px;
            ">
                <div style="
                    width:42px;
                    height:42px;
                    border-radius:12px;
                    background:#ecfdf5;
                    color:#059669;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:21px;
                ">
                    💵
                </div>

                <div>
                    <div style="
                        font-size:1.05rem;
                        font-weight:800;
                        color:#0f172a;
                    ">
                        Cash on Delivery
                    </div>

                    <div style="
                        font-size:.82rem;
                        color:#64748b;
                    ">
                        Pay at the time of vehicle/service delivery
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cod_col1, cod_col2 = st.columns([1.5, 1], gap="medium")

    with cod_col1:
        cod_selected = st.checkbox(
            "💵 Select Cash on Delivery",
            key="cash_on_delivery"
        )

    with cod_col2:
        if cod_selected:
            st.success("✓ Cash on Delivery selected")
            st.session_state["payment_method"] = "Cash on Delivery"
        else:
            st.session_state["payment_method"] = "Not Selected"

        lower_bound, upper_bound = estimate * 0.93, estimate * 1.07
        insight_one, insight_two, insight_three = st.columns(3)
        insight_one.metric(
            t['exp_range'], f"{money(lower_bound)} - {money(upper_bound)}"
        )
        insight_two.metric(
            t['conf_score'], t['high'], t['based_on_profile']
        )
        insight_three.metric(
            t['resale_signal'], t['positive'], t['popular_config']
        )

if "car_price" in st.session_state:
    st.markdown(
        f"<br><div class='section-title'>{t['financing_snapshot']}</div>",
        unsafe_allow_html=True,
    )
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        down_payment = st.number_input(
            t['down_payment'],
            min_value=0,
            max_value=int(st.session_state.car_price),
            value=min(100000, int(st.session_state.car_price)),
            step=10000,
        )
        interest = st.slider(t['interest_rate'], 5.0, 15.0, 9.0, 0.1)
        years = st.selectbox(t['loan_term'], [1, 2, 3, 4, 5, 6, 7], index=4)
        st.markdown("</div>", unsafe_allow_html=True)
    loan_amount = st.session_state.car_price - down_payment
    monthly_rate, months = interest / 1200, years * 12
    emi = (
        loan_amount / months
        if monthly_rate == 0
        else loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )
    with right:
        st.markdown(
            f"<div class='result-card'><div class='label'>{t['est_monthly_emi']}</div><div class='price'>{money(emi)}</div><div>{t['loan_amount']}: {money(loan_amount)} · {years} {t['years']}</div></div>",
            unsafe_allow_html=True,
        )
        if st.button(t['btn_view_report'], use_container_width=True):
            st.switch_page("pages/Invoice.py")

st.caption(t['footer_note'])