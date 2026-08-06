from flask import Blueprint, render_template, request, jsonify,flash
from flask_login import login_required, current_user
from .models import *
from .myconfig import *
from transformers import pipeline
from .chat import get_response
from spacy import displacy
from langchain_community.llms import HuggingFaceHub
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_classic.chains.conversation.memory import ConversationEntityMemory
from langchain_classic.chains import ConversationChain
from langchain_classic.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
import spacy,json,os
import google.generativeai as palm


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
views = Blueprint("views", __name__)

@views.route('/', methods=["GET", "POST"])
def index():  
     return render_template('index.html', user=current_user)


#Named Entitiy Recognition

@views.route('/ner', methods=["GET", "POST"])
@login_required
def ner():
     if request.method == 'POST':            
            raw_text = request.form['rawtext']
            result = ''            
            if len(raw_text.strip()) > 0:
               # Load English tokenizer, tagger, parser and NER
               nlp = spacy.load('en_core_web_sm')
               docx = nlp(raw_text)
               html = displacy.render(docx, style="ent")
               html = html.replace("\n\n", "\n")
               result = HTML_WRAPPER.format(html)
               return render_template('ner.html', user=current_user, result=result,rawtext = raw_text, pst=True )
        
     return render_template('ner.html', user=current_user, pst=False)

#Sentimental Analysis
@views.route('/sentimental', methods=["GET", "POST"])
@login_required
def sent():
     if request.method == 'POST':                      
            raw_text = request.form['rawtext']
            result = ''            
            if len(raw_text.strip()) > 0:
               classifier = pipeline('sentiment-analysis')
               result = classifier(raw_text)
               result = json.dumps(result)             
               return render_template('sentimental.html', user=current_user, result=result,rawtext = raw_text, pst=True )
        
     return render_template('sentimental.html', user=current_user, pst=False)

#HuggingFace Transformers GPT2 text generation
@views.route('/tgpt2', methods=["GET", "POST"])
@login_required
def tgpt2():
     if request.method == 'POST':            
            raw_text = request.form['rawtext']
            result = ''            
            if len(raw_text.strip()) > 0:
               classifier = pipeline('text-generation', model = 'gpt2')
               text= classifier(raw_text, max_length = 30, num_return_sequences=3)            
               result = ''
               for obj in text:               
                    result =  result +'\n' + obj["generated_text"]             

               return render_template('tgpt2.html', user=current_user, result=result,rawtext = raw_text, pst=True )
        
     return render_template('tgpt2.html', user=current_user, pst=False)


#Google Bard palm API, textGeneration
@views.route('/palmapi', methods = ["GET", "POST"])
@login_required
def palmapi():
     if request.method == 'POST':        
          raw_text = request.form['rawtext']
          result = ''
          if len(PALM_API_KEY) < 1:               
               flash('PALM_API_KEY not found. Please update the key in myconfig.py file', category='error')
               return render_template('palmapi.html', user=current_user, rawtext = raw_text, pst=False)          
          if len(raw_text.strip()) > 0:          
               palm.configure(api_key=PALM_API_KEY)
               models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
               model = models[0].name          
               completion = palm.generate_text(
               model=model,
               prompt=raw_text,
               temperature=0,
               # The maximum length of the response
               max_output_tokens=800,
               )
               return render_template('palmapi.html', user=current_user, result=completion.result,rawtext = raw_text, pst=True )

     return render_template('palmapi.html', user=current_user, pst=False)

#LangChain Hugging Face ChatGPT 
@views.route('/gflan', methods = ["GET", "POST"])
@login_required
def gflan():
     if request.method == 'POST':
          raw_text = request.form['rawtext']
          result = ''
          if len(HUGGINGFACEHUB_API_TOKEN) < 1:               
               flash('HUGGINGFACEHUB_API_TOKEN not found. Please update the key in myconfig.py file', category='error')
               return render_template('gflan.html', user=current_user, rawtext = raw_text, pst=False)          
          if len(raw_text.strip()) > 0:
               os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN
               #Flan, by Google               
               question = raw_text
               template = """Question: {question}"""
               prompt = PromptTemplate(template=template, input_variables=["question"])
               repo_id = "google/flan-t5-xxl"
               llm = HuggingFaceHub(
               repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
               )
               llm_chain = LLMChain(prompt=prompt, llm=llm)
               result = llm_chain.run(question)
               return render_template('gflan.html', user=current_user, result=result,rawtext = raw_text, pst=True )

     return render_template('gflan.html', user=current_user, pst=False)


