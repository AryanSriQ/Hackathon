import streamlit as st
from dotenv import dotenv_values

# Machine Learning libraries
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Libraries for processing image
from PIL import ImageTk

# private modules
# sec = dotenv_values('auth.env')
authen = "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"

# Download stable diffusion model from hugging face
prmpt = st.text_input("Enter your prompt")
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=authen)
stable_diffusion_model.to(device)

def generate():
    """ This function generate image from a text with stable diffusion"""
    with autocast(device):
        image = stable_diffusion_model(prmpt.get(), guidance_scale=8.5)["sample"][0]

    st.image(image)

st.button(label="Generate the Image")
