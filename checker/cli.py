import argparse


def read_user_cli_args():
    """
    Handle the CLI arguments and options.
    :return:
    """
    parser = argparse.ArgumentParser(prog="rpchecker", description="check the availability of websites")
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        default=[],
        help="enter one or more website URLs"
    )
    return parser.parse_args()
