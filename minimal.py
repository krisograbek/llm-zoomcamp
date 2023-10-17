import openai

openai.api_key = "Your API Key Here"


def get_chat_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content


print(get_chat_response("Tell me a fun fact"))
