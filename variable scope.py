localvar= 'this is a string in the main program'
def myfunction ():
    global localvar
    localvar= 'this is a string within a function'
    print (localvar)
    return

print (localvar)
myfunction()
print (localvar)

