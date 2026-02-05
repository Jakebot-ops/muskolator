import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# --- CONFIG ---
st.set_page_config(page_title="Muskolator", page_icon="🚀", layout="centered")

# --- STYLING ---
st.markdown("""
<style>
    .big-font { font-size:40px !important; font-weight: bold; color: #ff4b4b; text-align: center; }
    .stButton>button { width: 100%; height: 60px; font-size: 20px; font-weight: bold; }
    .footer { text-align: center; color: #888; margin-top: 50px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🚀 MUSKOLATOR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Translating 'Elon Time' into 'Earth Time' since 2014.</p>", unsafe_allow_html=True)
st.divider()

# --- INPUTS ---
col1, col2 = st.columns([2, 1])

with col1:
    promise = st.text_input("The Promise", placeholder="e.g. Mars Colony by 2028")

with col2:
    years = st.number_input("Promised Years", min_value=0.1, value=1.0, step=0.5, help="How many years away did he say it was?")

category = st.selectbox(
    "Category",
    ["Software / AI (FSD, Robotaxi, Grok)", 
     "Hardware (Cybertruck, Roadster 2.0)", 
     "Space (Starship, Colonization)", 
     "Infrastructure (Boring, Hyperloop)"]
)

# --- LOGIC ---
if st.button("CALCULATE REALITY 🔮"):
    multiplier = 1.0
    reason = ""
    
    if "Software" in category:
        multiplier = 10.0
        reason = "Software Factor (10x): 'Next Year' is a rolling window that resets annually."
    elif "Hardware" in category:
        multiplier = 2.5
        reason = "Hardware Factor (2.5x): Prototype is easy, production is hell."
    elif "Space" in category:
        multiplier = 3.0
        reason = "Space Factor (3.0x): Orbital mechanics + FAA Regulation + Raptor reliability."
    elif "Infrastructure" in category:
        multiplier = 5.0
        reason = "Boring Factor (5.0x): Moving dirt in the real world is harder than X posts imply."
        
    real_years = years * multiplier
    delivery_date = datetime.date.today() + relativedelta(months=int(real_years * 12))
    
    # --- RESULT ---
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Elon Said:")
        st.markdown(f"## {years} Years")
    with c2:
        st.markdown("### Reality Check:")
        st.markdown(f"## {real_years:.1f} Years")
        
    st.markdown(f"<p class='big-font'>📅 {delivery_date.strftime('%B %Y')}</p>", unsafe_allow_html=True)
    
    st.info(f"📝 **Why:** {reason}")
    
    # Viral Share Logic
    share_text = f"Elon promised '{promise}' in {years} years.\n The Muskolator predicts {delivery_date.strftime('%Y')}. #ElonTime #Muskolator\n\nCheck yours at Muskolator.com"
    st.text_area("Copy to Share:", value=share_text, height=100)

# --- FOOTER ---
st.markdown("<div class='footer'>Calculations powered by the Reality Distortion Field™ Detector.<br><i>Not financial advice. Not legal advice. Just math.</i></div>", unsafe_allow_html=True)
