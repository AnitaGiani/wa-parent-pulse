# ----- Imports -----
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

# Inject CSS to reduce iframe bottom margin
st.markdown(
    """
    <style>
    iframe {
        margin-bottom: -40px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import os
st.write("Current working directory:", os.getcwd())
# ----- Load Data -----
df = pd.read_csv("wa_parent_pulse_with_coords.csv")

# ----- Page Config -----
st.set_page_config(page_title="WA Parent Pulse", layout="wide")
st.title("📊 WA Parent Pulse – Family Wellbeing Dashboard")
st.markdown("A community-powered dashboard exploring parental stress and service access across Western Australia.")

# Region filter
region = st.selectbox("Filter by region", ["All"] + sorted(df["Region"].unique().tolist()))
if region != "All":
    df = df[df["Region"] == region]

# Challenge filter
selected_challenge = st.selectbox("Filter by main challenge", ["All"] + df["MainChallenge"].unique().tolist())
if selected_challenge != "All":
    df = df[df["MainChallenge"] == selected_challenge]

# Highlight suburb with highest stress
most_stressed = df.groupby("Suburb")["StressLevel"].mean().idxmax()
st.info(f"💡 *Suburb with highest average stress:* **{most_stressed}**")

# Key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Average Stress Level", f"{df['StressLevel'].mean():.2f}")
col2.metric("Lack of Services (%)", f"{(df['AccessToServices'] == 'No').mean() * 100:.1f}%")
col3.metric("Parents with Kids Under 5", f"{(df['KidsUnder5'] == 'Yes').sum()}")

# Bar chart of challenges
st.subheader("🧠 Most Common Challenges")
challenge_counts = df["MainChallenge"].value_counts().sort_index()
st.bar_chart(challenge_counts)

# Show pie chart of Access to Services
st.subheader("🧮 Access to Support Services")

access_counts = df["AccessToServices"].value_counts()
fig, ax = plt.subplots()
ax.pie(access_counts, labels=access_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis("equal")
st.pyplot(fig)



# Create map centered in WA
wa_map = folium.Map(location=[-30.0, 120.0], zoom_start=5)

# Optional map section
st.subheader("🗺️ Family Stress Map by Suburb")


# Add markers for each suburb
for _, row in df.iterrows():
    color = "green" if row["StressLevel"] <= 2 else "orange" if row["StressLevel"] == 3 else "red"
    popup_info = f"""
    <b>Suburb:</b> {row['Suburb']}<br>
    <b>Stress Level:</b> {row['StressLevel']}<br>
    <b>Challenge:</b> {row['MainChallenge']}<br>
    <b>Access to Services:</b> {row['AccessToServices']}
    """
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=8,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=popup_info
    ).add_to(wa_map)

# Show map in Streamlit
st_data = st_folium(wa_map, width=700, height=320)

# Screenshot tip
st.markdown("📸 Tip: To share this view, use **Windows+Shift+S** or your screen capture tool.")

# Table view 
# Show/Hide raw data
if st.checkbox("Show raw data"):
    st.subheader("📍 Raw Data")
    st.dataframe(df)

# Footer
st.markdown("---")
st.caption("Built by Anita Lalwani • Final Year CS Student • Tech + Mum Life 💻🍼")

