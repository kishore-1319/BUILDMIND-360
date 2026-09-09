import streamlit as st
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)


MODEL_NAME = "Qwen/Qwen3-0.6B"


@st.cache_resource
def load_model():

    print("Loading BUILDMIND-360 model...")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME
    )

    if torch.cuda.is_available():
        model = model.to("cuda")
        print("Using NVIDIA GPU")
    else:
        print("Using CPU")

    model.eval()

    print("Model loaded successfully!")

    return tokenizer, model