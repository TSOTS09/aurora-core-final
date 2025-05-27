from llama_cpp import Llama

MODEL_PATH = "models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"

dream_model = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=8)

def dream_response(prompt):
    prompt = f"[INST] {prompt} [/INST]"
    response = dream_model(prompt, max_tokens=1024, stop=["</s>"])
    return response["choices"][0]["text"].strip()

mistral_response = dream_response
