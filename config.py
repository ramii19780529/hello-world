# database.py
#
# This module contains the functions that manage all the configuration
# settings and server/member data used by lathremBot.


from database import read, update


def getConfig(configKey):
    """
    This function returns the application level value of a
    configuration setting, or None if the setting does not exist.

    Keyword arguments:
    configKey -- This is the name of the configuration setting.
    """
    sql = """select configValue from config where configKey = %(configKey)s"""
    data = {"configKey": configKey}
    for (value,) in read(sql, data):
        return value
    return None


def setConfig(configKey, configValue):
    """
    This function saves the specified application level value of the
    specified configuration setting to database, or creates a new
    configuration setting if it does not exist.

    Keyword arguments:
    configKey -- This is the name of the configuration setting.
    configValue -- This is the value of the configuration setting.
    """
    sql = ("""insert into config(configKey, configValue) """
           """values(%(configKey)s, %(configValue)s) """
           """on duplicate key update configValue = %(configValue)s""")
    data = {"configKey": configKey, "configValue": configValue}
    update(sql, data)


def getServerConfig(serverId, configKey):
    """
    This function returns the value of a server level configuration
    setting.  If the setting does not exist at the server level, the
    application level value is returned.  If the application level
    configuration setting doesn't exist, None is returned.

    Keyword arguments:
    serverId -- The server id related to the configuration setting.
    configKey -- The name of the configuration setting.
    """
    sql = ("""select configValue from serverConfig """
           """where serverId = %(serverId)s and configKey = %(configKey)s""")
    data = {"serverId": serverId, "configKey": configKey}
    for (value,) in read(sql, data):
        return value
    return getConfig(configKey)


def setServerConfig(serverId, configKey, configValue):
    """
    This function saves the specified value of the specified
    server level configuration setting to database, or creates a new
    server level configuration setting if it does not exist.

    Keyword arguments:
    serverId -- The server id related to the configuration setting.
    configKey -- The name of the configuration setting.
    configValue -- The value of the configuration setting.
    """
    sql = ("""insert into serverConfig(serverId, configKey, configValue) """
           """values(%(serverId)s, %(configKey)s, %(configValue)s) """
           """on duplicate key update configValue = %(configValue)s""")
    data = {"serverId": serverId,
            "configKey": configKey,
            "configValue": configValue}
    update(sql, data)


def getMemberConfig(memberId, configKey):
    """
    This function returns the value of a member level configuration
    setting.  If the setting does not exist at the member level, the
    application level value is returned.  If the application level
    configuration setting doesn't exist, None is returned.

    Keyword arguments:
    memberId -- The member id related to the configuration setting.
    configKey -- The name of the configuration setting.
    """
    sql = ("""select configValue from memberConfig """
           """where memberId = %(memberId)s and configKey = %(configKey)s""")
    data = {"memberId": memberId, "configKey": configKey}
    for (value,) in read(sql, data):
        return value
    return getConfig(configKey)


def setMemberConfig(memberId, configKey, configValue):
    """
    This function saves the specified value of the specified
    member level configuration setting to database, or creates a new
    member level configuration setting if it does not exist.

    Keyword arguments:
    serverId -- The member id related to the configuration setting.
    configKey -- The name of the configuration setting.
    configValue -- The value of the configuration setting.
    """
    sql = ("""insert into memberConfig(memberId, configKey, configValue) """
           """values(%(memberId)s, %(configKey)s, %(configValue)s) """
           """on duplicate key update configValue = %(configValue)s""")
    data = {"memberId": memberId,
            "configKey": configKey,
            "configValue": configValue}
    update(sql, data)
