# 🏥 C.A.L.M. (Critical Agent Logic Module)

> **Student Clash 2025** > **Category:**Tech
## 📖 Overview
**C.A.L.M.** is an autonomous **Clinical Decision Support System** designed to restore order to the chaotic environment of the Intensive Care Unit (ICU).

ICU clinicians suffer from severe **Alarm Fatigue**, caused by thousands of daily alerts from uncoordinated devices. **C.A.L.M.** solves this not by silencing sensors, but by employing a "Digital Team" of specialized AI agents that negotiate in real-time to filter noise and surface only **Critical Logic**.

## 🚀 The Problem
* **Cognitive Overload:** Clinicians must synthesize data from 10+ disconnected screens.
* **Alarm Fatigue:** 72-99% of clinical alarms are false or non-actionable, leading to desensitization.
* **Context Blindness:** Standard monitors scream "Low Heart Rate" even if the patient is a sleeping athlete; they lack the logic to understand *why*.

## 💡 The Solution: C.A.L.M. Architecture
We utilize a **Level 3 Multi-Agent Approach** to separate detection from reasoning. The system does not just *react*; it *thinks* before it notifies.

### The Agentic Workflow
The module consists of three autonomous agents working in a loop:

1.  **The Sentinel (Input Agent)**
    * *Function:* Pure data ingestion (Vitals, Labs, IoT).
    * *Logic:* High sensitivity. If a number is out of range, it flags an **"Anomaly Candidate"**.
    * *Motto:* "Miss nothing."

2.  **The Historian (Context Agent)**
    * *Function:* Deep EMR analysis (Patient History, Meds, Notes).
    * *Logic:* It validates the Sentinel's candidate against the patient's specific profile.
    * *Motto:* "Check the context."
    * *Capability:* Can issue an **"Objection"** (e.g., *Objecting to Low BP alert because patient was just administered a vasodilator*).

3.  **The Triage Officer (Output Agent)**
    * *Function:* Decision & Communication.
    * *Logic:* Weighs the Sentinel's fear against the Historian's facts.
    * *Action:* Autonomously decides the **Alert Level**:
        * 🔴 **Code Red:** Audible Alarm (Immediate Intervention).
        * 🟡 **Yellow Log:** Silent update to the dashboard (Watchlist).
        * 🟢 **Suppress:** False alarm dismissed with a log entry.

---

## ⚙️ Technical Implementation

### Prerequisites
* Python 3.8+
* OpenAI API Key (or compatible LLM endpoint)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/calm-agent.git](https://github.com/yourusername/calm-agent.git)
    cd calm-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Includes `openai`, `python-dotenv`, `pydantic`)*

3.  **Security Setup:**
    Create a `.env` file in the root directory. **Do not hardcode keys.**
    ```env
    OPENAI_API_KEY=sk-your-secret-key-here
    ```

### How to Run
Start the logic engine simulation:
```bash
python main.py
