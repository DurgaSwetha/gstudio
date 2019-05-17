from base_imports import *


class Benchmark(DynamicDocument):

  objects = models.Manager()

  

  # structure = {
  _type=StringField(),
  name= StringField(required = True),
  time_taken=StringField(),
  parameters=StringField(),
  size_of_parameters=StringField(),
  function_output_length=StringField(),
  calling_url=StringField(),
  last_update= DateTimeField(),
  action= StringField(),
  user= StringField(),
  session_key= StringField(),
  group= StringField(),
  has_data= DictField(),
  locale= StringField()
  # }

  # required_fields = ['name']
  meta = {
    'use_dot_notation' :  True,
  }
  collection_name = 'Benchmarks'
  def __unicode__(self):
    return self._id

  def identity(self):
    return self.__unicode__()


benchmark_collection= db["Benchmarks"]