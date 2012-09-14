# Open a file and assign to file object "r"
# File object accepts the following values:
#   w   = write-only
#   w+  = write-only, overwrite existing contents
#   r   = read-only
#   r+  = read AND write
i = open('Test.txt', 'r')               # Open a file for read operations.
o = open('Test.out', 'w+')              # Open a file for write operations.  (Overwrite file contents regardless of contents)
                                        #   --> This file will be created in the local directory if it doesn't exist.

"""
--------
READING THE CONTENTS OF A FILE
--------
"""
# Read file line-by-line
linebyline = i.readline()
print '''
readline()
%s''' % linebyline

# Read all lines of file without loading entire file into memory at once. More efficient than readline().
alllines = i.readlines()
print '''
readlines()
%s''' % alllines

i.close()
i = open('Test.txt','r')
# Notice what's happening here.  We have to close the read stream and reopen it because
#   readline(), readlines(), and read() are iterative.  Look at the readline() output versus
#   readlineS().  See how one picks up after the other?  You would need to call readline()
#   consecutively to iterate through a full file.  Since readlineS() takes the rest of the
#   file contents in, we would get an empty return for "fullread" below because read() wouldn't have
#   anything else to...well...read!  It starts at the end of the file!  Of course, this would
#   be entirely silly to do in a single Python module, but you get he idea.

# Read and load entire file into memory at once.  Not recommended for large files!
fullread = i.read()
print '''
read()
%s''' % fullread

# Loop through file object.  More efficient alternative to readlines() in terms of large file operations.
print "\nFor loop 'for line in f'"
for line in i:
    print i


"""
--------
WRITING TO A FILE
--------
"""
# Write module
o.write("Some string.")                 # Writes a string to the file declared by "o".  Notice that it is merely appended to the last line.
print 'Write "Some string."'
print o.read()

# Write to a new line.
o.write("\nSome string.")               # Notice that we've just added the "new line" special character to the end of the string.
print 'Write "\nSome string."'
print o.read()

# Anything written to a file must be converted into a string first.
value = '\nthe answer', 42
s = str(value)
o.write(s)

i.close()
o.close()                               # Close the file I/O stream

# Equivalent of a "try/finally" block for read/write ops
with open('Test.txt','r+') as rw:
    read_data = rw.read()
    print read_data
rw.close()