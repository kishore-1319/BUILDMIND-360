from preprocessing.cleaner import clean_text


test_feedback = """
    THIS APP IS SOOOOO BAD!!!! 😡😡😡

    Payment doesn't work!!!

    After the latest update.....
"""


cleaned = clean_text(test_feedback)

print("RAW:")
print(test_feedback)

print("\nCLEANED:")
print(cleaned)