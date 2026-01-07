# IDAI102-1000432-Naman_Om_Shrestha_Python
# 💊 MedTimer – Daily Medicine Companion

MedTimer is a **Streamlit-based web application** that acts as a calm, friendly **daily medicine companion**.  
It helps users remember scheduled medicines, track whether doses were taken, and visualize adherence — all in one simple interface.

---

## 🧠 What MedTimer Does

- Lets users **add medicines with scheduled times**
- Shows a **daily checklist** with clear status indicators
- Allows users to **mark medicines as taken**
- Calculates a **medicine adherence score**
- Rewards good adherence with a **visual encouragement**
- Generates and downloads a **CSV medicine report**

This app is designed to reduce missed doses and encourage consistency in daily medication routines.

---

## 🚀 Features

### ⏰ Medicine Scheduling
- Add medicine name and scheduled time
- Automatically classifies medicines as:
  - **Upcoming**
  - **Missed**
  - **Taken**

### 📋 Daily Medicine Checklist
- View all medicines scheduled for the day
- Mark medicines as **Taken** with one click
- Color-coded status for easy understanding

### 📊 Adherence Tracking
- Calculates adherence percentage based on taken medicines
- Displays progress using a visual progress bar
- Encouraging feedback based on performance

### 🎉 Reward System
- Displays a custom **reward image** when adherence is ≥ 80%
- Motivates users to stay consistent

### ⬇️ Downloadable Report
- Export medicine data as a **CSV file**
- Includes medicine name, scheduled time, and status

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI framework
- **Pandas** – Data handling & CSV export
- **Pillow (PIL)** – Reward image generation
- **Datetime** – Time-based logic
