def Rank(char):
    # if(char is 'e' or char is '5'):
    #   return 0
    # if(char is 't'):
    #   return 1
    # if(char is 'i' or char is '9'):
    #   return 2
    # if(
    #   return 5
    # if(char is 'u'):
    #   return 6
    # if(char is 'm'):
    #   return 7
    # if(char is 'g' or char is '7'):
    #   return 8
    # if(char is 'y'):
    #   return 9
    # if(char is 'v'):
    #   return 10
    # if(char is 'k'):
    #   return 11
    # if(char is 'q'):
    #   return 12
    # if(char is 'z'):
    #   return 13
    # if(char is ','):
    #   return 14
    # if(char is ';'):
    #   return 15
    # if(char is ':'):
    #   return 16
    # if(char is '.'):
    #   return 17
    # if(char is '!'):
    #   return 18
    # if(char is '(' or char is ')'):
    #   return 19
    # if(char is '?'):
    #   return 20
    # if(char is '*'):
    #   return 21
    # if(char is '\"'):
    #   return 22
    # if(char is '\''):
    #   return 23
    # if(char is '-'):
    #   return 24
    # if(char is ' '):
    #   return 25
    # if(char is '~'):
    #   return 26
    # if(char is '#'):
    #   return 27
    # if(char is ''):
    #   return 28
    # if(char is ''):
    #   return 29
    # if(char is ''):
    #   return 30
    # if(char is ''):
    #   return 31Try now
    # if(char is ''):
    #   return 32
    # if(char is ''):
    #   return 33
    # if(char is ''):
    #   return 34
    # if(char is ''):
    #   return 35
    # if(char is 'x'):
    #   return 36
    # if(char is 'j' or char is '0'):
    #   return 37
    # if(char is 'b' or char is '2'):
    #   return 38
    # if(char is 'p'):
    #   return 39
    # if(char is 'f' or char is '6'):
    #   return 40
    # if(char is 'w'):
    #   return 41
    # if(char is 'c' or char is '3'):
    #   return 42
    # if(char is 'l'):
    #   return 43
    # if(char is 'h' or char is '8'):
    #   return 44
    # if(char is 's'):
    #   return 45
    # if(char is 'o'):
    #   return 46
    # if(char is 'a' or char is '1'):
    #   return 47



	if(char is ' '):
		return int('20',16)
	if(char is 'the'):
		return int('21',16)
	if(char is ''):
		return int('22',16)
	if(char is ''):
		return int('23',16)
	if(char is 'ed'):
		return int('24',16)
	if(char is 'sh'):
		return int('25',16)
	if(char is 'and'):
		return int('26',16)
	if(char is "\'"):
		return int('27',16)
	if(char is 'of'):
		return int('28',16)
	if(char is 'with'):
		return int('29',16)
	if(char is 'ch'):
		return int('2A',16)
	if(char is 'ing'):
		return int('2B',16)
	if(char is ''):
		return int('2C',16)
	if(char is '-'):
		return int('2D',16)
	if(char is ''):
		return int('2E',16)
	if(char is 'st'):
		return int('2F',16)
	if(char is '\"'):
		return int('30',16)
	if(char is ','):
		return int('31',16)
	if(char is ';'):
		return int('32',16)
	if(char is ':'):
		return int('33',16)
	if(char is '.'):
		return int('34',16)
	if(char is 'en'):
		return int('35',16)
	if(char is '!'):
		return int('36',16)
	if(char is '(' or ')'):
		return int('37',16)
	if(char is ''):
		return int('38',16)
	if(char is 'in'):
		return int('39',16)
	if(char is 'wh'):
		return int('3A',16)
	if(char is ''):
		return int('3B',16)
	if(char is 'gh'):
		return int('3C',16)
	if(char is 'for'):
		return int('3D',16)
	if(char is 'ar'):
		return int('3E',16)
	if(char is 'th'):
		return int('3F',16)
	if(char is ''):
		return int('40',16)

