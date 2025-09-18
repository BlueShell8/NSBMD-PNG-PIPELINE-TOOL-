import os
from PIL import Image
import time
import sys
import random
import math
import shutil

# ===================================================
#        NSBMD PNG PIPELINE TOOL  😎😎😎
# ===================================================
# Autor: BlueShell
# Version: 1.0
# Beschreibung: ein tool um die weltkarten füer NSMB
# ===================================================

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------
FOLDER_MAP = "map"
FOLDER_PNG = "png"
FOLDER_FINISHED = "finished"
NSBMD_FILENAME = "w1.nsbmd"
ENABLE_LOG = True
DUMMY_OFFSET = 0x100
DEBUG_LEVEL = 3  # 0 = keine Logs, 1 = minimal, 2 = normal, 3 = mega-verbose

EASTER_EGGS = [
    "🌟 Du hast das geheime NSBMD Easter Egg gefunden! 🌟",
    "🚀 Bereit für epische Modding Missionen? 🚀",
    "💾 Speicher deine NSBMD gut ab! 💾",
    "🎮 NSMB DS Modding ist cool 😎🎮",
    "🔥 Du bist jetzt ein NSBMD Master! 🔥",
    "🎉 Mega-Lang-Code Bonus aktiviert! 🎉"
]

COLOR_SCHEME = ["red","green","yellow","blue","magenta","cyan","white"]

# ---------------------------------------------------
# UTILITY FUNCTIONS
# ---------------------------------------------------
def log(message, level=2):
    if ENABLE_LOG and level <= DEBUG_LEVEL:
        print(f"[LOG-{level}] {message}")

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Ordner erstellt: {path}", 1)
    else:
        log(f"Ordner existiert bereits: {path}", 2)

def list_png_files(path):
    files = [f for f in os.listdir(path) if f.lower().endswith(".png")]
    log(f"Gefundene PNG-Dateien: {files}", 2)
    return files

def print_banner():
    banner = r"""
  _   _ ____ ____ __  __ ____  __  __ ____   ____  _   _ 
 | \ | | __ ) ___|  \/  |  _ \|  \/  |  _ \ / ___|| | | |
 |  \| |  _ \___ \ |\/| | |_) | |\/| | |_) | |    | |_| |
 | |\  | |_) |__) | |  | |  __/| |  | |  __/| |___ |  _  |
 |_| \_|____/____/|_|  |_|_|   |_|  |_|_|    \____||_| |_|
                                                           
    """
    print(banner)
    print("="*80)
    print("       NSBMD PNG PIPELINE TOOL - ULTRA MAX TINKE EDITION 😎😎😎")
    print("="*80)
    print("Workflow: PNGs von Tinke → NSBMD importieren")
    print("Logs, Fortschrittsbalken, Easter Eggs, Slow-Prints, Dummy-Funktionen")
    print("="*80)

def slow_print(msg, delay=0.02):
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(delay)
    print("")

def print_progress_bar(current, total, bar_length=50):
    fraction = current / total
    filled_length = int(bar_length * fraction)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\r[{bar}] {int(fraction*100)}%", end='', flush=True)

def simulate_loading(msg="Lade Ressourcen", duration=2):
    slow_print(msg + "...", 0.03)
    steps = 20
    for i in range(steps):
        print_progress_bar(i+1, steps)
        time.sleep(duration/steps)
    print("\n")

def random_easter_egg():
    slow_print(random.choice(EASTER_EGGS), 0.01)

def colorize_console_output(msg, color="cyan"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m"
    }
    print(f"{colors.get(color,'')}{msg}{colors['end']}")

# ---------------------------------------------------
# DUMMY / EXTRA FUNCTIONS FÜR EPIC LENGTH
# ---------------------------------------------------
def backup_original_nsbmd(path):
    backup_path = path + ".bak"
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        with open(backup_path, "wb") as f:
            f.write(data)
        log(f"Backup erstellt: {backup_path}", 1)
    else:
        log(f"Original NSBMD nicht gefunden für Backup: {path}", 1)

def verify_png_integrity(png_path):
    try:
        with Image.open(png_path) as img:
            img.verify()
        log(f"PNG geprüft OK: {png_path}", 2)
        return True
    except Exception as e:
        log(f"[ERROR] PNG beschädigt: {png_path} | {e}", 1)
        return False

def scan_for_unused_offsets(nsbmd_data):
    log("Scanne NSBMD nach ungenutzten Offsets...", 2)
    unused = [hex(DUMMY_OFFSET + i*0x10) for i in range(20)]
    log(f"Gefundene ungenutzte Offsets: {unused}", 2)
    return unused

def generate_import_report(png_files, nsbmd_file):
    log("Erstelle Import-Report...", 2)
    slow_print(f"Import Report für NSBMD: {nsbmd_file}", 0.01)
    for idx, png in enumerate(png_files):
        slow_print(f"PNG[{idx+1}/{len(png_files)}]: {png}", 0.005)
    log("Report abgeschlossen.", 2)

