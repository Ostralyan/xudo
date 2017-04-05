
"""The base command."""


class Base(object):
    """A base command."""

    def __init__(self, path, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.path = path;
        
    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
        