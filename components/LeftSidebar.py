import streamlit as st
from settings import AppConfig

class LeftSidebar:
    @staticmethod
    def render():
        with st.sidebar:
            LeftSidebar.render_logo()
            LeftSidebar.render_team_info()
            LeftSidebar.render_lecturers_info()
            LeftSidebar.render_contact_button()

    @staticmethod
    def render_logo():
        st.image("assets/images/hcmus_logo.png")

    @staticmethod
    def render_team_info():
        st.markdown("<h3 style='text-align: center;'>Sinh viên thực hiện đồ án</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<p style='text-align: center;'>Phạm Thành Nhân</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Huỳnh Nhật Nam</p>", unsafe_allow_html=True)

        with col2:
            st.markdown("<p style='text-align: center;'>Dương Trung Nghĩa</p>", unsafe_allow_html=True)

    @staticmethod
    def render_lecturers_info():
        st.markdown("<h3 style='text-align: center;'>Giảng viên hướng dẫn</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>GT.TS. Đinh Điền</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>TS. Nguyễn Hồng Bửu Long</p>", unsafe_allow_html=True)
    
    @staticmethod
    def render_contact_button():
        contact_url = "ptnhanit230104@gmail.com"
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <a href="mailto:{contact_url}" style="
                    background-color: blue;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;">
                    Liên hệ với chúng tôi
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )