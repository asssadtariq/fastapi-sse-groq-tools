from fastapi import FastAPI

from api.app_routes import register_routes
from api.app_middleware import register_middleware

# init FastAPI app
app = FastAPI()


# register middleware to app
register_middleware(app)

# register routes to app
register_routes(app)


# define index route for health check
@app.get("/")
def healthcheck():
    """Health check endpoint."""
    return {
        "status": "OK",
        "message": "SuperCar Virtual Sales Assistant API is running! Replace this with your implementation.",
    }
