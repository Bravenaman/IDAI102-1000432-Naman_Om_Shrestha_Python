# IDAI102-1000432-Naman_Om_Shrestha_Python
# 💊 MedTimer – Daily Medicine Companion

**Student Name:** Naman Om Shrestha 
**Student ID:** 1000432  
**Course:** Artificial Intelligence | Python Programming  
**Assessment Type:** Summative Assessment  
**Project Title:** Design and Deploy an Interactive Python Application  

--- 

## 📋 Project Overview

**MedTimer** is a simple, **Streamlit-based web application** designed to help users remember and track their daily medicines.

The app allows users to add medicines, mark them as taken, receive motivational tips, earn badges for consistency, and delete old or unnecessary entries.

The main goal of this project is to solve a real-life problem faced by many people — forgetting to take medicines on time — while keeping the app engaging and easy to use.

---

## ❗ Problem Statement

Many people forget to take their medicines on time due to busy schedules, lack of reminders, or poor tracking methods. Missing or delaying medicines can negatively affect health and recovery.

This project values these issues by:-
- Being a simple, user-friendly application that helps users track their daily medicines
- Reminds them of scheduled times
- Motivates them to stay consistent with their medication routine

---

## 🎯 Project Objectives

- To **help users remember to take their medicines on time.**
- To **provide a simple and organised way to manage daily medicines.**
- To visually **indicate medicine status using colours.**
- To **motivate users through reminders, celebrations, and badges.**
- To **allow users to track their medicine adherence.**
- To generate and **download medicine reports for reference.**

---

## 🎨 User Interface Design

- The MedTimer interface is simple and easy to navigate.
- Medicines are added using a clear input form.
- Daily medicines are shown in a checklist format.
- Colour indicators show medicine status:
  🟩 Green: Taken
  🟧 Orange: Upcoming
  🟥 Red: Missed
- Buttons allow users to mark medicines as taken or delete them.
- Progress bars, motivational tips, celebrations, and badges are used to encourage regular usage.

---

## Key Features

- Add medicines with a scheduled time.
- Daily medicine checklist for easy tracking.
- Colour-coded status for taken, upcoming, and missed medicines.
- One-click button to mark medicines as taken.
- Option to delete medicines that are no longer required.
- Adherence tracking using a progress bar.
- Motivational tips to encourage consistency.
- Celebrations and badges for milestone achievements.
- Downloadable CSV report of medicine history.

---

## 📁 Project Structure

```text
IDAI102-1000432-Naman-Om-Shrestha-SA/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── interactive links/      # GitHub & Streamlit links
│   └── README.md
│
├── assets/
│   ├── stage1/             # Planning & design
│   │   ├── mindmap.png
│   │   ├── wireframe.png
│   │   └── turtle_mockup.png   # Early Turtle-based concept
│   │
│   ├── stage3/             # Interface development
│   │   ├── interface_1.png
│   │   ├── interface_2.png
│   │   └── interface_3.png
│   │
│   ├── stage4/             # Testing & gamification evidence
│   │   ├── testing_1.png
│   │   ├── badges.png
│   │   └── adherence_progress.png
│   │
│   └── screenshots/        # Final deployed app UI
│       ├── ui_dashboard.png
│       ├── ui_checklist.png
│       ├── ui_badges.png
│       ├── ui_progress.png
│       └── ui_motivation.png
```

---

## 📸 Interface Screenshots (Final UI)

<img width="1919" height="866" alt="Screenshot 2026-01-28 195058" src="https://github.com/user-attachments/assets/52d055f1-b560-4c05-aa3a-c57e5a1e75a3" />

<img width="1919" height="868" alt="Screenshot 2026-01-28 195130" src="https://github.com/user-attachments/assets/7556c13c-fea5-46ae-8dd5-7951c4657b62" />

<img width="1919" height="699" alt="Screenshot 2026-01-28 195204" src="https://github.com/user-attachments/assets/4991ee50-b199-4682-8ccf-ce098fece617" />

<img width="1919" height="764" alt="Screenshot 2026-01-28 195217" src="https://github.com/user-attachments/assets/dde25937-490d-41b4-bfba-35581aa35c5c" />

<img width="1918" height="734" alt="Screenshot 2026-01-28 195229" src="https://github.com/user-attachments/assets/195614e5-9235-44f9-94f1-f7d759620b6a" />


## 🔧 Integration Details & 🚀 Deployment Instructions

### 🔗 Integration Details

The MedTimer application is built using Python and integrates the following libraries:

- **Streamlit**  
  Used to create the interactive web interface, handle user input, buttons, forms,
  layouts, and live updates.

- **Datetime**  
  Used to work with time and compare scheduled medicine times with the current time.

- **Pandas**  
  Used to structure medicine data and generate downloadable CSV reports.

- **Pillow (PIL)**  
  Used to create simple graphics and visual rewards for user motivation.

These libraries work together to provide a smooth and interactive user experience.

---

## 🚀 Deployment Instructions

To run the MedTimer application locally, follow these steps:

1. Ensure Python 3.8 or higher is installed on your system.
2. Clone or download the project repository from GitHub.
3. Install the required Python libraries using the command below:
```bash
pip install streamlit pandas pillow
```


### Live Streamlit Application Link:-
https://idai102-1000432-namanomshrestha.streamlit.app/

