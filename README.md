# 🚀 Project Overview

This project demonstrates how to build a lightweight **LLM-powered question-answering application** using a local model instead of relying entirely on cloud-based APIs.

The application uses:
- **Streamlit** for the web interface  
- **LangChain** for prompt management and LLM chaining  
- **Ollama** for running LLMs locally  
- **Python** for application development  
- **python-dotenv** for environment configuration  

---

## 📊 Pipeline Flow

User Query
↓
ChatPromptTemplate
↓
Ollama LLM
↓
StrOutputParser
↓
Generated Response

Code

---

## ✨ Features

- 💬 Ask questions through an interactive chatbot interface  
- 🤖 Run LLMs locally using Ollama  
- 🔄 Select between different Ollama models  
- 🌡️ Adjust model temperature from the sidebar  
- 🔗 Use LangChain's prompt and chaining framework  
- ⚡ Generate responses locally without requiring a paid LLM API  
- 🖥️ Simple and interactive Streamlit interface  
- ⚠️ Basic error handling for model/API-related issues  

---

## 🛠️ Tech Stack

| Technology            | Purpose                                      |
|------------------------|----------------------------------------------|
| Python                 | Application development |
| Streamlit              | Web application interface |
| LangChain              | LLM orchestration and prompt chaining |
| Ollama                 | Local LLM execution |
| ChatPromptTemplate     | Prompt construction |
| StrOutputParser        | Converts model output into text |
| python-dotenv          | Environment configuration |

---

## 🤖 Supported Models

The application currently provides the following model options:
- llama3.2:1b  
- gemma3  
- gemma3:1b  

> These models must be available locally through Ollama before running the application.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ollama-llm-chatbot.git
cd ollama-llm-chatbot
2. Create a virtual environment
bash
python -m venv venv
Activate the environment:

Windows:

bash
venv\Scripts\activate
macOS/Linux:

bash
source venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
🦙 Install and Configure Ollama
Install Ollama on your system and make sure the Ollama service is running.
Then download the models you want to use.

Example:

bash
ollama pull llama3.2:1b
Other supported models:

bash
ollama pull gemma3
ollama pull gemma3:1b
Verify installed models:

bash
ollama list
▶️ Run the Application
bash
streamlit run app.py
Streamlit will provide a local URL where you can access the chatbot.

🎛️ How to Use
Enter a Query  
Example:

Code
What is Generative AI?
Select a Model  
Choose from:

llama3.2:1b

gemma3

gemma3:1b

Adjust Temperature

Lower → focused, predictable responses

Higher → varied, creative responses

Generate the Answer  
Click the Answer button to generate the response.

🧠 LangChain Workflow
The application creates a prompt using ChatPromptTemplate:

python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Question: {Question}")
])
Connected to the Ollama model and parser:

python
chain = prompt | model | parser
Flow:

Code
Prompt
  ↓
Ollama LLM
  ↓
Output Parser
  ↓
Text Response
Final response:

python
result = chain.invoke({
    "Question": query
})
📌 Key Learning Outcomes
Through this project, I explored:

Building an LLM-powered application

Running open-source LLMs locally with Ollama

Using LangChain's ChatPromptTemplate

Creating LCEL chains using the pipe operator

Using StrOutputParser

Integrating LangChain with Streamlit

Passing user input dynamically to an LLM

Controlling LLM generation using temperature

Building a simple interactive GenAI application

👩‍💻 Author
Prerna Kumari
