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

class ResourceLoader():
    def load_text(self, conf):
        """Load text content directly."""
        loader = Document(page_content=conf["text"])
        return loader.load()

    def load_airtable(self, configration):
        """Load data from Airtable."""
        loader = AirtableLoader(configration["api_key"], configration["table_id"], configration["base_id"])
        return loader.load()

    def load_blockchain(self, conf):
        """Load data from blockchain document."""
        blockchain_loader = BlockchainDocumentLoader(
            contract_address=conf["contract_address"], api_key=conf["api_key"]
        )
        return blockchain_loader.load()

    def load_confluence(self, conf):
        """Load data from Confluence."""
        loader = ConfluenceLoader(url=conf["doc_link"], username="me", api_key=conf["api_key"])
        return loader.load()

    def load_excel(self, conf):
        """Load data from an unstructured Excel file."""
        loader = UnstructuredExcelLoader(conf["file"], mode="elements")
        return loader.load()

    def load_gitbook(self, conf):
        """Load data from Gitbook."""
        loader = GitbookLoader(conf["link"])
        return loader.load()

    def load_ppt(self, conf):
        """Load data from an unstructured PowerPoint file."""
        loader = UnstructuredPowerPointLoader(conf["file"])
        return loader.load()

    def load_docx(self, conf):
        """Load data from DOCX format."""
        loader = Docx2txtLoader(conf["file"])
        return loader.load()

    def load_odt(self, conf):
        """Load data from ODT format."""
        loader = UnstructuredODTLoader(conf["file"], mode="elements")
        return loader.load()

    def load_youtube_transcript(self, conf):
        """Load transcript from a YouTube link."""
        loader = YoutubeLoader.from_youtube_url(
            conf["link"], add_video_info=True, language=["en", "id"], translation="en"
        )
        return loader.load()

    def load_web_link(self, conf):
        """Load data from a web link."""
        loader = WebBaseLoader(str(conf["link"]).split(","))
        return loader.load()

    def load_wikipedia(self, conf):
        """Load data from Wikipedia based on a topic."""
        loader = WikipediaLoader(query=conf["topic"], load_max_docs=2)
        return loader.load()

    def load_pdf(self, conf):
        """Load data from an unstructured PDF file."""
        loader = UnstructuredPDFLoader(conf["file"])
        return loader.load()

    def load_github_issue(self, conf):
        """Load GitHub issues from a repository."""
        loader = GitHubIssuesLoader(repo=conf["repo"], access_token=conf["token"])
        return loader.load()

    def load_csv(self, conf):
        """Load data from a CSV file."""
        loader = CSVLoader(conf["file"])
        return loader.load()


resourcehandler = ResourceLoader()
RESOURCE_LOADER = {
    "airtable": resourcehandler.load_airtable,
    "pdf": resourcehandler.load_pdf,
    "blockchain": resourcehandler.load_blockchain,
    "confluence": resourcehandler.load_confluence,
    "excel": resourcehandler.load_excel,
    "gitbook": resourcehandler.load_gitbook,
    "odt": resourcehandler.load_odt,
    "youtube": resourcehandler.load_youtube_transcript,
    "ppt": resourcehandler.load_ppt,
    "github": resourcehandler.load_github_issue,
    "csv": resourcehandler.load_csv,
    "link": resourcehandler.load_web_link,
    "wiki": resourcehandler.load_wikipedia
}