# Small Letters
	if(char is 'a'):
		return int('41',16)
	if(char is 'b'):
		return int('42',16)
	if(char is 'c'):
		return int('43',16)
	if(char is 'd'):
		return int('44',16)
	if(char is 'e'):
		return int('45',16)
	if(char is 'f'):
		return int('46',16)
	if(char is 'g'):
		return int('47',16)
	if(char is 'h'):
		return int('48',16)
	if(char is 'i'):
		return int('49',16)
	if(char is 'j'):
		return int('4A',16)
	if(char is 'k'):
		return int('4B',16)
	if(char is 'l'):
		return int('4C',16)
	if(char is 'm'):
		return int('4D',16)
	if(char is 'n'):
		return int('4E',16)
	if(char is 'o'):
		return int('4F',16)
	if(char is 'p'):
		return int('50',16)
	if(char is 'q'):
		return int('51',16)
	if(char is 'r'):
		return int('52',16)
	if(char is 's'):
		return int('53',16)
	if(char is 't'):
		return int('54',16)
	if(char is 'u'):
		return int('55',16)
	if(char is 'v'):
		return int('56',16)
	if(char is 'w'):
		return int('57',16)
	if(char is 'x'):
		return int('58',16)
	if(char is 'y'):
		return int('59',16)
	if(char is 'z'):
		return int('5A',16)

# Capital Letters
	cap_ret = [int('2C',16), None]
	if(char is 'A'):
		cap_ret[1]=int('41',16)
		return cap_ret
	if(char is 'B'):
		cap_ret[1]=int('42',16)
		return cap_ret
	if(char is 'C'):
		cap_ret[1]=int('43',16)
		return cap_ret
	if(char is 'D'):
		cap_ret[1]=int('44',16)
		return cap_ret
	if(char is 'E'):
		cap_ret[1]=int('45',16)
		return cap_ret
	if(char is 'F'):
		cap_ret[1]=int('46',16)
		return cap_ret
	if(char is 'G'):
		cap_ret[1]=int('47',16)
		return cap_ret
	if(char is 'H'):
		cap_ret[1]=int('48',16)
		return cap_ret
	if(char is 'I'):
		cap_ret[1]=int('49',16)
		return cap_ret
	if(char is 'J'):
		cap_ret[1]=int('4A',16)
		return cap_ret
	if(char is 'K'):
		cap_ret[1]=int('4B',16)
		return cap_ret
	if(char is 'L'):
		cap_ret[1]=int('4C',16)
		return cap_ret
	if(char is 'M'):
		cap_ret[1]=int('4D',16)
		return cap_ret
	if(char is 'N'):
		cap_ret[1]=int('4E',16)
		return cap_ret
	if(char is 'O'):
		cap_ret[1]=int('4F',16)
		return cap_ret
	if(char is 'P'):
		cap_ret[1]=int('50',16)
		return cap_ret
	if(char is 'Q'):
		cap_ret[1]=int('51',16)
		return cap_ret
	if(char is 'R'):
		cap_ret[1]=int('52',16)
		return cap_ret
	if(char is 'S'):
		cap_ret[1]=int('53',16)
		return cap_ret
	if(char is 'T'):
		cap_ret[1]=int('54',16)
		return cap_ret
	if(char is 'U'):
		cap_ret[1]=int('55',16)
		return cap_ret
	if(char is 'V'):
		cap_ret[1]=int('56',16)
		return cap_ret
	if(char is 'W'):
		cap_ret[1]=int('57',16)
		return cap_ret
	if(char is 'X'):
		cap_ret[1]=int('58',16)
		return cap_ret
	if(char is 'Y'):
		cap_ret[1]=int('59',16)
		return cap_ret
	if(char is 'Z'):
		cap_ret[1]=int('5A',16)
		return cap_ret

# Integers
	int_ret = [int('23',16), None]
	if(char is '1'):
		cap_ret[1]=int('41',16)
		return cap_ret
	if(char is '2'):
		cap_ret[1]=int('42',16)
		return cap_ret
	if(char is '3'):
		cap_ret[1]=int('43',16)
		return cap_ret
	if(char is '4'):
		cap_ret[1]=int('44',16)
		return cap_ret
	if(char is '5'):
		cap_ret[1]=int('45',16)
		return cap_ret
	if(char is '6'):
		cap_ret[1]=int('46',16)
		return cap_ret
	if(char is '7'):
		cap_ret[1]=int('47',16)
		return cap_ret
	if(char is '8'):
		cap_ret[1]=int('48',16)
		return cap_ret
	if(char is '9'):
		cap_ret[1]=int('49',16)
		return cap_ret
	if(char is '0'):
		cap_ret[1]=int('4A',16)
		return cap_ret

	if(char is 'ow'):
		return int('5B',16)
	if(char is 'ou'):
		return int('5C',16)
	if(char is 'er'):
		return int('5D',16)
	if(char is ''):
		return int('5E',16)
	if(char is ''):
		return int('5F',16)
