import termcolor
string = "type-name-function-location"
string = string.replace('-', termcolor.colored('-', 'red'))
print string
