import streamlit as st

st.set_page_config(
    page_title="Battery SoC Estimator",
    page_icon="🔋",
    layout="wide",
)

st.title("🔋 Battery State of Charge Estimator")

st.write(
    """
    Estimate battery State of Charge (SoC)
    using configurable battery profiles.
    """
)

st.sidebar.header("⚙️ Configuration")

battery_profile = st.sidebar.selectbox(
    "Battery Profile",
    [
        "Lithium-Ion",
        "LiFePO4",
        "Lead Acid",
    ],
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Battery CSV",
    type="csv",
)

st.sidebar.markdown("---")

st.sidebar.write("Selected Profile:")

st.sidebar.success(battery_profile)