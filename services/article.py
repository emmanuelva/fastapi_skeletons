from sqlalchemy.orm import Session

from db.models import DbArticle
from api.schemas import ArticleBase


class ArticleService:
    @classmethod
    def create_article(cls, db: Session, request_body: ArticleBase):
        new_article = DbArticle(
            title=request_body.title,
            content=request_body.content,
            published=request_body.published,
            user_id=request_body.creator_id,
        )
        db.add(new_article)
        db.commit()
        db.refresh(new_article)
        return new_article

    @classmethod
    def get_article_by_id(cls, db: Session, article_id: int):
        article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
        return article
