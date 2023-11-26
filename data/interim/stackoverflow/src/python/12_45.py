@router.get('/user/me')
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # get the current user from auth token

    # define credential exception
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # decode token and extract username and expires data
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        expires = payload.get("exp")
    except JWTError:
        raise credentials_exception

    # validate username
    if username is None:
        raise credentials_exception
    token_data = TokenData(username=username, expires=expires)
    user = Users.search(where('name') == token_data.username)
    if user is None:
        raise credentials_exception

    # check token expiration
    if expires is None:
        raise credentials_exception
    if datetime.utcnow() > token_data.expires:
        raise credentials_exception
    return user
