from sqlalchemy import text


def test_create_subject(db_session):
    db_session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9999, "title": "Test_Subject"}
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": 9999}
    ).fetchone()
    assert result is not None
    assert result[0] == "Test_Subject"

    db_session.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": 9999}
    )
    db_session.commit()


def test_update_teacher(db_session):
    db_session.execute(
        text(
            "INSERT INTO teacher (teacher_id, email, group_id) "
            "VALUES (:id, :email, :grp)"
        ),
        {"id": 9999, "email": "old@test.com", "grp": 1}
    )
    db_session.commit()

    db_session.execute(
        text("UPDATE teacher SET email = :new_email WHERE teacher_id = :id"),
        {"new_email": "new@test.com", "id": 9999}
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT email FROM teacher WHERE teacher_id = :id"),
        {"id": 9999}
    ).fetchone()
    assert result[0] == "new@test.com"

    db_session.execute(
        text("DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 9999}
    )
    db_session.commit()


def test_delete_student(db_session):
    db_session.execute(
        text(
            "INSERT INTO student (user_id, level, education_form, subject_id) "
            "VALUES (:uid, :lvl, :edu, :sub)"
        ),
        {"uid": 9999, "lvl": "Beginner", "edu": "test_form", "sub": 1}
    )
    db_session.commit()

    db_session.execute(
        text("DELETE FROM student WHERE user_id = :uid"),
        {"uid": 9999}
    )
    db_session.commit()

    result = db_session.execute(
        text("SELECT user_id FROM student WHERE user_id = :uid"),
        {"uid": 9999}
    ).fetchone()
    assert result is None
