# Summary
IRIS-GenLab is a generative AI Application that leverages the functionality of Flask web framework, SQLALchemy ORM, and InterSystems IRIS to demonstrate Machine Learning, LLM, NLP, Generative AI API, Google AI LLM, Flan-T5-XXL model, Flask Login and OpenAI ChatGPT use cases.

[![one](https://img.shields.io/badge/Platform-InterSystems%20IRIS-blue)](https://www.intersystems.com/data-platform/) [![one](https://img.shields.io/badge/WebFrameWork-Flask-Orange)](https://flask.palletsprojects.com/en/2.3.x/) [![one](https://img.shields.io/badge/ORM-SQLAlchemy-teal)](https://www.sqlalchemy.org/) [![one](https://img.shields.io/badge/Authentication-Flask%20Login-yellow)](https://flask-login.readthedocs.io/en/latest/) [![one](https://img.shields.io/badge/ChatBot-PyTorch-Maroon)](https://pytorch.org/) [![one](https://img.shields.io/badge/NLP-spaCy-Salmon)](https://spacy.io/) [![one](https://img.shields.io/badge/Pipeline-Hugging%20Face-yellow)](https://huggingface.co/) [![one](https://img.shields.io/badge/LLM-GPT2-Purple)](https://huggingface.co/gpt2) [![one](https://img.shields.io/badge/Generative%20AI%20API-PALM-blue)](https://developers.generativeai.google/)  [![one](https://img.shields.io/badge/Google%20AI%20LLM-FLAN%20T5%20XXL-Cyan)](https://huggingface.co/google/flan-t5-xxl) [![one](https://img.shields.io/badge/OpenAI-ChatGPT-yellow)](https://openai.com/) [![OEX](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://github.com/mwaseem75/iris-GenLab/blob/master/LICENSE) [![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mwaseem75/iris-GenLab/blob/master/LICENSE)
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/2717f704-a1d7-4e2c-9a48-609469c41cec)

# Features
* User registration and authentication
* Chatbot functionality with the help of Torch (python machine learning library)
* Named entity recognition (NER), natural language processing (NLP) method for text information extraction
* **PEX production to apply Named entity recognition (NER) on the given text**
* Sentiment analysis, NLP approch that identifies the emotional tone of the message 
* HuggingFace Text generation with the help of GPT2 LLM (Large Language Model) model and Hugging Face pipeline
* Google PALM API, to access the advanced capabilities of Google's large language models (LLM) like PaLM2
* Google Flan-T5 XXL, a fine-tuned on a large corpus of text data that was not filtered for explicit contents.
* OpenAI is a private research laboratory that aims to develop and direct artificial intelligence (AI)


# Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-GenLab.git
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```

# Getting Started 
Open myconfig.py file in python/genlab folder and enter the required keys (For where to get theses keys, please read section below)
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/ac91af95-d307-4269-896b-441c1fcbd8ab)


## To Run Flask application
Run the below command in Git Bash terminal
```
docker exec -it <container ID> bash
```
Now run below command to start flask application
```
irispython ./python/app.py
```
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/57c75351-2405-4488-b092-ae40d090aa16)


To run the application Navigate to [**http://localhost:4040**](http://localhost:4040) 
## Home Page
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/de2c53c6-669f-414a-9939-83ce7e645211)

## Register a User
To register a user, Click on Sign Up link
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/4ed2fb6b-3da6-4c65-b791-b40c5e7c9280)

Once registered, the user will log in automatically, To sign out click on the User Name link and then click on Sign out.
In order to log in, click on Login link
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/83e0776c-2c87-4a6e-adf4-141065db0451)

## Chatbot functionality with the help of Torch (python machine learning library)
Click on chatbot icon to start chating
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/e71ba8d2-f379-4d56-a7b3-770005fe08c8)

## Named entity recognition (NER)
Named entity recognition with spaCy, a open-source library for Natural Language Processing (NLP) in Python
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/03116a37-e6e9-4029-adb8-e8ccab8985cf)


## PEX production to apply Named entity recognition (NER) on the given text
The repository already has running production, To view the production navigate to the below URL
[**http://localhost:55038/csp/irisapp/EnsPortal.ProductionConfig.zen?$NAMESPACE=IRISAPP**](http://localhost:55038/csp/irisapp/EnsPortal.ProductionConfig.zen?$NAMESPACE=IRISAPP)
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/20aa66be-c57b-4e58-8ae0-39ff9fb30dd6)
Select Python.NERService and go to the message viewer from the messages tab 
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/9ab5d505-1fdf-4f5b-9970-f67616537a7b)
Click on View raw content to view message details
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/6c73d3db-8007-44cf-85e5-ea118d254eca)
The message displays NER text(selftext) along with the actual message

## Sentiment analysis
Sentiment analysis, also referred to as opinion mining, is an approach to natural language processing (NLP) that identifies the emotional tone of the message
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/46779e19-426e-4bda-97ca-9c3b89cd00b7)


## HuggingFace, Text generation (Gpt-2)
Text generation with the help of GPT2 LLM (Large Language Model) model and Hugging Face pipeline
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/92b75591-2e63-4e6a-ab26-1f3d67814fee)


## Google PALM API
Google API to access the advanced capabilities of Google's large language models (LLM) like PaLM2 with the PaLM API
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/a84e6c1f-8cd2-457e-ba85-e229f6f82f82)

Google PALM API requires [PALM_API_KEY] key
#### How to get Google Palm Api key
Navigate to [Google Palm Api Key page](https://makersuite.google.com/app/apikey), Click on "Create API Key in new project" and get API Key
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/1f0af75b-d24e-49fa-abb1-19b0dba5d4eb)

## Google Flan-T5-XXL
Flan-T5 is fine-tuned on a large corpus of text data that was not filtered for explicit content. Mainly used for Translation and question-answering
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/06e9a45e-a073-4c66-a008-298433ceaad8)
Google Flan-T5-XXl requires [HUGGINGFACEHUB_API_TOKEN] key
#### How to get Hugging Face key
Signup with hugging face and navigate to setting [Hugging Face account settings](https://huggingface.co/settings/tokens), click on the new token to create a new token  
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/7f57876e-4ef4-4ef9-8474-da056b1c8e78)


## OpenAI
OpenAI is a private research laboratory that aims to develop and direct artificial intelligence (AI)
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/b577c5e1-d59a-4d8c-a27e-10be8894382c)
#### Get OpenAI Key [OPENAI_API_KEY]
Application requires OpenAI API Key, sign up for OpenAI API on [this page](https://platform.openai.com/account/api-keys). Once you signed up and logged in, click on Personal, and select View API keys in drop-down menu. Create and copy the API Key
![image](https://github.com/mwaseem75/irisChatGPT/assets/18219467/7e7c7880-b9ac-4a60-9ec9-289dd2375a73)



## Application database
SQLALchemy will create below table:

* user: To store User information

To view table details, navigate to 
[**http://localhost:55038/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER&**](http://localhost:55038/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER&)
![image](https://github.com/mwaseem75/iris-GenLab/assets/18219467/a4d5d474-65eb-4026-a59b-7727fe7c592d)



## Special Thanks to:
Evgeny Shvarov for [iris-embedded-python-template](https://openexchange.intersystems.com/package/iris-embedded-python-template) and 
Guillaume Rongier for [interoperability-embedded-python](https://github.com/grongierisc/interoperability-embedded-python) template for guidance
