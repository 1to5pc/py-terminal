"""
This module defines all functions related to LLM functions
"""

def NatLangParser(userInput):
    """ Uses the Gemini API to extract  a filename and text from a user input string """
    import google.generativeai as genai
    import os
    import json
    try:
        genai.configure(api_key=os.environ["GEMINI_APIKEY"])
    except KeyError:
        return -2, "", ""
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = """Convert the final input into this format
    (where "text" refers to the content you want to write, and "file_name" refers to the file name):
    Example 1: Input: "write this is a note to myfile.txt"
    Here, the file_name is "myfile.txt" and the text is "this is a note".

    Example 2: Input: "write A paragraph of text. Not at all\nNew line to myfileNEW"
    Here, the file_name is "myfileNEW" and the text is "A paragraph of text. Not at all\nNew line".

    Use the following JSON schema (no extra formatting required):

    output = {"file_name": str, "text": str}

    Parse this input and return it in the format above: """ + userInput

    response = model.generate_content(prompt)
    content = response.text.replace("`","").replace("json","")
    print(content)
    try:
        respdic = json.loads(content)
        return 0, respdic['file_name'], respdic['text']
    except:
        return -1, "", "" # JSON parse error
