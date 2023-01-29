from django.core.management.base import BaseCommand
import pandas as pd
from dv1.settings import BASE_DIR


def test():
    df = pd.read_csv(BASE_DIR.parent / "data/brand.csv")
    print(df)
    # print(BASE_DIR)
    # print(type(BASE_DIR))


class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        test()
