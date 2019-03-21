import json

from questionary_service.encoder.mongo_serializer import JSONEncoder

from questionary_service.controller.base import BaseHandler


class QuestionaryHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    async def get(self, id):
        db = self.settings['db']

        questionary_doc = await db.questionary.find_one(
            {"patient_id": id}
        )
        if questionary_doc:
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(JSONEncoder().encode(questionary_doc))
            return

        self.write_error(status_code=404)

    async def post(self, *args, **kwargs):
        inc_body = self.request.body.decode('utf-8')

        db = self.settings['db']
        questionary_dict = json.loads(inc_body)

        msg_failed = {
            "created": False,
            "msg": "Could not create questionary."
        }
        msg_success = {
            "created": True,
            "msg": "Successfully created questionary."
        }
        self.set_header("Access-Control-Allow-Origin", "*")
        try:
            created_questionary = await db.questionary.insert_one(
                questionary_dict
            )
            if created_questionary:
                self.write(msg_success)
            else:
                self.write(msg_failed)
        except Exception:
            self.write(msg_failed)


