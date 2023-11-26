def updateblog (id:int, title:Optional[str]=None, body:Optional[str]=None, db:Session = Depends(get_db)):

    if title!=None:
            db.query(models.Blog).filter(models.Blog.id==id).update({'title':title})
    
    if body!=None:
            db.query(models.Blog).filter(models.Blog.id==id).update({'body':body})

    db.commit()
    
    return f'Blog #{id} has been updated.'
