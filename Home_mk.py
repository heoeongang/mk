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

    st.subheader("[ST]")
    st.write("전종석")
    image1 = Image.open("IMG_2949.jpg")
    st.image(image1, caption = "병신ㅋㅋ", width=100)

    st.subheader("[MF]")
    st.write("허언강")

    st.subheader("[DF]")
    st.write("허사강[C]")

    st.subheader("[GK]")

elif page == '연락처':
    st.title("연락처")

