import streamlit as st
import webbrowser
from PIL import Image

st.title("MKFC")

# 명가 엠블럼 사진
# 사진 불러오기
image_mk = Image.open("IMG_2101.PNG")
# 사진 크기 조절하기
resized_image = image_mk.resize((600,250))
# 크기 조절한 사진 넣기
st.image(resized_image)

page = st.radio('',['홈', '선수단', '갤러리'])

# 홈
if page == '홈':
    # 헤더_사이트 제목
    st.header("⚽️명가FC 공식 홈페이지 입니다⚽️.")
    # 서브헤더_연혁
    st.subheader("Since 2020.05.01 ~ ")
    # 서브헤더
    #st.subheader("MK_FC")
    # 텍스트
    #st.write("명가 FC")
    # 마크다운
    #st.markdown("TEST")

    if st.button("@m__kfc"):
        webbrowser.open("https://www.instagram.com/m__kfc?igsh=ZWVlcWZtejB0aXhk")

    image = Image.open("명가FC.JPG")
    st.image(image, caption="명가 FC")

# 선수단
elif page == '선수단':
    st.title("🏃‍♂️‍➡️선수단")

    page2 = st.radio('', ['FW🔴', 'MF🟢', 'DF🔵', 'GK🟡'])

    if page2 == 'FW🔴':

        st.header("[FW]")
        st.subheader("전종석 (No.10)")
        image1 = Image.open("전종석.jpg")
        st.image(image1, width=150)
        st.write("Slogan : \'퇴물\'")

        #st.subheader("김선호")
        #st.subheader("김선용")
        #st.subheader("조형준")
        #st.subheader("심정현")
        #st.subheader("노창환")
        #st.subheader("김한빈")
        #st.subheader("김원빈")
        #st.subheader("이민기")
        #st.subheader("한정훈")
        st.subheader("홍세왕 (No.99)")
        image2 = Image.open("홍세왕.jpg")
        st.image(image2, width=150)
        st.write("Slogan : \'한반도프스키\'")

    elif page2 == 'MF🟢':
        st.header("[MF]")
        st.subheader("허언강 (No.8)")
        image3 = Image.open("허언강.jpg")
        st.image(image3, width=150)
        st.write("Slogan : \'명가FC 화이팅!\'")
        st.subheader("강진욱 (No.18)")
        image4 = Image.open("강진욱.jpg")
        st.image(image4, width=150)
        st.write("Slogan : \'28세 돌싱남\'")
        #st.subheader("김종학")

    elif page2 == 'DF🔵':
        st.header("[DF]")
        st.subheader("허사강[C] (No.14)")
        image5 = Image.open("허사강.jpg")
        st.image(image5, width=150)
        st.write("Slogan : \'오빠랑 비밀친구할까?\'")
        #st.subheader("유호석")
        st.subheader("김용수 (No.25)")
        image6 = Image.open("김용수.jpg")
        st.image(image6, width=150)
        st.write("Slogan : \'나가자 해병대\'")
        #st.subheader("정연목")

    elif page2 == 'GK🟡':
        st.header("[GK]")

elif page == '갤러리':
    st.title("📷갤러리")

    page3 = st.radio('',['풋살', '축구', '워크샾'])

    if page3 == '풋살':
        st.header("[풋살 자체전]")
    elif page3 == '축구':
        st.header("[축구 매칭]")
    elif page3 == '워크샾':
        st.header("[정기 워크샾]")
        st.subheader("제 1회 워크샾")
        image6 = Image.open("1회 워크샾.jpg")
        st.image(image6, width=600)
        st.subheader("제 2회 워크샾")
        image7 = Image.open("2회 워크샾.jpg")
        st.image(image7, width=600)
        st.subheader("제 3회 워크샾")
        image8 = Image.open("3회 워크샾.jpg")
        st.image(image8, width=600)
        st.subheader("제 4회 워크샾")
        image9 = Image.open("4회 워크샾.jpg")
        st.image(image9, width=600)
        


