from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView

from app.routers import products, categories, carts, users, auth, accounts, orders
from app.db.database import engine
from app.models import models

app = FastAPI(title="GYM API", version="1.0.0")

# CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# SQLAdmin
# -------------------------
class UserAdmin(ModelView, model=models.User):
    column_list = [models.User.id, models.User.username, models.User.email]

class ProductAdmin(ModelView, model=models.Product):
    column_list = [models.Product.id, models.Product.title, models.Product.price]

class CategoryAdmin(ModelView, model=models.Category):
    column_list = [models.Category.id, models.Category.name]

class OrderAdmin(ModelView, model=models.Order):
    column_list = [models.Order.id, models.Order.total_amount, models.Order.status]

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(OrderAdmin)

# -------------------------
# Routers
# -------------------------
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(orders.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)
