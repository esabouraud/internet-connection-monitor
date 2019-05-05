"""Monitor configuration management"""

import os
import configparser
from collections import namedtuple

VERSION = "0.0.1"

CONF_ENV = "NETUPMON_CONF"
MAIN_SECTION = "main"
DEFAULT_HOST_PARAMETERS = {
    "protocol": "icmp",
    "port": "0",
    "timeout": "4"
}
MainConf = namedtuple("MainConf", ["hosts", "period"])
HostConf = namedtuple("HostConf", ["protocol", "address", "port", "timeout"])
FullConf = namedtuple("FullConf", ["main", "hostsconf"])

def load_configuration(path, environment):
    "Load configuration from INI file or environment variable"

    if environment:
        configstr = os.environ[CONF_ENV]
    else:
        configstr = open(path).read()
    config = configparser.SafeConfigParser(DEFAULT_HOST_PARAMETERS)
    config.read_string(configstr)
    for mandatory_section in [MAIN_SECTION]:
        if not config.has_section(mandatory_section):
            raise ValueError(
                "Configuration file '%s' has no section '%s'" % (path, mandatory_section))
    main_config = MainConf._make(
        [config[MAIN_SECTION][field] for field in MainConf._fields])
    hosts_config = {
        host: HostConf._make([config[host][field] for field in HostConf._fields])
        for host in main_config.hosts.split(",")
    }
    return FullConf._make([main_config, hosts_config])
