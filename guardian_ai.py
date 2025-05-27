from llama_cpp import Llama

# Load Zephyr model
GUARDIAN_PATH = "models/guardian_zephyr.gguf"
guardian_model = Llama(
    model_path=GUARDIAN_PATH,
    n_ctx=4096,
    n_threads=8,
    chat_format="chatml",
    verbose=True
)

# Truncate helper to avoid token overflow
def truncate_tokens(text: str, max_chars: int = 3000) -> str:
    return text[:max_chars] + "..." if len(text) > max_chars else text

# Guardian response generator
def guardian_critique_response(prompt: str, mistral_reply: str, openhermes_reply: str) -> str:
    try:
        mistral_reply = truncate_tokens(mistral_reply, 2000)
        openhermes_reply = truncate_tokens(openhermes_reply, 2000)


        combined_input = truncate_tokens(f"""<|system|>
        You are Guardian AI. Your job is to critique two AI responses.

        Your output must include:
        1. A critique comparing both responses.
        2. A short, simplified summary to help a layperson understand the topic better.

        In the critique, you must:
        - Identify strengths and weaknesses
        - Point out missing information
        - Say which response is better and why

        Keep your tone clear, neutral, and concise.
        <|user|>
        Prompt:
        {prompt}

        <|assistant|>
        Mistral's Response:
        {mistral_reply}

        OpenHermes's Response:
        {openhermes_reply}
        </s>
        """, 3500)



        output = guardian_model(combined_input, max_tokens=2048, echo=False)
        return output["choices"][0]["text"].replace("<|>", "").strip()

    except Exception as e:
        print(f"[Guardian Critique Error]: {e}")
        return "⚠️ Guardian critique failed."
