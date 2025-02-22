import sys
import json

def convert_spdx_to_cyclonedx(spdx_file, cyclonedx_file):
    # Load the SPDX file (assumed to be in JSON format)


    if '../' in spdx_file or '..\\' in spdx_file:
        raise Exception('Invalid file path')
    with open(spdx_file, 'r') as file:
        spdx_data = json.load(file)
    
    # Create the base structure of the CycloneDX document in JSON format
    cyclonedx_data = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "version": 1,
        "components": []
    }
    
    # Convert components
    for item in spdx_data.get('packages', []):
        component = {
            "type": "library",
            "name": item.get('name'),
            "version": item.get('version'),
            # Add more details as needed
        }
        cyclonedx_data["components"].append(component)
    
    # Save the CycloneDX file in JSON format
    if '../' in cyclonedx_file or '..\\' in cyclonedx_file:
        raise Exception('Invalid file path')
    with open(cyclonedx_file, 'w') as file:
        json.dump(cyclonedx_data, file, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_spdx_file> <output_cyclonedx_file>")
        return
    
    spdx_file = sys.argv[1]
    cyclonedx_file = sys.argv[2]

    convert_spdx_to_cyclonedx(spdx_file, cyclonedx_file)
    print(f"Conversion completed: {cyclonedx_file}")

if __name__ == '__main__':
    main()
