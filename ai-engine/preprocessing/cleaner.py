import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize customer feedback text.
    """

    if not isinstance(text, str):
        return ""

    # Remove leading/trailing spaces
    text = text.strip()

    # Normalize Unicode characters
    text = unicodedata.normalize("NFKC", text)

    # Replace multiple spaces/newlines
    text = re.sub(r"\s+", " ", text)

    return text


def remove_noise(text: str) -> str:
    """
    Remove unnecessary repeated characters and symbols.
    """

    # Reduce excessive repeated punctuation
    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r"\.{3,}", "...", text)

    # Reduce repeated characters:
    # soooo bad -> soo bad
    text = re.sub(r"(.)\1{3,}", r"\1\1", text)

    return text


def clean_text(text: str) -> str:
    """
    Complete preprocessing pipeline.
    """

    text = normalize_text(text)

    if not text:
        return ""

    text = remove_noise(text)

    return text