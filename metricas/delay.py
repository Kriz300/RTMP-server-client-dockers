def delay(packet):

    import time
    if packet['RTMPT']['header.csid'] == 7:
        try:
            delay = time.time() - packet.time
            packet.global_var('time',time.time())
            print("el delay es: ",round(delay,4))
            return packet
        except:
            print("paso")
            packet.global_var('time', time.time())
            return packet