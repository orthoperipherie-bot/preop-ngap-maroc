#!/usr/bin/env python3
"""Build searchable act catalog from the Moroccan NGAP PDF text layer."""
import json, re, sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "ngap_raw.txt")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "site/acts.json")
raw = src.read_text(encoding="utf-8", errors="replace").replace("\x0c", "\n")
lines = [re.sub(r"\s+", " ", s).strip() for s in raw.splitlines()]

# Rejoin identifiers split by PDF text extraction.
normalized, i = [], 0
while i < len(lines):
    line = lines[i]
    if re.fullmatch(r"[A-Z]{1,2}", line) and i + 1 < len(lines) and re.fullmatch(r"\d{3}", lines[i + 1]):
        normalized.append(line + lines[i + 1]); i += 2; continue
    if re.fullmatch(r"[A-Z]\d{2}", line) and i + 1 < len(lines) and lines[i + 1] == "0":
        normalized.append(line + "0"); i += 2; continue
    normalized.append(line); i += 1

code_pat = re.compile(r"^([A-Z])(\d{3})(?:\s+(.*))?$")
starts = []
for i, line in enumerate(normalized):
    m = code_pat.match(line)
    if m:
        starts.append((i, m.group(1) + m.group(2), (m.group(3) or "").strip()))

suffix_pat = re.compile(r"(?<![\w²%])((?:\d+(?:[,.]\d+)?\s+)?\d+(?:[,.]\d+)?)\s*$")
def split_coeff(s):
    m = suffix_pat.search(s)
    if not m: return s.strip(), []
    vals = [v.replace(",", ".") for v in m.group(1).split()]
    before = s[:m.start()].rstrip()
    return before, vals[-2:]

