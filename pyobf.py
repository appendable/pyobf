import base64, random, argparse
from os import sys, path


# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-obfuscate', help='[file | file path] | obfuscate a file', action='store', dest='filed', type=str, required=True)
args = parser.parse_args()


if not path.exists(args.__dict__['filed']):
    raise FileNotFoundError('The file does not exist.')

f = args.__dict__['filed']
fl = open(args.__dict__['filed'], 'r')

# padding and line vars
lines = []
postlines = []
random_ = base64.b64encode(bytes(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789' + 'kylie', k=500)), 'utf-8'))
random2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
random3 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
random4 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
string = base64.b64encode(bytes('<string>', 'utf-8'))
exc = base64.b64encode(bytes('exec', 'utf-8'))

if not fl.readable(): 
    exit(-1)
else:
    # appending file contents to variables
    for line in fl.readlines():
        lines.append(line)
    postlines = base64.b64encode(bytes('\n'.join([l for l in lines]), 'utf-8'))

# "obfuscation" process
def obf():
    fo = open(f'{f}_output.py', 'w')
    if len(postlines) <= 0:
        fo.write('None | Something went wrong.')
    else:
        fo.write(f'{random2}={str(random_)};import base64;{random3}={str(postlines)};exec(compile(base64.b64decode({random3}), base64.b64decode(\'{string.decode()}\').decode(), base64.b64decode(\'{exc.decode()}\').decode())){random4}={random_}')
        print('Successful Obfuscation')
    
if args.__dict__['filed']:
    obf()