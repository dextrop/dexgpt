import streamlit as st
from dexter.utils import upload_file
from dexter.config import APP_CONF, OPEN_AI_HELP

class ConfigureAppScreen():
    def __init__(self, conf=None, onSubmit=None):
        self.conf = conf
        if "app_conf" not in st.session_state:
            st.session_state.app_conf = {}

        if "onSubmit" not in st.session_state:
            st.session_state.onSubmit = onSubmit
        st.session_state.onSubmit = onSubmit

    def configure_resource(self, resource_type):

        if "resource" not in st.session_state.app_conf:
            st.session_state.app_conf["resource"] = {}
        st.session_state.app_conf["resource"] = {}

        resource_conf = APP_CONF["resources"][resource_type]

        st.session_state.app_conf["prompt"] = st.text_area(
            "Tell the AI something about the resource."
        )

        for key in resource_conf["inputs"]:
            curr_conf = {}
            if resource_conf["inputs"][key]["type"] == "file_uploader":
                curr_conf["type"] = "file"
                curr_conf["field_error"] = resource_conf["inputs"][key]["field_error"]
                curr_conf["value"] = st.file_uploader(
                    resource_conf["inputs"][key]["label"]
                )
            else:
                curr_conf["type"] = "text"
                curr_conf["field_error"] = resource_conf["inputs"][key]["field_error"]
                curr_conf["value"] = st.text_input(
                    resource_conf["inputs"][key]["label"]
                )

            st.session_state.app_conf["resource"][key] = curr_conf

    def validate_and_submit(self):
        st.session_state.app_conf["error"] = ""
        # Open AI Key Validation
        openaikey = str(st.session_state.app_conf["openai_api_key"])
        if not openaikey.startswith("sk-") or len(openaikey) != 51:
            st.session_state.app_conf["error"] = "Invalid Open AI API Key."
            return
        if "resource" in st.session_state.app_conf:
            resource = st.session_state.app_conf["resource"]
            for key in resource:
                value = resource[key]["value"]
                if value in [None, ""]:
                    st.session_state.app_conf["error"] = resource[key]["field_error"]
                    return

                if resource[key]["type"] == "file":
                    st.session_state.app_conf["resource"][key] = upload_file(value)
                else:
                    st.session_state.app_conf["resource"][key] = value

        if st.session_state.app_conf["resource_type"] != "None":
            prompt = ''''''
        st.session_state.onSubmit(
            st.session_state.app_conf
        )
        return

    @property
    def run(self):
        st.title("Create your own personal AI")
        if self.conf == None or "openai_api_key" not in self.conf:
            self.conf = {"openai_api_key": ""}

        st.session_state.app_conf["openai_api_key"] = st.text_input(
            "Input your Open AI Key", value=self.conf["openai_api_key"]
        )
        st.caption(OPEN_AI_HELP)
        resources = tuple(APP_CONF["resources"].keys())
        st.session_state.app_conf["resource_type"] = st.selectbox(
            'Select Resource for context!', resources
        )

        if st.session_state.app_conf["resource_type"] != "None":
            self.configure_resource(st.session_state.app_conf["resource_type"])

        if "error" in st.session_state.app_conf and st.session_state.app_conf["error"] != "":
            st.error(st.session_state.app_conf["error"])

        st.button(
            "Continue",
            on_click=self.validate_and_submit
        )
        return True