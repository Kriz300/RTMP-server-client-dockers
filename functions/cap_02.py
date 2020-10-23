def cap_02(packet):

    try:
        packet["RTMPT"]["header.timestamp"] = 10
        print("paquete modificado")
        return packet
        
    except:
        print("packete no tiene timestamp")
        return None