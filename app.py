import streamlit as st

st.markdown("# 앱 UI 만들기")
st.header("이름")
이름 = st.text_input(" ", placeholder="name_on_here")

st.header("학년)
학년 = st.radio(" ", [1, 2, 3], hrizontal=True)

st.header("반")
반 = st.slectbox(" ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

st.header("난이도")
난이도 = st.slect_slider(" ", options=["매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"])

st.header("점수")
점수 = st.slider(" ", 0, 100, 1)

st.header("소감")
소감 = st.text_area(" ", placeholder="소감입니다.")

if st.button("확인"):
  st.markdown(f"{이름}/{학년}학년/{반}반/{난이도}")
  st.markdown(f"점수: {점수}")
  st.markdown(f"소감: {소감}}")





