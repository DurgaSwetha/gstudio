from base_imports import *


class Analytics(DynamicDocument):

  objects = models.Manager()

  collection_name = 'analytics_collection'

  
  timestamp=DateTimeField(required = True),
  action=DictField(),
  user=DictField,
  obj=DictField,
  group_id=StringField(),
  session_key=StringField()


  # required_fields = ['timestamp']
  use_dot_notation = True

  def __unicode__(self):
    return self._id

  def identity(self):
    return self.__unicode__()
