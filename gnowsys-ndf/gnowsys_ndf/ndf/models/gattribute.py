from base_imports import *
from triple import *


class GAttribute(Triple):
    
    attribute_type_scope=DictField(),
    # 'attribute_type': AttributeType,  # Embedded document of AttributeType Class
    attribute_type=ObjectIdField(required=True),  # ObjectId of AttributeType node
    # 'object_value_scope': basestring,
    object_value=StringField(required = True)  # value -- it's data-type, is determined by attribute_type field

    meta = {

        'use_dot_notation' : True,
        'use_autorefs' : True,                   # To support Embedding of Documents

        'indexes' : [
            {
                # 1: Compound index
                    'fields': [
                    '_type','subject','attribute_type','status'
                ],
                'check': False  # Required because $id is not explicitly specified in the structure
            }
        ]
    }
    # required_fields = ['attribute_type', 'object_value']
        # default_values = {
    #                     'attribute_type_scope': {}
    #                 }

