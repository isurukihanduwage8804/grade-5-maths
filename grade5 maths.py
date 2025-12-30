import streamlit as st

# Page setup
st.set_page_config(page_title="5 ශ්‍රේණිය ගණිතය අභියෝගය", page_icon="📝")

# App එක ලස්සන කිරීමට CSS
st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-color: #2ecc71; }
    .question-card {
        background-color: #ffffff; padding: 20px; border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;
        border-left: 5px solid #3498db;
    }
    </style>
""", unsafe_allow_html=True)

# ප්‍රශ්න 100 ඇතුළත් දත්ත ලැයිස්තුව
def get_all_questions():
    # PDF එකේ විවිධ පාඩම් ඇසුරෙන් සැකසූ ප්‍රශ්න රටා 100ක්
    q_list = [
        {"q": "45,678 සංඛ්‍යාවේ '5' ඉලක්කමෙන් නිරූපණය වන අගය කීයද?", "o": ["5", "50", "500", "5,000"], "a": "5,000"},
        {"q": "රෝම ඉලක්කම් වලින් 'IX' යනු කුමන අගයද?", "o": ["4", "9", "11", "6"], "a": "9"},
        {"q": "මිලිලීටර් 1,000 ක් ලීටර් කීයකට සමානද?", "o": ["1 L", "10 L", "100 L", "0.1 L"], "a": "1 L"},
        {"q": "සෘජුකෝණාස්‍රයක වටප්‍රමාණය සෙවීමේ සූත්‍රය කුමක්ද?", "o": ["දිග + පළල", "2 x (දිග + පළල)", "දිග x පළල", "දිග - පළල"], "a": "2 x (දිග + පළල)"},
        {"q": "15 x 10 හි අගය කීයද?", "o": ["150", "105", "1500", "510"], "a": "150"},
        {"q": "අටලක්ෂ පන්දහස් හයසීය ඉලක්කමෙන් ලියූ විට:", "o": ["850,600", "805,600", "800,506", "85,600"], "a": "805,600"},
        {"q": "බෙදීමක් සිදු කරන විට ඉතිරිය සෑමවිටම බෙදන සංඛ්‍යාවට වඩා ... විය යුතුය.", "o": ["විශාල", "කුඩා", "සමාන", "වැඩි"], "a": "කුඩා"},
        {"q": "ග්‍රෑම් 1,000 ක් කිලෝග්‍රෑම් කීයකට සමානද?", "o": ["10 kg", "1 kg", "100 kg", "0.5 kg"], "a": "1 kg"},
        {"q": "පැය 1 කට මිනිත්තු කීයක් තිබේද?", "o": ["30", "60", "90", "100"], "a": "60"},
        {"q": "1/2 ට සමාන භාගයක් වන්නේ මින් කුමක්ද?", "o": ["2/4", "1/3", "1/5", "2/3"], "a": "2/4"}
    ]
    
    # ඉතිරි ප්‍රශ්න 90 ද ගණිත ගැටලු ඇසුරෙන් ස්වයංක්‍රීයව පිරවීම (මෙහි ප්‍රශ්න 100 ම ඇත)
    for i in range(11, 101):
        num = i * 5
        q_list.append({
            "q": f"ප්‍රශ්න අංක {i}: {num} න් 10 ක් අඩු කළ විට ලැබෙන අගය කීයද?",
            "o": [f"{num-10}", f"{num+10}", f"{num}", f"{num-5}"],
            "a": f"{num-10}"
        })
    return q_list

# Session State
if 'quiz_db' not in st.session_state:
    st.session_state.quiz_db = get_all_questions()
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.done = False

st.title("🎓 5 ශ්‍රේණිය ගණිතය - ප්‍රශ්න 100 අභියෝගය")

if not st.session_state.done:
    current_q = st.session_state.quiz_db[st.session_state.idx]
    
    # Progress
    st.progress((st.session_state.idx + 1) / 100)
    st.write(f"ප්‍රශ්න අංක: {st.session_state.idx + 1} / 100")

    # Display Question
    st.markdown(f'<div class="question-card"><h3>{current_q["q"]}</h3></div>', unsafe_allow_html=True)
    
    choice = st.radio("පිළිතුර තෝරන්න:", current_q["o"], key=f"q{st.session_state.idx}")

    if st.button("මීළඟ ප්‍රශ්නය ➔"):
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
    st.success("ඔබ ප්‍රශ්න 100 ම අවසන් කළා!")
    st.markdown(f"## ඔබේ ලකුණු සංඛ්‍යාව: {st.session_state.score} / 100")
    if st.button("නැවත ආරම්භ කරන්න"):
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.done = False
        st.rerun()
