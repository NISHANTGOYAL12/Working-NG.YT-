import openai

def create_script(topic):
    prompt = f"Create a 45-second YouTube Shorts script about: {topic}, in Hindi, storytelling style."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
