# Update Blog
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request_body: UpdateBlog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        content={'success': False, 'message': f"Blog with id {id} don't exists"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    
    # exclude_none=True will only update the field which you want to update
    # If you don't want to update "body" then only pass the "title" and "body" field will stay as it is
    db.query(models.Blog).filter(models.Blog.id == id).update(request_body.dict(exclude_none=True))
    db.commit()

    content={'success': True, 'message': f"Blog with id {id} Updated"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
