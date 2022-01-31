class multi:

    """

    Attributes
    ----------
    inner : inner
    innerinner : inner, inner
    """
    def __init__(self):
        """
        Sets up inner and inner inner
        """
        self.inner = self.Inner()
        self.innerinner = self.inner.InnerInner()

    def show(self):
        """
        Shows the outer class
        """
        def statement(x: str):
            """
            Prints a string

            Parameters
            ----------
            x : str

            """
            print(x)
        statement("This is Outer class")

    ## inner class
    class Inner:

        """

        Attributes
        ----------
        innerinner :  the inner
        """
        def __init__(self):
            """
            sets the stuff up
            """
            self.innerinner = self.InnerInner()

        def show_classes(self):
            """
            Shows the inner class
            """
            print("This is Inner class")
            print(self.innerinner)

        class InnerInner:

            """
            Innermost class
            """
            def inner_display(self, msg):
                """
                displays innermost class

                Parameters
                ----------
                msg : msg to print

                """
                print("InnerInner class")
                print(msg)

        def inner_display(self, msg):
            """

            dipslays inner class

            Parameters
            ----------
            msg : message to print

            """
            print("This is Inner class")
            print(msg)


class multiv2:

    """

    Attributes
    ----------
    inner : inner
    innerinner : inner, inner
    """
    def __init__(self):
        """
        Sets up inner and inner inner
        """
        self.inner = self.Inner()
        self.innerinner = self.inner.InnerInner()

    def show(self):
        """
        Shows the outer class
        """
        def statement(x: str):
            """
            Prints a string

            Parameters
            ----------
            x : str

            """
            print(x)
        statement("This is Outer class")

    ## inner class
    class Inner:

        """

        Attributes
        ----------
        innerinner :  the inner
        """
        def __init__(self):
            """
            sets the stuff up
            """
            self.innerinner = self.InnerInner()

        def show_classes(self):
            """
            Shows the inner class
            """
            print("This is Inner class")
            print(self.innerinner)

        class InnerInner:

            """
            Innermost class
            """
            def inner_display(self, msg):
                """
                displays innermost class

                Parameters
                ----------
                msg : msg to print

                """
                print("InnerInner class")
                print(msg)

        def inner_display(self, msg):
            """

            dipslays inner class

            Parameters
            ----------
            msg : message to print

            """
            print("This is Inner class")
            print(msg)