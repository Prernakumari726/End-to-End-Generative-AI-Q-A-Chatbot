import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()


# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    (
        "human",
        "Question: {Question}"
    )
])


# Generate response
def generate_r(llm, temperature, query):

    model = OllamaLLM(
        model=llm,
        temperature=temperature
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    result = chain.invoke({
        "Question": query
    })

    return result


# App title
st.title("Ollama ChatBot Q & A App")


# User query
query_user = st.text_input(
    "Hey What's your Query ?",
    key="query_input"
)


# Sidebar
st.sidebar.title("Settings")


# Temperature
temperature = st.sidebar.slider(
    "Temperature:",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    key="temperature"
)


# Model selection
model_name = st.sidebar.selectbox(
    "Model is:",
    [
        "llama3.2:1b",
        "gemma3",
        "gemma3:1b"
    ],
    key="model_name"
)


# Answer button
if st.button("Answer", key="answer_button"):

    if query_user:

        try:
            response = generate_r(
                model_name,
                temperature,
                query_user
            )

            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Hey, please write some query.")