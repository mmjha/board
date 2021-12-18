from django.db import models, DEFAULT_DB_ALIAS

class QueryUtil():

    def __init__(self, db):
        if db is None:
            db = DEFAULT_DB_ALIAS 
        self._db = db

    # TODO 다른 방식 찾아보기
    def start_with_connect_by(self, id=None):
        """
            https://docs.djangoproject.com/en/4.0/topics/db/queries/
            https://roqkffhwk.tistory.com/entry/MSSQL-%EA%B3%84%EC%B8%B5%ED%98%95-%ED%8A%B8%EB%A6%AC%EA%B5%AC%EC%A1%B0-%EC%BF%BC%EB%A6%AC-%EC%9E%AC%EA%B7%80%ED%98%B8%EC%B6%9C-with-col-1-col-2-col-n-as-union
        """
        return (
            '''
            WITH comment_q AS (
                SELECT
                    id,
                    post_id, 
                    parent_comment_id,
                    content,
                    cast(id as text) sort,
                    cast(content as text) depth_fullname
                FROM comment
                WHERE parent_comment_id IS NULL AND comment.post_id= %s
                UNION ALL
                SELECT
                    B.id,
                    B.post_id,
                    B.parent_comment_id,
                    B.content,
                    cast(C.sort as text) || cast(B.id as text) AS sort,
                    cast(C.depth_fullname as text)  || cast(B.content as text) AS depth_fullname
                FROM comment B, comment_q C
                WHERE B.parent_comment_id = C.id 
                )
            SELECT id, post_id, parent_comment_id, content, depth_fullname FROM comment_q order by SORT
            ''' % id
        )

class PostQuerySet(models.QuerySet):
    pass


class CommentQuerySet(models.QuerySet):
    
    def less_comments(self, id=None):
        return self.raw(QueryUtil(self._db).start_with_connect_by(id))