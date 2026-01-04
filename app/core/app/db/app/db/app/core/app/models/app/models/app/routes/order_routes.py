from fastapi import APIRouter, HTTPException
from app.services.cart_service import get_cart, clear_cart
from app.services.order_service import create_order
from app.core.rate_limiter import rate_limiter

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/checkout/{user_id}")
def checkout(user_id: str):
    rate_limiter(user_id)

    cart_items = get_cart(user_id)
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = {
        "user_id": user_id,
        "items": cart_items,
        "status": "PLACED"
    }

    create_order(order)
    clear_cart(user_id)

    return {"message": "Order placed successfully"}
