import compy

print(compy.load('Advanced.com')['Line1'])
print(compy.overload('Advanced.com')) # This will return a string like this:
                                      # Line1: Value1
                                      # Line2: Value2
                                      # Etc. for each line in the file
