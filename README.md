# DealPilot

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5.1-black?style=for-the-badge&logo=openai)](https://openai.com/) [![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple?style=for-the-badge)](https://www.trychroma.com/) [![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=for-the-badge)](https://gradio.app/)

DealPilot is an autonomous multi-agent system that discovers, analyzes, and evaluates online deals. It combines RAG with gpt-5-mini, a QLoRA fine-tuned LLaMA specialist agent, and a neural network model to estimate true product value, identify high-discount opportunities, and deliver intelligent alerts with visualization.

![Image](https://github.com/user-attachments/assets/223c7b1a-8e1b-4bf9-9125-a2dc79355d05)
---

## System Architecture and Workflow

```mermaid
graph TD
    User((User)) --> UI[Gradio UI]
    UI --> Framework[Agent Framework]

    subgraph Core_System
    Framework --> Planner[Planning Agent]

    Planner --> Scanner[Scanner Agent]
    Planner --> Ensemble[Ensemble Agent]
    Planner --> Messenger[Messaging Agent]

    subgraph Pricing_Intelligence
    Ensemble --> GPT[RAG + gpt-5-mini]
    Ensemble --> Specialist[QLoRA LLaMA Specialist]
    Ensemble --> NN[Neural Network Model]
    end

    Scanner --> Deals[Deal Data]
    Deals --> Ensemble
    Ensemble --> Decision[Discount Calculation]

    Decision --> Messenger
    Messenger --> UI
    end

    Framework --> DB[(ChromaDB)]
    Framework --> Memory[(memory.json)]
```
## Methodology

To design a robust pricing system, multiple approaches were systematically evaluated using Mean Squared Error (MSE) as the primary metric.

### Approach

- Started with baseline models such as Constant prediction and Linear Regression to establish reference performance  
- Introduced traditional ML models including Random Forest and XGBoost for improved numerical estimation  
- Integrated NLP-based methods and neural networks to capture textual and feature-based patterns  
- Evaluated large language models for contextual reasoning and price understanding  
- Applied fine-tuning (QLoRA on LLaMA 3.2) to create a domain-specific Specialist Agent  
- Enhanced performance further using Retrieval-Augmented Generation (RAG) with gpt-5-mini  

### Key Insight

No single model performed best across all scenarios. While LLMs provided strong reasoning and neural networks offered stable predictions, combining them led to significantly better results.

### Final Methodology

The final system uses an ensemble approach combining:
- gpt-5-mini with RAG for contextual reasoning  
- Specialist Agent for domain-specific accuracy  
- Neural Network for numerical stability  

This hybrid design achieved the lowest error and forms the core of DealPilot.
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/e7f4c39d-e4bd-4efd-a21d-6c33e1b56c59" />


## Key Features

### Autonomous Multi-Agent System
- Fully automated pipeline from scraping to evaluation and alerting  
- Coordinated by a Planning Agent  

### Hybrid Pricing Intelligence
- RAG with gpt-5-mini for context-aware reasoning  
- Specialist Agent using QLoRA fine-tuned LLaMA 3.2  
- Neural Network Agent for numerical estimation  

Final price is derived using ensemble logic.

### Real-Time Deal Discovery
- Scrapes deals from RSS feeds  
- Extracts structured product information  

### Intelligent Discount Detection
- Discount = estimated_price - acutal_price
- Filters high-value opportunities  

### Notification System
- Generates alert messages using GPT  
- Sends push notifications Using PushOver

### Visualization
- Uses TSNE for embedding visualization  
- Provides fallback visualization when data is limited  

---

## Tech Stack

### Core
- Python 3.9+  
- Gradio  
- ChromaDB
- Beautiful Soup
- Pushover

### AI and ML
- gpt-5-mini  
- RAG pipeline  
- LLaMA 3.2 (QLoRA fine-tuned)  
- PyTorch  

### Data Processing
- RSS feeds and Selenium  
- TSNE (scikit-learn)  
---

## Agent Architecture

| Agent | Role |
|------|------|
| Planning Agent | Orchestrates workflow |
| Scanner Agent | Scrapes deals |
| Ensemble Agent | Combines pricing models |
| Specialist Agent | Fine-tuned domain model |
| Neural Network Agent | Price estimation |
| Messaging Agent | Sends alerts |

---

## Example Logic

Input Deal:  
iPhone listed at 500 dollars  

System Estimation:
RAG = 650 dollars
Specialist = 630 dollars
Neural Net = 640 dollars

Estimated Value = 640
Discount = 140

Final output = 640 - 500
discount = 140 dollars (sends the Notification about the deal)

## Installation and Setup

```bash
git clone <your-repo-link>
cd DealPilot

pip install -r requirements.txt
python price_is_right.py
```

## Highlights

- Multi-agent architecture  
- Hybrid AI system  
- Autonomous decision-making  
- End-to-end pipeline  
- Visualization and alerts  



