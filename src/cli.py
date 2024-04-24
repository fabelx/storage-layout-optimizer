import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path

from sl_optimizer import LayoutError, new_storage_layout

VERSION = "v0.0.4"
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%I:%M:%S',
    level=logging.INFO
)


def log_fatal(message: str):
    logger.error(message)
    exit(1)


def cli(parser: ArgumentParser) -> Namespace:
    parser.add_argument(
        "filepath",
        type=Path,
        help="""path to the JSON file containing a storage layout, 
        which can be obtained using the `solc --storage-layout -o output Contract.sol` command.""",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="fl",
        dest="output",
        type=Path,
        default=Path("optimized_storage_layout.json"),
        required=False,
        help="""path to the file where the data will be saved. Default: optimized_storage_layout.json.""",
    )
    parser.add_argument(
        "-f",
        "--force-save",
        dest="force",
        action="store_true",
        default=False,
        required=False,
        help="""if True, overwrite the file even if it already exists.""",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=VERSION,
        help="""returns the version.""",
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        default=False,
        required=False,
        help="""suppress logs.""",
    )
    return parser.parse_args()


def main():
    parser = ArgumentParser(
        description="A Python cli tool designed to optimize the storage layout for Solidity smart contracts."
    )
    args = cli(parser)
    if args.silent:
        logger.setLevel(logging.ERROR)

    if not args.filepath.exists():
        log_fatal(f"Error: File not found: {args.filepath}.")

    if not args.force and args.output.exists():
        log_fatal(
            f"Error: Output file: '{args.output}' already exists, to overwrite use '-f' flag."
        )

    if args.filepath == args.output:
        log_fatal(f"Error: The input file cannot be equal to the output file.")
    try:
        sl = new_storage_layout(filepath=args.filepath)
    except ValueError:
        log_fatal(
            f"Error: JSON decoding failed. "
            f"The system encountered an issue while attempting to decode the JSON data. "
            f"Please check the validity of the JSON input and ensure it adheres to the correct syntax."
        )
    except LayoutError as e:
        log_fatal(f"Error: {e}")

    logger.info(f"Optimizing {sl.contract_name} smart contact.")
    osl = sl.optimize()
    logger.info(f"Slot usage decreased by: {(1 - osl.number_of_slots / sl.number_of_slots) * 100:.2f}%")
    logger.info(f"Saving to {args.output} ...")
    osl.save(filepath=args.output, force=args.force)
    logger.info("Done.")


if __name__ == "__main__":
    main()
