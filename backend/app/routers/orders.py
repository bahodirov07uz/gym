from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.schemas.orders import OrderCreate, OrderResponse, OrderUpdate
from app.services.orders import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# 🔹 GET /orders - barcha buyurtmalarni olish
@router.get("/", response_model=List[OrderResponse])
def get_orders(
    page: int = 1,
    limit: int = 10,
    search: Optional[str] = "",
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return OrderService.get_all_orders(
        db=db,
        page=page,
        limit=limit,
        search=search,
        status_filter=status
    )


# 🔹 GET /orders/{order_id} - bitta buyurtmani olish
@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return OrderService.get_order(db=db, order_id=order_id)


# 🔹 POST /orders - yangi buyurtma yaratish
@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return OrderService.create_order(db=db, order=order)


# 🔹 PUT /orders/{order_id} - mavjud buyurtmani yangilash
@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, updated_order: OrderUpdate, db: Session = Depends(get_db)):
    return OrderService.update_order(db=db, order_id=order_id, updated_order=updated_order)


# 🔹 DELETE /orders/{order_id} - buyurtmani o‘chirish
@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    OrderService.delete_order(db=db, order_id=order_id)
    return None  # 204 No Content shuning uchun body qaytarmaydi
