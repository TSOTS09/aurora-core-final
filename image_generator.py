from diffusers import StableDiffusionPipeline
from PIL import Image
import torch
import uuid
import os

# Load the normal Stable Diffusion model (not ONNX)
MODEL_ID = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available

def generate_image(prompt: str, output_dir="static/generated"):
    os.makedirs(output_dir, exist_ok=True)
    image = pipe(prompt).images[0]
    image = image.convert("RGB")
    filename = f"{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join(output_dir, filename)
    image.save(filepath)
    return filepath
