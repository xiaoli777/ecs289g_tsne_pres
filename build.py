#!/usr/bin/python3
import argparse
import os
import shutil

def handleAutoComplete():
    if sys.platform == 'Mac OS X':
        complete_cmd = 'complete -F _longopt {}'.format(os.path.basename(__file__))
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path) as f:
            if not complete_cmd in f.read():
                os.system('echo "{}" >> {}'.format(complete_cmd, bashrc_path))
    else:
        pass

class BuildDirectory():
    def __init__(self):
        self.script_folder = os.path.abspath(os.path.dirname(__file__))
        self.build_root = os.path.join(self.script_folder, 'build')

    def sourceFilename(self, base_filename_tex):
        return os.path.join(os.path.join(self.script_folder), base_filename_tex)

    def outputFilename(self, base_filename_tex):
        return os.path.join(os.path.join(self.script_folder), os.path.splitext(base_filename_tex)[0] + '.pdf')

def runBuild(dirs, tex_filename):
    os.makedirs(dirs.build_root, exist_ok=True)
    exit_code = os.system("pdflatex {}".format(dirs.sourceFilename(tex_filename)))
    if exit_code != 0:
        quit(1)

def runPreview(dirs, tex_filename):
    os.system("evince {}".format(dirs.outputFilename(tex_filename)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true', help='Clean build folder')
    # parser.add_argument('filename', nargs=1, help="Name of the target LaTeX file")
    parser.add_argument('--preview', action='store_true', help='Open output file with pdf viewer')
    args = parser.parse_args()
    dirs = BuildDirectory()

    target_name = 'pres.tex'

    if args.clean:
        shutil.rmtree(dirs.build_root, ignore_errors=True)
        quit()

    runBuild(dirs, target_name)
    if args.preview:
        runPreview(dirs, target_name)
        
    print("finished")

    
    


    
