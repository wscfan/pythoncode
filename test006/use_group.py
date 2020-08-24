import re

def test_group():
    content = 'hello, world'
    p = re.compile(r'world')
    rest = p.search(content)
    print(rest)
    if rest is not None:
        print(rest.group())

def test_groups():
    p = re.compile(r'(?P<first>aaa)(?P<second>\d+)(?P<third>\w+)')
    str = 'aaa2131dsfsdf123'
    rest = p.search(str)
    print(rest.group(3))
    print(rest.groups())
    print(rest.groupdict())


if __name__ == '__main__':
    test_group()
    test_groups()