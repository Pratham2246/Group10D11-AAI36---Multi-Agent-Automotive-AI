\# 🚗 Multi-Agent Automotive System (Agentic AI)



\## 📌 Project Overview



This project implements a \*\*Multi-Agent Automotive System\*\* using Agentic AI principles.

It simulates collaboration between intelligent agents to fetch, process, and present car-related information.



The system consists of specialized agents that work together to deliver structured outputs.



\---



\## 🧠 Architecture



\### 🔹 Agents Involved



\* \*\*Researcher Agent\*\*



&#x20; \* Collects car specifications and details

\* \*\*Writer Agent\*\*



&#x20; \* Formats and presents the collected data in a user-friendly way



\---



\## 🔄 Workflow



1\. User enters car name

2\. Request sent to Researcher Agent

3\. Researcher gathers car specifications

4\. Data passed to Writer Agent

5\. Writer formats the content

6\. Final output displayed on UI



\---



\## 🛠️ Tech Stack



\* Python 🐍

\* CrewAI / LangChain

\* LLM API (Groq / OpenAI compatible)

\* Streamlit (UI)



\---



\## 📂 Project Structure



```

Multi-Agent\_Automotive\_System/

│

├── app.py              # Streamlit UI

├── main.py             # Main execution logic

├── researcher.py       # Researcher Agent

├── writer.py           # Writer Agent

├── requirements.txt    # Dependencies

├── README.md

└── .gitignore

```



\---



\## ⚙️ Setup Instructions



\### 1. Clone the repository



```

git clone https://github.com/Pratham2246/Group10D11-AAI36---Multi-Agent-Automotive-AI.git

cd Multi-Agent\_Automotive\_System

```



\### 2. Create virtual environment



```

python -m venv venv

venv\\Scripts\\activate

```



\### 3. Install dependencies



```

pip install -r requirements.txt

```



\### 4. Add API Key



Create a `.env` file and add:



```

GROQ\_API\_KEY=your\_api\_key\_here

```



\---



\## ▶️ Run the Project



```

streamlit run app.py

```



\---



\## 💡 Features



\* Multi-agent collaboration

\* Real-time car data generation

\* Modular architecture

\* Clean UI with Streamlit



\---



\## 🔐 Security Note



⚠️ Do NOT upload `.env` file to GitHub.

Keep your API keys private.



\---



\## 📸 Future Improvements



\* Add more specialized agents

\* Integrate real-time APIs

\* Improve UI/UX

\* Add database support



\---



\## 👨‍💻 Author



\*\*Pratham Bhawar\*\*



\---



\## ⭐ If you like this project



Give it a star on GitHub!



