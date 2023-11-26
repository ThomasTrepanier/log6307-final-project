from requests import Session

class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
        """
        No code here means requests will always preserve the Authorization
        header when redirected.
        Be careful not to leak your credentials to untrusted hosts!
        """

session = NoRebuildAuthSession()
response = session.post('https://myserver.com/endpoint', headers=headers, data=data)
