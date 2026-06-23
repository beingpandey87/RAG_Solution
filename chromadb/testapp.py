import chromadb
client = chromadb.Client()

collecion_name = "test_collection"
collection = client.create_collection(name=collecion_name)

documents=[
    {"id": "doc1", "text": "Hello world!"},
    {"id": "doc2", "text": "How are you doing today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

for doc in documents:
    collection.upsert(
        documents=[doc["text"]],
        ids=doc["id"]
    )
# to run the query you need to install onnxruntime
# and also install the latest c++ msr package from link : 
# https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-supported-redistributable-version
query_texts = "Hello world!"
results = collection.query(query_texts=[query_texts],n_results=3)
print(results) 