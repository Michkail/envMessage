from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from core.container import Container
from core.dependencies import get_current_active_user
from core.middleware import inject
from schema.auth_schema import SignIn, SignInResponse, SignUp
from schema.user_schema import User
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign-in", response_model=SignInResponse)
@inject
def sign_in(user_info: SignIn, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_in(user_info)


@router.post("/sign-up", response_model=User)
@inject
def sign_up(user_info: SignUp, service: AuthService = Depends(Provide[Container.auth_service])):
    return service.sign_up(user_info)


@router.get("/me", response_model=User)
@inject
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user
