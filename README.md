# WA Parent Pulse – Family Wellbeing Dashboard

📊 **WA Parent Pulse** is a community-driven interactive dashboard that visualises the challenges faced by parents across Western Australia. Built by a final-year Computer Science student and mum, this project aims to surface real stories behind the data — from stress levels to service gaps — in a way that’s easy to understand and act on.

---

## 🚀 Live App

👉 [Click here to view the live dashboard](https://your-streamlit-link-goes-here)

---

## 🎯 Project Purpose

The goal of this dashboard is to:

- Help families, local councils, and service providers better understand parental stress trends
- Showcase how digital tools can drive community insight and policy conversation
- Demonstrate end-to-end skills in data, UX, and public sector impact

---

## 🧰 Tech Stack

- **Python**
- **Streamlit** (for the interactive web app)
- **Folium + Streamlit-Folium** (for mapping suburb-level data)
- **Pandas** (data handling and filtering)
- **Matplotlib** (simple pie chart rendering)

---

## 📍 Key Features

- Filter by **region** and **challenge type**
- View suburb-level **stress levels** and **service access**
- See key metrics like average stress level and lack of services
- Explore an interactive **map** with colour-coded stress markers
- Access raw data right inside the app

---

## 📊 Sample Data Fields

This dashboard uses mock or community-collected data (not official government data). Fields include:

- `Suburb`
- `Region`
- `MainChallenge`
- `StressLevel` (1 to 5)
- `AccessToServices` (Yes/No)
- `KidsUnder5` (Yes/No)
- `Latitude`, `Longitude`

---

## 🙋‍♀️ Creator

**Anita Lalwani**  
Final Year BSc Computer Science | Mum of Two | Digital Public Sector Enthusiast  
📧 anitalalwani.dev@gmail.com  
📷 Instagram: [@yourhandle](https://instagram.com/yourhandle)

---

## 📦 Setup

Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
streamlit run app.py
