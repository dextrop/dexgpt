from langchain.document_loaders import (
    GitHubIssuesLoader,
    UnstructuredPDFLoader,
    WikipediaLoader,
    WebBaseLoader,
    YoutubeLoader,
    UnstructuredODTLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
    GitbookLoader,
    UnstructuredExcelLoader,
    ConfluenceLoader,
    AirtableLoader,
)
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders.blockchain import BlockchainDocumentLoader
from langchain.docstore.document import Document

def load_text(conf):
    """Load text content directly."""
    loader = Document(page_content=conf["text"])
    return loader.load()

def load_airtable(configration):
    """Load data from Airtable."""
    loader = AirtableLoader(configration["api_key"], configration["table_id"], configration["base_id"])
    return loader.load()

def load_blockchain(conf):
    """Load data from blockchain document."""
    blockchain_loader = BlockchainDocumentLoader(
        contract_address=conf["contract_address"], api_key=conf["api_key"]
    )
    return blockchain_loader.load()

def load_confluence(conf):
    """Load data from Confluence."""
    loader = ConfluenceLoader(url=conf["doc_link"], username="me", api_key=conf["api_key"])
    return loader.load()

def load_excel(conf):
    """Load data from an unstructured Excel file."""
    loader = UnstructuredExcelLoader(conf["file"], mode="elements")
    return loader.load()

def load_gitbook(conf):
    """Load data from Gitbook."""
    loader = GitbookLoader(conf["link"])
    return loader.load()

def load_ppt(conf):
    """Load data from an unstructured PowerPoint file."""
    loader = UnstructuredPowerPointLoader(conf["file"])
    return loader.load()

def load_docx(conf):
    """Load data from DOCX format."""
    loader = Docx2txtLoader(conf["file"])
    return loader.load()

def load_odt(conf):
    """Load data from ODT format."""
    loader = UnstructuredODTLoader(conf["file"], mode="elements")
    return loader.load()

def load_youtube_transcript(conf):
    """Load transcript from a YouTube link."""
    loader = YoutubeLoader.from_youtube_url(
        conf["link"], add_video_info=True, language=["en", "id"], translation="en"
    )
    return loader.load()

def load_web_link(conf):
    """Load data from a web link."""
    loader = WebBaseLoader(str(conf["link"]).split(","))
    return loader.load()

def load_wikipedia(conf):
    """Load data from Wikipedia based on a topic."""
    loader = WikipediaLoader(query=conf["topic"], load_max_docs=2)
    return loader.load()

def load_pdf(conf):
    """Load data from an unstructured PDF file."""
    loader = UnstructuredPDFLoader(conf["file"])
    return loader.load()

def load_github_issue(conf):
    """Load GitHub issues from a repository."""
    loader = GitHubIssuesLoader(repo=conf["repo"], access_token=conf["token"])
    return loader.load()

def load_csv(conf):
    """Load data from a CSV file."""
    loader = CSVLoader(conf["file"])
    return loader.load()