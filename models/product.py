#creacion de modelo o esquema:

from pydantic import BaseModel, Field   #para crear nuestros modelos, field es para validaciones
from typing import Optional

class Product(BaseModel):   #va a heredar de basemodel
    id: Optional[int] = None       #campo opcional
    name: str =Field(default="new Product", min_lenght=5, max_lenght=15)  #si no se cumple, aparecera error
    price: float = Field(default=0, ge=0, le=1000)  #ge es mayor o igual, le es menor a
    stock: int = Field(default=0,gt=0)  #mayor que 0, valor por defeecto 0.
    
    
    
    