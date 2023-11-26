def test_foo_form(user_client):
    url = reverse('foo')
    response = user_client.get(url)
    assert response.status_code == 200
    data = parse_form(response.content)
    response = user_client.post(url, data)
    assert response.status_code == 302
