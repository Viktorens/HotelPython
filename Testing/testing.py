def gast_name(name):
    # x = Special Characters
    special = '!' or '#' or '$' or '%' or '&' or "'" or '(' or ')' or '*' or '+' or ',' or '-' or '.' or '/' or ':' or ';' or '<' or '=' or '>' or '?' or '@' or '[' or '\\' or ']' or '^' or '_' or '`' or '{' or '|' or '}' or '~' or ' '
    # Test
    if name.isalpha() and name[0].isupper() and name[1:].islower() and special not in name:
        return True
    else:
        return False


def zimmer_farbe(farbe):
    # x = Special Characters
    special = '!' or '#' or '$' or '%' or '&' or "'" or '(' or ')' or '*' or '+' or ',' or '-' or '.' or '/' or ':' or ';' or '<' or '=' or '>' or '?' or '@' or '[' or '\\' or ']' or '^' or '_' or '`' or '{' or '|' or '}' or '~'
    # Test
    if farbe.isalpha() and farbe[0].isupper() and farbe[1:].islower() and special not in farbe:
        return True
    else:
        return False


def zimmer_mehrblick(mehrblick):
    x = ['Nein', 'Ja']
    if mehrblick in x:
        return True
    else:
        return False
