# hello_world.py
from boa3.builtin.compile_time import public
from boa3.builtin.interop import storage


@public     # the public decorator will make this method callable
def save_hello_world():             # an empty return type indicates that the return is None
    storage.put(b"first script", "Hello World")      # the put method will store the "Hello World" value with the "first script" key


@public     # the public decorator will make this method callable too
def get_hello_world() -> str:       # this method will return a string, so it needs to specify it
    return str(storage.get(b"first script"))              # the get method will return the value associated with "first script" key


# def test_hello_word() 