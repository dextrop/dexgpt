GENERAL_PROMPT_STRUCTURE = '''You are a simple AI Assistant\n\nQuestion: {question}\nAnswer :'''

RESOURCE_PROMPT_STRUCTURE = '''Go through the below context and reply based on the same.
{context}

Also this is the relevent information for the context 
PROMPT_FROM_USER
Summarize the above details in a structured format, when user ask about any information from the CV reply back

Make sure when you replying back to user reply as his assistant.
{question}'''

INPUTS_CONF = {
    "pdf": {
        "type": "file_uploader",
        "label": "Upload PDF resource for the context",
        "field_error": "Missing PDF file for context"
    },
    "wiki": {
        "type": "text",
        "label": "Name your topic",
        "field_error": "Must input at least 1 topic name"
    },
    "link": {
        "type": "text",
        "label": "Provide the https Link for your context",
        "field_error": "Missing link for context"
    },
    "youtube": {
        "type": "text",
        "label": "Provide your youtube link",
        "field_error": "Missing link for context"
    }
}

APP_CONF = {
    "resources": {
        "None": None,
        "PDF": {
            "default_prompt": "",
            "prompt_should_include": ["{context}", "{question}"],
            "inputs": {
                "file": INPUTS_CONF["pdf"]
            }
        },
        "Link": {
            "default_prompt": "",
            "prompt_should_include": ["{context}", "{question}"],
            "inputs": {
                "link": INPUTS_CONF["link"]
            }
        },
        "Wiki": {
            "default_prompt": "",
            "prompt_should_include": ["{context}", "{question}"],
            "inputs": {
                "topic": INPUTS_CONF["wiki"]
            }
        }
    }
}

OPEN_AI_HELP = "Lets start by setting up Base LLM Model. Currently we are using Open AI ChatGPT 3.5 as base Model. Input you open AI key to get started, If you dont have an openai key get it from [here](https://platform.openai.com/account/api-keys)"
