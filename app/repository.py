from sqlalchemy.orm import Session
from . import entities

def get_all_words(db_session: Session):

    return db_session.query(entities.Word).all()

def get_word_by_id(db_session: Session, id: int):

    return db_session.query(entities.Word).filter(entities.Word.id == id).first()

def get_word_by_name(db_session: Session, name: str):

    return db_session.query(entities.Word).filter(entities.Word.name == name).first()

def add_word(db_session: Session, word_name: str, word_definition: str):

    entity = entities.Word(name = word_name, definition = word_definition)
    
    db_session.add(entity)
    
    db_session.commit()
    
    db_session.refresh(entity)
    
    return entity

def update_word(db_session: Session, name: str, new_definition: str):
    
    word = db_session.query(entities.Word).filter(entities.Word.name == name).first()
    
    word.definition = new_definition
    
    db_session.commit()
    
    db_session.refresh(word)
    
    return word

def delete_word(db_session: Session, id: str):

    word = db_session.query(entities.Word).filter(entities.Word.id == id).first()
    
    if word:
    
        db_session.delete(word)
    
        db_session.commit()
    
    return True