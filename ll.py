from dotenv import load_dotenv
import warnings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import PyPDF2

# Load environment variables (for OpenAI API key)
load_dotenv()

# Ignore LangChainDeprecationWarning
warnings.simplefilter("ignore")

# Initialize LLM (ChatOpenAI)
LLM = ChatOpenAI(model="gpt-4o-mini")  # Use the correct OpenAI model

# Initialize memory with updated API
memory = ConversationBufferWindowMemory(k=5, return_messages=True, memory_key="history")

# Define the prompt template
prompt_template = ChatPromptTemplate.from_template(
    """You are a first aid assistant that answers questions **only** based on the content of the provided first aid PDF
    and the context of the previous conversation.

    The content from the PDF is:
    {pdf_content}

    Previous conversation:
    {history}

    Question:
    {input}

    Please answer the question using only the information from the first aid PDF and the context of the previous conversation.
    """
)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"

# Function to generate a response using LangChain memory
def generate_response(question, pdf_content):
    try:
        history = memory.load_memory_variables({}).get("history", [])
        formatted_prompt = prompt_template.format(
            pdf_content=pdf_content,
            history=history,
            input=question
        )

        response = LLM.predict(formatted_prompt)

        # Save the interaction to memory
        memory.save_context({"input": question}, {"output": response})

        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"An error occurred: {e}"
