def cap_03(packet):

    try:
        if packet["RTMPT"]["scm.limittype"] == 2:
            packet["RTMPT"]["scm.limittype"] = 10
            print("cambiado")
        return packet
        
    except:
        print("No se pudo modificar")
        return None