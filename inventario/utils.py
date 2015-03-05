def string_to_positive_int_or_default(input, default):
    try:
        output = int(input)
        if output <= 0:
            return default
        return output
    except:
        return default
