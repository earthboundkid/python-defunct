from subprocess import Popen, PIPE

def run_applescript(script):
    "Returns the result of running string in osascript (Applescript)"
    
    if hasattr(script, "encode"):
        script = script.encode("utf-8")
    
    osa = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    results, err = osa.communicate(script)
    
    if err:
        raise Exception(err)
    
    return results.decode("utf-8")
