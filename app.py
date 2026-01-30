import streamlit as st
from utils.emissions import calculate_footprint, lifestyle_footprint
from utils.firebase_utils import save_data, load_user_data
from utils.ml_models import train_model, predict_future
from utils.tips import random_tip
from utils.goals import calculate_progress
import pandas as pd

st.set_page_config(page_title="GreenGauge", page_icon="🌱", layout="wide")

st.title("🌍 GreenGauge - Your Carbon Tracker")
st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.header("Navigation")

menu = st.sidebar.radio("Go to", ["Home", "Track Carbon", "Lifestyle Calculator", "Dashboard", "Goals", "Awareness"])

if menu == "Home":
    st.subheader("Welcome to GreenGauge!")
    st.write("Track, measure, and reduce your carbon footprint with simple analytics and eco-tips.")
    st.sidebar.success(random_tip())

elif menu == "Track Carbon":
    st.header("🚗 Daily Carbon Tracker")
    transport = st.number_input("Transportation (km per day)", min_value=0.0)
    electricity = st.number_input("Electricity usage (kWh per day)", min_value=0.0)
    fuel = st.number_input("Fuel consumption (litres per day)", min_value=0.0)

    if st.button("Calculate Footprint"):
        total = calculate_footprint(transport, electricity, fuel)
        st.success(f"Your daily footprint is {total:.2f} kg CO₂")
        save_data("daily_data.csv", {"transport": transport, "electricity": electricity, "fuel": fuel, "total": total})

elif menu == "Lifestyle Calculator":
    st.header("🧬 Lifestyle-Based Calculator")
    transport = st.selectbox("Main mode of transport", ["Car", "Bus", "Bike", "Cycle/Walk"])
    diet = st.selectbox("Diet type", ["Meat-heavy", "Mixed", "Vegetarian", "Vegan"])
    energy = st.selectbox("Energy source", ["Coal", "Electric", "Renewable"])
    shopping = st.selectbox("Shopping habits", ["Frequent", "Moderate", "Minimal"])

    if st.button("Estimate Lifestyle Footprint"):
        total = lifestyle_footprint(transport, diet, energy, shopping)
        st.success(f"Your estimated yearly footprint: {total:.2f} tonnes CO₂")
        save_data("lifestyle.csv", {"transport": transport, "diet": diet, "energy": energy, "shopping": shopping, "total": total})

elif menu == "Dashboard":
    st.header("📊 Your Carbon Dashboard")
    df = load_user_data("daily_data.csv")
    if not df.empty:
        st.line_chart(df["total"])
        avg = df["total"].mean()
        st.metric("Average Daily Emission", f"{avg:.2f} kg CO₂")
    else:
        st.warning("No data yet. Please record your carbon usage first.")

elif menu == "Goals":
    st.header("🎯 Set Green Goals")
    goal = st.number_input("Set your monthly CO₂ goal (in kg):", min_value=0.0)
    df = load_user_data("daily_data.csv")
    if not df.empty:
        current = df["total"].sum()
        progress = calculate_progress(current, goal)
        st.progress(progress / 100)
        st.metric("Progress towards goal", f"{progress:.2f}%")
    else:
        st.warning("Please start tracking to see progress.")

elif menu == "Awareness":
    st.header("💡 Climate Awareness & Tips")
    st.image("assets/bg.jpg", use_container_width=True)
    for _ in range(5):
        st.info(random_tip())