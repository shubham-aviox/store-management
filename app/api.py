from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from db import get_db
import crud, schemas
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

router: APIRouter = APIRouter()

@router.post('/item')
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
	return await crud.create(db=db, item=item_request)


@router.get('/items')
def get_all_items(db: Session = Depends(get_db)):
	return crud.get_all(db)


@router.get('/items/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
	db_item = crud.get_by_id(db, item_id)
	if db_item is None:
		raise HTTPException(status_code=404, detail="Item not found")
	return db_item


@router.delete('/items{item_id')
def delete_item(item_id: int, db: Session = Depends(get_db)):
	db_item = crud.get_by_id(db, item_id)
	if db_item is None:
		raise HTTPException(status_code=404, detail="Item not found")
	crud.delete(db, item_id)
	return "Item delete successfully"


@router.put('/items{item_id}')
def update_item(item_id: int, item: schemas.Item, db: Session = Depends(get_db)):
	db_item = crud.update(db, item_id, item)
	return item