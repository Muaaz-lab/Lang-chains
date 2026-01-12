import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain.chains import LLMChain

# -------------------------------
# 1️⃣ Set your OpenAI API key
# -------------------------------
# Option 1: Environment variable already set
# Option 2: Set it here directly (not recommended for public code)
# os.environ["OPENAI_API_KEY"] = "sk-......"

# -------------------------------
# 2️⃣ Simulate database search
# -------------------------------
def simulate_database_search(query):
    # Demo historical case
    return """
    Case History #402: Ali vs. Landlord (2022).
    Court Decision: Landlord cannot evict a tenant without a 30-day prior written notice.
    Immediate eviction is illegal under Rent Control Act Section 15.
    """

# -------------------------------
# 3️⃣ Create PromptTemplate
# -------------------------------
prompt_template = PromptTemplate(
    template="""
You are an expert Lawyer AI named 'LegalBot'.

Use the following context (Historical Case) to draft a response:
{context}

User Request: {question}

Draft the legal response professionally:
""",
    input_variables=["context", "question"]
)

# -------------------------------
# 4️⃣ Initialize ChatOpenAI
# -------------------------------
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# -------------------------------
# 5️⃣ Create LLMChain
# -------------------------------
chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_parser=StrOutputParser()
)

# -------------------------------
# 6️⃣ User Query
# -------------------------------
user_query = "My landlord asked me to leave immediately without notice. Can I send a legal reply?"

# Step A: Retrieve relevant context
retrieved_context = simulate_database_search(user_query)

# Step B: Run chain to get legal draft
response = chain.run(
    context=retrieved_context,
    question=user_query
)

# -------------------------------
# 7️⃣ Print the result
# -------------------------------
print("--- FINAL LEGAL DRAFT ---\n")
print(response)
