sniff(iface='wlp59s0', prn=lambda p: p.summary(), store=0)

#Explanation
#
#Sniff functions has a couple of arguments. You can check their meaning in scapy sources. Argument "store=0" means that packets storing will be disabled, so there will be no result.
#
#You also need to stop sniffing after some time. You can use one of the following options:
#
#    stop_filter: Python function applied to each packet to determine if we have to stop the capture after this packet.
#    count: number of packets to capture. 0 means infinity.
#    timeout: stop sniffing after a given time (default: None).
#
#As an alternative to such solution you can just use:
#
#    prn: function to apply to each packet.
