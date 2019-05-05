import argparse
# daemon

from netupmon import conf
from netupmon import monitor


def main():
    parser = argparse.ArgumentParser(
        prog="netupmon", description="Run internet connection monitor")
    parser.add_argument(
        "-f", "--file", dest="conf_file", default=None, help="Configuration file path")
    parser.add_argument(
        "-e", "--environment", dest="environment", action="store_true", default=False,
        help="Load configuration from NETUPMON_CONF environment variable")
    parser.add_argument(
        "-d", "--daemon", dest="daemon", action="store_true", default=False,
        help="Run as daemon")
    options = parser.parse_args()

    config = conf.load_configuration(options.conf_file, options.environment)

    if options.daemon:
        #with daemon.DaemonContext():
        #    monitor.run(config)
        pass
    else:
        monitor.run(config)

if __name__ == "__main__":
    main()
