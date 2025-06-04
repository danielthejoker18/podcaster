# Podcaster

This project generates podcast episodes using LLMs and text-to-speech providers.

## Running Locally

```bash
python main.py
```


## Deploying to Cloudflare Workers

A sample configuration is provided in `cloudflare/wrangler.toml`. It deploys
the Python worker defined in `cloudflare/worker.py`.

Install Wrangler and deploy:

```bash
npm install -g wrangler
wrangler deploy
```
