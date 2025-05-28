PROMPTS = {
    "topic_planner": {
        "en": """You are a podcast planning assistant. A user wants to create a podcast on the topic: "{theme}".
The podcast should be about {duration} minutes long, with {speakers} speakers.

Break this podcast into clearly titled sections. Each section should include:
- A title
- An estimated duration (in minutes)
- A short description of what the speakers will cover

Respond in JSON format like this:
{
  "summary": "...",
  "sections": [
    {
      "title": "...",
      "duration": "...",
      "description": "..."
    },
    ...
  ]
}
""",
        "pt": """Você é um assistente que ajuda a planejar podcasts. O tema é: "{theme}".
O podcast deve durar cerca de {duration} minutos, com {speakers} apresentadores.

Divida o episódio em seções com:
- Título
- Duração estimada (em minutos)
- Uma breve descrição do conteúdo

Responda no formato JSON assim:
{
  "summary": "...",
  "sections": [
    {
      "title": "...",
      "duration": "...",
      "description": "..."
    },
    ...
  ]
}
"""
    }
}
