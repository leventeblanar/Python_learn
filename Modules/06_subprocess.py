import subprocess

# pythonból terminál parancs futtatás

def feladat1():

    # a külsős program maga intézi a kimenetet
    result = subprocess.run(["ls", "-la"])
    print(result)

def feladat2():

    # a check elkapja a hibát és leáll (CalledProcessError)
    subprocess.run(["ls", "/nincs ilyen"], check=True)

def feladat3():

    # kimenet begyűjtése
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
    print("returncode:", result.returncode)
    print("stdout:\n", result.stdout)
    print("stderr:\n", result.stderr)

def feladat4():

    # külön sectionökben helyezzük el a printet
    try:
        result = subprocess.run(
            ["ls", "/nincs_ilyen"],
            capture_output=True,
            text=True,
            check=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Parancs hibával tért vissza:", e.returncode)
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)

def feladat5():
    # kiírjuk két külön fájlba a hibát és a sima outot
    with open("out.txt", "w", encoding="utf-8") as out, open("err.txt", "w", encoding="utf-8") as err:
        subprocess.run(["ls", "-la"], stdout=out, stderr=err, text=True, check=True)

def feladat6():

    # a kettő egy kimeneten
    result = subprocess.run(
        ["ls", "/nincs_ilyen"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        )
    
    print(result.stdout)


def feladat7():

    # timout hogy ne tudjon örökké állni
    try:
        subprocess.run(["sleep", "10"], timeout=1, check=True)
    except subprocess.TimeoutExpired:
        print("Túl sokáig futott, kilőttük / timout lett.")


def feladat8():

    #  bemenet beadása
    result = subprocess.run(
        ["wc", "-c"],
        input="hello",
        text=True,
        capture_output=True,
        check=True
    )
    print(result.stdout)

def feladat8b():

    p = subprocess.Popen(["wc", "-l"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate("a\nb\nc\n")
    print("out:", out)
    print("err:", err)
    print("code:", p.returncode)

def feladat9():

    # hosszú folyamat logja soronként
    p = subprocess.Popen(["ping", "-c", "4", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in p.stdout:
        print("LOG:", line.rstrip())

    code = p.wait()
    print("exit:", code)
    
feladat9()