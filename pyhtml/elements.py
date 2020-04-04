from pyhtml import HTMLElement
# Elements sourced from
# https://developer.mozilla.org/en-US/docs/Web/HTML/Element

# Structural
html = HTMLElement('html')
body = HTMLElement('body')

# Metadata
base = HTMLElement('base')
head = HTMLElement('head')
link = HTMLElement('link')
meta = HTMLElement('meta')
style = HTMLElement('style')
title = HTMLElement('title')

# Content sectioning
address = HTMLElement('address')
article = HTMLElement('article')
section = HTMLElement('section')
footer = HTMLElement('footer')
header = HTMLElement('header')
hgroup = HTMLElement('hgroup')
aside = HTMLElement('aside')
main = HTMLElement('main')
nav = HTMLElement('nav')

# Section headings
h1 = HTMLElement('h1', arity=1)
h2 = HTMLElement('h2', arity=1)
h3 = HTMLElement('h3', arity=1)
h4 = HTMLElement('h4', arity=1)
h5 = HTMLElement('h5', arity=1)
h6 = HTMLElement('h6', arity=1)

# Text content
blockquote = HTMLElement('blockquote')
dd = HTMLElement('dd')
div = HTMLElement('div')
dl = HTMLElement('dl')
dt = HTMLElement('dt')
figcaption = HTMLElement('figcaption')
figure = HTMLElement('figure')
hr = HTMLElement('hr')
li = HTMLElement('li')
main = HTMLElement('main')
ol = HTMLElement('ol')
p = HTMLElement('p')
pre = HTMLElement('pre')
ul = HTMLElement('ul')

# Inline text
a = HTMLElement('a')
abbr = HTMLElement('abbr')
b = HTMLElement('b')
bdi = HTMLElement('bdi')
bdo = HTMLElement('bdo')
br = HTMLElement('br')
cite = HTMLElement('cite')
code = HTMLElement('code')
data = HTMLElement('data')
dfn = HTMLElement('dfn')
em = HTMLElement('em')
i = HTMLElement('i')
kbd = HTMLElement('kbd')
mark = HTMLElement('mark')
q = HTMLElement('q')
rb = HTMLElement('rb')
rp = HTMLElement('rp')
rt = HTMLElement('rt')
ruby = HTMLElement('ruby')
s = HTMLElement('s')
samp = HTMLElement('samp')
small = HTMLElement('small')
span = HTMLElement('span')
strong = HTMLElement('strong')
sub = HTMLElement('sub')
sup = HTMLElement('sup')
time = HTMLElement('time')
u = HTMLElement('u')
var = HTMLElement('var')
wbr = HTMLElement('wbr')

# Media
area = HTMLElement('area')
audio = HTMLElement('audio')
img = HTMLElement('img')
map = HTMLElement('map')
track = HTMLElement('track')
video = HTMLElement('video')

# Embedded content
embed = HTMLElement('embed')
iframe = HTMLElement('iframe')
object = HTMLElement('object')
param = HTMLElement('param')
picture = HTMLElement('picture')
source = HTMLElement('source')

# Scripting
canvas = HTMLElement('canvas')
noscript = HTMLElement('noscript')
script = HTMLElement('script')

# Demarcating edits
# del = HTMLElement('del')
ins = HTMLElement('ins')

# Tables
caption = HTMLElement('caption')
col = HTMLElement('col')
colgroup = HTMLElement('colgroup')
table = HTMLElement('table')
tbody = HTMLElement('tbody')
td = HTMLElement('td')
tfoot = HTMLElement('tfoot')
th = HTMLElement('th')
thead = HTMLElement('thead')
tr = HTMLElement('tr')

# Forms
button = HTMLElement('button')
datalist = HTMLElement('datalist')
fieldset = HTMLElement('fieldset')
form = HTMLElement('form')
input = HTMLElement('input')
label = HTMLElement('label')
legend = HTMLElement('legend')
meter = HTMLElement('meter')
optgroup = HTMLElement('optgroup')
option = HTMLElement('option')
output = HTMLElement('output')
progress = HTMLElement('progress')
select = HTMLElement('select')
textarea = HTMLElement('textarea')

# Interactivity
details = HTMLElement('details')
dialog = HTMLElement('dialog')
menu = HTMLElement('menu')
summary = HTMLElement('summary')

# Web components
slot = HTMLElement('slot')
template = HTMLElement('template')
