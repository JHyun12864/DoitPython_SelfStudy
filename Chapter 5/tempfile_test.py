import tempfile

filename = tempfile.mkstemp()

print(filename)
print(type(filename))