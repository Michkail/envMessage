# Setup Environment

## uv _Package Manager_
### Installation
> $ curl -LsSf https://astral.sh/uv/install.sh | sh 

### Sync Project
> $ uv sync
 
## run FastAPI
### with reload option
> $ uv run uvicorn app.main:app --reload

### with specific host option
> $ uv run uvicorn app.main:app --host 0.0.0.0

### with specific port option
> $ uv run uvicorn app.main:app --port 8000




