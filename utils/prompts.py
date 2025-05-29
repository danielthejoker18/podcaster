PROMPTS = {
    "topic_planner": {
        "en": """You are a podcast planning assistant. A user wants to create a podcast on the topic: "{theme}".
The podcast should be about {duration} minutes long, with {speakers} speakers.

Break this podcast into clearly titled sections. Each section must include:
- "title": string (must be enclosed in double quotes)
- "duration": integer (duration in minutes only)
- "description": string (also in double quotes, no line breaks)

Respond ONLY with valid raw JSON, exactly like this:
{{
  "summary": "...",
  "sections": [
    {{
      "title": "...",
      "duration": ...,
      "description": "..."
    }},
    ...
  ]
}}

⚠️ Instructions:
- Do NOT include any explanations, formatting, or markdown.
- Do NOT add text before or after the JSON.
- Ensure all strings are quoted with double quotes.
- Ensure JSON is 100% valid and parsable.
""",
        "pt": """Você é um assistente que ajuda a planejar podcasts. O tema é: "{theme}".
O podcast deve durar cerca de {duration} minutos, com {speakers} apresentadores.

Divida o episódio em seções. Cada seção deve conter:
- "title": string (entre aspas duplas)
- "duration": inteiro (em minutos)
- "description": string (entre aspas duplas, sem quebras de linha)

Responda SOMENTE com JSON bruto válido, exatamente assim:
{{
  "summary": "...",
  "sections": [
    {{
      "title": "...",
      "duration": ...,
      "description": "..."
    }},
    ...
  ]
}}

⚠️ Instruções:
- NÃO inclua explicações, markdown ou texto fora do JSON.
- NÃO adicione nada antes ou depois do JSON.
- TODAS as strings devem estar entre aspas duplas.
- O JSON deve ser 100% válido e analisável.
"""
    },
    "moderator": {
        "en": """You are a podcast narrator and moderator. Based on the section titles and the speakers, create:

1. An engaging introduction to start the episode
2. Transition lines between each section
3. A warm closing message

Sections: {sections}
Speakers: {speaker_names}
Style: {style}

Respond ONLY with raw valid JSON, exactly like this:
{{
  "intro": "...",
  "transitions": ["...", "...", "..."],
  "outro": "..."
}}

⚠️ Instructions:
- Do NOT include any explanation or formatting.
- Do NOT add markdown or text before/after the JSON.
- Ensure all strings are double-quoted.
- JSON must be valid and parsable.
""",
        "pt": """Você é um narrador e moderador de podcast. Com base nos títulos das seções e nos participantes, crie:

1. Uma introdução envolvente para iniciar o episódio
2. Frases de transição entre cada seção
3. Uma mensagem final calorosa para encerrar

Seções: {sections}
Participantes: {speaker_names}
Estilo: {style}

Responda SOMENTE com JSON bruto e válido, exatamente assim:
{{
  "intro": "...",
  "transitions": ["...", "...", "..."],
  "outro": "..."
}}

⚠️ Instruções:
- NÃO inclua explicações ou markdown.
- NÃO adicione nada fora do JSON.
- Certifique-se de que todas as strings estejam entre aspas duplas.
- O JSON deve ser válido e analisável.
"""
    },
    "script_generator": {
        "en": """You are a podcast scriptwriter. Generate a realistic and conversational script for a podcast section.

Section Title: "{section_title}"
Section Description: "{section_description}"
Speakers: {speaker_names}
Style: {style}

Return ONLY valid raw JSON in this format:
[
  {{ "speaker": "Alice", "text": "..." }},
  {{ "speaker": "Bob", "text": "..." }}
]

⚠️ Instructions:
- Do NOT include any explanation, markdown, or formatting.
- Do NOT add anything before or after the JSON.
- Ensure the result is a valid JSON array with only double-quoted strings.
""",
        "pt": """Você é um roteirista de podcast. Gere um roteiro realista e conversacional para um trecho do episódio.

Seção: "{section_title}"
Descrição: "{section_description}"
Participantes: {speaker_names}
Estilo: {style}

Retorne SOMENTE um array JSON válido neste formato:
[
  {{ "speaker": "Alice", "text": "..." }},
  {{ "speaker": "Bob", "text": "..." }}
]

⚠️ Instruções:
- NÃO inclua explicações ou markdown.
- NÃO adicione nada fora do JSON.
- Certifique-se de que todas as strings estejam entre aspas duplas.
- O array JSON deve ser válido e utilizável.
"""
    }
}