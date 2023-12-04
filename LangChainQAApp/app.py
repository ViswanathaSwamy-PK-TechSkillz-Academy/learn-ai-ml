import streamlit as st
import openai

from langchain.llms import AzureOpenAI  # Import Azure OpenAI
from dotenv import dotenv_values

# Load config values
config_details = dotenv_values(".env")

########################################### Azure Open AI ###########################################
openai.api_type = "azure"
openai.api_base = config_details['OPENAI_API_BASE']
openai.api_version = config_details['OPENAI_API_VERSION']

# Function to return the response


def load_answer(question):
    # llm = AzureOpenAI(model_name="text-davinci-003",temperature=1)
    llm = AzureOpenAI(
        deployment_name=config_details['COMPLETIONS_MODEL'], temperature=1)
    answer = llm(question)
    return answer


# App UI starts here
st.set_page_config(page_title="Lang Chain Demo", page_icon=":robot:")
st.header("Lang Chain Demo")

# Gets the user input


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input = get_text()
response = load_answer(user_input)

submit = st.button('Generate')

# If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)
