import sys  # arguments
import argparse

match sys.argv[1:]:
    case ["ffdist", *args]:
        parser = argparse.ArgumentParser(prog="ffdist", description="Far-Field Distance of an Antenna")
        parser.add_argument("D", help="antenna maximum cross-section size", type=float, nargs=1)
        parser.add_argument("freq", help="frequency of interest in Hz", type=float, nargs=1)
        parser.add_argument("--human", help="human readable output like cm, mm, km", action='store_true')
        args = parser.parse_args(sys.argv[2:])
        print(args)
        # parser.print_help()
    case _:
        parser = argparse.ArgumentParser(prog="antenna", description="Antenna Toolkit")
        parser.add_argument("[func] ffdist", help="Far-Field Distance of an Antenna", type=str, nargs='?')
        print(parser.format_help().replace("positional arguments","module/function").replace("[ffdist]","[module/function]"))
        # parser.print_help()

