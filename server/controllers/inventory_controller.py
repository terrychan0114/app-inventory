import connexion
from loguru import logger
import six

from server.models.inventory_info import InventoryInfo  # noqa: E501
from server import util
from server.models.database import Database  # noqa: E501

database_object = Database(host='10.10.4.61', user='root', password='adminpwd', db='WorkOrder', charset='utf8mb4')

def add_pn(body):  # noqa: E501
    """Add a new work order to the server

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryInfo.from_dict(connexion.request.get_json())  # noqa: E501
    lot_number = body.lot_number
    quantity = body.quantity
    part_number = body.part_number
    location = body.location
    description = body.description
    status = body.status
    lead_time = body.lead_time
    outside_process = body.outside_process
    remarks = body.remarks

    database_object.open_connection()
    sql_query = "INSERT INTO Paterson_Inventory (part_number,quantity,lot_number,location,description,status,lead_time,outside_process,remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    input = (part_number,quantity,lot_number,location,description,status,lead_time,outside_process,remarks)
    logger.debug(input)
    try:
        database_object.update_data(sql_query,input)
    except:
        logger.error("Unable to add new inventory")
        raise

    sql_query = "SELECT * FROM Paterson_Inventory WHERE lot_number=%s"
    input = lot_number
    logger.debug(input)
    try:
        database_object.fetch_data(sql_query,input)
        logger.info("Successful extraction")
    except:
        logger.error("Data return is empty")
        raise
    return 200


def get_inv():  # noqa: E501
    """Get the information of all inventory

     # noqa: E501


    :rtype: List[InventoryInfo]
    """
    database_object.open_connection()
    sql_query = "SELECT * FROM Paterson_Inventory"
    input = ""
    try:
        data = database_object.fetch_data(sql_query,input)
        logger.info("Successful extraction")
    except:
        logger.error("Data return is empty")
        raise
    if data=={}:
        logger.error("Part number does not exist")
    else:
        logger.debug(data)
    database_object.close_connection()
    return data

def get_ln(lot_number):  # noqa: E501
    """Get the information of a lot number

     # noqa: E501

    :param lot_number: This is the input for getting lot number
    :type lot_number: str

    :rtype: InventoryInfo
    """
    database_object.open_connection()
    sql_query = "SELECT * FROM Paterson_Inventory WHERE lot_number=%s"
    input = lot_number
    try:
        data = database_object.fetch_data(sql_query,input)
        logger.info("Successful extraction")
    except:
        logger.error("Data return is empty")
        raise
    if data=={}:
        logger.error("Part number does not exist")
    else:
        logger.debug(data)
    database_object.close_connection()
    return data


def get_pn(part_number):  # noqa: E501
    """Get the information of a part number

     # noqa: E501

    :param part_number: This is the input
    :type part_number: str

    :rtype: List[InventoryInfo]
    """
    database_object.open_connection()
    sql_query = "SELECT * FROM Paterson_Inventory WHERE part_number=%s"
    input = part_number
    logger.debug(input)
    try:
        data = database_object.fetch_data(sql_query,input)
        logger.info("Successful extraction")
    except:
        logger.error("Data return is empty")
        raise
    if data=={}:
        logger.error("Part number does not exist")
    else:
        logger.debug(data)
    database_object.close_connection()
    return data


def update_pn(body):  # noqa: E501
    """Update a part number

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = InventoryInfo.from_dict(connexion.request.get_json())  # noqa: E501
    lot_number = body.lot_number
    quantity = body.quantity
    part_number = body.part_number
    location = body.location
    description = body.description
    status = body.status
    lead_time = body.lead_time
    outside_process = body.outside_process
    remarks = body.remarks

    database_object.open_connection()
    sql_query = "UPDATE Paterson_Inventory SET quantity=%s, part_number=%s, location=%s, description=%s, status=%s, lead_time=%s, outside_process=%s, remarks=%s WHERE lot_number=%s"
    input = (quantity,part_number,location,description,status,lead_time,outside_process,remarks,lot_number)
    logger.debug(type(input))
    logger.debug(input)
    try:
        database_object.update_data(sql_query,input)
    except:
        logger.error("Unable to update")
        raise

    sql_query = "SELECT * FROM Paterson_Inventory WHERE lot_number=%s"
    input = lot_number
    logger.debug(input)
    try:
        data = database_object.fetch_data(sql_query,input)
        logger.info("Successful extraction")
    except:
        logger.error("Data return is empty")
        raise

    if data[0]["quantity"]==quantity:
        logger.info("Update successful")
    else:
        logger.error("Unsuccessful update")
        return 500
    database_object.close_connection()
    return 200
