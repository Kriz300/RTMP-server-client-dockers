def cap_04(packet):

    try:
        if packet["RTMPT"]["header.streamid"] == 0:
            packet["RTMPT"]["header.streamid"] = 1
            print("cambiado")
        return packet
        
    except:
        print("no se pudo cambiar")
        return None