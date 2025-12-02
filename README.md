<div align="center">

# 🎙️ AI Podcaster

[🇺🇸 English](#-ai-podcaster) | [🇧🇷 Português](#-ai-podcaster-pt-br)

</div>

---

# 🇺🇸 AI Podcaster

**AI Podcaster** is an automated tool that generates podcast episodes from a simple text theme. It uses advanced AI agents to plan topics, write scripts, and synthesize realistic speech using multi-speaker TTS (Text-to-Speech).

## ✨ Features

-   **🤖 AI Topic Planning**: Automatically researches and structures a podcast episode based on a given theme.
-   **📝 Script Generation**: Creates engaging, multi-speaker dialogues with distinct personalities.
-   **🗣️ Realistic TTS**: Uses **Coqui TTS (XTTS v2)** for high-quality, emotive voices (or gTTS for fast prototyping).
-   **🎧 Audio Assembly**: Combines intro, dialogue sections, and outro into a single seamless podcast file.
-   **🌍 Multi-language Support**: Configurable language support (default: Portuguese/English).

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

-   **Python 3.10+**
-   **ffmpeg** (Required for audio processing)
    -   macOS: `brew install ffmpeg`
    -   Ubuntu: `sudo apt install ffmpeg`
    -   Windows: `winget install ffmpeg`

## 🚀 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/danielthejoker18/podcaster.git
    cd podcaster
    ```

2.  **Run the setup script**:
    This script creates a virtual environment and installs all necessary dependencies (including pinned versions for compatibility).
    ```bash
    chmod +x start-setup.sh
    ./start-setup.sh
    ```

## ⚙️ Configuration

1.  **Environment Variables (`.env`)**:
    Copy `.env.example` to `.env` and set your API keys (Groq/OpenAI) and TTS provider settings.

2.  **Podcast Settings (`podcast_config.yaml`)**:
    Edit `podcast_config.yaml` to customize:
    -   **Theme**: The topic of the podcast.
    -   **Speakers**: Names, personalities, and voice files.
    -   **Style**: The tone of the conversation.

    ```yaml
    episode:
      theme: "Future of AI"
      duration_minutes: 10
    speakers:
      - name: "Alice"
        voice_file: "voices/alice.wav"
    ```

3.  **Voice Cloning**:
    To use distinct voices, place `.wav` reference files in the `voices/` directory and update `podcast_config.yaml` to point to them.

## 🎬 Usage

1.  **Activate the virtual environment**:
    ```bash
    source venv/bin/activate
    ```

2.  **Run the Generator**:
    Uses settings from `podcast_config.yaml`.
    ```bash
    python main.py
    ```

3.  **Command Line Overrides**:
    You can override settings without editing the config file:
    ```bash
    # Generate a podcast on a specific topic
    python main.py --theme "The History of Jazz"
    
    # Set a custom duration
    python main.py --theme "Quick News" --duration 2
    
    # Use a different config file
    python main.py --config my_custom_config.yaml
    ```

4.  **Output**:
    -   Individual audio segments are saved in `output/audio/`.
    -   The final podcast mix is saved in the `output/` directory.

## 📂 Project Structure

```
podcaster/
├── agents/             # AI Agents for planning and scripting
├── llms/               # LLM Provider wrappers (Groq/OpenAI)
├── tts/                # Text-to-Speech providers (Coqui/gTTS)
├── utils/              # Audio processing and helper functions
├── voices/             # Reference audio files for voice cloning
├── main.py             # Entry point
├── podcast_config.yaml # Podcast configuration
├── requirements.txt    # Python dependencies
└── start-setup.sh      # Installation script
```

## ⚠️ Known Issues & Fixes

-   **Coqui TTS & PyTorch**: If you encounter `ImportError: cannot import name 'add_safe_globals'`, ensure you are using the patched `tts/coqui_provider.py` included in this repo.
-   **Groq Models**: If you see `model_decommissioned` errors, update `MODELO` in `.env` to a current model like `llama-3.3-70b-versatile`.

---

# 🇧🇷 AI Podcaster (PT-BR)

**AI Podcaster** é uma ferramenta automatizada que gera episódios de podcast a partir de um tema simples em texto. Ela utiliza agentes de IA avançados para planejar tópicos, escrever roteiros e sintetizar fala realista usando TTS (Text-to-Speech) com múltiplos oradores.

## ✨ Funcionalidades

-   **🤖 Planejamento de Tópicos com IA**: Pesquisa e estrutura automaticamente um episódio de podcast com base em um tema fornecido.
-   **📝 Geração de Roteiro**: Cria diálogos envolventes entre múltiplos oradores com personalidades distintas.
-   **🗣️ TTS Realista**: Usa **Coqui TTS (XTTS v2)** para vozes emotivas de alta qualidade (ou gTTS para prototipagem rápida).
-   **🎧 Montagem de Áudio**: Combina introdução, seções de diálogo e encerramento em um único arquivo de podcast contínuo.
-   **🌍 Suporte Multi-idioma**: Suporte a idiomas configurável (padrão: Português/Inglês).

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

-   **Python 3.10+**
-   **ffmpeg** (Necessário para processamento de áudio)
    -   macOS: `brew install ffmpeg`
    -   Ubuntu: `sudo apt install ffmpeg`
    -   Windows: `winget install ffmpeg`

## 🚀 Instalação

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/danielthejoker18/podcaster.git
    cd podcaster
    ```

2.  **Execute o script de configuração**:
    Este script cria um ambiente virtual e instala todas as dependências necessárias (incluindo versões fixadas para compatibilidade).
    ```bash
    chmod +x start-setup.sh
    ./start-setup.sh
    ```

## ⚙️ Configuração

1.  **Variáveis de Ambiente (`.env`)**:
    Copie `.env.example` para `.env` e configure suas chaves de API (Groq/OpenAI) e provedor de TTS.

2.  **Configurações do Podcast (`podcast_config.yaml`)**:
    Edite `podcast_config.yaml` para personalizar:
    -   **Tema**: O tópico do podcast.
    -   **Speakers**: Nomes, personalidades e arquivos de voz.
    -   **Estilo**: O tom da conversa.

    ```yaml
    episode:
      theme: "Futuro da IA"
      duration_minutes: 10
    speakers:
      - name: "Alice"
        voice_file: "voices/alice.wav"
    ```

3.  **Clonagem de Voz**:
    Para usar vozes distintas, coloque arquivos de referência `.wav` no diretório `voices/` e atualize o `podcast_config.yaml` para apontar para eles.

## 🎬 Uso

1.  **Ative o ambiente virtual**:
    ```bash
    source venv/bin/activate
    ```

2.  **Execute o Gerador**:
    Usa as configurações do `podcast_config.yaml`.
    ```bash
    python main.py
    ```

3.  **Argumentos de Linha de Comando**:
    Você pode substituir configurações sem editar o arquivo:
    ```bash
    # Gerar um podcast sobre um tópico específico
    python main.py --theme "A História do Jazz"
    
    # Definir uma duração personalizada
    python main.py --theme "Notícias Rápidas" --duration 2
    
    # Usar um arquivo de configuração diferente
    python main.py --config meu_config_customizado.yaml
    ```

4.  **Saída**:
    -   Segmentos de áudio individuais são salvos em `output/audio/`.
    -   O mix final do podcast é salvo no diretório `output/`.

## 📂 Estrutura do Projeto

```
podcaster/
├── agents/             # Agentes de IA para planejamento e roteiro
├── llms/               # Wrappers para provedores de LLM (Groq/OpenAI)
├── tts/                # Provedores de Text-to-Speech (Coqui/gTTS)
├── utils/              # Processamento de áudio e funções auxiliares
├── voices/             # Arquivos de áudio de referência para clonagem de voz
├── main.py             # Ponto de entrada
├── podcast_config.yaml # Configuração do podcast
├── requirements.txt    # Dependências Python
└── start-setup.sh      # Script de instalação
```

## ⚠️ Problemas Conhecidos & Correções

-   **Coqui TTS & PyTorch**: Se você encontrar `ImportError: cannot import name 'add_safe_globals'`, certifique-se de estar usando o `tts/coqui_provider.py` corrigido incluído neste repositório.
-   **Modelos Groq**: Se você vir erros `model_decommissioned`, atualize o `MODELO` no `.env` para um modelo atual como `llama-3.3-70b-versatile`.

---
*Bom Podcasting!* 🎙️
