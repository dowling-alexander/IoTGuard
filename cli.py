# Command line interface for IoTGuard

import argparse
import os
import sys
from vigilance import start_sniffing
from kataskopos import get_active_interfaces

# need to support three modes. in the meantime when a mode is requested print I'm in development

def main():
    # parser object

    parser = argparse.ArgumentParser(description="Welcome to IoT Guard, an IDS/IPS tool designed for IoT devices")

    parser.add_argument("-w", "--watch", type=str, nargs="?",
                        metavar="watch_traffic", default=None,
                        help="Displays Current Traffic")

    parser.add_argument("-l", "--log", type=str, nargs="?",
                        metavar="log_traffic", default=None,
                        help="Logs Current Traffic")

    parser.add_argument("-d", "--dome", type=str, nargs="?",
                        metavar="enables_rules", default=None,
                        help="Enables the actual IDS/IPS rules")

    parser.add_argument("-I","--interface",type=str, nargs="?",
                        metavar="searches_for_interfaces", default=None,
                        help="Will list the available interfaces")


    args = parser.parse_args()

    print(f"Args received: {vars(args)}")
    # Check if any arguments were provided
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(0)

    if args.watch:
        print("Traffic Incoming")
        try:
            while True:
                start_sniffing(args.watch)
        except KeyboardInterrupt:
            print("Exited gracefully")
            sys.exit(0)

    elif args.log:
        print("Logging Traffic")
        print("I'm in development")
        try:
            while True:
                start_logging(args.log)
        except KeyboardInterrupt:
            print("Exited gracefully")
            sys.exit(0)

    elif args.dome:
        print("Enabling IDS/IPS Rules")
        print("I'm in development")
        sys.exit(0)
    
    elif args.interface:
        print("Please See Active Interfaces")
        get_active_interfaces()
        print("Im In Development")
        sys.exit(0)

if __name__ == "__main__":
    # calling the main function
    main()
