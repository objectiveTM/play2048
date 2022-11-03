class Custom:
    """
    # Custom
    Customize the color in the returned image

    ## description
    - When the number that comes out is n, the background color of n can be received as the _n parameter.
        - If you want to change the font color of n, you can use font_n.
    - If there is no match, the background color is determined by the color of the none parameter.
    - The default background color is received as the bg parameter.
    - The font color is received as the font parameter.
    - When there is nothing, the color is received as the _0 parameter.
    
    ## Example
    ```py
    play2048.Custom(none = "#ffffff", bg = "#BBADA0", font = "#ffffff",  _0 = "#CCC0B3", _2 = "#202020", _4 = "#523523", _8 = "#ff00ff")
    ```
    """
    def __init__(self, none:str, font:str, bg:str, **kw):
        self.none = none
        self.bg = bg
        self.font = font
        for name in kw:
            self.__setattr__(name, kw[name])