import os, re

def main():
    dirstorename = []
    filestorename = []

    ser = os.getcwd()
    tcdirs = os.listdir(ser)
    for tcname in tcdirs:
        tcdir = os.path.join(ser,tcname)
        if os.path.isdir(tcdir):
            servicedirs = os.listdir(tcdir)
            for servicedirname in servicedirs:
                servicedir = os.path.join(ser,tcname,servicedirname)
                #rename service dirs
                if os.path.isdir(servicedir):
                    dirstorename.append(servicedir)
                    xmlfiles = os.listdir(servicedir)
                    for xmlfilename in xmlfiles:
                        xmlfile = os.path.join(ser,tcname,servicedirname,xmlfilename)
                        if os.path.isfile(xmlfile):
                            #rename xml files
                            filestorename.append(xmlfile)
                            # print xmlfile
    print "> renamed files:\n"
    for file in filestorename:
        filewov = replaceVersionFile(file)
        print filewov
        os.rename(file, filewov)

    print "\n\n> renamed dirs:\n"
    for dir in dirstorename:
        dirwov = replaceVersionDir(dir)
        print dirwov
        os.rename(dir, dirwov)

def replaceVersionFile(filename):
    sp = re.search("KSA\$", filename)
    if sp is not None:
        return filename
    bb = re.search("[0-9]\.xml$",filename)
    if bb is not None:
        b = bb.group()
        v = re.search("^[0-9]", b).group()
        x = b.replace(v, "")
        return filename.replace(b,x)
    else:
        return filename

def replaceVersionDir(filename):
    sp = re.search("KSA\$", filename)
    if sp is not None:
        return filename
    if filename[len(filename)-1:].isdigit():
        return filename[:len(filename)-1]
    else:
        return filename

if __name__ == '__main__':
    main()