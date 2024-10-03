from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apis.v1.routes import routers as v1_routers
from apis.v2.routes import routers as v2_routers
from core.config import configs
from core.container import Container
from utils.class_object import singleton


@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(title=configs.PROJECT_NAME,
                           openapi_url=f"{configs.API}/openapi.json",
                           version="1.0.0")

        self.container = Container()
        self.db = self.container.db()

        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(CORSMiddleware,
                                    allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                                    allow_credentials=True,
                                    allow_methods=["*"],
                                    allow_headers=["*"])

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(v1_routers, prefix=configs.API_V1_STR)
        self.app.include_router(v2_routers, prefix=configs.API_V2_STR)


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
