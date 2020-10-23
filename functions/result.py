def cap_11(packet):

    # your code here
    try:
        if packet["RTMPT"]["string"] == '_result':
            packet["RTMPT"]["string"] = '_123456'
            print("cambiado")
            return packet
    except:
        print("fallo")
        return None
