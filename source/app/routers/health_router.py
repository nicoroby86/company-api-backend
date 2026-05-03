from fastapi import APIRouter, HTTPException, status
from app.core.db import get_connection

router = APIRouter(
    prefix="/health",
    tags=['health'],
)

@router.get("")
def get_health():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        cur.fetchone()
        
        return {
            "status": "ok",
            "database": "connected",
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='database unavailable',
        )
    finally:
        conn.close()