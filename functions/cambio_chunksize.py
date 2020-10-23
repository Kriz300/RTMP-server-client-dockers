def cap_06(packet):

    # your code here
    try:
        if packet["RTMPT"]["scm.chunksize"] == 5000000:
            packet["RTMPT"]["scm.chunksize"] = 10
            print("cambiado")
        return packet
    except:
        print("no se pudo cambiar")
        return None
