from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float
    subtotal: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int  

    class Config:
        from_attributes = True  



class OrderBase(BaseModel):
    full_name: str
    phone: str
    tg_username: Optional[str] = None
    address_line: str
    city: str
    postal_code: Optional[str] = None
    region: str = "Andijon"
    status: str = "pending"
    total_amount: float


class OrderCreate(OrderBase):
    user_id: int  # OrderBase dan mustaqil
    items: List[OrderItemCreate]


class OrderResponse(OrderBase):
    id: int
    user_id: int 
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True  


class OrderItemUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    subtotal: Optional[float] = None


class OrderUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    tg_username: Optional[str] = None
    address_line: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    region: Optional[str] = None
    status: Optional[str] = None
    total_amount: Optional[float] = None
    # items: Optional[List[OrderItemUpdate]] = None  # O'chirish kerak, chunki alohida update qilinadi