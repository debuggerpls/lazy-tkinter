import tkinter as tk

import yaml


class Window(yaml.YAMLObject):
    yaml_tag = '!Tk'

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def convert(self) -> tk.Tk:
        w = tk.Tk()
        if self.__getattribute__("title"):
            w.title = self.__getattribute__("title")
        return w


class Label(yaml.YAMLObject):
    yaml_tag = '!Label'

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def convert(self) -> tk.Label:
        l = tk.Label()
        return l


if __name__ == "__main__":
    window = yaml.full_load("""
!Tk
title: hello

label_b: !Label
  text: world

label_a: !Label
  text: hello
    """)

    arts = vars(window).keys()

    assert isinstance(window, Window)

    window.convert().mainloop()

    # print(yaml.dump(window))

    # window = tk.Tk(baseName="Hello")

    # window.mainloop()

    # window = tk.Tk()

    # greeting = tk.Label(text="Hello, Tkinter", background="#34A2fe", foreground="white")
    # greeting.pack()

# entry = tk.Entry()
# entry.pack()

#    text = tk.Text()
#    text.pack()

# window.mainloop()
