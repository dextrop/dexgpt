import streamlit as st
from dexter.ui.configration_screen import ConfigureAppScreen
from dexter.assistant import Dexter
from dexter.ui.chatbot_screen import AIAssistantChatbotScreen

class MainApp():
    def __init__(self):
        """
        States : 1: Configration State, 2: Chatbot State.
        """
        if "state" not in st.session_state:
            st.session_state.state = 0

        if "app_config" not in st.session_state:
            st.session_state.app_config = {
                "openai_api_key": "",
                "resource_type": "Link",
                "prompt": "The context is an medium article",
                "error": ""
            }

        BASIC_CSS = '''<style>{}</style>'''.format(
            open("assets/style.css").read()
        )
        st.markdown(BASIC_CSS, unsafe_allow_html=True)

    def start_chatbot(self, app_config):
        if "bot" not in st.session_state:
            st.session_state.bot = None

        st.session_state.app_config = app_config
        st.session_state.bot = Dexter(
            conf = st.session_state.app_config
        ).bot
        st.session_state.state = 1

    def configure_again(self):
        st.session_state.state = 0
        st.session_state.app_config = {
            "openai_api_key": st.session_state.app_config["openai_api_key"],
            "resource_type": "None",
            "prompt": "",
            "error": ""
        }

    def run(self):
        if st.session_state.state == 0:
            resp = ConfigureAppScreen(st.session_state.app_config, onSubmit=self.start_chatbot).run
        elif st.session_state.state == 1:
            col_1, col_2 = st.columns(2)
            with col_1:
                st.subheader("AI Assistant is ready to work")

            with col_2:
                st.button("Reset", on_click=self.configure_again)

            AIAssistantChatbotScreen().run(
                st.session_state.bot
            )

MainApp().run()