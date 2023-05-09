from services.article import ArticleService
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas import ArticleDisplay, ArticleBase
from services.exceptions.exceptions import NotFoundException

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return ArticleService.create_article(db, request)


@router.get('/{article_id}', response_model=ArticleDisplay)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    try:
        return ArticleService.get_article_by_id(db, article_id)
    except NotFoundException:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Article not found.')
