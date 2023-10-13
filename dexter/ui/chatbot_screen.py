import streamlit as st

class AIAssistantChatbotScreen():
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                {
                    "role": "assistant",
                    "content": "Hey I am your AI Assistant, How can i help you today?"
                }
            ]

    def run(self, ai_assistant):
        """
        Assistant Chatbot Screen
        :param ai_assistant: LLM Chain to be used by chatbot.
        :return: None
        """
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = ai_assistant.run(prompt)
            st.session_state.messages.append({"role": "assistant", "content": str(response)})
            st.chat_message("assistant").write(str(response))