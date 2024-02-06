from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from models.data_models import Customer,Task
from core import setup as db_setup
#from api.v1.router import customers



class AppBuilder:
    def __init__(self):
        self._app = FastAPI(
            title=settings.API_TITLE, description=settings.APP_DESPRICTION
        )

    def register_routes(self):
        # self._app.include_router(
        #     customers.router,
        #     prefix=setting.API_PREFIX,
        #     tags=["Authentication"],
        #)
        # self._app.include_router(
        #     enquiry.name_router, prefix=settings.API_PREFIX, tags=["Name Enquiry"]
        # )

        @self._app.get("/", include_in_schema=False)
        def _index():
            return responses.RedirectResponse("/docs")
        
        @self._app.get("/about", include_in_schema=False)
        def _about():
            return {"message":"a task management api"}

    def register_middlewares(self):
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def register_database(self) -> None:
        """Register all databases"""
        db_setup.Base.metadata.create_all(
            bind=db_setup.database.get_engine  # type : ignore
        )
    

    def get_app(self):
        self.register_routes()
        self.register_middlewares()
        self.register_database()
        return self._app
