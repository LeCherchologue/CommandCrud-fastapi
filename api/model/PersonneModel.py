
    from sqlalchemy import Column, Integer, String, func, DateTime, Boolean, ForeignKey,Date
    from sqlalchemy.orm import relationship
    from ..bdd.connexion import Base

    class Personne(Base):
        __tablename__ = "personne"
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        nom = Column(String(255))
prenom = Column(String(255))
