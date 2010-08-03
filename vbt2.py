import sys
import lpod
import lpod.document
#doc = lpod.document.odf_new_document_from_type('text')
doc = lpod.document.odf_get_document('simple.odt')
body = doc.get_body()
text = [] #list of paragraphs, each paragraph a tuple of the lpod paragraph and a list containing spans, where each span is a tuple of the lpod span and a string, containting it's text
elemlist = []
metalist = body.get_children()[1:]
print(type(text))
for e in metalist:
	#print(e)
	t = []
	text.append((e, t))
	t.append((e,e.get_text()))
	start = len(e.get_text())
	spans = []
	for k in e.get_span_list():
		end = start + len(k.get_text())
		style = k.get_text_style()
		mode = '\x1b[0m'
		if style:
			style = doc.get_style("text", style)
			properties = style.get_style_properties()
			if properties.get('fo:font-weight') == 'bold':
				mode = '\x1b[1m'
			elif properties.get('fo:font-style') == 'italic':
				mode = '\x1b[4m'
		spans.append((start,end, mode))
		t.append((k,k.get_text()))
		start = end
	g = t[-1][0].get_tail()
	if g:
		t.append((None,g))
	#print(e.get_children())
for paragraph in text:
	p, spans = paragraph
	if p.get_tag() == 'text:h':
		print ' '*(e.get_outline_level()-1) + '\x1b[1;4m' + spans[0][1] + '\x1b[0m'
	else:
		sys.stdout.write('    ' + spans[0][1])
		for span in spans[1:]:
			if span[0]:
				style = span[0].get_text_style()
				if style:
					prop = doc.get_style("text", style).get_style_properties()
					if prop.get('fo:font-weight') == 'bold':
						sys.stdout.write('\x1b[1m')
					elif prop.get('fo:font-style') == 'italic':
						sys.stdout.write('\x1b[4m')
					else:
						sys.stdout.write('\x1b[0m')
			sys.stdout.write(span[1])
			sys.stdout.write('\x1b[0m')
		sys.stdout.write('\n')
