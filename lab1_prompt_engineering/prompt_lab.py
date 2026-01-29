import openai

prompt = "Write a 150-word explanation of renewable energy."

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role":"user","content":prompt}]
)

print(response["choices"][0]["message"]["content"])
