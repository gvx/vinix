def i(env, document):
	env.mode = 'i'
	refreshscreen()

def p(env, document):
	env.x = 0
	updatepos()

def j(env, document):
	env.y += env.num or 1
	if env.y > Hmaxw:
		if (document.yindex + env.y - Hmaxw) < len(document.text): #FIXME
			document.yindex += env.y - Hmaxw
		else:
			document.yindex = len(document.text) - 1
		env.y = Hmaxw
		refreshscreen()
	env.clampx(env, document)
	updatepos()
def k(env, document):
	env.y -= env.num or 1
	if env.y < 0:
		if document.yindex > -env.y:
			document.yindex += env.y
		else:
			document.yindex = 0
		env.y = 0
		refreshscreen()
	env.clampx(env, document)
	updatepos()
def h(env, document):
	env.x = max(env.x - 1, 0)
	env.clampx(env, document)
	updatepos()
def l(env, document):
	#env.x = min(env.x + 1, Wmax)
	env.x = env.x + 1
	env.clampx(env, document)
	updatepos()

def refresh(env,document):
	global H, W, Wmax, Hmax, Hmaxw
	W, H = console.getTerminalSize()
	Wmax = W - 1
	Hmax = H - 1
	Hmaxw = Hmax - 1
	refreshscreen()

def colon(env, document):
	env.mode = 'c'
	env.cstring = ''
	ttyLinux.writeChar(Hmax, 0, ':')
	env.x = 1
	env.y = Hmax

def gg(env, document):
	env.num = min(env.num or 1, len(document.text)) - 1
	env.y = 0
	document.yindex = env.num
	env.x = 0
	env.clampx(env, document)
	refreshscreen()
def G(env, document):
	if not env.num:
		env.num = len(document.text)-1
	return n.gg(env, document)

self[':'] = colon
self['\x1b[A'] = k
self['\x1b[B'] = j
self['\x1b[C'] = l
self['\x1b[D'] = h
