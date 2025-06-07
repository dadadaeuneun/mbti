import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

st.title("📚 MBTI별 국어 과목 성취도 분석")
st.write("당신의 MBTI 유형은 국어 과목에서 어떤 성취도를 보일까요? 아래에서 MBTI 유형을 선택해주세요!")

# Hypothetical data for Korean language achievement by MBTI type
# You can replace this with actual data if available
mbti_data = {
    "ISTJ": {"평균 점수": 85, "이해도": "높음 🧐", "문제 해결 능력": "우수 👍", "서술형 강점": "정확성 높은 답변"},
    "ISFJ": {"평균 점수": 88, "이해도": "매우 높음 😇", "문제 해결 능력": "탁월 💯", "서술형 강점": "세심하고 구체적인 답변"},
    "INFJ": {"평균 점수": 90, "이해도": "심오함 ✨", "문제 해결 능력": "창의적 💡", "서술형 강점": "깊이 있는 통찰력"},
    "INTJ": {"평균 점수": 92, "이해도": "논리적 🧠", "문제 해결 능력": "전략적 🎯", "서술형 강점": "체계적이고 명확한 논리"},
    "ISTP": {"평균 점수": 80, "이해도": "실용적 🛠️", "문제 해결 능력": "직관적 👀", "서술형 강점": "간결하고 핵심적인 답변"},
    "ISFP": {"평균 점수": 83, "이해도": "감성적 💖", "문제 해결 능력": "유연함 🤸", "서술형 강점": "풍부한 표현력"},
    "INFP": {"평균 점수": 87, "이해도": "사색적  contemplation", "문제 해결 능력": "개방적 🍃", "서술형 강점": "독창적이고 다양한 관점"},
    "INTP": {"평균 점수": 91, "이해도": "분석적 🔬", "문제 해결 능력": "논리적 📈", "서술형 강점": "복잡한 개념의 명확한 설명"},
    "ESTP": {"평균 점수": 78, "이해도": "활동적 🏃", "문제 해결 능력": "빠른 판단 ⚡", "서술형 강점": "명료하고 설득력 있는 답변"},
    "ESFP": {"평균 점수": 81, "이해도": "표현력 풍부 🎤", "문제 해결 능력": "적응력 강함  chameleon", "서술형 강점": "생동감 있고 구체적인 예시"},
    "ENFP": {"평균 점수": 89, "이해도": "열정적 🔥", "문제 해결 능력": "다각적 🌈", "서술형 강점": "흥미롭고 창의적인 아이디어"},
    "ENTP": {"평균 점수": 93, "이해도": "통찰력 있음 🌟", "문제 해결 능력": "혁신적 🚀", "서술형 강점": "논리적 비약과 기발한 전개"},
    "ESTJ": {"평균 점수": 86, "이해도": "체계적 🗂️", "문제 해결 능력": "조직적 📊", "서술형 강점": "명확하고 구조화된 답변"},
    "ESFJ": {"평균 점수": 89, "이해도": "공감 능력 우수 🤗", "문제 해결 능력": "협력적 🤝", "서술형 강점": "친근하고 이해하기 쉬운 설명"},
    "ENFJ": {"평균 점수": 91, "이해도": "리더십 👑", "문제 해결 능력": "영향력 🗣️", "서술형 강점": "설득력 있고 감동적인 답변"},
    "ENTJ": {"평균 점수": 94, "이해도": "결단력 👍", "문제 해결 능력": "효율적 ✅", "서술형 강점": "강력하고 설득력 있는 논증"},
}

# MBTI types for the selectbox
mbti_types = list(mbti_data.keys())

# Selectbox for MBTI type
selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

st.write("---")

if selected_mbti:
    st.subheader(f"✨ **{selected_mbti}** 유형의 국어 과목 성취도")
    
    # Get data for the selected MBTI type
    data = mbti_data[selected_mbti]
    
    # Create a DataFrame for better table presentation
    df = pd.DataFrame([data]).T
    df.columns = ["성취도 내용"]
    
    st.table(df)

    st.write(f"*{selected_mbti} 유형은 국어 과목에서 위와 같은 특징을 보일 수 있습니다. 이는 가상 데이터이며, 실제 성취도와는 다를 수 있습니다.*")
