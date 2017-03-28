

# try:
# 	# pass
# 	f = open('abc.txt')
# except Exception:
# 	print("sorry this file is not exit")


try:
	# pass
	f = open('text.txt')
	# varas = variable_not_exist
except FileNotFoundError:
	print("sorry this file is not exit")
except Exception:
	print("Sorry some this went wrong")

else: 
	print(f.read())
	f.close()
finally:
	#always executes
	print("Always goes up")