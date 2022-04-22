import re


def replace_chars(number):
    replacingChars = '.!#$^&*'
    for char in replacingChars:
        number = number.replace(char, '')
    return number


def validate(number):
    number = replace_chars(number)
    optimized_number = []
    regex = re.compile(r'''(
		(                    # Ländercode
			(
				\[           # mit Klammern
				(\+|[0]{2})  # + oder 00
				[1-9]{1,3}   # Ländercode
				\]
			|
				(\+|[0]{2})  # + oder 00
				[1-9]{1,2}   # Ländercode
			)
		|
			(0|\(0\))        # 0 mit/ohne Klammern
		)
		(\s|\/|-)?           # Trennzeichen
		(                    # Vorwahl
			\d{3,4}
		|
			\(\d{3,4}\)      # mit Klammern
		|
			\d+(-\d+)*
		)
		(\s|\/|-)?           # Trennzeichen
		(
			\[               # mit Klammern
			(\d+)            # Durchwahl
			(\s|\/|-)?       # Trennzeichen
			(\d+)?           # Endung
			\]
		|
			(\d+)            # Durchwahl
			(\s|\/|-)?       # Trennzeichen
			(\d+)?           # Endung
		)
	)''', re.VERBOSE)
    result = regex.findall(number)[0]

    if result:
        optimized_number.append(result[0])
        optimized_number.append(result[1])
        optimized_number.append(result[7])
        optimized_number.append(result[11] + result[14])
        optimized_number.append(result[13] + result[16])
    else:
        optimized_number.append(["Ungültige Nummer", "", "", "", ""])
    return optimized_number
#    split_pattern = re.split(pattern, number)
#    split_pattern = list(filter(None, split_pattern))
#    for match in split_pattern:
#        match = match.strip()
#        split_number.append(match)
#    print(split_number)
#    return split_number
