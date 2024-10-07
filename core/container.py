from dependency_injector import containers, providers

from core.config import configs
from core.database import Database
from repositories.post_repository import PostRepository
from repositories.tag_repository import TagRepository
from repositories.user_repository import UserRepository
from services.auth_service import AuthService
from services.post_service import PostService
from services.tag_service import TagService
from services.user_service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["apis.v1.endpoints.auth",
                                                            "apis.v1.endpoints.post",
                                                            "apis.v1.endpoints.tag",
                                                            "apis.v1.endpoints.user",
                                                            "apis.v2.endpoints.auth",
                                                            "core.dependencies"])

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    post_repository = providers.Factory(PostRepository, session_factory=db.provided.session)
    tag_repository = providers.Factory(TagRepository, session_factory=db.provided.session)
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    post_service = providers.Factory(PostService, post_repository=post_repository, tag_repository=tag_repository)
    tag_service = providers.Factory(TagService, tag_repository=tag_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
