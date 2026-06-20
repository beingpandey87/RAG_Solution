# This file is part of the LangChain project.
from dotenv import load_dotenv
load_dotenv()

import os
import tempfile
from pathlib import Path

'''
`langchain-community` is being sunset and is no longer actively maintained. 
'''
#from langchain_community.document_loaders import TextLoader



from langchain_core.documents import Document 
import pymupdf

def load_text_file(file_path):
    """
    Load a text file and return its content as a list of Document objects.
    Args:
        file_path (str): The path to the text file to load.
    Returns:
        document (Document): object of type Document with page content and metadata including source, file_name, file_extension, file_size, last_modified, created_time.
    """
    
        # Load the text file using TextLoader
    with open(file_path, "r") as file:
        content = file.read()

    return [
        Document(
            page_content=content, 
            metadata={
                "source": str(file_path),
                "file_name": file_path.name,
                "file_extension": file_path.suffix,
                "file_size": file_path.stat().st_size, 
                "last_modified": file_path.stat().st_mtime, 
                "created_time": file_path.stat().st_ctime}
        )
    ]
    
def doc_structure(file_path: str, encoding: str = "utf-8"):
    """
    Load a text file and return it as a LangChain Document object.
    Args:
        file_path (str): The path to the text file to load.
        encoding (str): The encoding of the text file. Defaults to "utf-8".
    Returns:
        document object (Document): Page content and 
        metadata including source, file_name, file_extension, file_size, last_modified, created_time.
    Raises:
    """
    path = Path(file_path)
    
    # Read the file's text content
    text_content = path.read_text(encoding=encoding)
    
    # Create the Document object with page content and source metadata
    return [
        Document(
            page_content=text_content, 
            metadata={
                "source": str(path),
                "file_name": path.name,
                "file_extension": path.suffix,
                "file_size": path.stat().st_size, 
                "last_modified": path.stat().st_mtime, 
                "created_time": path.stat().st_ctime}
        )
    ]

def pdf_loader(pdf_path: str):
    
    # Open the PDF using PyMuPDF's internal document loader
    fitz_doc = pymupdf.open(pdf_path)
    document_objects = []
    
    # Loop through pages and store each as a Document object
    for page_num, page in enumerate(fitz_doc):
        text = page.get_text("text")  # Extract clean layout text
        
        # Instantiate a formal Document object
        doc_obj = Document(
            page_content=text,
            metadata={"source": pdf_path, "page": page_num + 1,"content_len": len(text)}
        )
        document_objects.append(doc_obj)
        
    fitz_doc.close()
    return document_objects

if __name__ == "__main__":   
    # Example text usage:
    file_path = "docs/sample.txt"
    documents = doc_structure(file_path)

    print(documents[0].page_content)
    print(documents[0].metadata)

    file_path = "docs/git_cheat.pdf"
    pdf_documents = pdf_loader(file_path)
    for doc in pdf_documents:
        print(doc.page_content)
        print(doc.metadata)
