# coding: utf-8

"""
    리로스쿨 API

    리로스쿨 2.9 버전의 API  # noqa: E501

    OpenAPI spec version: 2.9.0
    Contact: develop@rirosoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Member(object):
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
        'uuid': 'str',
        'fcm_code': 'str',
        'version': 'str',
        'id': 'str',
        'password': 'str',
        'phone': 'str',
        'name': 'str',
        'sex': 'str',
        'me_verified': 'bool',
        'birth': 'str',
        'nation': 'str',
        'ci': 'str',
        'child_name': 'str',
        'site_id': 'str',
        'parent': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'fcm_code': 'fcmCode',
        'version': 'version',
        'id': 'id',
        'password': 'password',
        'phone': 'phone',
        'name': 'name',
        'sex': 'sex',
        'me_verified': 'meVerified',
        'birth': 'birth',
        'nation': 'nation',
        'ci': 'ci',
        'child_name': 'childName',
        'site_id': 'siteId',
        'parent': 'parent'
    }

    def __init__(self, uuid=None, fcm_code=None, version=None, id=None, password=None, phone=None, name=None, sex=None, me_verified=None, birth=None, nation=None, ci=None, child_name=None, site_id=None, parent=None):  # noqa: E501
        """Member - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._fcm_code = None
        self._version = None
        self._id = None
        self._password = None
        self._phone = None
        self._name = None
        self._sex = None
        self._me_verified = None
        self._birth = None
        self._nation = None
        self._ci = None
        self._child_name = None
        self._site_id = None
        self._parent = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if fcm_code is not None:
            self.fcm_code = fcm_code
        if version is not None:
            self.version = version
        if id is not None:
            self.id = id
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if name is not None:
            self.name = name
        if sex is not None:
            self.sex = sex
        if me_verified is not None:
            self.me_verified = me_verified
        if birth is not None:
            self.birth = birth
        if nation is not None:
            self.nation = nation
        if ci is not None:
            self.ci = ci
        if child_name is not None:
            self.child_name = child_name
        if site_id is not None:
            self.site_id = site_id
        if parent is not None:
            self.parent = parent

    @property
    def uuid(self):
        """Gets the uuid of this Member.  # noqa: E501


        :return: The uuid of this Member.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Member.


        :param uuid: The uuid of this Member.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def fcm_code(self):
        """Gets the fcm_code of this Member.  # noqa: E501


        :return: The fcm_code of this Member.  # noqa: E501
        :rtype: str
        """
        return self._fcm_code

    @fcm_code.setter
    def fcm_code(self, fcm_code):
        """Sets the fcm_code of this Member.


        :param fcm_code: The fcm_code of this Member.  # noqa: E501
        :type: str
        """

        self._fcm_code = fcm_code

    @property
    def version(self):
        """Gets the version of this Member.  # noqa: E501


        :return: The version of this Member.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Member.


        :param version: The version of this Member.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def id(self):
        """Gets the id of this Member.  # noqa: E501


        :return: The id of this Member.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.


        :param id: The id of this Member.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def password(self):
        """Gets the password of this Member.  # noqa: E501


        :return: The password of this Member.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Member.


        :param password: The password of this Member.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this Member.  # noqa: E501


        :return: The phone of this Member.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Member.


        :param phone: The phone of this Member.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def name(self):
        """Gets the name of this Member.  # noqa: E501


        :return: The name of this Member.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Member.


        :param name: The name of this Member.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sex(self):
        """Gets the sex of this Member.  # noqa: E501


        :return: The sex of this Member.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this Member.


        :param sex: The sex of this Member.  # noqa: E501
        :type: str
        """

        self._sex = sex

    @property
    def me_verified(self):
        """Gets the me_verified of this Member.  # noqa: E501


        :return: The me_verified of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._me_verified

    @me_verified.setter
    def me_verified(self, me_verified):
        """Sets the me_verified of this Member.


        :param me_verified: The me_verified of this Member.  # noqa: E501
        :type: bool
        """

        self._me_verified = me_verified

    @property
    def birth(self):
        """Gets the birth of this Member.  # noqa: E501


        :return: The birth of this Member.  # noqa: E501
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this Member.


        :param birth: The birth of this Member.  # noqa: E501
        :type: str
        """

        self._birth = birth

    @property
    def nation(self):
        """Gets the nation of this Member.  # noqa: E501


        :return: The nation of this Member.  # noqa: E501
        :rtype: str
        """
        return self._nation

    @nation.setter
    def nation(self, nation):
        """Sets the nation of this Member.


        :param nation: The nation of this Member.  # noqa: E501
        :type: str
        """

        self._nation = nation

    @property
    def ci(self):
        """Gets the ci of this Member.  # noqa: E501


        :return: The ci of this Member.  # noqa: E501
        :rtype: str
        """
        return self._ci

    @ci.setter
    def ci(self, ci):
        """Sets the ci of this Member.


        :param ci: The ci of this Member.  # noqa: E501
        :type: str
        """

        self._ci = ci

    @property
    def child_name(self):
        """Gets the child_name of this Member.  # noqa: E501


        :return: The child_name of this Member.  # noqa: E501
        :rtype: str
        """
        return self._child_name

    @child_name.setter
    def child_name(self, child_name):
        """Sets the child_name of this Member.


        :param child_name: The child_name of this Member.  # noqa: E501
        :type: str
        """

        self._child_name = child_name

    @property
    def site_id(self):
        """Gets the site_id of this Member.  # noqa: E501


        :return: The site_id of this Member.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Member.


        :param site_id: The site_id of this Member.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def parent(self):
        """Gets the parent of this Member.  # noqa: E501


        :return: The parent of this Member.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Member.


        :param parent: The parent of this Member.  # noqa: E501
        :type: str
        """

        self._parent = parent

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
        if issubclass(Member, dict):
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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other