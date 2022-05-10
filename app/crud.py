from sqlalchemy.orm import Session
import models, schemas

async def create(db: Session, item: schemas.ItemCreate):
	db_item = models.Item(name=item.name,price=item.price,description=item.description,store_id=item.store_id)
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item


def get_all(db: Session):
	return db.query(models.Item).all()


def get_by_id(db:Session, id):
	return db.query(models.Item).filter(models.Item.id==id).first()


def get_by_name(db: Session, name):
	return db.query(models.Item).filter(models.Item.name==name)


def delete(db: Session, item_id):
	db_item = get_by_id(db, item_id)
	db.delete(db_item)
	db.commit()


def update(db: Session, item_id: int, item: schemas.Item):
	db_item = get_by_id(db, item_id)
	print(db_item, 'hhhhhhhhhhhhhhh')
	if db_item:
		updated_data = models.Item(**item.dict())
		db.commit()
