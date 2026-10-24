import pyxel
import math

try:
    from js import window
    from pyodide.ffi import JsNull
except Exception:
    window = None

#==========
# StorageManagerクラス
class StorageManager:

    @staticmethod
    def set_item(key:str, value:str):
        if window is None:
            return
        print(f"set_str() key:{key}, value:{value}")
        window.localStorage.setItem(key, value)

    @staticmethod
    def get_item(key:str, default=None)->str|None:
        if window is None:
            return None
        print(f"get_str() key:{key}")
        value = window.localStorage.getItem(key)
        if isinstance(value, JsNull):
            return default
        return str(value)