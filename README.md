# 🚀 CareerPilot AI

## Multi-Agent Career Guidance System using Google ADK

CareerPilot AI is an intelligent multi-agent application built using **Google Agent Development Kit (ADK) 2.3** and **Gemini 2.5 Flash**. It helps students choose careers, identify skill gaps, improve resumes, prepare for interviews, and create learning roadmaps.

---

## Features

- 🎯 Career Guidance Agent
- 📚 Skills Recommendation Agent
- 📄 Resume Review Agent
- 🎤 Interview Preparation Agent
- 🛣️ Learning Roadmap Agent
- 🧠 Skill Gap Analyzer Tool

---

## Architecture

```text
                User
                  │
                  ▼
         CareerPilot Root Agent
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Career      Skills      Resume
 Agent        Agent        Agent
      ▼           ▼           ▼
 Interview   Roadmap   Skill Gap Tool
    Agent      Agent
                  │
                  ▼
          Gemini 2.5 Flash
```

---

## Technologies Used

- Python 3.11
- Google ADK 2.3
- Gemini 2.5 Flash

---

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run:

```bash
adk web
```

---

## Example Query

**Input**

> My current skills are Python, Java, SQL and Git. I want to become an AI Engineer. Analyze my skill gap.

**Output**

- Skill Readiness Score
- Missing Skills
- Recommended Technologies
- Learning Recommendations

---

## Future Improvements

- ATS Resume Checker
- Career Match Score
- PDF Resume Analysis
- Learning Progress Tracker

---

## Author

**Vishnu Priya E**
