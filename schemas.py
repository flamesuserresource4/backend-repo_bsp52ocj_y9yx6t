"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

class Contactlead(BaseModel):
    """
    Collection: "contactlead"
    Stores enquiries/quote requests from the website contact form.
    """
    name: str = Field(..., description="Full name of the requester")
    email: EmailStr = Field(..., description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company/Store name")
    interest: Optional[Literal[
        'Wholesale Purchase',
        'Custom Box Making',
        'Branding on Boxes/Purses',
        'Other'
    ]] = Field(None, description="Primary interest category")
    message: Optional[str] = Field(None, description="Message/requirements")

# Example schemas (kept for reference)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = Field(None, ge=0, le=120)
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    category: str
    in_stock: bool = True
