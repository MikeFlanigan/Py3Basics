'''
the backslash char \ is a "plain text" tool so it ignores any special
functions assocaited with the letter 
'''
text = 'sample text saving\nNew Line!'
saveFile = open('exampleFile.txt','w') #if it didn't exist it is created
# if no directory is specfied then goes to root
# otherwise can specificy: 'c:\exampleFile.txt'
saveFile.write(text)
saveFile.close()


#appending now
appendMe = '\nNew info!'
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()


'''
reading!
'''
readMe = open('exampleFile.txt','r').read()

print(readMe)

readMe = open('exampleFile.txt','r').readlines()
# creates a python list
print(readMe)


