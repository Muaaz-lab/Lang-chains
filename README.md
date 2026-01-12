1️⃣ langchain

The main library for connecting LLMs with prompts and chains.

Features used:

chat_models.ChatOpenAI → Interface to OpenAI GPT models (e.g., GPT-3.5).

prompts.PromptTemplate → Create structured prompts with placeholders (context, question).

output_parsers.StrOutputParser → Ensures clean string output from the model.

chains.LLMChain → Connects the prompt + LLM + parser into a single callable chain.

2️⃣ openai

Needed as the backend API for GPT models.

Used implicitly via ChatOpenAI.

Handles sending requests to OpenAI servers and returning responses.

3️⃣ os

Python standard library.

Used for reading or setting environment variables, especially the OpenAI API key:

os.environ["OPENAI_API_KEY"] = "sk-..."

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LegalBot Data Flow</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.4.0/mermaid.min.js"></script>
    <script>mermaid.initialize({ startOnLoad: true });</script>
</head>
<body>
    <h2>LegalBot Data Flow: Query → Database → Prompt → LLM → Response</h2>
    <div class="mermaid">
        flowchart TD
            A[User Query] --> B[Database / Context Retrieval]
            B --> C[Prompt Template]
            C --> D[ChatOpenAI LLM]
            D --> E[Parsed Response (Legal Draft)]

            style A fill:#f9f,stroke:#333,stroke-width:2px
            style B fill:#9f9,stroke:#333,stroke-width:2px
            style C fill:#9cf,stroke:#333,stroke-width:2px
            style D fill:#fc9,stroke:#333,stroke-width:2px
            style E fill:#ff9,stroke:#333,stroke-width:2px
    </div>
</body>
</html>
