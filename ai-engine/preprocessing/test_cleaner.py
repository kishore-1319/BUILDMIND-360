from preprocessing.cleaner import clean_text

test_reviews = [
    "   This app is sooo good!!!!! 😍😍   ",
    "Payment      is not working!!!",
    "I HATE THIS APP!!!!!! 😡😡😡",
    "Good",
    "😍😍😍",
    "   "
]

for review in test_reviews:

    cleaned = clean_text(review)

    print("RAW     :", repr(review))
    print("CLEANED :", repr(cleaned))
    print("-" * 50)
