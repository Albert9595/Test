# Conversion 10 yo 16
def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):        
        dec_to_base.table = '0123456789ABCDEF'       
    x, y = divmod(N, base)        
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]


# Conversion 16 yo 10
def convert_base(num, from_base=16, to_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


