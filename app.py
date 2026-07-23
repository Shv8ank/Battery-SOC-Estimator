import streamlit as st
from pathlib import Path

from src.data_loader import load_battery_data
from src.profile_loader import load_battery_profile
from src.soc_estimator import estimate_soc
from src.statistics import generate_summary

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

# ---------------- Sidebar ---------------- #

st.sidebar.header("⚙️ Configuration")

profile_paths = {
    "Lithium-Ion": "data/profiles/lithium_ion.csv",
    "LiFePO4": "data/profiles/lifepo4.csv",
    "Lead Acid": "data/profiles/lead_acid.csv",
}

battery_profile = st.sidebar.selectbox(
    "Battery Profile",
    list(profile_paths.keys()),
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Battery Data CSV",
    type="csv",
)

analyze = st.sidebar.button("Analyze Battery")

st.sidebar.markdown("---")
st.sidebar.write("Selected Profile:")
st.sidebar.success(battery_profile)

# ---------------- Processing ---------------- #

if analyze:

    if uploaded_file is None:
        st.warning("Please upload a battery CSV file.")

    else:
        try:
            uploaded_path = Path("uploaded_battery.csv")

            with open(uploaded_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            battery_data = load_battery_data(uploaded_path)

            profile = load_battery_profile(
                profile_paths[battery_profile]
            )

            battery_data["SoC(%)"] = battery_data["Voltage(V)"].apply(
                lambda voltage: estimate_soc(
                    voltage,
                    profile,
                )
            )

            summary = generate_summary(
                battery_data,
                battery_profile,
            )

            st.success("Battery analysis completed successfully. Results are displayed below.")

            st.subheader("Processed Battery Data")

            st.dataframe(
                battery_data,
                use_container_width=True,
            )

            st.subheader("Battery Summary")

            for key, value in summary.items():
                st.write(f"**{key}:** {value}")

        except Exception as e:
            st.error(f"Error: {e}")