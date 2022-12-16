import replicate
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

model = replicate.models.get("stability-ai/stable-diffusion")
output_url = model.predict(prompt="multicolor space")[0]
print(output_url)
webbrowser.open(output_url)
