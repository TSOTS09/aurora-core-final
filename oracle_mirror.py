# oracle_mirror.py
from llama_cpp import Llama

ORACLE_PATH = "models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"

oracle = Llama(model_path=ORACLE_PATH, n_ctx=2048, n_threads=8)

def oracle_response(prompt: str) -> str:
    output = oracle(prompt, max_tokens=256, echo=False)
    return output["choices"][0]["text"].strip()
