
from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
from ..model.PersonneModel import Personne
from ..model import PersonneModel
from ..schema import PersonneSchema

#------------------------------------requetes crud personne--------------------------------#

def get_all_personne(db: Session):
    return db.query(PersonneModel.Personne).all()

def create_personne(db: Session, personne: PersonneSchema):

    new_personne = Personne(**personne.dict())

    db.add(new_personne)
    db.commit()
    db.refresh(new_personne)

    return {
        "message": "personne cree",
        "detail": "success",
        "personne": new_personne
    }

def update_personne(db: Session, personne_id: int, personne: PersonneSchema):

    db_personne = db.query(Personne).filter(Personne.id == personne_id).first()
    if not db_personne:
        raise HTTPException(status_code=404, detail="Personne non trouvé")

    for key, value in personne.dict().items():
        setattr(db_personne, key, value)

    db.commit()
    db.refresh(db_personne)

    return {
        "message": "personne mis à jour avec succès",
        "detail": "success",
        "personne": db_personne
    }

def delete_personne(db: Session, id: int):
    del_personne = db.query(Personne).filter(Personne.id == id).first()
    if not del_personne:
        raise HTTPException(status_code=404, detail="Personne non trouvé")
    db.delete(del_personne)
    db.commit()
