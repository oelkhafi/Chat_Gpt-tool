# put your python code here
import re

pattern = re.compile(r'(-?)(\d*)\*?x\^?(\d*)')

powers = {}

for term in pattern.findall(input()):
    sign, c, exp = (x if i == 0 else int(x or 1) for i, x in enumerate(term))
    powers[exp] = powers.setdefault(exp, 0) + (-c if sign == '-' else c)

terms = []
for exp in sorted(powers, reverse=True):
    if exp == 1:
        terms.append('{}'.format(powers[exp]))
    elif exp == 2:
        terms.append('{}*x'.format(powers[exp] * exp))
    else:
        terms.append('{}*x^{}'.format(powers[exp] * exp, exp - 1))

print('+'.join(terms).replace('+-', '-'))
 