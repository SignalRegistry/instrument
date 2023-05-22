import sys  # arguments
import argparse

match ("" if not len(sys.argv)>1 else  sys.argv[1]):
    case "ceyear":
        match ("" if not len(sys.argv)>2 else  sys.argv[2]):
            case "connect":
                # Requirements: 
                # - Pyvisa-Py: A pure python PyVISA backend https://pyvisa-py.readthedocs.io/, pip install pyvisa-py
                # - psutil: pip install psutil
                # - zeroconf: pip install zeroconf
                print("Connecting...")
            case _:
                print("Exiting")
    case "list":
        # Requirements: 
        # - Pyvisa-Py: A pure python PyVISA backend https://pyvisa-py.readthedocs.io/, pip install pyvisa-py
        # - psutil: conda install psutil
        # - zeroconf: pip install zeroconf
        import pyvisa
        rm = pyvisa.ResourceManager('@py')
        print(rm.list_resources())
    case _:
        parser = argparse.ArgumentParser(prog="instrument", description="Toolkit for Signal Instruments")
        parser.add_argument("list", help="[f] list VISA supported instruments", type=str, nargs='?')
        parser.add_argument("ceyear", help="[m] Ceyear Signal Instruments", type=str, nargs='?')
        print(parser.format_help().replace("positional arguments","module/function").replace("[list] [ceyear]","[module/function]"))
        # print(parser.format_help().replace("positional arguments","module/function").replace("[ceyear]",""))
        # parser.print_help()

