import re
import unicodedata


def clean_text(text):
    """
    Clean customer feedback without destroying its meaning.
    """

    # If the value is not text, return empty text
    if not isinstance(text, str):
        return ""

    # 1. Normalize Unicode characters
    text = unicodedata.normalize("NFKC", text)

    # 2. Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    # 3. Reduce excessive punctuation
    text = re.sub(r"!{3,}", "!!", text)
    text = re.sub(r"\?{3,}", "??", text)
    text = re.sub(r"\.{4,}", "...", text)

    # 4. Reduce extreme repeated characters
    # Example: "sooooo" -> "soo"
    text = re.sub(r"(.)\1{3,}", r"\1\1", text)

    # 5. Remove spaces from beginning/end
    text = text.strip()

    return text
