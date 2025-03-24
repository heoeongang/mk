import streamlit as st
import webbrowser
from PIL import Image

page = st.radio('[페이지를 선택하세요] : ', ['홈', '선수단', '갤러리'])

# 홈
if page == '홈':
    # 사이트 제목
    st.title("⚽️명가 FC 공식 홈페이지 입니다⚽️.")
    # 헤더_연혁
    st.header("Since 2020.05.01 ~ ")
    # 서브헤더
    #st.subheader("MK_FC")
    # 텍스트
    #st.write("명가 FC")
    # 마크다운
    #st.markdown("TEST")

    if st.button("@m__kfc"):
        webbrowser.open("https://www.instagram.com/m__kfc?igsh=ZWVlcWZtejB0aXhk")

    image = Image.open("IMG_2908.JPG")
    st.image(image, caption="명가 FC")

# 선수단
elif page == '선수단':
    st.title("🏃‍♂️‍➡️선수단")

    page2 = st.radio('[포지션을 선택하세요] : ', ['FW🔴', 'MF🟢', 'DF🔵', 'GK🟡'])

    if page2 == 'FW🔴':

        st.header("[FW]")
        st.subheader("전종석")
        image1 = Image.open("IMG_2949.jpg")
        st.image(image1, caption = "병신ㅋㅋ", width=100)

        st.subheader("김선호")
        st.subheader("김선용")
        st.subheader("조형준")
        st.subheader("심정현")
        st.subheader("노창환")
        st.subheader("김한빈")
        st.subheader("김원빈")
        st.subheader("이민기")
        st.subheader("한정훈")
        st.subheader("홍세왕")

    elif page2 == 'MF🟢':
        st.header("[MF]")
        st.subheader("허언강")
        st.subheader("강진욱")
        st.subheader("김종학")

    elif page2 == 'DF🔵':
        st.header("[DF]")
        st.subheader("허사강[C]")
        st.subheader("유호석")
        st.subheader("김용수")
        st.subheader("정연목")

    elif page2 == 'GK🟡':
        st.header("[GK]")

elif page == '연락처':
    st.title("연락처")

