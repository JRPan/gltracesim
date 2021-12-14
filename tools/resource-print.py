#!/usr/bin/env python

import sys, io
sys.path.append("../gltracesim/proto")
sys.path.append("../gltracesim/proto/gem5")
import packet_pb2 as packet
import resource_pb2 as resource
import stream

# Example from https://developers.google.com/protocol-buffers/docs/pythontutorial
if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "resources.pb.gz"
    sys.exit(-1)

# Open the file and discard the header
istream = stream.open(sys.argv[1], "rb")

for msg in istream:
    hdr = packet.PacketHeader()
    hdr.ParseFromString(msg)
    print hdr
    break

for msg in istream:
    ResourceInfo = resource.ResourceInfo()
    ResourceInfo.ParseFromString(msg)
    print ResourceInfo

# Close the file
istream.close()

