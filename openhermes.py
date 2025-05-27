from llama_cpp import Llama

OPENHERMES_PATH = "models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"

openhermes_model = Llama(
    model_path=OPENHERMES_PATH,
    n_ctx=2048,
    n_threads=8,
    chat_format="chatml",  # critical for proper output
    verbose=True
)

def openhermes_response(prompt: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful and knowledgeable AI assistant."},
        {"role": "user", "content": prompt}
    ]
    output = openhermes_model.create_chat_completion(
    messages=messages,
    max_tokens=2048,  # or even 3072 if needed
    temperature=0.7
)

    result = output["choices"][0]["message"]["content"].strip()
    print("[OpenHermes Result]:", result)
    return result
