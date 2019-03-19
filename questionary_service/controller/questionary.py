import pprint

from questionary_service.encoder.mongo_serializer import JSONEncoder

from questionary_service.controller.base import BaseHandler


class QuestionaryHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    async def get(self, id):
        db = self.settings['db']
        document = await db.questionary.find_one(
            {"patient_id": id}
        )
        if document:
            self.write(JSONEncoder().encode(document))

        self.write_error(status_code=404)

    '''
    # bulk read
        async def get(self, id):
        db = self.settings['db']
        questionary_cursor = db.questionary.find(
            {"patient_id": id}
        )
        for document in await questionary_cursor.to_list(length=30):
            pprint.pprint(document)
            self.write(JSONEncoder().encode(document))
    '''
