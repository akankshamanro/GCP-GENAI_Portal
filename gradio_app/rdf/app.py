from SPARQLWrapper import SPARQLWrapper, N3, JSON, XML, TURTLE, JSONLD
from rdflib import Graph, URIRef, Literal
import networkx as nx
from networkx import Graph as NXGraph
from networkx.readwrite import json_graph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from rdflib.namespace import Namespace, RDFS, FOAF
import matplotlib.pyplot as plt
import statistics
import collections

import gradio as gr
import os
import sys
import vertexai
from google.cloud import aiplatform


os.mkdir('images')



# # Get the directory of the current script
# dir_path = os.path.dirname(os.path.abspath(__file__))

# # Construct the absolute path of the credentials file in the secrets directory
# credentials_path = os.path.join(dir_path, 'secrets', 'credentials.json')

# # Set the environment variable to the credentials file path
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
model = TextGenerationModel.from_pretrained('text-bison@001')


def generate2(input):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    query = """CONSTRUCT { ?childNodes skos:broader <http://dbpedia.org/resource/Category:Deep_learning> .
    ?childNodes skos:broader ?siblingConceptsFromChildNodes .
    <http://dbpedia.org/resource/Category:Deep_learning> skos:broader ?parentNodes .
    ?siblingConceptsFromParentNodes skos:broader ?parentNodes
    }
    WHERE  {
        { ?childNodes skos:broader <http://dbpedia.org/resource/Category:Deep_learning> . ?childNodes skos:broader ?siblingConceptsFromChildNodes}
    UNION  #get parents
    {<http://dbpedia.org/resource/Category:Deep_learning> skos:broader ?parentNodes . ?siblingConceptsFromParentNodes skos:broader ?parentNodes}
    }
    group by ?parentNodes ?childNodes
    """


    output = query.replace("Deep_learning", input)
    sparql.setQuery(output)
    results = sparql.queryAndConvert()

    # generate graph
    g = Graph()
    g = results
    #Undirected graphs will be converted to a directed graph with two directed edges for each undirected edge.
    dg = rdflib_to_networkx_graph(g, False, edge_attrs=lambda s,p,o:{})


    #generate network text for LLM
    network_text = "\n".join(nx.generate_network_text(dg))
    #print(network_text)


    #PageRank calculation
    p1 = nx.pagerank(dg, alpha=0.85)
    pr = sorted(p1.items(), key=lambda x:x[1],reverse=True)[:10]


    #Draw graph
    #nx.draw(dg, with_labels=True)
    nx.draw(dg)
    plt.draw()
    img_suffix = "images/" + input + ".jpg"
    img = os.path.join(os.path.abspath(''), img_suffix)
    plt.savefig(img, dpi=150)
    
  
 
    
    return output, network_text, pr, img





def generate_llm(input):

    prompt = f"""
    You are an assistant with an ability to generate response based on network text {input} from python networkx graph library, \
    showing how the listed edges are linked/connected nodes in directed graph. \
    Explain how Top 5 nodes are linked. Do not include any other explanations. \
    """

    # Text generation parameters
    parameters = {
            "max_output_tokens": 1000,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
    

    response = model.predict(prompt, **parameters)
        
    return response

html_code = """
<div class="navbar"
<div class="logo" 
  <a href="https://www.cognizant.com/in/en" aria-label="Cognizant-logo"><img aria-label="Cognizant Logo" alt="Cognizant Logo"  src="https://cognizant.scene7.com/is/content/cognizant/COG-Logo-2022-8?fmt=png-alpha"/></a>
 </div> 
<div class="studioHome">
  <a href="https://dev-gen-ai-web-app-kcvokjzgdq-ew.a.run.app/dashboard" style="text-decoration:none">
    <button style="padding:5px 8px; background-color: #000048; color:white; border:none; border-radius: 5px; cursor: pointer;">Demo Home</button>
  </a>
</div>
</div>
"""

css = """
.tabs {
  border-radius: 0.5rem 0.5rem 0 0;
  padding-left: 0;
  margin-bottom: 0;
}
.tab-nav {
  display: flex;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  background-color: #e5eff9;
  border-top: 1px solid #d0d0ce;
  border-right: 1px solid #d0d0ce;
  border-top-right-radius: 0.5rem;
  border-top-left-radius: 0.5rem;
}
.tabs .tab-nav button:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 10px;
}
.tabs .tab-nav button {
  padding: 0.75rem 1.25rem;
  border-radius: inherit;
  color: #2f78c4;
  cursor: pointer;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out;
  background: none;
  border: none;
  cursor: pointer;
}

.tabs .tab-nav button.selected:first-child {
  border-top-left-radius: 0.5rem;
  border-left: 1px solid #d0d0ce;
}

.tabs .tab-nav button:hover:not(.selected) {
  background: #fff;
  border-radius: 0;
}

.tabs .tab-nav button.selected {
  color: #000048;
  font-size: 20px;
  font-weight: 700;
  padding: 15px 25px;
  margin-bottom: -1px;
  box-shadow: inset 0 4px 0 0 #2f78c4, 0 0px 0 0 #ffffff;
  padding: 0.75rem 1.25rem;
  background: #fff;
  border-bottom: none;
}
.tabs .tab-nav button.selected:not(:first-child) {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.tabs .tab-item {
  background: #fff;
  border-radius: 0 0 0.5rem 0.5rem;
  border: 1px solid #d0d0ce;
  border-width: 1px;
  padding: 1.25rem;
}


.studioHome {
  display: flex;
  justify-content: flex-end;
  height:30px;
  align-items:center;
}
 img {
  float:left;
  width:140px;
  height:120px;
}
h1 {
  font-size:13px;
}
button.lg {
background: #000048 !important;
color: #ffffff !important;
}

"""

with gr.Blocks(css=css) as demo:
    gr.HTML(html_code)
    gr.HTML("<h1>Network Analysis of RDF Graphs</h1>")
    with gr.Tab("Input"):
        with gr.Row():
            with gr.Column():
                seed = gr.Text(label="Select the Child and Parent Nodes of: ")
                gr.Examples(["Deep_learning", "Machine_learning", "Evolutionary_algorithms", "Classification_algorithms"], inputs=[seed])
                btn = gr.Button("Construct, Generate, Visualise and Analyse Graph")
                sparql = gr.Text(label="SPARQL Used...")
            with gr.Column():
                
                net_txt = gr.Text(label="Hierarchical Data Retrieved")
                df = gr.Dataframe(headers=["Node", "PageRanks Score"],
                                  datatype=["str", "str"],
                                  row_count=5,
                                  col_count=(2, "fixed"))   
    with gr.Tab("LLM Graph Response"):
        with gr.Row():
            with gr.Column():
                llmres = gr.Text(label="LLM response")
                llm_btn = gr.Button("Generate LLM response") 
            with gr.Column():
                 graph = gr.Image(label="Generated Graph", type="pil") 


    btn.click(generate2, inputs=[seed], outputs=[sparql, net_txt, df, graph])
    llm_btn.click(generate_llm, inputs=[df], outputs=[llmres])


gr.close_all()
#demo3.launch(debug=True)
demo.queue().launch(server_name="0.0.0.0", server_port=8080)
