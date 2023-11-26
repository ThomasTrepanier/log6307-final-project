def my_gen():
  ...

m1 = Muxer(my_gen)
m2 = Muxer(my_gen)

consumer1(m1).start()
consumer2(m2).start()
