# -*- coding: utf-8 -*-

from pyramid_oereb.lib.sources import Base
from pyramid_oereb.lib.records.address import AddressRecord


class AddressBaseSource(Base):
    """
    Base class for address sources.

    Attributes:
        records (list of pyramid_oereb.lib.records.address.AddressRecord): List of address records.
    """
    _record_class_ = AddressRecord

    def read(self, street_name, zip_code, street_number):
        """
        Every address source has to implement a read method. This method must accept the three parameters. If
        you want adapt to your own source for addresses, this is the point where to hook in.

        Args:
            street_name (unicode): The name of the street for the desired address.
            zip_code (int): The postal zipcode for the desired address.
            street_number (str): The house or so called street number of the desired address.
        """
        pass  # pragma: no cover
