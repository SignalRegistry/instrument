import sys  # arguments
import argparse
import textwrap
import time

import pyvisa_py
import pyvisa as visa
import win32com.client

rm = visa.ResourceManager('@py')

match sys.argv[1:]:
    case ["list", *args]:
        parser = argparse.ArgumentParser(prog="list", description="list of connected VISA supported instruments", 
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         epilog=textwrap.dedent('''
                                         '''))
        args = parser.parse_args(sys.argv[2:])
        print(rm.list_resources())
    case ["ping", *args]:
        parser = argparse.ArgumentParser(prog="ping", description="test connection to an instrument with '*IDN?' query", 
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         epilog=textwrap.dedent('''
                                         '''))
        parser.add_argument("address", help="VISA or COM address of an instrument", type=str, nargs=1)
        args = parser.parse_args(sys.argv[2:])
        if('::' in args.address[0]):
            print("VISA instrument")
        else:
            try:
              app = win32com.client.Dispatch(args.address[0] + ".application")
            except:
              print("ping: error: failed establishing COM server connection to " + args.address[0] + ".", file=sys.stderr)
              exit(1)

            #Wait up to 20 seconds for instrument to be ready
            if app.Ready == 0:
                print("ping: info: waiting...")
                for k in range (1, 21):
                    time.sleep(1)
                    if app.Ready != 0:
                        break

            # If the software is still not ready, cancel the program
            if app.Ready == 0:
              print("ping: error: timeout waiting for instrument to be ready.", file=sys.stderr)
              print("ping: error: instrument is powered on and connected to PC.", file=sys.stderr)
              exit(1)
            else:
                print(app.scpi.IEEE4882.IDN)
                # print(app.name)
           

    case _:
        parser = argparse.ArgumentParser(prog="antenna", description="Instrument Toolkit",
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         epilog=textwrap.dedent('''
                                         Supported Instruments:
                                         - Copper Mountain: RVNA, TRVNA, S2VNA, S4VNA
                                         '''))
        parser.add_argument("list", help="[f] list of connected VISA supported instruments", type=str, nargs='?')
        parser.add_argument("ping", help="[f] test connection to an instrument iwth '*IDN?' query", type=str, nargs='?')
        print(parser.format_help().replace("positional arguments","module/function")
              .replace("[list] ","")
              .replace("[ping]","[module/function]")
              )