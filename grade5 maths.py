import streamlit as st

# පිටුවේ සැකසුම්
st.set_page_config(page_title="5 ශ්‍රේණිය ගණිතය අභියෝගය", page_icon="📝", layout="centered")

# CSS මගින් අකුරු සහ බොත්තම් ඉතා විශාල කිරීම
st.markdown("""
    <style>
    /* මුළු ප්‍රශ්න පෙට්ටිය */
    .question-card {
        background-color: #ffffff; padding: 30px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px;
        border-left: 10px solid #3498db;
    }
    
    /* ප්‍රශ්නයේ අකුරු විශාලත්වය */
    h2 { font-size: 40px !important; color: #2c3e50; }

    /* බහුවරණ පිළිතුරු වල අකුරු ඉතා විශාල කිරීම (3x Size) */
    div[data-testid="stRadio"] label p {
        font-size: 35px !important; 
        font-weight: bold !important;
        line-height: 1.5 !important;
    }

    /* රේඩියෝ බොත්තමේ රවුම ඉතා විශාල කිරීම */
    div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
        transform: scale(3.0) !important; /* 3 ගුණයකින් විශාල කර ඇත */
        margin-right: 30px !important;
        margin-left: 10px !important;
    }

    /* පිළිතුරු අතර පරතරය වැඩි කිරීම */
    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 30px !important;
        padding: 20px 0 !important;
    }

    /* 'මීළඟ ප්‍රශ්නය' බොත්තම විශාල කිරීම */
    .stButton > button {
        background-color: #2ecc71 !important;
        color: white !important;
        height: 80px !important;
        font-size: 30px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
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
    
    # ප්‍රශ්න 100 දක්වා පිරවීම
    for i in range(len(q_list) + 1, 101):
        num = i * 2
        q_list.append({
            "q": f"ප්‍රශ්න අංක {i}: {num} න් 10 ක් අඩු කළ විට ලැබෙන අගය කීයද?",
            "o": [f"{num-10}", f"{num+10}", f"{num}", f"{num-5}"],
            "a": f"{num-10}"
        })
    return q_list

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
    
    # පිළිතුරු තේරීම
    choice = st.radio("නිවැරදි පිළිතුර තෝරන්න:", current_q["o"], key=f"q{st.session_state.idx}")

    st.write("") # Space

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
    st.balloons()
    st.success("සියලු ප්‍රශ්න අවසන්! 🎉")
    st.markdown(f"""
        <div style='text-align: center; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);'>
            <h1 style='font-size: 50px;'>ඔබේ ලකුණු සංඛ්‍යාව</h1>
            <h1 style='font-size: 100px; color: #3498db;'>{st.session_state.score} / 100</h1>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("නැවත ආරම්භ කරන්න"):
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.done = False
        st.rerun()
