import openai
import config

openai.api_key = config.api_key

messages = [{"role": "system",
            "content": "Eres un asistenete util."}]

content = input("¿Sobre que quiere hablar?")

messages.append({"role": "user", 
                  "content": content})

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                            messages=[{"role":"user", "content": content}])

print(response.choices[0].message.content)