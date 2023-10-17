from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from dexter.assistant.resources import RESOURCE_LOADER
from langchain.chains import RetrievalQA, LLMChain
from dexter.assistant.prompt import generate_prompt
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

class Dexter():
    def __init__(self, conf):
        """
        Main Chatbot Class responsible for loading resource and creating LLMChain.
        :param conf: {
            'openai_api_key': '<Open AI API Key>',
            'resource_type': '<Selected Resource Type>',
            'resource': {<Resource Configration>},
            'prompt': '<User Prompt>',
            'error': '<Error If Any>'
        }
        """
        print (conf)
        self.llm = OpenAI(temperature=0, openai_api_key=conf["openai_api_key"], model_name="gpt-3.5-turbo")
        self.vector = self.load_resource(conf)

        # If Resource is available then generate prompt.
        if self.vector:
            self.chain_type_kwargs = {
                "prompt": generate_prompt(
                    conf["prompt"], ["context", "question"]
                )
            }

    def load_resource(self, conf):
        """
        Load Resource
        :param conf: {
            'openai_api_key': '<Open AI API Key>',
            'resource_type': '<Selected Resource Type>',
            'resource': {<Resource Configration>},
            'prompt': '<User Prompt>',
            'error': '<Error If Any>'
        }
        :return:
        """
        if conf["resource_type"] == "None":
            return None

        handler = RESOURCE_LOADER[conf["resource_type"].lower()]
        resource_data = handler(conf["resource"])
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(resource_data)
        embeddings = OpenAIEmbeddings(openai_api_key=conf["openai_api_key"])
        return Chroma.from_documents(texts, embeddings, collection_name="agent_resource")

    @property
    def bot(self):
        """
        Create a bot using AI configration.
        :param conf: {
            'openai_api_key': '<Open AI API Key>',
            'resource_type': '<Selected Resource Type>',
            'resource': {<Resource Configration>},
            'prompt': '<User Prompt>',
            'error': '<Error If Any>'
        }
        :return:
        """

        # If vector is not none, return RetrievalQA with vector as retriever
        if self.vector:
            return RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever = self.vector.as_retriever(),
                chain_type_kwargs=self.chain_type_kwargs
            )
        else:
            return LLMChain(
                llm=self.llm,
                prompt=generate_prompt(),
            )