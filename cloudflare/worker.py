import json
from js import Response
from main import main

async def on_request(request):
    """Cloudflare Worker entrypoint."""
    main()
    return Response.new(
        json.dumps({"message": "Podcast generation started"}),
        {"headers": {"Content-Type": "application/json"}}
    )
