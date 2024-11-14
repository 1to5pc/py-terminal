def NatLangParser(userInput):
    import google.generativeai as genai
    import os
    import json

    genai.configure(api_key=os.environ["GEMINI_APIKEY"])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = """Convert the final input to this format("text" refers to the text that needs to be written other than the commands/order).
    Example input: "write this is a note to myfile.txt"
    The file_name here is "myfile.txt" and the text is "this is a note".
    Example input 2: "write A paragraph of text. Not at all\nNew line to myfileNEW"
    The file_name here is "myfilenEW" and the text is "A paragraph of text. Not at all\nNew line".


    Use this JSON schema without any formatting:

    output = {"file_name": str, "text": str}
    Return: output\n This is the input to parse: """ + userInput

    response = model.generate_content(prompt)
    content = response.text.replace("`","").replace("json","")
    print(content)
    try:
        respdic = json.loads(content)
        return 0, respdic['file_name'], respdic['text']
    except:
        return -1, "", "" # JSON parse error
