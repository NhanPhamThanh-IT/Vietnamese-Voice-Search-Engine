import streamlit as st

class PageHeader:
    @staticmethod
    def render(title: str, description: str):
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h1>{title}</h1>
                <p style="font-size: 18px;">{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
