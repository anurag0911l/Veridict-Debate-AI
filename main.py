from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# ---------------- APP ---------------- #

app = FastAPI()

# ... BACK AREA ... #

client = OpenAI(
    api_key="API_KEY_HERE",
    base_url="https://api.groq.com/openai/v1"
)

# .... ENGINE MODEL ... #

class ChatRequest(BaseModel):
    messages: list[dict]

# ... CHAT ENDPOINT ... #

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        # System prompt

        system_prompt = """
You are an elite AI debate opponent.

Your job:
- Debate against the user intelligently.
- Defend your position strongly.
- Counter the user's arguments.
- Sound human and persuasive.
- Use logic, evidence, and reasoning.
- Keep responses conversational.
- DO NOT write essays.
- DO NOT sound robotic.
- Keep responses concise but powerful.
- Engage like a real live debate.

You are in a REAL-TIME debate.
"""

        # Build messages

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add conversation history

        for msg in request.messages:

            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Generate response

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.8
        )

        response = completion.choices[0].message.content

        return {
            "response": response
        }

    except Exception as e:

        return {
            "error": str(e)
        }
