def cap_01V6(packet):

    # your code here
    try:
        if packet["RTMPT"]["header.csid"] == 3:
             return packet
    except:
        return None
