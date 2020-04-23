def spn_func(toponym):
    d1 = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    d2 = toponym['boundedBy']['Envelope']['upperCorner'].split()
    deltax, deltay = str(float(d2[0]) - float(d1[0])), str(float(d2[1]) - float(d1[1]))
    return[deltax, deltay]