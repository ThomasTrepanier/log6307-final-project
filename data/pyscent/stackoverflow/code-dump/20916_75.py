import io

class EncodeIO(io.BufferedIOBase):
  def __init__(self,s,e='utf-8'):
    self.stream=s               # not raw, since it isn't
    self.encoding=e
    self.buf=b""                # encoded but not yet returned
  def _read(self,s): return self.stream.read(s).encode(self.encoding)
  def read(self,size=-1):
    b=self.buf
    self.buf=b""
    if size is None or size<0: return b+self._read(None)
    ret=[]
    while True:
      n=len(b)
      if size<n:
        b,self.buf=b[:size],b[size:]
        n=size
      ret.append(b)
      size-=n
      if not size: break
      b=self._read(min((size+1024)//2,size))
      if not b: break
    return b"".join(ret)
  read1=read
