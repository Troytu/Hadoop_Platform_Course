def split_show_views(line):
    line.strip()
    show_view = line.split(',')
    show = show_view[0]
    # views = show_view[1]
    views = int(show_view[1])
    return (show, views)


def split_show_channel(line):
    line = line.strip()
    show_channel = line.split(',')
    show = show_channel[0]
    channel = show_channel[1]
    return (show, channel)


def extract_channel_views(show_views_channel):
    channel_views = show_views_channel[1]
    channel = channel_views[0]
    views = channel_views[1]
    return (channel, views)


def some_function(a, b):
    some_result = a + b
    return some_result


def concat_function(a, b):
    some_result = a + ',' + b
    return some_result


def unique_values(key_value):
    key = key_value[0]
    value = key_value[1]
    value = value.strip()
    values = value.split(',')
    unique_values = []
    for val in values:
        if not val in unique_values:
            unique_values.append(val)
    return_values = []
    for val in unique_values:
        return_values.append((key, val))
    return tuple(return_values)


if __name__ == '__main__':
    print unique_values(('PostModern_Cooking', 'DEF,CNO,CNO,NOX,MAN,MAN,XYZ,BAT,CAB,DEF'))
