import streamlit as st
from datetime import datetime, time
import turtle

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MedTimer - Daily Medicine Companion",
    layout="wide"
)

st.title("💊 MedTimer – Daily Medicine Companion")
st.write("A friendly app to help you track medicines with ease and confidence.")

# -----------------------------
# Initialize Session State
# -----------------------------
if "medicines" not in st.session_state:
    st.session_state.medicines = []

# -----------------------------
# Functions
# -----------------------------
def get_status(med_time, taken):
    now = datetime.now().time()
    if taken:
        return "Taken", "green"
    elif now < med_time:
        return "Upcoming", "orange"
    else:
        return "Missed", "red"

def calculate_adherence():
    if len(st.session_state.medicines) == 0:
        return 0
    taken_count = sum(1 for m in st.session_state.medicines if m["taken"])
    return int((taken_count / len(st.session_state.medicines)) * 100)

def draw_turtle_smiley():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(3)

    # Face
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.circle(100)

    # Eyes
    t.penup()
    t.goto(-35, 40)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(35, 40)
    t.pendown()
    t.circle(10)

    # Smile
    t.penup()
    t.goto(-40, 0)
    t.pendown()
    t.setheading(-60)
    t.circle(50, 120)

    t.hideturtle()
    screen.exitonclick()

# -----------------------------
# Input Section
# -----------------------------
st.header("➕ Add Medicine")

with st.form("medicine_form"):
    med_name = st.text_input("Medicine Name")
    med_time = st.time_input("Scheduled Time")
    submitted = st.form_submit_button("Add Medicine")

    if submitted and med_name:
        st.session_state.medicines.append({
            "name": med_name,
            "time": med_time,
            "taken": False
        })
        st.success("Medicine added successfully!")

# -----------------------------
# Medicine Checklist
# -----------------------------
st.header("📋 Today's Medicine Checklist")

if len(st.session_state.medicines) == 0:
    st.info("No medicines added yet.")
else:
    for i, med in enumerate(st.session_state.medicines):
        status, color = get_status(med["time"], med["taken"])

        col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

        col1.write(f"**{med['name']}**")
        col2.write(med["time"].strftime("%H:%M"))
        col3.markdown(f"<span style='color:{color}'>{status}</span>", unsafe_allow_html=True)

        if col4.button("Mark as Taken", key=i):
            st.session_state.medicines[i]["taken"] = True
            st.experimental_rerun()

# -----------------------------
# Adherence Score
# -----------------------------
st.header("📊 Weekly Adherence Score")

score = calculate_adherence()
st.progress(score)
st.write(f"**Adherence: {score}%**")

if score >= 80:
    st.success("Great job! You're doing very well 🌟")
    st.write("🎉 Click the button below for a reward!")
    if st.button("Show Reward"):
        draw_turtle_smiley()
else:
    st.warning("Keep going! Every dose matters 💙")

# -----------------------------
# Motivational Tip
# -----------------------------
st.info("💡 Tip: Taking medicines on time keeps your treatment effective and stress-free.")
