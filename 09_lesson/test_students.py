import pytest

from db import SessionLocal
from models import Student


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        session.query(Student).delete()
        session.commit()
        yield session
    finally:
        session.close()


def test_create_student(db_session):
    student = Student(
        user_id=99999,
        level="Beginner",
        education_form="group",
        subject_id=1,
    )

    db_session.add(student)
    db_session.commit()

    saved = (
        db_session.query(Student)
        .filter_by(user_id=99999)
        .first()
    )

    assert saved is not None
    assert saved.user_id == 99999


def test_update_student(db_session):
    student = Student(
        user_id=99998,
        level="Beginner",
        education_form="group",
        subject_id=1,
    )

    db_session.add(student)
    db_session.commit()

    student.level = "Intermediate"
    db_session.commit()

    assert student.level == "Intermediate"


def test_delete_student(db_session):
    student = Student(
        user_id=99997,
        level="Beginner",
        education_form="group",
        subject_id=1,
    )

    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    assert (
        db_session.query(Student)
        .filter_by(user_id=99997)
        .first()
        is None
    )
