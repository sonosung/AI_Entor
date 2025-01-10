import streamlit as st

st.title("AI English Tutor is Here!")
st.subheader("All you can learn about Englsh!")
st.write("hello world!")

# #markdown 형식으로 글쓰기!
# """
# # This is title
# ## This is sub title
# ### This is our content

# - First
# - Second
# - Third

# """

#다양한 input 방식
text = st.text_input("text input")
st.write(text)

gender = st.selectbox('성별', ('male', 'female'))
st.write(f"gender: {gender}")

#Checkbox!
selected = st.checkbox("Do you agree?")

if selected:
    st.success("You've agreed")


options = st.multiselect('취미', ['음악 감상', '독서', '게임'])
st.write(', '.join(options)) #list 형식의 결과물을 text 형식으로 변환후, ','로 join함.

#Layouts
with st.sidebar:
    add_radio = st.radio("language", ("Korean", "English"))

#column 형식
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")


#tab 형식
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)