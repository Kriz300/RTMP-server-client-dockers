def cap_08(packet):

    # your code here
    try:
        if packet["RTMPT"]["string7"] == 'Start live':
            packet["RTMPT"]["string5"] = 'NetStream.Play.StreamNotFound'
            print("cambiado")
        return packet
    except:
        return None
