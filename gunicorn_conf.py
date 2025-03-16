import os

APP_PORT = os.getenv("PORT", 8000)

bind = f"0.0.0.0:{APP_PORT}"
module = "core.asgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

# certfile = "/etc/letsencrypt/live/your_domain.com/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/your_domain.com/privkey.pem"
