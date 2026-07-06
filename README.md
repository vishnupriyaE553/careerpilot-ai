# 🚀 CareerPilot AI

A Multi-Agent Career Guidance System built using **Google Agent Development Kit (ADK) 2.3** and **Gemini 2.5 Flash**.

CareerPilot AI helps students and job seekers make informed career decisions by providing personalized career recommendations, skill gap analysis, resume suggestions, interview preparation, and learning roadmaps through specialized AI agents.

---

## 📌 Features

- 🎯 Career Recommendation Agent
- 📚 Skill Gap Analyzer
- 📄 Resume Improvement Assistant
- 💼 Interview Preparation Agent
- 🛣️ Personalized Learning Roadmap
- 🤖 Multi-Agent Routing using Google ADK
- ⚡ Powered by Gemini 2.5 Flash

---

## 🏗️ Project Architecture

```
                User
                  │
                  ▼
          CareerPilot AI
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Career      Skills      Resume
 Agent        Agent       Agent
      ▼           ▼           ▼
 Interview   Roadmap   Skill Gap Tool
    Agent      Agent
```

The coordinator agent analyzes the user's query and routes it to the appropriate specialized agent using Google ADK's transfer mechanism.

---

## 📂 Project Structure

```
careerpilot-ai/
│
├── agents/
│   ├── career_agent.py
│   ├── skills_agent.py
│   ├── resume_agent.py
│   ├── interview_agent.py
│   └── roadmap_agent.py
│
├── tools/
│   └── skill_gap_tool.py
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## ⚙️ Technologies Used

- Python 3.11
- Google ADK 2.3
- Gemini 2.5 Flash
- Streamlit
- FastAPI
- Google GenAI SDK

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/vishnupriyaE553/careerpilot-ai.git
```

Go to the project directory

```bash
cd careerpilot-ai
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the project

```bash
adk web
```

---

# 📸 Demo

## Career Recommendation Agent

<img width="1600" height="896" alt="image" src="https://github.com/user-attachments/assets/dbf609a8-7e19-4c24-8c8d-1429f532a6b1" />

---

## Skills Agent

<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/589d5a77-ff1d-4ccc-b487-697bf75a31a0" />

---

## Skill Gap Analyzer

<img width="1600" height="853" alt="image" src="https://github.com/user-attachments/assets/2d436b19-8e09-4087-a3ab-5aa2eaa96f19" />


---

## Google ADK Event Trace

<img width="1916" height="961" alt="Screenshot 2026-07-06 200843" src="https://github.com/user-attachments/assets/56c64f28-46e0-4ace-b192-4d4278fca2c1" />

---

## Agent Routing

<img width="1600" height="899" alt="image" src="https://github.com/user-attachments/assets/26195f72-6c6f-4b12-9d2f-ee7de082c79d" />

---

# Example Query

> I am an ECE student. I know Java and Python. I want to become a Software Engineer.

CareerPilot AI provides

- Career Suggestions
- Skill Gap Analysis
- Resume Tips
- Interview Questions
- Learning Roadmap

---

# Future Enhancements

- Job Recommendation Agent
- LinkedIn Profile Analyzer
- Resume ATS Score Checker
- Voice-based Career Assistant
- PDF Resume Generator

---

# Author

**Vishnu Priya E**

Electronics and Communication Engineering

Saveetha Engineering College

GitHub:
https://github.com/vishnupriyaE553

LinkedIn:
https://www.linkedin.com/in/vishnu-priya-e-

---

# Acknowledgements

- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Kaggle AI Agents Capstone Project
- Google AI
