import connexion
import six

from server.models.inventory_info import InventoryInfo  # noqa: E501
from server import util


def add_pn(body):  # noqa: E501
    """Add a new work order to the server

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_inv():  # noqa: E501
    """Get the information of all inventory

     # noqa: E501


    :rtype: List[InventoryInfo]
    """
    return 'do some magic!'


def get_ln(lot_number):  # noqa: E501
    """Get the information of a lot number

     # noqa: E501

    :param lot_number: This is the input for getting lot number
    :type lot_number: str

    :rtype: InventoryInfo
    """
    return 'do some magic!'


def get_pn(part_number):  # noqa: E501
    """Get the information of a part number

     # noqa: E501

    :param part_number: This is the input
    :type part_number: str

    :rtype: List[InventoryInfo]
    """
    return 'do some magic!'


def update_pn(body):  # noqa: E501
    """Update a part number

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
