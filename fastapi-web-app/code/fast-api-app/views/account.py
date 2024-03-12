import fastapi

from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/account')
def account():
    return {}


@router.get('/register')
def register():
    return {}


@router.get('/login')
def login():
    return {}


@router.get('/logout')
def logout():
    return {}
