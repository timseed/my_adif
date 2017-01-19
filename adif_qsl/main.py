
import yaml
import argparse
import logging
import logging.config
from adif_qsl import QslCard

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Adif QSL Printing')
    parser.add_argument('--infile', type=str, dest='infile',
                        help='Adif with the QSO')
    parser.add_argument('--call', dest='call',
                        help='Call Sign you want to check)')
    args = parser.parse_args()
    if not (args.infile or args.call):
        parser.print_help()
        quit()

    with open('logging.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    logging = logging.getLogger(__name__)
    logging.info("qsl being called using call of {}".format(args.call))
    q = QslCard(args.infile)
    q.qsl(args.call)
