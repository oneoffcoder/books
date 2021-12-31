from elasticsearch_dsl import Document, Integer, Text

class Person(Document):
    first_name = Text(analyzer='snowball')
    last_name = Text(analyzer='snowball')
    gender = Text(analyzer='snowball')
    age = Integer()

    class Index:
        name = 'person'
        settings = {
          'number_of_shards': 2,
        }

    def save(self, ** kwargs):
        return super(Person, self).save(**kwargs)