import convert,sys

def main():
	contents = ""
	if len(sys.argv)==1:
		contents = sys.stdin.read()
	else:
		with open(sys.argv[1]) as f:
			contents = f.read()
	res = convert.nasmToASM(contents)
	if len(sys.argv)==3:
		with open(sys.argv[2],"w") as f:
			f.write(res)
	else:
		print res
