import argparse

def main():
    parser = argparse.ArgumentParser(
        prog = "protein-structure-auto-description",
        description = "Automated description generator for protein structures.",
        epilog = "To be added"
    )
    parser.add_argument('-p', '--protein-structure-file', type=str, required=True, help='Path to the protein structure file (PDB format).')
    
    args = parser.parse_args()
    print(f"Processing protein structure file: {args.protein_structure_file}")

if __name__ == "__main__":
    main()