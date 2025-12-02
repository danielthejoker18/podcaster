# Voice Samples

To enable distinct voices for your podcast speakers, please add reference audio files to this directory.

## Instructions

1.  Find or record a short audio clip (6-10 seconds) for each speaker.
    -   Ideally `.wav` format (22050Hz or 24000Hz mono/stereo).
    -   The audio should be clean speech without background music.
2.  Name them clearly, for example:
    -   `dick.wav`
    -   `sean.wav`
    -   `narrator.wav`
3.  Update your `.env` file to map the speakers to these files (see `VOICE_MAP`).

## Example .env Configuration

```env
VOICE_MAP={"dick": "voices/dick.wav", "sean": "voices/sean.wav", "narrator": "voices/narrator.wav"}
```
