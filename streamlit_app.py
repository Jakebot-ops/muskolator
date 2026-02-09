import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="Muskolator", page_icon="🚀", layout="centered")

# --- CLOUDFLARE ANALYTICS ---
# Injecting the Cloudflare Web Analytics beacon
components.html(
    """
    <script defer src='https://static.cloudflareinsights.com/beacon.min.js' 
            data-cf-beacon='{"token": "6655383f135b00432af582223e59c3ad"}'></script>
    """,
    height=0,
    width=0
)

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
    import urllib.parse
    
    share_text = f"Elon promised '{promise}' in {years} years. The Muskolator predicts {delivery_date.strftime('%Y')}. 🚀\n\n#ElonTime #Muskolator\n\nCheck yours at Muskolator.com"
    encoded_share = urllib.parse.quote(share_text)
    share_url = f"https://twitter.com/intent/tweet?text={encoded_share}"

    st.markdown(f"""
    <a href="{share_url}" target="_blank" style="text-decoration: none;">
        <div style="
            width: 100%;
            background-color: #000000;
            color: white;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            font-family: sans-serif;
            margin-top: 10px;
        ">
            ✖️ Share on X
        </div>
    </a>
    """, unsafe_allow_html=True)


# --- FOOTER ---
st.markdown("<div class='footer'>Calculations powered by the Reality Distortion Field™ Detector.<br><i>Not financial advice. Not legal advice. Just math.</i></div>", unsafe_allow_html=True)
