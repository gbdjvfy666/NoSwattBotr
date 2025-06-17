from .start import router as start_router
from .shop import router as shop_router
from .profile import router as profile_router
from .support import router as support_router
from .bonus import router as bonus_router

routers = [
    start_router,
    shop_router,
    profile_router,
    support_router,
    bonus_router
]