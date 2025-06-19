# 🧠 ProductStrategyAgent

**AI-Powered Product Launch Orchestrator** using Google's Agent Development Kit (ADK)

This project automates and orchestrates the complex, multi-step process of launching a new product or feature using a system of intelligent agents. It is built with the Agent Development Kit (ADK) and integrates Gemini, OpenAI, and Google Cloud services to simulate a multi-agent team for product management.

---

## 🚀 What It Does

This system mimics the strategic workflows of a product manager, automatically handling:

- 📊 **Market Research**: Analyze user needs and trends  
- 🏁 **Competitive Analysis**: Evaluate competing products and positioning  
- ✍️ **PRD Generation**: Create product requirement documents and user stories  
- 📣 **Marketing Assets**: Generate press releases and social media copy  
- 🤖 **Orchestration**: Central coordination of all agents through a single root agent

---

## 🧱 Agent Architecture

| Agent Name               | Role                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `product_strategy_agent` | Orchestrates the workflow, delegates to all sub-agents               |
| `market_analysis_agent`  | Gathers market trends and user needs                                 |
| `competitive_analysis_agent` | Reviews competitors, strengths, and gaps                     |
| `prd_agent`              | Creates PRDs, features, and user stories                             |
| `marketing_agent`        | Generates launch communications and marketing copy                   |

---

## 🛠 Tech Stack

- 🧠 **Agent Development Kit (ADK)**
- 🤖 **Gemini / OpenAI (O3 Mini) for LLM-based generation**
- 🗂️ **Google Cloud Storage / BigQuery (planned for expansion)**
- 🧪 **Python (venv)**
- 🌐 **Optional web/CLI interface**

---

## 🏁 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/EliBabakhani/ProductStrategyAgent.git
cd ProductStrategyAgent
2. Create .env File
Create a .env file using the provided .env.example:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Root Agent
Use CLI or script to run:

bash
Copy
Edit
python run.py
(Example run.py should call product_strategy_agent.run() with sample inputs.)

📦 Outputs
The system produces:

📄 Product Requirements Document (PRD)

🧠 Market & Competitive summaries

📣 Marketing content drafts

All outputs are structured in JSON or Markdown and ready for integration into your PM stack.

📁 File Structure
arduino
Copy
Edit
ProductStrategyAgent/
│
├── agents/
│   ├── product_strategy_agent.py
│   ├── market_analysis_agent.py
│   ├── competitive_analysis_agent.py
│   ├── prd_agent.py
│   └── marketing_agent.py
├── run.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
🤝 Contributing
PRs and feedback welcome! For major changes, please open an issue first.

📄 License
This project is for educational and hackathon use. For production licensing, please contact the maintainer.

🔗 Acknowledgments
Built with ❤️ for the [Google ADK Hackathon] using the Agent Development Kit, Gemini, and OpenAI APIs.

yaml
Copy
Edit

---

Would you like me to generate:
- `.env.example`
- `requirements.txt`
- or `run.py` boilerplate to demo agent orchestration?

Let me know!
