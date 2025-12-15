from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "student"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level: Mapped[str] = mapped_column(String)
    education_form: Mapped[str] = mapped_column(String)
    subject_id: Mapped[int] = mapped_column(Integer)
