from sqlalchemy.orm import Session
from app.models.models import Order, OrderItem, Product
from app.schemas.orders import OrderCreate, OrderUpdate
from fastapi import HTTPException, status

class OrderService:
    @staticmethod
    def get_all_orders(db: Session, page: int = 1, limit: int = 10, search: str = "", status_filter: str = None):
        query = db.query(Order).order_by(Order.id.desc())
        
        if status_filter:
            query = query.filter(Order.status == status_filter)
        
        if search:
            query = query.filter(Order.full_name.contains(search))
        
        orders = query.limit(limit).offset((page - 1) * limit).all()
        return orders  # Return orders list directly, not wrapped in dict

    @staticmethod
    def get_order(db: Session, order_id: int):
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Order with id {order_id} not found"
            )
        return order  # Return order object directly, not wrapped in dict

    @staticmethod
    def create_order(db: Session, order: OrderCreate):
        # Create the main order
        db_order = Order(
            user_id=order.user_id,
            full_name=order.full_name,
            phone=order.phone,
            tg_username=order.tg_username,
            address_line=order.address_line,
            city=order.city,
            postal_code=order.postal_code,
            region=order.region,
            status=order.status,
            total_amount=order.total_amount
        )
        
        # Add order items
        for item in order.items:
            # Verify product exists
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Product with id {item.product_id} not found"
                )
            
            # Create order item
            order_item = OrderItem(
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price,
                subtotal=item.subtotal
            )
            db_order.items.append(order_item)
        
        # Save to database
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        
        return db_order  # Return order object directly, not wrapped in dict

    @staticmethod
    def update_order(db: Session, order_id: int, updated_order: OrderUpdate):
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Order with id {order_id} not found"
            )
        
        # Update only provided fields
        update_data = updated_order.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_order, key, value)
        
        db.commit()
        db.refresh(db_order)
        
        return db_order  # Return order object directly, not wrapped in dict

    @staticmethod
    def delete_order(db: Session, order_id: int):
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Order with id {order_id} not found"
            )
        
        db.delete(db_order)
        db.commit()
        
