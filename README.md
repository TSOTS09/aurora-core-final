# Aurora Core

Aurora Core is a locally hosted multi-model AI platform built for the NVIDIA Agent Toolkit Hackathon. It features:

- **Model Selector**: Choose from Mistral, OpenHermes, Guardian AI, or FuseCore (a fusion of all three).
- **Image Generation**: Powered by Stable Diffusion.
- **Research Agent**: Performs live web searches using the AgentIQ framework.
- **Chat History**: Displays past interactions and allows for clearing history.

---

## 🧠 Features

- **Chat Interface** – Chat with Mistral, OpenHermes, or both using Guardian critique.
- **FuseCore Mode** – Get the most logical fusion of multiple LLM outputs.
- **Stable Diffusion Image Generator** – Select a style and prompt to create images.
- **Live Web Researcher** – Powered by NVIDIA AgentIQ to retrieve real-time info.

---

## 💻 Getting Started

### Requirements
- Python 3.10+
- `llama-cpp-python`
- `flask`, `requests`, `datetime`
- Your own local `.gguf` models in the `models` folder

### How to Run

```bash
python app.py


## 🧾 License
This project is for the NVIDIA Agent Toolkit Hackathon 2025. All rights reserved by the creator.

## 👤 Author
Built by Noah Ogle.
