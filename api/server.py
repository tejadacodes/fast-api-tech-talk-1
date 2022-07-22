from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api.deps import get_db
from api.models.items import Item
from api.core.database import Base, engine
from api.schemas.items import ItemCreate, ItemUpdate


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"message": "Tech talk is awesome!"}


@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items


@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    item_obj = Item(**item.dict())
    db.add(item_obj)
    db.commit()
    db.refresh(item_obj)
    return item_obj


@app.put("/items/{id}")
def create_item(id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(Item).where(Item.id == id).first()

    if not item:
        raise HTTPException(status_code=401, detail="Item not found")

    obj_data = jsonable_encoder(item)
    update_data = item_update.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(item, field, update_data[field])
    
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/items/{id}")
def create_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).where(Item.id == id).first()

    if not item:
        raise HTTPException(status_code=401, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}