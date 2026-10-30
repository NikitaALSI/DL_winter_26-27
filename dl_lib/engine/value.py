class Value:

    @property
    def ops_dict(self): 
        return {'__add__': '+', '__mul__': '*', '__radd__': '+', '__rmul__': '*'}

    @staticmethod
    def track_prev_op(func):
        def wrapper(self, *args, **kwargs):
            new = func(self, *args, **kwargs)
            new._prev.update([self, args[0]])
            new._op = self.ops_dict[func.__name__]
            return new
        return wrapper

    def __init__(self, data: float, label: str =""):
        self.data = data
        self.label = label
        self.grad = 0
        self._prev = set()
        self._op = ""

    def __repr__(self) -> str:
        return f"Value(data={self.data})"

    @track_prev_op
    def __add__(self, other):
        if other.__class__ != self.__class__:
            other = self.__class__(other)
        return self.__class__(self.data + other.data)
    
    @track_prev_op
    def __mul__(self, other):
        if other.__class__ != self.__class__:
            other = self.__class__(other)
        return self.__class__(self.data * other.data)
    
    @track_prev_op
    def __radd__(self, other):
        if other.__class__ != self.__class__:
            other = self.__class__(other)
        return self.__class__(self.data + other.data)
    
    @track_prev_op
    def __rmul__(self, other):
        if other.__class__ != self.__class__:
            other = self.__class__(other)
        return self.__class__(self.data * other.data)

    