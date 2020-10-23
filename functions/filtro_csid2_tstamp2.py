def cap_01(packet):

    # your code here
    try:    
        if packet["RTMPT"]["header.csid"] == 2 and packet["RTMPT"]["header.timestamp"] == 0:
            return packet
    except:
        return None
