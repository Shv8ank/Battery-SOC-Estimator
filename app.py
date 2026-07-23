import streamlit as st
import plotly.express as px
from pathlib import Path

from src.data_loader import load_battery_data
from src.profile_loader import load_battery_profile
from src.soc_estimator import estimate_soc
from src.statistics import generate_summary

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Battery State of Charge Estimator",
    page_icon="🔋",
    layout="wide",
)

st.title("🔋 Battery State of Charge Estimator")

st.write(
    "Estimate battery State of Charge (SoC) using configurable battery profiles."
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

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
    "Upload Battery Discharge CSV",
    type="csv",
)

analyze = st.sidebar.button(
    "Analyze Battery",
    use_container_width=True,
)

st.sidebar.markdown("---")
st.sidebar.success(f"Selected Profile\n\n**{battery_profile}**")

# -------------------------------------------------------
# Analysis
# -------------------------------------------------------

if analyze:

    if uploaded_file is None:
        st.warning("Please upload a battery discharge CSV file.")

    else:

        try:

            uploaded_path = Path("uploaded_battery.csv")

            with open(uploaded_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

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

            st.success(
                "Battery analysis completed successfully."
            )

            st.divider()

            # ===================================================
            # Battery Summary
            # ===================================================

            with st.container(border=True):

                st.subheader("📊 Battery Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Initial Voltage",
                        f"{summary['Initial Voltage']:.2f} V",
                    )

                with col2:
                    st.metric(
                        "Average Voltage",
                        f"{summary['Average Voltage']:.2f} V",
                    )

                with col3:
                    st.metric(
                        "Average SoC",
                        f"{summary['Average SoC']:.2f} %",
                    )

                with col4:
                    st.metric(
                        "Duration",
                        f"{summary['Duration']} s",
                    )

                st.caption(f"Battery Profile: **{battery_profile}**")

            # ===================================================
            # Voltage Plot
            # ===================================================

            st.subheader("📈 Battery Voltage vs Time")

            fig_voltage = px.line(
                battery_data,
                x="Time(s)",
                y="Voltage(V)",
                markers=True,
                title="Battery Voltage vs Time",
            )

            fig_voltage.update_layout(
                template="plotly_dark",
                xaxis_title="Time (s)",
                yaxis_title="Voltage (V)",
                legend_title="",
            )

            st.plotly_chart(
                fig_voltage,
                use_container_width=True,
            )

            # ===================================================
            # SoC Plot
            # ===================================================

            st.subheader("🔋 Battery State of Charge")

            fig_soc = px.line(
                battery_data,
                x="Time(s)",
                y="SoC(%)",
                markers=True,
                title="Battery State of Charge vs Time",
            )

            fig_soc.update_layout(
                template="plotly_dark",
                xaxis_title="Time (s)",
                yaxis_title="State of Charge (%)",
                legend_title="",
            )

            st.plotly_chart(
                fig_soc,
                use_container_width=True,
            )

            # ===================================================
            # Processed Data
            # ===================================================

            st.subheader("📄 Processed Battery Data")

            st.dataframe(
                battery_data,
                use_container_width=True,
                hide_index=True,
            )

            # ===================================================
            # Download
            # ===================================================

            csv = battery_data.to_csv(index=False)

            st.download_button(
                label="📥 Download Processed CSV",
                data=csv,
                file_name=f"{battery_profile.lower().replace(' ', '_')}_processed.csv",
                mime="text/csv",
                use_container_width=True,
            )

        except Exception as e:

            st.error(f"❌ {e}")