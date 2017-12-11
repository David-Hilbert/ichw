"""currency.py: change one currency to another currency.

__author__ = "Zhou Junjie"
__pkuid__  = "1700011800"
__email__  = "1700011800@pku.edu.cn"
"""

from urllib.request import urlopen

def from_str_to_number(strings):
	'''
	to pick the numbers from a string
	'''
	s=''
	u=[]
	t=['1','2','3','4','5','6','7','8','9','0','.']
	for iii in strings:
		if iii in t:
			s=s+iii
		elif s!='':
			u.append(s)
			s=''
	return u
def exchange(currency_from, currency_to, amount_from):
	'''Returns: amount of currency received in the given exchange.
	In this exchange, the user is changing amount_from money in 
	currency currency_from to the currency currency_to. The value 
	returned represents the amount in currency currency_to.
	The value returned has type float.
	Parameter currency_from: the currency on hand
	Precondition: currency_from is a string for a valid currency code
	Parameter currency_to: the currency to convert to
	Precondition: currency_to is a string for a valid currency code
	Parameter amount_from: amount of currency to convert
	Precondition: amount_from is a float'''
	doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii')
	jjssttrr=float(from_str_to_number (jstr)[-1])
	return jjssttrr

def test_exchange():
	'''
	test the function exchange
	'''
	assert(exchange('EUR','USD',exchange('USD', 'EUR', 2.5))==2.5)
	return
def test_from_str_to_number():
	'''
	test the function from_str_to_number
	'''
	assert(['3.1415926','3.14']==from_str_to_number('the number 3.1415926 is always shorten to 3.14 '))
	return
def test_All():
	'''
	test all the functions
	'''
	test_exchange()
	test_from_str_to_number()
	print('All tests passed')
	return
def main():
	test_All()
	return
if __name__=='__main__':
    main()
