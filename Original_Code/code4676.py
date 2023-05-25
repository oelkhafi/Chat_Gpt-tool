# put your python code here
WIDTH, HEIGHT = 4, 7

middle = WIDTH - 2
top = (HEIGHT - 3) // 2
bottom = HEIGHT - 3 - top

digits = {
    '1': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', ' ' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', ' ' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', ' ' * middle, ' ')),
    '2': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, ' ') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '3': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '4': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', ' ' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', ' ' * middle, ' ')),
    '5': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, ' ') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '6': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, ' ') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '7': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', ' ' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', ' ' * middle, ' ')),
    '8': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '9': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format(' ', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
    '0': '{}{}{}{}{}'.format(
        '{}{}{}'.format(' ', '-' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * top,
        '{}{}{}'.format(' ', ' ' * middle, ' '),
        '{}{}{}'.format('|', ' ' * middle, '|') * bottom,
        '{}{}{}'.format(' ', '-' * middle, ' ')),
}

line = input()
print('x{}x'.format('-' * (len(line) * (WIDTH + 1) - 1)))
for row in range(HEIGHT):
    print('|{}|'.format(' '.join((digits[ch][row * WIDTH:(row + 1) * WIDTH] for ch in line))))
print('x{}x'.format('-' * (len(line) * (WIDTH + 1) - 1))) 