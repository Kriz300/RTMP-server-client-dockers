def cap_01V3(packet):

    # your code here
    try:
        if packet["RTMPT"]["header.csid"] == 5 and packet["RTMPT"]["header.timestamp"] == 0:
            return packet
    except:    
        return None
