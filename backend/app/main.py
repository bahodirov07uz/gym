from app.routers import products, categories, carts, users, auth, accounts,orders
from fastapi import FastAPI


description = """
Welcome to the GYM API"""


app = FastAPI(
    description=description,
    title="GYM API",
    version="1.0.0",

    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
    debug=True
)


app.include_router(products.router)
app.include_router(categories.router)
app.include_router(orders.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)
