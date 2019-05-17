from base_imports import *
from attribute_type import *
from relation_type import *


class MetaType(Node):
    """MetaType class: Its members are any of GSystemType, AttributeType,
    RelationType, ProcessType.

    It is used to express the NodeTypes that are part of an
    Application developed using GNOWSYS-Studio. E.g, a GSystemType
    'Page' or 'File' become applications by expressing them as members
    of a MetaType, 'GAPP'.

    """

    # structure = {
    description= StringField(),    # Description (name)
    attribute_type_set= ListField(ReferenceField(AttributeType)),  # Embed list of Attribute Type Class as Documents
    relation_type_set= ListField(ReferenceField(RelationType)),    # Holds list of Relation Types
    parent= ObjectIdField()                      # Foreign key to self
# }
    use_dot_notation = True

