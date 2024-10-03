from dependency_injector import containers, providers

from core.config import configs
from core.database import Database
from repositories import *
from services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["api.v1.endpoints.auth",
                                                            "api.v1.endpoints.post",
                                                            "api.v1.endpoints.tag",
                                                            "api.v1.endpoints.user",
                                                            "api.v2.endpoints.auth",
                                                            "core.dependencies"])

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    post_repository = providers.Factory(PostRepository, session_factory=db.provided.session)
    tag_repository = providers.Factory(TagRepository, session_factory=db.provided.session)
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    post_service = providers.Factory(PostService, post_repository=post_repository, tag_repository=tag_repository)
    tag_service = providers.Factory(TagService, tag_repository=tag_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
