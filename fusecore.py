from guardian_ai import guardian_critique_response
from dreamweaver import mistral_response
from openhermes import openhermes_response


# FuseCore Combiner
def fusecore_response(prompt: str, mistral_out: str, openhermes_out: str, guardian_out: str) -> str:
    print("DEBUG: fusecore_response called")
    print("Mistral:", mistral_out)
    print("OpenHermes:", openhermes_out)
    print("Guardian:", guardian_out)

    return f"""🧠 Mistral says:\n{mistral_out}\n\n🧠 OpenHermes says:\n{openhermes_out}\n\n🛡️ Critique:\n{guardian_out}"""





# Optional: remove this if unused
def fusecore_logic(prompt: str, mistral_out: str, openhermes_out: str, guardian_out: str) -> str:
    return f"""
🧠 Mistral says:\n{mistral_out}\n\n
💡 OpenHermes says:\n{openhermes_out}\n\n
🛡️ Critique:\n{guardian_out}
"""
