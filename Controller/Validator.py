import re
import json

with open("Model/CountryCodes.json", "r") as read_file:
    codes = json.load(read_file)

def replace_chars(number):
    replacingChars = '.!#$^&*'
    for char in replacingChars:
        number = number.replace(char, '')
    return number

def replace_cc(cc):
    cc = cc
    for code in codes:
        if code['dial_code'] == cc:
            cc = code['code']
            break
        else:
            cc = cc
    return cc


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
    try:
        result = regex.findall(number)[0]
        optimized_number.append(result[1])
        optimized_number.append(result[7])
        optimized_number.append(result[11] + result[14])
        optimized_number.append(result[13] + result[16])
        optimized_number.append(True)
        print(optimized_number)
    except:
        optimized_number.append("")
        optimized_number.append("")
        optimized_number.append("")
        optimized_number.append("")
        optimized_number.append(False)
    return optimized_number
