def cap_07(packet):
    try:
        if packet["RTMPT"]["ucm.eventtype"] == 0:
            packet["RTMPT"]["ucm.eventtype"] = 1
            print("cambiado")
            return packet
    except:
        print("no se pudo cambiar")
        return None
