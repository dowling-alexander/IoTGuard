# Command line interface for IoTGuard

import argparse
import os
import sys
from vigilance import start_sniffing

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

    args = parser.parse_args()

    # Check if any arguments were provided
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(0)

    if args.watch is not None:
        print("Traffic Incoming")
        start_sniffing()


if __name__ == "__main__":
    # calling the main function
    main()
