import os
import dotenv
from openai import AzureOpenAI
import gradio as gr


dotenv.load_dotenv()

    
# set up Azure OpenAI client
client = AzureOpenAI(
    api_key="524e5269ea524937afdel488f7f9a769",  
    api_version='2023-05-15',
    azure_endpoint = "hhtps://genai23-01.openai.azure.com/"
)


def produce_response(question, history):
    """
      question: user input, normally it is a question asked
      history: chat history
    """
    model=os.getenv("MODEL_NAME")

    # converting history into OpenAI message format
    messages = []
    for e in history:
      messages.append({"role": "system", "content": e[0]})
      messages.append({"role": "user", "content": e[1]})
    ## Here We will add first layer security model and if the model approve it then proceed else provide predefine answer
    # security_model = ModelABC() ## security model 
    # flag = security_model(question) ## return the output as flag (Yes: Voillation, NO: Non-viollation )
    # if False:
    #     return predefined_answer
    # else:
        # adding the new message from the user
    content = """all the relavent sentences related to the question:
      Adnan was born in Qatar, and he liks football. He is a student at Qatar University.
    """
    content += question
    messages.append({"role": "user", "content": content})

    # call openAI API
    response = client.chat.completions.create(
      model=model,
      messages=messages,
    )
    ## Here we can also apply secondlayer security layer model on the response
    

    # return response to user
    return response.choices[0].message.content

demo = gr.ChatInterface(
  produce_response,
  title="OpenAI Chatbot Example",
  description="A chatbot example for QCRI Generative AI Hackathon 2023",
  )

if __name__ == "__main__":
    demo.launch(share=True)
