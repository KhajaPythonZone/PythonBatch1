
fout = open('important.bin', 'wb')
binary_data = bytes(range(0, 256))
fout.write(binary_data)
fout.close()