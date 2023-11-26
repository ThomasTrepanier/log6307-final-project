class test:
    def foo(self, pic_path, enc_path, key_path):
        return pic_path, enc_path, key_path


if __name__ == "__main__":
    s = test()
    pic_path = "pic.png"
    key_path = "keys.txt"
    enc_path = "asd.sc"
    s.foo(pic_path,enc_path, key_path)
    print("done")
