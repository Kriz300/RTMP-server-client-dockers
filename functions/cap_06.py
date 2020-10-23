def cap_06(packet):

    try:
        if packet["RTMPT"]["scm.chunksize"] == 5000000:
            packet["RTMPT"]["scm.chunksize"] = 0
            print("cambiado")
        return packet
        
    except:
        print("no se pudo cambiar")
        return None