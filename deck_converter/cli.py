"""
The command-line interface for the downloader
"""
import argparse
from .deck_converter import deck_converter


def main():
    parser = argparse.ArgumentParser(
        description="A tool to convert decks from tcg-arena to paste into UVS for competitions."
    )
    parser.add_argument(
        "deck_list_in", type=str,
        help="File path to (and including) the txt file from tcg-arena."
    )
    parser.add_argument(
        "--output", "-o", type=str,
        help=("Destination local file path (and name). If not set, the deck list "
                "will be saved to the current working directory, with filename "
                "uvs")
    )
    args = parser.parse_args()

    if args.output != None:
        deck_converter(args.deck_list_in, args.output)
    else:
        deck_converter(args.deck_list_in)
    print("Save successful! - Github worked")

if __name__ == "__main__":
    main()
