#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    switch_num = 0
    switch_intf = {}

    def build( self ):
        # Read star.in
        # Load configuration of Hosts, Switches, and Links
        # You can write other functions as you need.
        with open("star.in") as fin:
            next(fin)
            for line in fin:
                temp = line.split(",")
                left = temp[0]
                right = temp[1].strip()
                if (left[0] == "h"):
                    self.addHost(left)
                else:
                    self.addSwitch(left)
                if (right[0] == "h"):
                    self.addHost(right)
                else:
                    self.addSwitch(right)

                self.addLink(left, right)
        fin.close()
        # Add hosts
        # > self.addHost('h%d' % [HOST NUMBER])

        # Add switches
        # > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
        # > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)

        # Add links
        # > self.addLink([HOST1], [HOST2])
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )