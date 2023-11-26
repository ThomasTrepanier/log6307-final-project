class ResolveThread(threading.Thread):
            def __init__(self,result1,fun,url):
                self.result1= result1
                self.fun = fun
                self.url = url
                threading.Thread.__init__(self)
            def run(self):
                result1[0] = asyncio.run(self.fun(self.url))


result1 = [None]
sp = ResolveThread(result1)
sp.start()
sp.join() # connect main thread
result = result1[0]
