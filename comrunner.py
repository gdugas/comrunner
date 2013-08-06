
class Argument(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class CommandRunner(object):
    
    description = ""
    args = []
    
    def __init__(self):
        self.subcommands = {}
    
    def add_subcommand(self, name, cls):
        if not issubclass(cls, CommandRunner):
            m = "not a CommandRunner subclass"
            raise Exception(m)
        self.subcommands[name] = cls
    
    def create_parser(self):
        import argparse
        return argparse.ArgumentParser(description = self.description)
    
    def init_parser(self, parser=None):
        if not parser:
            parser = self.create_parser()
        
        for arg in self.args:
            if not isinstance(arg, Argument):
                raise Exception("Not an Argument instance")
            parser.add_argument(*arg.args, **arg.kwargs)
        
        
        if len(self.subcommands) == 0:
            parser.set_defaults(func=self.execute)
            return parser
        
        subparsers = parser.add_subparsers()
        for k in self.subcommands:
            if not issubclass(self.subcommands[k], CommandRunner):
                raise Exception("Not a CommandRunner subclass")
            cmd = self.subcommands[k]()
            
            subparser = subparsers.add_parser(k, help=cmd.description)
            cmd.init_parser(subparser)
        
        return parser
    
    
    def parse_args(self, args=None):
        parser = self.init_parser()
        if args == None:
            return parser.parse_args()
        else:
            return parser.parse_args(args)
    
    
    def run(self, args=None):
        args = self.parse_args(args)
        args.func(args)
    
    
    def execute(self, args):
        m = "Undefined abstract method 'handle()'"
        raise NotImplementedError(m)
