import re
import unicodedata


def normalize_text(text: str) -> str:
    """Normalize customer feedback text."""

    if not isinstance(text, str):
        return ""

    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def remove_noise(text: str) -> str:
    """Reduce excessive punctuation and repeated characters."""

    text = re.sub(r"!{3,}", "!!", text)
    text = re.sub(r"\?{3,}", "??", text)
    text = re.sub(r"\.{4,}", "...", text)
    text = re.sub(r"(.)\1{3,}", r"\1\1", text)
    return text


def clean_text(text: str) -> str:
    """Clean customer feedback without destroying its meaning."""

    text = normalize_text(text)
    if not text:
        return ""
    return remove_noise(text)
