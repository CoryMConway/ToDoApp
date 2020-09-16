import subprocess
import re
import sys
from pathlib import Path
import pyperclip


def getEnviroPythonPath(): ## Finds the path to the python file that the environment is using and copies it to clipboard ##
    try:
        result = subprocess.check_output(["where","python"])
    except subprocess.CalledProcessError as e:
        return_code = e.returncode

    ## Converts BytesObjectTo String and replaces the \\\\ with / for use in the Path module for a crossplatform solution ##
    result = re.sub("b'(.*)'",r"\g<1>", str(result)); result = re.sub('\\\\\\\\','/',result); result = re.sub("\\\\r","",result); result = list(filter(None,result.split("\\n")))
    ## finds the path that contains the module name ##

    for r in result:
        if len(re.compile(sys.argv[1]).findall(r)) > 0:
            result = r
    return Path(result)

if __name__ == "__main__": 
    result = getEnviroPythonPath()
    pyperclip.copy(str(Path(result)))
    print("Copied")