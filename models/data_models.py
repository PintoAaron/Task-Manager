import sqlalchemy as sq
from sqlalchemy.orm import relationship
from core import setup



class Customer(setup.Base):
    __tablename__ = "customers"
    
    id = sq.Column(sq.Integer, primary_key=True)
    username = sq.Column(sq.String, nullable=False)
    first_name = sq.Column(sq.String, nullable=False)
    last_name = sq.Column(sq.String, nullable=False)
    password = sq.Column(sq.String, unique=True)
    email = sq.Column(sq.String, unique=True, nullable=False)
    phone = sq.Column(sq.String, unique=True, nullable=True)
    
    
    
    def __str__(self):
        return f"Customer-{self.username}"


class Task(setup.Base):
    __tablename__ = "tasks"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, nullable=False)
    description = sq.Column(sq.String, nullable=False)
    status = sq.Column(sq.Enum("pending", "completed", name="status"), default="pending", nullable=False)
    time = sq.Column(sq.types.DateTime(timezone=True), nullable=False)
    customer_id = sq.Column(sq.Integer, sq.ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", backref="tasks")
    
    
    def __str__(self):
        return f"Task-{self.title}"
    
