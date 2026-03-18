from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def review_code(code):

    prompt = f"""
You are a senior software engineer.

Review the following code and provide:

1. Bugs
2. Code improvements
3. Security issues
4. Code quality score out of 10

Code:
{code}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content