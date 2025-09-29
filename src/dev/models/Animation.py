import string
import time

class Animation:

    @staticmethod
    def string_animation(text):
        temp = ""
        for char in text:
            for p in string.printable:
                if char == p:
                    time.sleep(0.05)
                    print("\r" + temp + p, end="")
                    temp += p
                    break

    @staticmethod
    def glitchy_string(text):
        temp = ""
        for char in text:
            for p in string.printable:
                if char == p:
                    time.sleep(0.05)
                    print("\r" + temp + p, end="")
                    temp += p

                    break
                else:
                    time.sleep(0.001)
                    print("\r" + temp + p, end="")


