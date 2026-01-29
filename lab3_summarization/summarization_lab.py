import openai

text = open("source_texts.txt").read()

prompt = f"Summarize the following text in three bullet points:\n{text}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role":"user","content":prompt}]
)

print(response["choices"][0]["message"]["content"])
