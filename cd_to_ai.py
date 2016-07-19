import glob,re

def remove_cd_style(src):
    repl = r''
    src = re.sub(r'(?<=css">\n)[\s\S]*<!\[CDATA\[\n',repl,src)
    src = re.sub(r'(?<=\n).*?]]>\n',repl,src)
    return src

if __name__ == '__main__':
    q = glob.glob('./9398/**/*.svg', recursive=True)
    for item in q:
        f = open(item,'r')
        src = f.read()
        f.close()
        src = remove_cd_style(src)
        f = open(item,'w')
        f.writelines(src)
        f.close()
        print(item,'changed')
