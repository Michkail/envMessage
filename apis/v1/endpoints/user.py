from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from core.container import Container
from core.dependencies import get_current_super_user
from core.middleware import inject
from core.security import JWTBearer
from schema.base_schema import Blank
from schema.user_schema import FindUser, FindUserResult, UpsertUser, User
from services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"], dependencies=[Depends(JWTBearer())])


@router.get("", response_model=FindUserResult)
@inject
def get_user_list(find_query: FindUser = Depends(),
                  service: UserService = Depends(Provide[Container.user_service]),
                  current_user: User = Depends(get_current_super_user)):
    return service.get_list(find_query)


@router.get("/{user_id}", response_model=User)
@inject
def get_user(user_id: int,
             service: UserService = Depends(Provide[Container.user_service]),
             current_user: User = Depends(get_current_super_user)):
    return service.get_by_id(user_id)


@router.post("", response_model=User)
@inject
def create_user(user: UpsertUser,
                service: UserService = Depends(Provide[Container.user_service]),
                current_user: User = Depends(get_current_super_user)):
    return service.add(user)


@router.patch("/{user_id}", response_model=User)
@inject
def update_user(user_id: int,
                user: UpsertUser,
                service: UserService = Depends(Provide[Container.user_service]),
                current_user: User = Depends(get_current_super_user)):
    return service.patch(user_id, user)


@router.delete("/{user_id}", response_model=Blank)
@inject
def delete_user(user_id: int,
                service: UserService = Depends(Provide[Container.user_service]),
                current_user: User = Depends(get_current_super_user)):
    return service.remove_by_id(user_id)