# Deep Research AI Agent - Project Writeup

## Project Overview - Deep Research AI Agent
**NOTE**: This is a submission for the Agent AI Capstone project.

This project contains the core logic for the **Deep Research AI Agent**, an autonomous system designed to assist users in researching complex topics. The agent is built using a modern Python/React stack and follows a modular architecture to gather, process, and synthesize information from the web.

## Problem Statement
Conducting deep research on a new topic is laborious because it requires significant time investment in searching, filtering through irrelevant results, reading lengthy articles, and synthesizing key insights. The repetitive nature of verifying sources and maintaining context across multiple searches can quickly become mentally exhausting. Manual research also struggles to scale; when you need to understand multiple complex domains quickly, you are forced to choose between depth and speed. Automation can streamline data gathering, filter for credibility, and generate comprehensive reports, allowing human researchers to focus their expertise on strategic decision-making and creative application of knowledge.

## Solution Statement
The **Deep Research AI Agent** automatically researches topics by gathering information from Google Search, synthesizing key insights, and identifying credible sources relevant to your query. It generates structured reports based on specific parameters, significantly reducing the time spent on the "blank page" problem. Additionally, the agent manages the context of the research using vector memory, ensuring that facts are not lost and citations are accurate—transforming research from a manual chore into a streamlined, data-driven process.

## Architecture
Core to the Deep Research AI Agent is its modular backend system. It's not just a script but an ecosystem of specialized modules, each contributing to a different stage of the research process.

The central orchestrator of this system is the **FastAPI Backend**.

### Core Components

#### Search Specialist: `google_search.py`
This module is responsible for the initial information gathering. It connects to the **Google Custom Search API** to fetch live, relevant web results. It handles the nuances of query formation and result parsing to ensure high-quality raw data.

#### Memory Manager: `memory.py` (ChromaDB)
Once data is gathered, the Memory Manager takes over. This component utilizes **ChromaDB**, a vector database, to store search results as semantic embeddings. This allows the system to "remember" context and retrieve the most relevant snippets when generating the final report, rather than relying on simple keyword matching.

#### Analyst & Writer: `generator.py` (Gemini)
The Analyst is powered by **Google's Gemini Pro** model. It takes the user's topic and the context retrieved from memory to craft in-depth and engaging reports. It uses a sophisticated prompt structure to ensure the output is factual, well-structured, and includes a credibility score.

#### Quality Control: `quality.py`
The `CitationEvaluator` acts as a quality assurance step. It validates the structure of the generated JSON and ensures that the report contains necessary fields like insights, credibility scores, and sources.

## Essential Tools and Utilities
The agent is equipped with a variety of tools to perform its tasks effectively.

### Web Search (`search_google`)
A robust tool that interfaces with external search APIs. It includes error handling and, crucially, a **Mock Mode** that generates realistic synthetic data when API keys are missing, ensuring development can continue without dependencies.

### Vector Storage (`ResearchMemory`)
This utility manages the lifecycle of embeddings. It handles the addition of new documents and the semantic querying of existing knowledge, bridging the gap between raw search results and the LLM's context window.

### Report Generation (`generate_report`)
The core creative tool that synthesizes the "read" information into a "written" format. It formats the output as a structured JSON object, making it easy for the frontend to render.

## Conclusion
The beauty of the Deep Research AI Agent lies in its streamlined workflow. The backend acts as a project manager, coordinating the efforts of its specialized modules. It delegates tasks (Search -> Store -> Retrieve -> Generate), and ensures that each stage of the research process is completed successfully. This modular coordination results in a system that is robust, scalable, and easy to extend.

## Value Statement
The Deep Research AI Agent reduced my research time for new topics by **90%**, enabling me to produce comprehensive briefs in seconds rather than hours. I have also been able to explore new domains—as the agent drives research that I'd otherwise not be able to do given time constraints.

If I had more time, I would add an additional agent to recursively follow up on interesting sub-topics found in the initial search, creating a "Deep Dive" loop.

## Author
**Swastik Tiwari**

## License
This Writeup has been released under the Attribution 4.0 International (CC BY 4.0) license.
