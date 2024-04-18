# Genereted by chatGPT v4.0
import json

# Předpokládáme, že soubor SPD je načten do proměnné `spdx_data`
with open('manifest.spdx.json') as spdx_file:
    spdx_data = json.load(spdx_file)

bom = {
    "bomFormat": "CycloneDX",
    "specVersion": "1.2",
    "version": 1,
    "components": []
}

for package in spdx_data["packages"]:
    component = {
        "type": "library",
        "name": package["name"],
        "version": package.get("versionInfo", "unknown"),
        "purl": package["externalRefs"][0]["referenceLocator"] if package.get("externalRefs") else "unknown"
    }
    bom["components"].append(component)

with open('mpss.cyclonedx.json', 'w') as out_file:
    json.dump(bom, out_file, indent=4)
