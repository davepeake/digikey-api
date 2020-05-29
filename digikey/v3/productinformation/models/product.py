# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: v3
    Contact: api.support@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Product(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'standard_pricing': 'list[PriceBreak]',
        'ro_hs_status': 'str',
        'lead_status': 'str',
        'parameters': 'list[PidVid]',
        'product_url': 'str',
        'primary_datasheet': 'str',
        'primary_photo': 'str',
        'primary_video': 'str',
        'series': 'PidVid',
        'manufacturer_lead_weeks': 'str',
        'manufacturer_page_url': 'str',
        'product_status': 'str',
        'date_last_buy_chance': 'datetime',
        'alternate_packaging': 'list[BasicProduct]',
        'detailed_description': 'str',
        'tariff_description': 'str',
        'manufacturer_part_number': 'str',
        'minimum_order_quantity': 'int',
        'non_stock': 'bool',
        'packaging': 'PidVid',
        'quantity_available': 'int',
        'digi_key_part_number': 'str',
        'product_description': 'str',
        'unit_price': 'float',
        'manufacturer': 'PidVid',
        'manufacturer_public_quantity': 'int',
        'quantity_on_order': 'int',
        'dk_plus_restriction': 'bool',
        'supplier_direct_ship': 'bool'
    }

    attribute_map = {
        'standard_pricing': 'StandardPricing',
        'ro_hs_status': 'RoHSStatus',
        'lead_status': 'LeadStatus',
        'parameters': 'Parameters',
        'product_url': 'ProductUrl',
        'primary_datasheet': 'PrimaryDatasheet',
        'primary_photo': 'PrimaryPhoto',
        'primary_video': 'PrimaryVideo',
        'series': 'Series',
        'manufacturer_lead_weeks': 'ManufacturerLeadWeeks',
        'manufacturer_page_url': 'ManufacturerPageUrl',
        'product_status': 'ProductStatus',
        'date_last_buy_chance': 'DateLastBuyChance',
        'alternate_packaging': 'AlternatePackaging',
        'detailed_description': 'DetailedDescription',
        'tariff_description': 'TariffDescription',
        'manufacturer_part_number': 'ManufacturerPartNumber',
        'minimum_order_quantity': 'MinimumOrderQuantity',
        'non_stock': 'NonStock',
        'packaging': 'Packaging',
        'quantity_available': 'QuantityAvailable',
        'digi_key_part_number': 'DigiKeyPartNumber',
        'product_description': 'ProductDescription',
        'unit_price': 'UnitPrice',
        'manufacturer': 'Manufacturer',
        'manufacturer_public_quantity': 'ManufacturerPublicQuantity',
        'quantity_on_order': 'QuantityOnOrder',
        'dk_plus_restriction': 'DKPlusRestriction',
        'supplier_direct_ship': 'SupplierDirectShip'
    }

    def __init__(self, standard_pricing=None, ro_hs_status=None, lead_status=None, parameters=None, product_url=None, primary_datasheet=None, primary_photo=None, primary_video=None, series=None, manufacturer_lead_weeks=None, manufacturer_page_url=None, product_status=None, date_last_buy_chance=None, alternate_packaging=None, detailed_description=None, tariff_description=None, manufacturer_part_number=None, minimum_order_quantity=None, non_stock=None, packaging=None, quantity_available=None, digi_key_part_number=None, product_description=None, unit_price=None, manufacturer=None, manufacturer_public_quantity=None, quantity_on_order=None, dk_plus_restriction=None, supplier_direct_ship=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501

        self._standard_pricing = None
        self._ro_hs_status = None
        self._lead_status = None
        self._parameters = None
        self._product_url = None
        self._primary_datasheet = None
        self._primary_photo = None
        self._primary_video = None
        self._series = None
        self._manufacturer_lead_weeks = None
        self._manufacturer_page_url = None
        self._product_status = None
        self._date_last_buy_chance = None
        self._alternate_packaging = None
        self._detailed_description = None
        self._tariff_description = None
        self._manufacturer_part_number = None
        self._minimum_order_quantity = None
        self._non_stock = None
        self._packaging = None
        self._quantity_available = None
        self._digi_key_part_number = None
        self._product_description = None
        self._unit_price = None
        self._manufacturer = None
        self._manufacturer_public_quantity = None
        self._quantity_on_order = None
        self._dk_plus_restriction = None
        self._supplier_direct_ship = None
        self.discriminator = None

        if standard_pricing is not None:
            self.standard_pricing = standard_pricing
        if ro_hs_status is not None:
            self.ro_hs_status = ro_hs_status
        if lead_status is not None:
            self.lead_status = lead_status
        if parameters is not None:
            self.parameters = parameters
        if product_url is not None:
            self.product_url = product_url
        if primary_datasheet is not None:
            self.primary_datasheet = primary_datasheet
        if primary_photo is not None:
            self.primary_photo = primary_photo
        if primary_video is not None:
            self.primary_video = primary_video
        if series is not None:
            self.series = series
        if manufacturer_lead_weeks is not None:
            self.manufacturer_lead_weeks = manufacturer_lead_weeks
        if manufacturer_page_url is not None:
            self.manufacturer_page_url = manufacturer_page_url
        if product_status is not None:
            self.product_status = product_status
        if date_last_buy_chance is not None:
            self.date_last_buy_chance = date_last_buy_chance
        if alternate_packaging is not None:
            self.alternate_packaging = alternate_packaging
        if detailed_description is not None:
            self.detailed_description = detailed_description
        if tariff_description is not None:
            self.tariff_description = tariff_description
        if manufacturer_part_number is not None:
            self.manufacturer_part_number = manufacturer_part_number
        if minimum_order_quantity is not None:
            self.minimum_order_quantity = minimum_order_quantity
        if non_stock is not None:
            self.non_stock = non_stock
        if packaging is not None:
            self.packaging = packaging
        if quantity_available is not None:
            self.quantity_available = quantity_available
        if digi_key_part_number is not None:
            self.digi_key_part_number = digi_key_part_number
        if product_description is not None:
            self.product_description = product_description
        if unit_price is not None:
            self.unit_price = unit_price
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_public_quantity is not None:
            self.manufacturer_public_quantity = manufacturer_public_quantity
        if quantity_on_order is not None:
            self.quantity_on_order = quantity_on_order
        if dk_plus_restriction is not None:
            self.dk_plus_restriction = dk_plus_restriction
        if supplier_direct_ship is not None:
            self.supplier_direct_ship = supplier_direct_ship

    @property
    def standard_pricing(self):
        """Gets the standard_pricing of this Product.  # noqa: E501

        Standard pricing for the validated locale.  # noqa: E501

        :return: The standard_pricing of this Product.  # noqa: E501
        :rtype: list[PriceBreak]
        """
        return self._standard_pricing

    @standard_pricing.setter
    def standard_pricing(self, standard_pricing):
        """Sets the standard_pricing of this Product.

        Standard pricing for the validated locale.  # noqa: E501

        :param standard_pricing: The standard_pricing of this Product.  # noqa: E501
        :type: list[PriceBreak]
        """

        self._standard_pricing = standard_pricing

    @property
    def ro_hs_status(self):
        """Gets the ro_hs_status of this Product.  # noqa: E501

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :return: The ro_hs_status of this Product.  # noqa: E501
        :rtype: str
        """
        return self._ro_hs_status

    @ro_hs_status.setter
    def ro_hs_status(self, ro_hs_status):
        """Sets the ro_hs_status of this Product.

        RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant.  # noqa: E501

        :param ro_hs_status: The ro_hs_status of this Product.  # noqa: E501
        :type: str
        """

        self._ro_hs_status = ro_hs_status

    @property
    def lead_status(self):
        """Gets the lead_status of this Product.  # noqa: E501

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :return: The lead_status of this Product.  # noqa: E501
        :rtype: str
        """
        return self._lead_status

    @lead_status.setter
    def lead_status(self, lead_status):
        """Sets the lead_status of this Product.

        Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification.  # noqa: E501

        :param lead_status: The lead_status of this Product.  # noqa: E501
        :type: str
        """

        self._lead_status = lead_status

    @property
    def parameters(self):
        """Gets the parameters of this Product.  # noqa: E501

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :return: The parameters of this Product.  # noqa: E501
        :rtype: list[PidVid]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Product.

        Parameters for the part. Can be used for filtering keyword searches.  # noqa: E501

        :param parameters: The parameters of this Product.  # noqa: E501
        :type: list[PidVid]
        """

        self._parameters = parameters

    @property
    def product_url(self):
        """Gets the product_url of this Product.  # noqa: E501

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :return: The product_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """Sets the product_url of this Product.

        Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values.  # noqa: E501

        :param product_url: The product_url of this Product.  # noqa: E501
        :type: str
        """

        self._product_url = product_url

    @property
    def primary_datasheet(self):
        """Gets the primary_datasheet of this Product.  # noqa: E501

        The URL to the product's datasheet.  # noqa: E501

        :return: The primary_datasheet of this Product.  # noqa: E501
        :rtype: str
        """
        return self._primary_datasheet

    @primary_datasheet.setter
    def primary_datasheet(self, primary_datasheet):
        """Sets the primary_datasheet of this Product.

        The URL to the product's datasheet.  # noqa: E501

        :param primary_datasheet: The primary_datasheet of this Product.  # noqa: E501
        :type: str
        """

        self._primary_datasheet = primary_datasheet

    @property
    def primary_photo(self):
        """Gets the primary_photo of this Product.  # noqa: E501

        The URL to the product's image.  # noqa: E501

        :return: The primary_photo of this Product.  # noqa: E501
        :rtype: str
        """
        return self._primary_photo

    @primary_photo.setter
    def primary_photo(self, primary_photo):
        """Sets the primary_photo of this Product.

        The URL to the product's image.  # noqa: E501

        :param primary_photo: The primary_photo of this Product.  # noqa: E501
        :type: str
        """

        self._primary_photo = primary_photo

    @property
    def primary_video(self):
        """Gets the primary_video of this Product.  # noqa: E501

        The URL to the product's video.  # noqa: E501

        :return: The primary_video of this Product.  # noqa: E501
        :rtype: str
        """
        return self._primary_video

    @primary_video.setter
    def primary_video(self, primary_video):
        """Sets the primary_video of this Product.

        The URL to the product's video.  # noqa: E501

        :param primary_video: The primary_video of this Product.  # noqa: E501
        :type: str
        """

        self._primary_video = primary_video

    @property
    def series(self):
        """Gets the series of this Product.  # noqa: E501


        :return: The series of this Product.  # noqa: E501
        :rtype: PidVid
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this Product.


        :param series: The series of this Product.  # noqa: E501
        :type: PidVid
        """

        self._series = series

    @property
    def manufacturer_lead_weeks(self):
        """Gets the manufacturer_lead_weeks of this Product.  # noqa: E501

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :return: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_lead_weeks

    @manufacturer_lead_weeks.setter
    def manufacturer_lead_weeks(self, manufacturer_lead_weeks):
        """Sets the manufacturer_lead_weeks of this Product.

        The number of weeks expected to receive stock from manufacturer.  # noqa: E501

        :param manufacturer_lead_weeks: The manufacturer_lead_weeks of this Product.  # noqa: E501
        :type: str
        """

        self._manufacturer_lead_weeks = manufacturer_lead_weeks

    @property
    def manufacturer_page_url(self):
        """Gets the manufacturer_page_url of this Product.  # noqa: E501

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :return: The manufacturer_page_url of this Product.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_page_url

    @manufacturer_page_url.setter
    def manufacturer_page_url(self, manufacturer_page_url):
        """Sets the manufacturer_page_url of this Product.

        The URL to Digi-Key's page on the manufacturer.  # noqa: E501

        :param manufacturer_page_url: The manufacturer_page_url of this Product.  # noqa: E501
        :type: str
        """

        self._manufacturer_page_url = manufacturer_page_url

    @property
    def product_status(self):
        """Gets the product_status of this Product.  # noqa: E501

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :return: The product_status of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_status

    @product_status.setter
    def product_status(self, product_status):
        """Sets the product_status of this Product.

        Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity.  # noqa: E501

        :param product_status: The product_status of this Product.  # noqa: E501
        :type: str
        """

        self._product_status = product_status

    @property
    def date_last_buy_chance(self):
        """Gets the date_last_buy_chance of this Product.  # noqa: E501

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :return: The date_last_buy_chance of this Product.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_buy_chance

    @date_last_buy_chance.setter
    def date_last_buy_chance(self, date_last_buy_chance):
        """Sets the date_last_buy_chance of this Product.

        Last date that the product will be available for purchase. Date is in ISO 8601.  # noqa: E501

        :param date_last_buy_chance: The date_last_buy_chance of this Product.  # noqa: E501
        :type: datetime
        """

        self._date_last_buy_chance = date_last_buy_chance

    @property
    def alternate_packaging(self):
        """Gets the alternate_packaging of this Product.  # noqa: E501

        Other packaging types available for this product.  # noqa: E501

        :return: The alternate_packaging of this Product.  # noqa: E501
        :rtype: list[BasicProduct]
        """
        return self._alternate_packaging

    @alternate_packaging.setter
    def alternate_packaging(self, alternate_packaging):
        """Sets the alternate_packaging of this Product.

        Other packaging types available for this product.  # noqa: E501

        :param alternate_packaging: The alternate_packaging of this Product.  # noqa: E501
        :type: list[BasicProduct]
        """

        self._alternate_packaging = alternate_packaging

    @property
    def detailed_description(self):
        """Gets the detailed_description of this Product.  # noqa: E501

        Extended catalog description of the product.  # noqa: E501

        :return: The detailed_description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._detailed_description

    @detailed_description.setter
    def detailed_description(self, detailed_description):
        """Sets the detailed_description of this Product.

        Extended catalog description of the product.  # noqa: E501

        :param detailed_description: The detailed_description of this Product.  # noqa: E501
        :type: str
        """

        self._detailed_description = detailed_description

    @property
    def tariff_description(self):
        """Gets the tariff_description of this Product.  # noqa: E501

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :return: The tariff_description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._tariff_description

    @tariff_description.setter
    def tariff_description(self, tariff_description):
        """Sets the tariff_description of this Product.

        Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied.  # noqa: E501

        :param tariff_description: The tariff_description of this Product.  # noqa: E501
        :type: str
        """

        self._tariff_description = tariff_description

    @property
    def manufacturer_part_number(self):
        """Gets the manufacturer_part_number of this Product.  # noqa: E501

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :return: The manufacturer_part_number of this Product.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_part_number

    @manufacturer_part_number.setter
    def manufacturer_part_number(self, manufacturer_part_number):
        """Sets the manufacturer_part_number of this Product.

        The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts.  # noqa: E501

        :param manufacturer_part_number: The manufacturer_part_number of this Product.  # noqa: E501
        :type: str
        """

        self._manufacturer_part_number = manufacturer_part_number

    @property
    def minimum_order_quantity(self):
        """Gets the minimum_order_quantity of this Product.  # noqa: E501

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :return: The minimum_order_quantity of this Product.  # noqa: E501
        :rtype: int
        """
        return self._minimum_order_quantity

    @minimum_order_quantity.setter
    def minimum_order_quantity(self, minimum_order_quantity):
        """Sets the minimum_order_quantity of this Product.

        The minimum quantity to order from Digi-Key.  # noqa: E501

        :param minimum_order_quantity: The minimum_order_quantity of this Product.  # noqa: E501
        :type: int
        """

        self._minimum_order_quantity = minimum_order_quantity

    @property
    def non_stock(self):
        """Gets the non_stock of this Product.  # noqa: E501

        Indicates this product is a non stock product.  # noqa: E501

        :return: The non_stock of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._non_stock

    @non_stock.setter
    def non_stock(self, non_stock):
        """Sets the non_stock of this Product.

        Indicates this product is a non stock product.  # noqa: E501

        :param non_stock: The non_stock of this Product.  # noqa: E501
        :type: bool
        """

        self._non_stock = non_stock

    @property
    def packaging(self):
        """Gets the packaging of this Product.  # noqa: E501


        :return: The packaging of this Product.  # noqa: E501
        :rtype: PidVid
        """
        return self._packaging

    @packaging.setter
    def packaging(self, packaging):
        """Sets the packaging of this Product.


        :param packaging: The packaging of this Product.  # noqa: E501
        :type: PidVid
        """

        self._packaging = packaging

    @property
    def quantity_available(self):
        """Gets the quantity_available of this Product.  # noqa: E501

        Quantity of the product available for immediate sale.  # noqa: E501

        :return: The quantity_available of this Product.  # noqa: E501
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """Sets the quantity_available of this Product.

        Quantity of the product available for immediate sale.  # noqa: E501

        :param quantity_available: The quantity_available of this Product.  # noqa: E501
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def digi_key_part_number(self):
        """Gets the digi_key_part_number of this Product.  # noqa: E501

        The Digi-Key part number.  # noqa: E501

        :return: The digi_key_part_number of this Product.  # noqa: E501
        :rtype: str
        """
        return self._digi_key_part_number

    @digi_key_part_number.setter
    def digi_key_part_number(self, digi_key_part_number):
        """Sets the digi_key_part_number of this Product.

        The Digi-Key part number.  # noqa: E501

        :param digi_key_part_number: The digi_key_part_number of this Product.  # noqa: E501
        :type: str
        """

        self._digi_key_part_number = digi_key_part_number

    @property
    def product_description(self):
        """Gets the product_description of this Product.  # noqa: E501

        Catalog description of the product.  # noqa: E501

        :return: The product_description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this Product.

        Catalog description of the product.  # noqa: E501

        :param product_description: The product_description of this Product.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def unit_price(self):
        """Gets the unit_price of this Product.  # noqa: E501

        The price for a single unit of this product.  # noqa: E501

        :return: The unit_price of this Product.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this Product.

        The price for a single unit of this product.  # noqa: E501

        :param unit_price: The unit_price of this Product.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def manufacturer(self):
        """Gets the manufacturer of this Product.  # noqa: E501


        :return: The manufacturer of this Product.  # noqa: E501
        :rtype: PidVid
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this Product.


        :param manufacturer: The manufacturer of this Product.  # noqa: E501
        :type: PidVid
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_public_quantity(self):
        """Gets the manufacturer_public_quantity of this Product.  # noqa: E501

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :return: The manufacturer_public_quantity of this Product.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_public_quantity

    @manufacturer_public_quantity.setter
    def manufacturer_public_quantity(self, manufacturer_public_quantity):
        """Sets the manufacturer_public_quantity of this Product.

        Quantity of this product available to order from manufacturer.  # noqa: E501

        :param manufacturer_public_quantity: The manufacturer_public_quantity of this Product.  # noqa: E501
        :type: int
        """

        self._manufacturer_public_quantity = manufacturer_public_quantity

    @property
    def quantity_on_order(self):
        """Gets the quantity_on_order of this Product.  # noqa: E501

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :return: The quantity_on_order of this Product.  # noqa: E501
        :rtype: int
        """
        return self._quantity_on_order

    @quantity_on_order.setter
    def quantity_on_order(self, quantity_on_order):
        """Sets the quantity_on_order of this Product.

        Quantity of this product ordered but not immediately available.  # noqa: E501

        :param quantity_on_order: The quantity_on_order of this Product.  # noqa: E501
        :type: int
        """

        self._quantity_on_order = quantity_on_order

    @property
    def dk_plus_restriction(self):
        """Gets the dk_plus_restriction of this Product.  # noqa: E501

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :return: The dk_plus_restriction of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._dk_plus_restriction

    @dk_plus_restriction.setter
    def dk_plus_restriction(self, dk_plus_restriction):
        """Sets the dk_plus_restriction of this Product.

        If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site  # noqa: E501

        :param dk_plus_restriction: The dk_plus_restriction of this Product.  # noqa: E501
        :type: bool
        """

        self._dk_plus_restriction = dk_plus_restriction

    @property
    def supplier_direct_ship(self):
        """Gets the supplier_direct_ship of this Product.  # noqa: E501

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :return: The supplier_direct_ship of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._supplier_direct_ship

    @supplier_direct_ship.setter
    def supplier_direct_ship(self, supplier_direct_ship):
        """Sets the supplier_direct_ship of this Product.

        If true- this product is shipped directly from the Supplier  # noqa: E501

        :param supplier_direct_ship: The supplier_direct_ship of this Product.  # noqa: E501
        :type: bool
        """

        self._supplier_direct_ship = supplier_direct_ship

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Product, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
