import termios, sys, time

def setSpecial () :
	"set keyboard to read single chars lookahead only"
	global oldSettings
	fd = sys.stdin.fileno()
	oldSettings = termios.tcgetattr(fd)
	new = termios.tcgetattr(fd)
	new[3] = new[3] & ~termios.ECHO    # lflags
	new[3] = new[3] & ~termios.ICANON  # lflags
	new[6][6] = '\000'    # Set VMIN to zero for lookahead only
	termios.tcsetattr(fd, termios.TCSADRAIN, new)

def setNormal () :
	"restore previous keyboard settings"
	global oldSettings
	fd = sys.stdin.fileno()
	termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

def readLookAhead () :
	"read max 3 chars (arrow escape seq) from look ahead"
	return sys.stdin.read(4)

def clearScreen():
	sys.stdout.write('\033[1;1H\033[J')

def writeChar(row,col,char) :
	'write char to screen at row,col'
	sys.stdout.write('\033[%d;%dH%s' % (row+1,col+1,char))
	sys.stdout.flush()