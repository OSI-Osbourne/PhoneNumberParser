import re

def validate(number):
    number = ''.join(char for char in number if char.isalnum())
    optimized_number = []
    pattern = '^(\[?\+[1-9]{1,2}\]?|\(?0{1,2}[1-9]{0,2}\)?){1}(\(?\d{3,4}\)?){1}(\-?\/?\(?\[?\d{3,}\)?\]?){1}'
    result = re.search(pattern, number)
    if result:
        optimized_number.append(result.group(1))
        optimized_number.append(result.group(2))
        optimized_number.append(result.group(3))
    else:
        optimized_number.append("+49")
    return optimized_number
#    split_pattern = re.split(pattern, number)
#    split_pattern = list(filter(None, split_pattern))
#    for match in split_pattern:
#        match = match.strip()
#        split_number.append(match)
#    print(split_number)
#    return split_number





