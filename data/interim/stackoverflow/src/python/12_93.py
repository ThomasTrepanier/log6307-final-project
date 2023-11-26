def int2bin( num ) :
    result = []
    while num :
        result.append( str(num & 1) )
        num >>= 1
    return ''.join( result[::-1] )
