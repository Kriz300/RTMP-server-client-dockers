def cap_01V2(packet):

    try:    
        if packet["RTMPT"]["header.csid"] == 2 and packet["RTMPT"]["header.timestamp"] == 0:
            return packet
            
    except:
        return None