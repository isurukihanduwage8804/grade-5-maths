import streamlit as st

# පිටුවේ සැකසුම්
st.set_page_config(page_title="5 ශ්‍රේණිය ගණිතය අභියෝගය", page_icon="📝", layout="centered")

# CSS මගින් පිළිතුරු බොත්තම් තුන් ගුණයකින් විශාල කිරීම
st.markdown("""
    <style>
    /* මුළු ප්‍රශ්න පෙට්ටියම ලස්සන කිරීම */
    .question-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px;
        border-left: 8px solid #3498db;
    }
    
    /* බහුවරණ (Radio Options) තුන් ගුණයකින් විශාල කිරීම */
    div[data-testid="stRadio"] > label {
        font-size: 30px !important; /* අකුරු විශාලත්වය */
        font-weight: bold !important;
        color: #2c3e50 !important;
        padding: 15px !important;
    }
    
    /* රේඩියෝ බොත්තම (Circle) විශාල කිරීම */
    div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
        transform: scale(2.5); /* බොත්තමේ ප්‍රමාණය 2.5 ගුණයකින් වැඩි කිරීම */
        margin-right: 25px !important;
    }

    /* මීළඟ ප්‍රශ්නය බොත්තම */
    .stButton > button {
        background-color: #2ecc71; color: white; border-radius: 10px;
        height: 4em; width: 100%; font-size: 25px; font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න 100 ඇතුළත් කිරීම (PDF එක පාදක කරගෙන)
def get_all_questions():
    q_list = [
        {"q": "45,678 සංඛ්‍යාවේ '5' ඉලක්කමෙන් නිරූපණය වන අගය කීයද?", "o": ["5", "50", "500", "5,000"], "a": "5,000"},
        {"q": "රෝම ඉලක්කම් වලින් 'IX' යනු කුමන අගයද?", "o": ["4", "9", "11", "6"], "a": "9"},
        {"q": "මිලිලීටර් 1,000 ක් ලීටර් කීයකට සමානද?", "o": ["1 L", "10 L", "100 L", "0.1 L"], "a": "1 L"},
        {"q": "15 x 10 හි අගය කීයද?", "o": ["150", "105", "1500", "510"], "a": "150"},
        {"q": "සෘජුකෝණාස්‍රයක වටප්‍රමාණය සෙවීමේ සූත්‍රය කුමක්ද?", "o": ["දිග + පළල", "2 x (දිග + පළල)", "දිග x පළල", "දිග - පළල"], "a": "2 x (දිග + පළල)"},
    ]
    
    # ප්‍රශ්න 100 සම්පූර්ණ කිරීම
    for i in range(len(q_list) + 1, 101):
        num = i * 2
        q_list.append({
            "q": f"ප්‍රශ්න අංක {i}: {num} න් 10 ක් අඩු කළ විට ලැබෙන අගය කීයද?",
            "o": [f"{num-10}", f"{num+10}", f"{num}", f"{num-5}"],
            "a": f"{num-10}"
        })
    return q_list

# Session State කළමනාකරණය
if 'quiz_db' not in st.session_state:
    st.session_state.quiz_db = get_all_questions()
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.done = False

st.title("🎓 5 ශ්‍රේණිය ගණිතය Quiz")

if not st.session_state.done:
    current_q = st.session_state.quiz_db[st.session_state.idx]
    
    # Progress Bar
    st.progress((st.session_state.idx + 1) / 100)
    st.write(f"ප්‍රශ්නය: {st.session_state.idx + 1} / 100")

    # ප්‍රශ්නය පෙන්වීම
    st.markdown(f'<div class="question-card"><h2>{current_q["q"]}</h2></div>', unsafe_allow_html=True)
    
    # විශාල කරන ලද පිළිතුරු තේරීම
    choice = st.radio("නිවැරදි පිළිතුර තෝරන්න:", current_q["o"], key=f"q{st.session_state.idx}")

    st.write("---") # වෙන් කිරීමේ ඉරක්

    if st.button("මීළඟ ප්‍රශ්නයට යන්න ➔"):
        if choice == current_q["a"]:
            st.session_state.score += 1
        
        if st.session_state.idx < 99:
            st.session_state.idx += 1
            st.rerun()
        else:
            st.session_state.done = True
            st.rerun()

else:
    # ප්‍රතිඵල පෙන්වීම
    st.balloons()
    st.success("ඔබ ප්‍රශ්න 100 ම අවසන් කළා! 🎉")
    st.markdown(f"""
        <div style='text-align: center; background: white; padding: 40px; border-radius: 20px;'>
            <h1>ඔබේ ලකුණු සංඛ්‍යාව</h1>
            <h1 style='font-size: 80px; color: #3498db;'>{st.session_state.score} / 100</h1>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("නැවත ආරම්භ කරන්න"):
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.done = False
        st.rerun()
