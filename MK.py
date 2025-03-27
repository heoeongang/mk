import streamlit as st  # streamlit 불러오기
import webbrowser       # 웹브라우저 열기위해 불러오기
from PIL import Image   # 이미지 삽입하기 위해 불러오기

# 홈페이지 제목 설정
st.title("⚽️MKFC⚽️")

# 명가 엠블럼 사진 불러오기
image_mk1 = Image.open("IMG_2100.PNG")
image_mk2 = Image.open("IMG_2099.PNG")

# 사진, 글 배치하기
col1 = st.columns(3)
with col1[0]:
    st.image(image_mk1)
with col1[1]:
    st.image(image_mk2)
    st.subheader("   Since 200501   ")
    st.write("명가 FC 공식 홈페이지 입니다.")
with col1[2]:
    if st.button("@m__kfc"):
        st.markdown('(https://www.instagram.com/m__kfc?igsh=ZWVlcWZtejB0aXhk)', unsafe_allow_html=True)
        #webbrowser.open("https://www.instagram.com/m__kfc?igsh=ZWVlcWZtejB0aXhk")

# 페이지 배치하기
page = st.radio("", ["HOME🏠", "유니폼👕", "선수단👤", "갤러리📷"])
st.write("")

if page == 'HOME🏠':
    image_home = Image.open("명가FC.jpg")
    st.image(image_home, caption = "[명가 FC]")
elif page == "유니폼👕":
    uniform = st.radio("", ["홈", "어웨이"])
    col_uniform = st.columns(2)
    if uniform == '홈':
        with col_uniform[0]:
            st.markdown("<h4 style='text-align: left;'>[앞]</h4>", unsafe_allow_html=True)
            image = Image.open("홈_앞.PNG")
            st.image(image, width = 250)
        with col_uniform[1]:
            st.markdown("<h4 style='text-align: left;'>[뒤]</h4>", unsafe_allow_html=True)
            image = Image.open("홈_뒤.PNG")
            st.image(image, width = 250)
    elif uniform == '어웨이':
        col_uniform = st.columns(2)
        with col_uniform[0]:
            st.markdown("<h4 style='text-align: left;'>[앞]</h4>", unsafe_allow_html=True)
        with col_uniform[1]:
            st.markdown("<h4 style='text-align: left;'>[뒤]</h4>", unsafe_allow_html=True)
        image = Image.open("어웨이.png")
        st.image(image, width = 1000)

elif page == '선수단👤':
    st.header("선수현황 [00명]")

    position = st.selectbox("포지션을 선택하세요", ['FW🔴', 'MF🟢', 'DF🔵', 'GK🟡'])

    if position == 'FW🔴':
        st.header("[FW]")
        st.write("")

        col_FW1 = st.columns(3)
        col_FW2 = st.columns(3)

        with col_FW1[0]:
            st.markdown("<h5 style='text-align: center;'>조형준 [총무] (No.9)</h5>", unsafe_allow_html=True)
            image1 = Image.open("조형준2.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"안녕 난 쭈니야😘\"</h6>", unsafe_allow_html=True)

        with col_FW1[1]:
            st.markdown("<h5 style='text-align: center;'>전종석 (No.10)</h5>", unsafe_allow_html=True)
            image1 = Image.open("전종석.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"퇴물\"</h6>", unsafe_allow_html=True)

        with col_FW1[2]:
            st.markdown("<h5 style='text-align: center;'>홍세왕 (No.99)</h5>", unsafe_allow_html=True)
            image1 = Image.open("홍세왕.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"한반도프스키\"</h6>", unsafe_allow_html=True)

        with col_FW2[0]:
            st.markdown("<h5 style='text-align: center;'>김한빈 (No.19)</h5>", unsafe_allow_html=True)
            image1 = Image.open("김한빈.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"------\"</h6>", unsafe_allow_html=True)

    elif position == 'MF🟢':
        st.header("[MF]")
        st.write("")

        col_MF1 = st.columns(3)
        col_MF2 = st.columns(3)

        with col_MF1[0]:
            st.markdown("<h5 style='text-align: center;'>허언강 (No.8)</h5>", unsafe_allow_html=True)
            image1 = Image.open("허언강.JPG")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"말좀하자 제발\"</h6>", unsafe_allow_html=True)

        with col_MF1[1]:
            st.markdown("<h5 style='text-align: center;'>강진욱 (No.18)</h5>", unsafe_allow_html=True)
            image1 = Image.open("강진욱.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"28세 돌싱남입니다.\"</h6>", unsafe_allow_html=True)

        with col_MF1[2]:
            st.markdown("<h5 style='text-align: center;'>이민기 (No.23)</h5>", unsafe_allow_html=True)
            image1 = Image.open("이민기.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"부평 항시대기중\"</h6>", unsafe_allow_html=True)
        
        with col_MF2[0]:
            st.markdown("<h5 style='text-align: center;'>김종학 (No.2)</h5>", unsafe_allow_html=True)
            image1 = Image.open("김종학.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"-------\"</h6>", unsafe_allow_html=True)


    elif position == 'DF🔵':
        st.header("[DF]")
        st.write("")

        col_DF1 = st.columns(3)

        with col_DF1[0]:
            st.markdown("<h5 style='text-align: center;'>허사강[C] (No.14)</h5>", unsafe_allow_html=True)
            image1 = Image.open("허사강2.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"패스 빠르게.\"</h6>", unsafe_allow_html=True)

        with col_DF1[1]:
            st.markdown("<h5 style='text-align: center;'>김용수 (No.25)</h5>", unsafe_allow_html=True)
            image1 = Image.open("김용수.jpg")
            image2 = image1.resize((200,200))
            st.image(image2)
            st.markdown("<h6 style='text-align: center;'>Slogan : \"나가자 해병대\"</h6>", unsafe_allow_html=True)

        # with col_DF1[2]:
        #     st.markdown("<h5 style='text-align: center;'>이민기 (No.23)</h5>", unsafe_allow_html=True)
        #     image1 = Image.open("이민기.jpg")
        #     image2 = image1.resize((200,200))
        #     st.image(image2)
        #     st.markdown("<h6 style='text-align: center;'>Slogan : \"부평 항시대기중\"</h6>", unsafe_allow_html=True)

    elif position == 'GK🟡':
        st.header("[GK]")
        st.write("None")