def dummy_function_1():
    log("Dummy Funktion 1 ausgeführt",3)
def dummy_function_2():
    log("Dummy Funktion 2 ausgeführt",3)
def dummy_function_3():
    log("Dummy Funktion 3 ausgeführt",3)
def dummy_function_4():
    log("Dummy Funktion 4 ausgeführt",3)
def dummy_function_5():
    log("Dummy Funktion 5 ausgeführt",3)
def dummy_function_6():
    log("Dummy Funktion 6 ausgeführt",3)
def dummy_function_7():
    log("Dummy Funktion 7 ausgeführt",3)
def dummy_function_8():
    log("Dummy Funktion 8 ausgeführt",3)
def dummy_function_9():
    log("Dummy Funktion 9 ausgeführt",3)
def dummy_function_10():
    log("Dummy Funktion 10 ausgeführt",3)

# ===================================================
# PNG -> NSBMD CORE FUNCTION
# ===================================================
def import_png_to_nsbmd(png_folder, original_nsbmd, finished_folder):
    log("Starte Mega-PNG→NSBMD-Prozess...",1)
    ensure_folder(finished_folder)

    if not os.path.exists(png_folder):
        print("[ERROR] PNG-Ordner nicht gefunden!")
        return False

    png_files = list_png_files(png_folder)
    if len(png_files) == 0:
        print("[ERROR] Keine PNGs gefunden!")
        return False

    nsbmd_path = os.path.join(FOLDER_MAP, NSBMD_FILENAME)
    if not os.path.exists(nsbmd_path):
        print("[ERROR] NSBMD nicht gefunden!")
        return False

    # Backup erstellen
    backup_original_nsbmd(nsbmd_path)

    # NSBMD laden
    with open(nsbmd_path, "rb") as f:
        nsbmd_data = bytearray(f.read())
    log(f"Original NSBMD geladen: {len(nsbmd_data)} Bytes", 2)

    current_offset = DUMMY_OFFSET
    log(f"Beginne PNG-Import bei Offset: {hex(DUMMY_OFFSET)}", 2)

    for idx, png_file in enumerate(png_files):
        png_path = os.path.join(png_folder, png_file)
        if not verify_png_integrity(png_path):
            log(f"PNG übersprungen: {png_file}", 1)
            continue

        with Image.open(png_path) as img:
            bitmap_data = img.tobytes()
        size = len(bitmap_data)

        if current_offset + size > len(nsbmd_data):
            size = len(nsbmd_data) - current_offset
            log(f"[WARN] Bitmap passt nicht komplett, wird gekürzt: {png_file}", 1)

        nsbmd_data[current_offset:current_offset+size] = bitmap_data[:size]
        log(f"Bitmap eingefügt: {png_file} | Offset={hex(current_offset)} | Größe={size} Bytes",2)
        current_offset += size + 0x10

        print_progress_bar(idx+1, len(png_files))
        time.sleep(0.05)

    generate_import_report(png_files, nsbmd_path)
    output_path = os.path.join(finished_folder, "w1_fixed.nsbmd")
    with open(output_path, "wb") as f:
        f.write(nsbmd_data)
    log(f"Fertige NSBMD erstellt: {output_path}", 1)
    random_easter_egg()
    return True

# ===================================================
# HAUPTLOGIK
# ===================================================
def main():
    print_banner()
    ensure_folder(FOLDER_MAP)
    ensure_folder(FOLDER_PNG)
    ensure_folder(FOLDER_FINISHED)

    slow_print("Bereite Mega-Ultra-Tinke-Workflow vor...",0.01)
    simulate_loading("Initialisiere Mega-Tool",2)

    nsbmd_file = os.path.join(FOLDER_MAP, NSBMD_FILENAME)

    slow_print("Bitte bearbeite die PNG-Dateien im Ordner 'png' mit Tinke.",0.01)
    slow_print("Alle TEX0/TEX1-Korrekturen werden von Tinke erledigt.",0.01)
    input("\nDrücke Enter, wenn die PNGs fertig bearbeitet wurden...")

    success = import_png_to_nsbmd(FOLDER_PNG, nsbmd_file, FOLDER_FINISHED)
    if not success:
        print("[ERROR] Import fehlgeschlagen! Überprüfe PNGs und Ordnerstruktur.")
        sys.exit(1)

    print("\n" + "="*80)
    slow_print("[INFO] Fertige NSBMD erstellt und im Ordner 'finished' abgelegt!",0.01)
    slow_print("Du kannst sie nun mit NSMBe oder anderen Tools weiter verwenden.",0.01)
    print("="*80)

# ---------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------
if __name__ == "__main__":
    main()












