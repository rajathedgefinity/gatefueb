from sqlalchemy import Column, String, ForeignKey, Boolean, Integer, Numeric
# from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    # profiles = relationship("Profile", back_populates="user_id")
    # homes = relationship("Home", back_populates="home_id")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    mobile_no = Column(String)
    gender = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    # tenants = relationship("Tenant", back_populates="tenants_id")


class Home(Base):
    __tablename__ = "homes"

    id = Column(Integer, primary_key=True, index=True)
    community_name = Column(String)
    community_block = Column(String)
    community_no = Column(Numeric)
    user_id = Column(Integer, ForeignKey("users.id"))
    # tanants = relationship("Tenant", back_populates="tenants_id")


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    home_id = Column(Integer, ForeignKey("homes.id"))
    profile_id = Column(Integer, ForeignKey("profiles.id"))
