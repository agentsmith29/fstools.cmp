from inspect import Signature, Parameter

from cmp import CProcessControl as CProcessControl


class CResultRecord:

    def __init__(self, signal_name: str, result):
        self.signal_name: str = signal_name
        self.result = result

    def emit_signal(self, class_object: CProcessControl):
        if hasattr(class_object, '_internal_logger'):
            class_object._internal_logger.info(f"Emitting {self} in {class_object.__class__.__name__}.")
        emitter = getattr(class_object, self.signal_name).emit
        if isinstance(self.result, tuple):
            emitter(*self.result)
        elif self.result is None:
            emitter()
        else:
            emitter(self.result)


    def __repr__(self):
        if isinstance(self.result, tuple):
            args_str = ', '.join(map(repr, self.result))
        else:
            args_str = repr(self.result)
        # shorten arg_str if too long
        if len(args_str) > 100:
            args_str = args_str[0:10] + '...' + args_str[-10:]
        return f"Signal {self.signal_name}({args_str})"