#Command line interface for IoTGuard

import argparser
import os
#need to support three modes. in the meantime when a mode is requested print I'm development

def main():
    #parser object
    parser = argparse.ArgumentParser(description="Welcome to IoT Guard, an IDS/IPS tool designed for IoT devices")

    
    parser.add_argument("-w", "--watch", type = str, nargs = 1,
                        metavar = "watch_traffic", default = None,
                        help = "Displays Current Traffic")

    parser.add_argument("-l", "--log", type = str, nargs = 1,
                        metavar = "log_traffic", default = None,
                        help = "Logs Current Traffic")

    parser.add_argument("-d", "--dome", type = str, nargs = 1,
                        metavar = "enables_rules", default = None,
                        help = "Enables the actual IDS/IPS rules")
    
    args = parser.parse_args()


if __name__ == "__main__":
    # calling the main function
    main()
