import streamlit as st

st.markdown("# 앱 UI 만들기")

st.header("이름")
이름 = st.text_input(" ", placeholder="name_on_here")

st.header("학년") # 수정: 닫는 따옴표 추가
학년 = st.radio(" ", [1, 2, 3], horizontal=True) # 수정: horizontal 오타 수정

st.header("반")
반 = st.selectbox(" ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 수정: selectbox 오타 수정

st.header("난이도")
난이도 = st.select_slider(" ", options=["매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"]) # 수정: select_slider 오타 수정

st.header("점수")
점수 = st.slider(" ", 0, 100, 1)

st.header("소감")
소감 = st.text_area(" ", placeholder="소감입니다.")

if st.button("확인"):
    st.markdown(f"{이름}/{학년}학년/{반}반/{난이도}")
    st.success(f"점수: {점수}")
    st.error(f"소감: {소감}") # 수정: 중복된 중괄호 삭제
