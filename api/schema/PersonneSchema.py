
    from pydantic import BaseModel, EmailStr
    from typing import Optional
    from datetime import datetime

    class PersonneSchema(BaseModel):

        nom : str
prenom : str
