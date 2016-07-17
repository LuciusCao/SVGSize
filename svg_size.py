import glob,re

def has_size(src):
    tar = re.findall(r'<svg([\s\S]*?)>',src)[0]
    have_height = re.findall(r'height',tar)
    have_width = re.findall(r'width',tar)
    if have_width and have_height:
        return True
    else:
        return False

def get_size(src):
    s = re.findall(r'(?<=viewBox=")(.*?)(?=")',src)[0]
    size = s.split(' ')
    w = size[2]+'px'
    h = size[3]+'px'
    return w,h

def add_size(src,width,height):
    repl = r' width="'+width+'" height="'+height+'" '
    new_code = re.sub(r'(?<=<svg).',repl,src)
    return new_code

if __name__ == '__main__':
    path = input('enter your directory here')
    q = glob.glob(path, recursive=True)
    for item in q:
        f = open(item,'r')
        src = f.read()
        f.close()
        if not has_size(src):
            width, height = get_size(src)
            f = open(item,'w')
            new_src = add_size(src,width,height)
            f.writelines(new_src)
            f.close()
            print('changed')
        else:
            print('already has size')
