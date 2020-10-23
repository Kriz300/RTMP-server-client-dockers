def cap_05(packet):

    try:
        if packet["RTMPT"]["scm.was"] == 5000000:
            packet["RTMPT"]["scm.was"] = 0
            print("cambiado")
        return packet
        
    except:
        print("No se pudo modificar")
        return None