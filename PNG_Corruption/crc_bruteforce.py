from binascii import crc32

correct_crc = int.from_bytes(b'\x00\x00\x00\x00',byteorder='big') #Change to the CRC32 of the chunk 

for h in range(2000):
	for w in range(2000):
		crc=b"\x49\x48\x44\x52"+w.to_bytes(4,byteorder='big')+h.to_bytes(4,byteorder='big')+b"\x00\x00\x00\x00\x00" #Change the last 5 bytes to the last bytes of the IHDR chunk 
		if crc32(crc) % (1<<32) == correct_crc:
			print ('FOUND!')
			print ('Width: ',end="")
			print (hex(w))
			print ('Height :',end="")
			print (hex(h))
			exit()
