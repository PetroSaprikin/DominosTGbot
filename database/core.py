from peewee import *

db = SqliteDatabase('shelf_life.db')


class Souses(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


class Cheese(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


class Meat(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


class Vegans(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


class Fish(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


class Significant_other(Model):

    product_name = CharField()
    cooler = CharField()
    defrost = CharField()
    opened = CharField()
    prepared_make_line = CharField()
    prepared_owen = CharField()

    class Meta:
        database = db


Souses.create_table()
Cheese.create_table()
Meat.create_table()
Vegans.create_table()
Fish.create_table()
Significant_other.create_table()
