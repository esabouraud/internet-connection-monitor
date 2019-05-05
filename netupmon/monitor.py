import time
import ping3

def run(config):
    while True:
        for _host, hostconf in config.hostsconf.items():
            ping3.verbose_ping(
                hostconf.address,
                count=1,
                timeout=int(hostconf.timeout))
        time.sleep(int(config.main.period))
