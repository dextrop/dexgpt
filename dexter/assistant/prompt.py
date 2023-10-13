from langchain.prompts import PromptTemplate
from dexter.config import RESOURCE_PROMPT_STRUCTURE, GENERAL_PROMPT_STRUCTURE

def generate_prompt(prompt_text="", does_contain_resource=False):
    """
    Generate prompt for resource type chain and non resource type chain.
    :param prompt_text: Context provided by user
    :param does_contain_resource: boolean "does contain resource?"
    :return: PromptTemplate
    """
    input_variables = ["question"]
    template = GENERAL_PROMPT_STRUCTURE
    if does_contain_resource:
        input_variables = ["context", "question"]
        template = RESOURCE_PROMPT_STRUCTURE.replace(
            "PROMPT_FROM_USER", prompt_text
        )

    return PromptTemplate(
            template=template,
            input_variables=input_variables
        )




