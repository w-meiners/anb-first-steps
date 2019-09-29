def ermittle_normdurchmesser(d):
    """ Ermittle zum gegebenen Durchmesser d in mm
        den zugehörigen Normdurchmesser in mm.
        
        Der Normdurchmesser wird als der nächstgrößere
        Durchmesser aus der Reihe der Normdurchmesser
        ausgelesen.
        
        Sind z.B. die Normdurchmesser
        [65, 80, 90, 100]
        gegeben, so liefert
        >>> $:ermittle_normdurchmesser(87)
        den Wert
        90
    """
    
    # Liste der Normdurchmesser
    norm_durchmesser = [80,90,100,112,125,140,
                        150,160,180,200,224,250,
                        280,300,315,355,400,450,
                        500,560,600,630,710,800,
                        900,1000,1120,1250,1400,
                        1600,1800,2000]
    
    for d_n in norm_durchmesser:
        if d_n >= d:
            return d_n
        
    raise Exception(f'Der Durchmesser {d} ist zu groß. Wählen Sie einen kleineren!')
