from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float, ARRAY, Enum,DateTime,JSON
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy.sql import func
import enum


class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    role = Column(String(10), default="user", nullable=False)
    
    # Barcha relationshiplar
    carts = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    total_amount = Column(Float, nullable=False)

    # Relationship with user
    user = relationship("User", back_populates="carts")

    # Relationship with cart items
    cart_items = relationship("CartItem", back_populates="cart")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)

    # Relationship with cart and product
    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(250), unique=True, nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column(String(400), nullable=False)
    description = Column(String(400), nullable=False)
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    brand = Column(String(400), nullable=False)
    thumbnail = Column(String(400), nullable=False)
    images = Column(JSON, nullable=False)  # ARRAY o'rniga JSON
    is_published = Column(Boolean, server_default="1", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)

    # Relationship kategoriyalar
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")

    # Relationshiplar
    order_items = relationship("OrderItem", back_populates="product")
    cart_items = relationship("CartItem", back_populates="product")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer,primary_key=True,nullable=False,unique=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    full_name = Column(String, nullable=False)
    phone = Column(String(255),nullable=False)
    tg_username = Column(String(255),nullable=True)

    address_line = Column(String, nullable=False)      # Asosiy manzil
    city = Column(String, nullable=False)              # Shahar
    postal_code = Column(String, nullable=True)        
    region = Column(String, nullable=False, default="Andijon")
    
    status = Column(String, nullable=False, default="pending")  
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False) 
    subtotal = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
    
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.INFO)   # umumiy log
logging.getLogger("sqlalchemy.orm.mapper").setLevel(logging.DEBUG)  # mapper log