@views.route('/openai', methods = ["GET", "POST"])
@login_required
def openai():
     if request.method == 'POST':       
          raw_text = request.form['rawtext']
          result = ''
          if len(OPENAI_API_KEY) < 1:               
               flash('OPENAI_API_KEY not found. Please update the key in myconfig.py file', category='error')
               return render_template('openai.html', user=current_user, rawtext = raw_text, pst=False)
          if len(raw_text.strip()) > 0:
               MODEL = "gpt-3.5-turbo-0613"
               K = 10
               os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY                        
               try:
                    llm = ChatOpenAI(temperature=0,openai_api_key=OPENAI_API_KEY, model_name=MODEL, verbose=False) 
                    entity_memory = ConversationEntityMemory(llm=llm, k=K )
                    qa = ConversationChain(llm=llm,   prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, memory=entity_memory)
               except Exception as e:  
                    flash(e, category='error')
                    return render_template('openai.html', user=current_user, rawtext = raw_text, pst=False) 
               result =  qa.run(raw_text)    
               return render_template('openai.html', user=current_user, result=result,rawtext = raw_text, pst=True )

     return render_template('openai.html', user=current_user, pst=False)


@views.route('/predict', methods=['POST', 'GET'])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

#@views.route('/ner', methods=["GET", "POST"])
#def ner():
#     if request.method == 'POST':
#            raw_text = request.form['rawtext']
#            tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
#            model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
#            nlp = pipeline("ner", model=model, tokenizer=tokenizer)
#            html = nlp(raw_text)
#            html = displacy.render(html, style="ent")
#            #html = html.replace("\n\n", "\n")
#            result = HTML_WRAPPER.format(html)   
                        
#            return render_template('ner.html', user=current_user, result=result,rawtext = raw_text, pst=True )
        
#     return render_template('ner.html', user=current_user, pst=False)

#@views.route('/bard', methods=["GET", "POST"])
#def bard():
#     if request.method == 'POST':
#            raw_text = request.form['rawtext']                               
#            bard = Bard(token="") 
#            result = bard.get_answer(raw_text)                 
#            result = result['content']                     
#            return render_template('bard.html', user=current_user, result=result,rawtext = raw_text, pst=True )
        
#     return render_template('bard.html', user=current_user, pst=False)


#@views.route('/llama', methods=["GET", "POST"])
#def llama():
#     if request.method == 'POST':
#            raw_text = request.form['rawtext']
#            result=split_text_chunks_and_summary_generator(raw_text)                
#            return render_template('llama.html', user=current_user, result=result,rawtext = raw_text, pst=True )
       
#     return render_template('llama.html', user=current_user, pst=False)

#Used in huggingface model
#def split_text_chunks_and_summary_generator(text):
  #  text_splitter=CharacterTextSplitter(separator='\n',
  #                                      chunk_size=1000,
  #                                      chunk_overlap=20)
  #  text_chunks=text_splitter.split_text(text)
        
    #LLAMA - LANGCHAIN = HUGGINGFACE
  #  llm = CTransformers(model='\models\llama-2-7b-chat.ggmlv3.q2_K.bin',
  #                      model_type='llama',
  #                      config={'max_new_tokens': 20,
  #                              'temperature': 0.01}
  #                      )
  #  docs = [Document(page_content=t) for t in text_chunks]
  #  chain=load_summarize_chain(llm=llm, chain_type='map_reduce', verbose=True)
  #  summary = chain.run(docs)
  #  return summary

