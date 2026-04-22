import os
import streamlit as st
from crewai import Crew, Task
from writer import writer
import logging

# 🔐 SET YOUR GROQ API KEY (PUT YOUR REAL KEY HERE)


# 🔇 Hide logs
logging.getLogger("crewai").setLevel(logging.ERROR)

# Page config
st.set_page_config(page_title="Automotive AI", layout="centered")

# ------------------ UI DESIGN ------------------ #
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #cce6ff, #e6f2ff);
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #003366;
    margin-bottom: 20px;
}
.subtitle {
    text-align: center;
    color: #004080;
    margin-bottom: 30px;
}
.stTextInput>div>div>input {
    background-color: white;
    color: black;
    border-radius: 12px;
    padding: 12px;
    border: 2px solid #66b3ff;
}
.stButton>button {
    background: linear-gradient(to right, #3399ff, #66ccff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton>button:hover {
    background: linear-gradient(to right, #0073e6, #3399ff);
}
.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #3399ff;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------ #
st.markdown('<div class="title">🚗 Automotive Multi Agent System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fast car specs generator</div>', unsafe_allow_html=True)

car = st.text_input("🔍 Enter Car Name")

# Session state
if "result" not in st.session_state:
    st.session_state.result = ""

status = st.empty()

# ------------------ BUTTON ------------------ #
if st.button("Generate Report 🚀"):

    if car.strip() == "":
        st.warning("⚠️ Please enter a car name")

    else:
        status.markdown("""
        <div style="
            background:#fff3cd;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;
        ">
        🤖 Generating... ⏳
        </div>
        """, unsafe_allow_html=True)

        try:
            # TASK
            task = Task(
                description=f"""
Give EXACTLY 5 lines about {car}:

1. Car Name  
2. Price  
3. Top Speed  
4. Range  
5. One-line summary  

No extra text.
""",
                expected_output="5-line report",
                agent=writer
            )

            # CREW
            crew = Crew(
                agents=[writer],
                tasks=[task],
                verbose=False,
                max_iterations=1
            )

            result = crew.kickoff()

            # Safety
            if hasattr(result, "raw"):
                result = result.raw

            if not result:
                result = "⚠️ No output generated"

            status.empty()
            st.session_state.result = str(result)

        except Exception as e:
            status.empty()
            st.error(f"❌ Error: {e}")

# ------------------ OUTPUT ------------------ #
if st.session_state.result:
    st.markdown("### 📊 Result")

    clean = str(st.session_state.result or "").replace("\n", "<br>")

    st.markdown(
        f"""
        <div class="result-box">{clean}</div>
        """,
        unsafe_allow_html=True
    )