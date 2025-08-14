import os



from langchain.embeddings import VertexAIEmbeddings

from langchain.llms import VertexAI

from langchain.document_loaders import GCSDirectoryLoader

 

# Chroma DB as Vector Store Database

from langchain.vectorstores import Chroma
import os
 

# Using Vertex AI

import vertexai

from google.cloud import aiplatform

 # Get the directory of the current script
#dir_path = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path of the credentials file in the secrets directory
#credentials_path = os.path.join(dir_path, 'secrets', 'credentials.json')

# Set the environment variable to the credentials file path
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

PROJECT_ID = "gbg-neuro"  # @param {type:"string"}

 

LOCATION = "us-central1"  # @param {type:"string"}

 

# Initialize Vertex AI SDK

vertexai.init(project=PROJECT_ID, location=LOCATION)

 

 

loader = GCSDirectoryLoader(

    project_name=PROJECT_ID, bucket="rentokil4"

)

documents = loader.load()

 

 

# split the documents into chunks

from langchain.text_splitter import RecursiveCharacterTextSplitter

 

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

docs = text_splitter.split_documents(documents)

print(f"# of documents = {len(docs)}")

 

embedding = VertexAIEmbeddings()

 

contracts_vector_db = Chroma.from_documents(docs, embedding)

 

 

# Expose index to the retriever

retriever = contracts_vector_db.as_retriever(

    search_type="similarity", search_kwargs={"k": 2}

)

 

# Create chain to answer questions

from langchain.chains import RetrievalQA

 

llm = VertexAI(

    model_name="text-bison-32k",

    max_output_tokens=256,

    temperature=0.1,

    top_p=0.8,

    top_k=40,

    verbose=True,

)

 

# Uses LLM to synthesize results from the search index.

# We use Vertex PaLM Text API for LLM

qa = RetrievalQA.from_chain_type(

    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True

)

 

#query = "Who all entered into agreement with Sagebrush?"

#result = qa({"query": query})

#print(result)

 

 

from google.cloud import storage

import gradio as gr

import markdown

 

 

def chatbot(inputtext):

    result = qa({"query": inputtext})

 

    return (

        result["result"],

        get_public_url(result["source_documents"][0].metadata["source"]),

        result["source_documents"][0].metadata["source"],

    )

 

 

def get_public_url(uri):

    """Returns the public URL for a file in Google Cloud Storage."""

    # Split the URI into its components

    components = uri.split("/")

    # Get the bucket name

    bucket_name = components[2]

 

    # Get the file name

    file_name = components[3]

 

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)

    return blob.public_url

 

 

print("Launching Gradio")

 

iface = gr.Interface(

    fn=chatbot,

    inputs=[gr.Textbox(label="Query")],

    examples=[

        "What is rentokil ? ",

        "how much tonne of waste recycled in melbourne?",

        "what is the goal of Rentokil?",

    ],

    title="Rentokil InfoBOT",

    outputs=[

        gr.Textbox(label="Response"),

        gr.Textbox(label="URL"),

        gr.Textbox(label="Cloud Storage URI"),

    ],

    theme=gr.themes.Soft,

)

 

iface.launch(server_name="0.0.0.0", server_port=8080)

 

