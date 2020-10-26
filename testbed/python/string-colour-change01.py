# import termcolor
# string = "type-name-function-location"
# string = string.replace('-', termcolor.colored('-', 'red'))
# print (string)



import colorful as cf

# create a colored string using clever method translation
print(cf.bold_white('Hello World'))
# create a colored string using `str.format()`
print('{c.bold}{c.lightCoral_on_white}Hello World{c.reset}'.format(c=cf))

# nest colors
print(cf.red('red {0} red'.format(cf.white('white'))))
print(cf.red('red' + cf.white(' white ', nested=True) + 'red'))

# combine styles with strings
print(cf.bold & cf.red | 'Hello World')

# use true colors
cf.use_true_colors()

# extend default color palette
cf.update_palette({'mint': '#c5e8c8'})
print(cf.mint_on_snow('Wow, this is actually mint'))

# choose a predefined style
cf.use_style('solarized')
# print the official solarized colors
print(cf.yellow('yellow'), cf.orange('orange'),
    cf.red('red'), cf.magenta('magenta'),
    cf.violet('violet'), cf.blue('blue'),
    cf.cyan('cyan'), cf.green('green'))

# directly print with colors
cf.print('{c.bold_blue}Hello World{c.reset}')

# choose specific color mode for one block
with cf.with_8_ansi_colors() as c:
    print(c.bold_green('colorful is awesome!'))

# create and choose your own color palette
MY_COMPANY_PALETTE = {
    'companyOrange': '#f4b942',
    'companyBaige': '#e8dcc5'
}
with cf.with_palette(my_company_palette) as c:
    print(c.companyOrange_on_companyBaige('Thanks for choosing our product!'))

# use f-string (only Python >= 3.6)
print(f'{cf.bold}Hello World')

# support for chinese
print(cf.red('你好'))
