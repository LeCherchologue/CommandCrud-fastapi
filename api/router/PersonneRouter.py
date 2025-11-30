"
    from sqlalchemy.orm import Session
    from fastapi import APIRouter, Depends,Form, UploadFile,File
    from api.bdd.connexion import SessionLocal
    from api.schema.PersonneSchema import PersonneSchema
    from api.controller import PersonneController

    router = APIRouter()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    #--------------route Personne--------------------#

    @router.get("/personne" , tags=["personne"], response_model=list[PersonneSchema])
    async def get_personne():
        return PersonneController.get_all_Personne(db=SessionLocal())

    @router.post("/personne", tags=["personne"])
    async def create_personne(personne: PersonneSchema):
        db=SessionLocal()
        return PersonneController.create_personne(db=db, personne=personne)

    @router.put("/personne/id", tags=["personne"])
    async def update_personne(id: int, personne: PersonneSchema):
        db=SessionLocal()
        return PersonneController.update_personne(db=db, personne=personne, personne_id=id)

    @router.delete("/personne/id", tags=["personne"])
    async def delete_personne(id: int):
        db=SessionLocal()
        return PersonneController.delete_personne(db=db, id=id)

