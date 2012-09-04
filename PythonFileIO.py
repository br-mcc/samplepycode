# Generic open and close
f = open(iofile, 'r+')                  # Open a file for read/write.  'w' = write-only, 'w+' = overwrite existing file contents, 'r' = read-only, 'r+' = read and write
f.close()                               # Close an open file stream
    
# Read modules.
f.read()                                # Read entire file at once
f.readline()                            # Read file line-by-line
f.readlines()                           # Read all lines of file without loading entire file into memory at once
for line in f:                          # Loops through file object.  More efficient alternative to readlines() in terms of large file operations.
    print f
    
# Write module
f.write("Some string.")                 # Writes a string to the file declared by "f"
                
# Equivalent of a "try/finally" block for read/write ops
with open(iofile,'r+') as f:
    read_data = f.read()
    print read_data
f.close()
        
# Anything written to a file must be converted into a string first.
value = ('the answer', 42)
s = str(value)
f.write(s)