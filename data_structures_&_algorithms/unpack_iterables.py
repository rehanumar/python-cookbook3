# all iterables can be unpacked in python
# this file will include examples on all iterables (tuples, lists, strings, files, iterators, generators)
# as well as examples on exceptions and iterables of arbitrary length


# Tuples
p = 4, 5
x, y = p

symbols = ('POL', 'EFERT', 'PICT', 'OGDC')
fav, *_ = symbols


# Lists
company = ['POL', 1000, 350, 20, (2021, 3, 21)]
sym, shares, price, div_yield, (bought_year, bought_month, bought_day) = company

sales = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing, current = sales
trailing_avg = sum(trailing) / len(trailing)
print('average of trailing quarters is {} whereas current quarter sales are at {}'.format(round(trailing_avg, 2), current))


# strings
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')



# files

# iterators

# generators





# Exceptions
# too many values to unpack
p = 5, 6, 7
x, y = p
# not enough values to unpack
x, y, z, _ = p

# unpacking iterables of arbitrary length
records = [('foo', 1, 2), ('bar', 'hello'), ("foo", 3, 4),]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


items = [1, 10, 7, 4, 5, 9]
# warning recursion is not python's forte
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
