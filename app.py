import streamlit as st
from datetime import datetime
from PIL import Image, ImageDraw

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MedTimer - Daily Medicine Companion",
    layout="wide"
)

st.title("💊 MedTimer – Daily Medicine Companion")
st.write("A calm, friendly app to help you remember daily medicines.")

# -----------------------------
# Session State
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
    taken = sum(1 for m in st.session_state.medicines if m["taken"])
    return int((taken / len(st.session_state.medicines)) * 100)

def draw_reward_image():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Face
    draw.ellipse((50, 50, 250, 250), outline="green", width=6)

    # Eyes
    draw.ellipse((110, 120, 130, 140), fill="black")
    draw.ellipse((170, 120, 190, 140), fill="black")

    # Smile
    draw.arc((110, 150, 190, 220), start=0, end=180, fill="green", width=5)

    return img

# -----------------------------
# Add Medicine Section
# -----------------------------
st.header("➕ Add Medicine")

with st.form("medicine_form"):
    name = st.text_input("Medicine Name")
    med_time = st.time_input("Scheduled Time")
    add = st.form_submit_button("Add Medicine")

    if add and name:
        st.session_state.medicines.append({
            "name": name,
            "time": med_time,
            "taken": False
        })
        st.success("Medicine added successfully!")

# -----------------------------
# Medicine Checklist
# -----------------------------
st.header("📋 Today's Medicine Checklist")

if not st.session_state.medicines:
    st.info("No medicines added yet.")
else:
    for i, med in enumerate(st.session_state.medicines):
        status, color = get_status(med["time"], med["taken"])

        c1, c2, c3, c4 = st.columns([3, 2, 2, 2])
        c1.write(f"**{med['name']}**")
        c2.write(med["time"].strftime("%H:%M"))
        c3.markdown(
            f"<span style='color:{color}'><b>{status}</b></span>",
            unsafe_allow_html=True
        )

        if c4.button("Mark as Taken", key=i):
            st.session_state.medicines[i]["taken"] = True
            st.rerun()

# -----------------------------
# Adherence Score
# -----------------------------
st.header("📊 Weekly Adherence Score")

score = calculate_adherence()
st.progress(score)
st.write(f"**Adherence: {score}%**")

if score >= 80:
    st.success("Excellent! You're taking great care of your health 🌟")
    st.image(draw_reward_image(), caption="🎉 Great Adherence Reward")
else:
    st.warning("Keep going! Every dose matters 💙")

# -----------------------------
# Motivational Tip
# -----------------------------
st.info("💡 Tip: Taking medicines on time improves recovery and peace of mind.")
