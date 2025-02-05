import json
import pandas as pd
import streamlit as st

# Streamlit 앱 레이아웃 설정
st.set_page_config(page_title="오늘의 영어 표현", layout="wide")

# 앱 제목 및 설명
st.title('오늘의 영어 단어 추천',)


@st.cache_data
def load_data():
    df = pd.read_excel("./words.xlsx")
    #Json string 타입의 값. 각각의 row를 load하여 dictionary 형태로 변환.
    df["usage"] = df.apply(lambda row: json.loads(row["usage"]), axis=1)
    return df


df = load_data()

for i, sample in df.iterrows():
    with st.container(border=True):
        st.subheader(f"{sample['imoj']} {sample['word']}")

        # situation 의 영단어의 뜻 
        st.markdown(sample["meaning"])

        with st.container(border=True):
            """사용법 usage"""

            for i, row in enumerate(sample["usage"]["conversation"]):
                avatar = '🧑' if i % 2 == 0 else '👩🏼'
                with st.chat_message(avatar):
                    st.markdown(row['content'])
