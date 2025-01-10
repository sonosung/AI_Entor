import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("hello!")

with st.chat_message("assistant"):
    st.write("hello user!")
    st.bar_chart(np.random.randn(30,3))

# message = st.chat_message("assistant")      #특정 영역을 차지하여 place holder 의 역할을 함. 
# message.write("hello human")              #message 변수를 선언한 이후 코드를 수행하고,
# message.bar_chart(np.random.randn(30,3))  #나중에 정보를 업데이트 할 경우에 이 방식으로 변경이 가능함.

prompt = st.chat_input("Ask me any question!")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)