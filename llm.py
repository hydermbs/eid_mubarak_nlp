from langchain import PromptTemplate, LLMChain
from langchain_huggingface import HuggingFaceEndpoint

import os

api_key = os.getenv("API_KEY")
print(api_key)

def greetings_function(tone, recipient, rec_name, sender_name):
    token = api_key
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    
    llm = HuggingFaceEndpoint(
        repo_id=repo_id, 
        max_length=128, 
        temperature=0.7, 
        huggingfacehub_api_token=token
    )

    template = "Write a heartfelt Eid Mubarak message in a {tone} tone for {recipient_name}, who is a {recipient_type}, from {sender_name}. The message should be warm, celebratory, and within 50 words."
    prompt = PromptTemplate(template=template, input_variables=["tone", "recipient", "rec_name", "sender_name"])
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain.invoke({"tone": tone, "recipient": recipient, "rec_name": rec_name, "sender_name":sender_name})

def main(tone,recipient, rec_name, sender_name):
    greetings = greetings_function(tone,recipient, rec_name, sender_name)
    message = greetings['text']

    return message

if __name__ == "__main__":
    main()
