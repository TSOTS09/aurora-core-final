# Aurora Core

Aurora Core is a locally hosted multi-model AI platform built for the NVIDIA Agent Toolkit Hackathon. It features:

* **Model Selector**: Choose from Mistral, OpenHermes, or FuseCore (a fusion of both).
* **Image Generation**: Powered by Stable Diffusion.
* **Research Agent**: Performs live web searches using the AgentIQ framework.
* **Chat History**: Displays past interactions and allows for clearing history.

---

## 💬 Features

* **Chat Interface** – Chat with Mistral, OpenHermes, or both using Guardian critique.
* **FuseCore Mode** – Get the most logical fusion of multiple LLM outputs.
* **Stable Diffusion Image Generator** – Select a style and prompt to create images.
* **Live Web Researcher** – Powered by NVIDIA AgentIQ to retrieve real-time info.

---

## 📁 Model Setup

To run Aurora Core successfully, you must download **three** `.gguf` models and place them in the `models/` folder.

### Required Models

1. **Mistral-7B-Instruct GGUF**
   🔗 [Download from TheBloke on Hugging Face](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
   ⬇️ File needed: `mistral-7b-instruct-v0.1.Q5_K_M.gguf`
   📁 Place in: `models/`

2. **OpenHermes-2.5-Mistral GGUF**
   🔗 [Download from TheBloke on Hugging Face](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)
   ⬇️ File needed: `openhermes-2.5-mistral-7b.Q4_K_M.gguf`
   📁 Place in: `models/`

   ⚠️ **Important:** Rename the file to:

   ```bash
   openhermes-2.5-mistral-7b.Q4_K_M.gguf
   ```

3. **Guardian AI - Zephyr GGUF** (used for critique in FuseCore mode)
   🔗 [Download Zephyr model (e.g. Zephyr 7B-beta Q4\_K\_M)](https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF)
   ⬇️ File needed: `zephyr-7b-beta.Q4_K_M.gguf`
   📁 Place in: `models/`

   ⚠️ **Important:** Rename the file to:

   ```bash
   guardian_zephyr.gguf
   ```

---

### 📂 Final Folder Structure Example

```
aurora_core_backup/
├── models/
│   ├── mistral-7b-instruct-v0.1.Q5_K_M.gguf
│   ├── openhermes-2.5-mistral-7b.Q4_K_M.gguf
│   └── guardian_zephyr.gguf
├── llama.cpp/
├── AgentIQ/
```

---

## 🛠 Getting Started

### Requirements

* Python 3.10+
* `llama-cpp-python`
* `flask`, `requests`, `datetime`
* Your own local `.gguf` models in the `models` folder

📦 You will also need to download and install the following project dependencies manually:

* [AgentIQ (Official NVIDIA GitHub)](https://github.com/NVIDIA/AgentIQ)
* [llama.cpp (GitHub)](https://github.com/ggerganov/llama.cpp)

Place them in folders `AgentIQ/` and `llama.cpp/` respectively within the root directory.

### How to Run

```bash
python app.py
```

---

## 🔗 Additional Resources

📁 Google Drive Backup Folder: [AuroraCore-Final Submission Files](https://drive.google.com/drive/folders/1MAyhTnDcFe6ZaJTgdmzi4ItYP5XH0Jps?usp=drive_link)

🛠 If a response seems incomplete or doesn't load correctly in the chat UI, please try submitting the prompt again.

---

## 📟 License

This project is for the NVIDIA Agent Toolkit Hackathon 2025. All rights reserved by the creator.

## 👤 Author

Built by Noah Ogle.
