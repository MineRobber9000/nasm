loadinstrs = {"a":"LDA","x":"LDX","y":"LDY"}
storeinstrs = {"a":"STA","x":"STX","y":"STY"}
compareinstrs = {"a":"CMP","x":"CPX","y":"CPY"}
branches = {"equal":"BEQ","diff":"BNE","carry-set":"BCS","carry-clear":"BCC","positive":"BPL","negative":"BMI","overflow-clear":"BVC","overflow-set":"BVS","unconditional":"JMP"}
clearables = {"carry":"CLC","decimal":"CLD","interrupt":"CLI","overflow":"CLV"}
setables = {"carry":"SEC","decimal":"SED","interrupt":"SEI"}
logical = {"and":"AND","or":"ORA","xor":"EOR","shift-right":"LSR"}
increment = {"x":"INX","y":"INY"}
decrement = {"x":"DEX","y":"DEY"}
def incErrorHandler(v,l,errmsg):
  if not v in increment and not v.startswith("$"):
    raise Exception(errmsg)
  else:
    l.append("INC "+v)
def decErrorHandler(v,l,errmsg):
  if not v in decrement and not v.startswith("$"):
    raise Exception(errmsg)
  else:
    l.append("DEC "+v)
def defaultErrorHandler(v,l,errmsg):
  raise Exception(errmsg)
def nasmToASM(s,li=loadinstrs,si=storeinstrs,ci=compareinstrs,branches=branches):
  ret = []
  lines = s.split("\n")
  for line in lines:
    line = line.lower().split(";",1)[0].rstrip()
    if not line:
      continue
    if line=="return":
      ret.append("rts")
    elif line.endswith(":"):
      ret.append(line)
    elif line.startswith("load "):
      formatLine(line,li,ret)
    elif line.startswith("store "):
      formatLine(line,si,ret)
    elif line.startswith("compare "):
      formatLine(line,ci,ret)
    elif line.startswith("branch "):
      formatLine(line,branches,ret,"Invalid branch type \"{}\"!")
    elif line.startswith("clear-flag "):
      formatLine(line,clearables,ret,"Invalid clear flag {}!",False)
    elif line.startswith("set-flag "):
      formatLine(line,setables,ret,"Invalid set flag {}!",False)
    elif line.startswith("logical "):
      formatLine(line,logical,ret,"Invalid logical operation {}!",False)
    elif line.startswith("inc "):
      formatLine(line,increment,ret,"Cannot increment register {}!",False,incErrorHandler)
    elif line.startswith("dec "):
      formatLine(line,decrement,ret,"Cannot decrement register {}!",False,decErrorHandler)
    elif line.startswith("add "):
      ret.append("ADC "+line.split(" ",1)[1])
    elif line.startswith("subtract "):
      ret.append("SBC "+line.split(" ",1)[1])
    elif line=="do-nothing":
      ret.append("NOP")
    elif line.startswith("callsub "):
      ret.append(line.replace("callsub ","JSR "))
    elif line=="save-a":
      ret.append("PHA")
    elif line=="restore-a":
      ret.append("PLA")
    elif line.startswith("accumulator-shift-left "):
      ret.append("ASL "+line.split()[1])
    elif line.startswith("rotate "):
      parts = line.split()
      if parts[1]=="left":
        ret.append("ROL "+parts[2])
      elif parts[1]=="right":
        ret.append("ROR "+parts[2])
      else:
        raise Exception("Invalid rotate direction!")
    elif line.startswith("transfer"):
      parts = line.split()
      if parts[1] not in ("a","x","y") or parts[2] not in ("a","x","y"):
        raise Exception("Invalid register!")
      ret.append("".join(["T",parts[1],parts[2]]).upper())
  return "\n".join(ret).upper()

def formatLine(line,idict,l,errmsg="Invalid register {}!",usethirdpart=True,errorHandler=defaultErrorHandler):
  parts = line.split(" ",2)
  try:
    if usethirdpart:
      l.append(" ".join((idict[parts[1]],parts[2])))
    else:
      l.append(idict[parts[1]])
  except KeyError:
    errorHandler(parts[1],l,errmsg.format(parts[1]))