overrides = {
 "C409":("Biopsie intra-articulaire : coude, épaule, hanche, sacro-iliaque ou genou","biopsie articulation"),
 "C410":("Biopsie intra-articulaire : autres articulations","biopsie articulation"),
 "C430":("Arthroplastie avec prothèse : épaule","prothèse épaule arthroplastie"),
 "C431":("Arthroplastie avec prothèse : coude","prothèse coude arthroplastie"),
 "C432":("Arthroplastie avec prothèse : poignet","prothèse poignet arthroplastie"),
 "C433":("Arthroplastie avec prothèse : hanche","PTH prothèse totale hanche arthroplastie coxarthrose"),
 "C434":("Arthroplastie avec prothèse : genou","PTG prothèse totale genou arthroplastie gonarthrose"),
 "C435":("Arthroplastie avec prothèse : cheville","prothèse cheville arthroplastie"),
 "C436":("Ablation de prothèse articulaire : hanche","ablation retrait explantation PTH reprise"),
 "C437":("Ablation de prothèse articulaire : autres articulations","ablation retrait explantation reprise"),
 "C438":("Arthrodèse : coude, épaule, genou ou sacro-iliaque","arthrodèse fusion articulaire"),
 "C439":("Arthrodèse : hanche","arthrodèse fusion hanche"),
 "C440":("Arthrodèse : carpe ou poignet","arthrodèse fusion carpe poignet"),
 "C303":("Ablation de matériel d’ostéosynthèse ou de prothèse : bassin, hanche, fémur, rachis","retrait matériel ostéosynthèse plaque vis clou"),
 "C304":("Ablation de matériel d’ostéosynthèse ou de prothèse : autres localisations","retrait matériel ostéosynthèse plaque vis clou cheville pied poignet"),
 "C408":("Arthroscopie : biopsies et gestes thérapeutiques éventuels inclus","arthroscopie genou épaule cheville poignet chirurgie sport"),
 "C609":("Libération du nerf médian dans le syndrome du canal carpien","canal carpien CTS nerf médian décompression main"),
 "C610":("Libération du nerf médian dans le syndrome du canal carpien","canal carpien CTS nerf médian décompression main"),
 "C218":("Exérèse totale d’une ou plusieurs gaines synoviales","synovectomie gaine tendon fléchisseur extenseur"),
 "N109":("Traitement d’une lésion du pivot central du genou avec autogreffe","LCA LCP ligament croisé antérieur postérieur reconstruction ligamentoplastie"),
 "N111":("Méniscectomie, quelle que soit la technique, arthroscopie éventuelle incluse","ménisque meniscectomie genou chirurgie sport"),
 "N117":("Arthroplastie intéressant le fémur et le bassin","PTH prothèse hanche arthroplastie"),
 "N127":("Prothèse totale du genou","PTG prothèse totale genou remplacement gonarthrose"),
 "N128":("Réparation des ruptures du tendon d’Achille ou du tendon rotulien","tendon achille rotulien réparation rupture"),
 "G132":("Doigt à ressort","doigt à ressaut trigger finger main"),
 "A130":("Humérus — fracture articulaire : unifragmentaire","fracture humérus épaule ostéosynthèse"),
 "A131":("Humérus — fracture articulaire : multifragmentaire","fracture humérus épaule ostéosynthèse"),
 "A139":("Tibia — fracture articulaire : unifragmentaire","fracture tibia plateau tibial ostéosynthèse"),
 "A140":("Tibia — fracture articulaire : multifragmentaire","fracture tibia plateau tibial ostéosynthèse"),
 "A142":("Fémur — fracture parcellaire extra-articulaire","fracture fémur ostéosynthèse"),
 "A143":("Fémur — fracture diaphysaire","fracture fémur diaphyse ostéosynthèse clou centromédullaire"),
 "A144":("Fémur — fracture de l’extrémité supérieure","fracture fémur proximale hanche ostéosynthèse"),
 "A145":("Fémur — fracture de l’extrémité inférieure : unifragmentaire","fracture fémur distale genou ostéosynthèse"),
 "A146":("Fémur — fracture de l’extrémité inférieure : multifragmentaire","fracture fémur distale genou ostéosynthèse"),
 "A150":("Bassin — fractures transcotyloïdiennes","fracture bassin cotyle acetabulum"),
 "A151":("Bassin — fracture transcotyloïdienne : un pilier","fracture bassin cotyle acetabulum ostéosynthèse"),
 "A152":("Bassin — fracture transcotyloïdienne : deux piliers","fracture bassin cotyle acetabulum ostéosynthèse"),
}
tags = {
 "A100":"fracture immobilisation main poignet avant-bras clavicule pied péroné",
 "A101":"fracture coude bras épaule genou tibia jambe réduction immobilisation",
 "A102":"fracture rachis hanche cuisse",
 "A103":"fracture main poignet styloïde radius ulna cubitus",
 "A104":"fracture avant-bras radius ulna cubitus",
 "A105":"fracture deux os avant-bras radius ulna",
 "A106":"fracture humérus bras", "A107":"fracture clavicule",
 "A108":"fracture omoplate scapula", "A109":"fracture avant-pied métatarse tarse",
 "A110":"fracture astragale talus calcanéum", "A111":"fracture malléole cheville",
 "A112":"fracture bimalléolaire cheville", "A113":"fracture jambe tibia péroné",
 "A114":"fracture rotule patella", "A115":"fracture fémur cuisse",
 "A116":"fracture rachis colonne vertébrale", "A117":"fracture hanche", "A118":"fracture cotyle bassin acetabulum",
 "A119":"fracture bassin", "C609":"canal carpien CTS nerf médian", "C610":"canal carpien CTS nerf médian",
 "C433":"PTH THA prothèse totale de hanche", "C434":"PTG TKA prothèse totale du genou",
 "N109":"LCA ACL ligament croisé antérieur LCP PCL ligamentoplastie genou",
 "N111":"ménisque méniscectomie", "N127":"PTG genou prothèse",
}
records, seen = [], set()
for n, (idx, code, tail) in enumerate(starts):
    end = starts[n + 1][0] if n + 1 < len(starts) else len(normalized)
    block, coeffs, stopped = [], [], False
    if tail:
        before, vals = split_coeff(tail)
        if vals:
            if before: block.append(before)
            coeffs, stopped = vals, True
        else: block.append(tail)
    if not stopped:
        for s in normalized[idx + 1:end]:
            if not s: continue
            if re.match(r"^(Article\s|Chapitre\s|Titre\s|Section\s|Annexe\b|Nota\.?\s)", s, re.I) and block: break
            before, vals = split_coeff(s)
            if vals:
                if before: block.append(before)
                coeffs, stopped = vals, True
                break
            block.append(s)
            if len(block) >= 8: break
    title = re.sub(r"\s+", " ", " ".join(block)).strip(" -:;,.")
    title = re.sub(r"\s+(?:Article\s+\w+|Chapitre\s+\w+|Titre\s+\w+).*$", "", title, flags=re.I)
    if code == "C101" and "Traitement par acupuncture" in title:
        title = title.split("Traitement par acupuncture", 1)[0].strip()
        if not coeffs: coeffs = ["5"]
    if code in ("C609", "C610"): coeffs = ["50"]
    if len(title) > 420: title = title[:417] + "…"
    if code in overrides:
        title = overrides[code][0]
    key = (code, title)
    if key in seen: continue
    seen.add(key)
    numeric = []
    for c in coeffs:
        try: numeric.append(float(c))
        except ValueError: pass
    extra = overrides.get(code, ("",""))[1]
    extra += " " + tags.get(code, "")
    # Add useful generic words without asserting a billing category.
    if code.startswith("A"): extra += " fracture traumatisme orthopédie ostéosynthèse immobilisation"
    elif code.startswith("C") or code.startswith("N"): extra += " chirurgie opératoire orthopédie traumatologie"
    terms = " ".join([code, title, extra, " ".join(coeffs)]).strip()
    records.append({
      "code":code, "title":title or "Libellé à vérifier dans le PDF",
      "coeffs":coeffs, "coeffText":coeffs, "coef":numeric[0] if numeric else None,
      "secondary":coeffs[1] if len(coeffs)>1 else None, "key":"K",
      "source_line":idx+1, "terms":terms,
      "note":"Référence extraite du texte du PDF NGAP marocain fourni. Vérifier le libellé exact, la lettre-clé, les règles de cumul et la cotation applicable avant facturation."
    })
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("Catalogue construit :", len(records), "références ;", len({r['code'] for r in records}), "codes distincts.")
