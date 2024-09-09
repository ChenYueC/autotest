from api.meeting_app import App_Meeting_Api
import logging


class Assert_Meeting_App:
    @classmethod
    def add_meeting_assert(cls, token_phone, body, code, msg_expect):
        add_response = App_Meeting_Api.add_meeting(token_phone, body)
        logging.info(f"预期：{msg_expect}\t实际：{add_response.get('message')}")
        assert code == add_response.get("code")
        assert msg_expect in add_response.get("message")

    @classmethod
    def cancel_meeting(cls, token_phone, meeting_id, code, msg):
        cancel_response = App_Meeting_Api.cancel_meeting(token_phone, meeting_id)
        logging.info(f"预期：{msg}\t实际：{cancel_response.get('message')}")
        assert code == cancel_response.get("code")
        assert msg in cancel_response.get("message")

    @classmethod
    def apply_meeting(cls, token_phone, meeting_id, code, msg):
        apply_response = App_Meeting_Api.apply_meeting(token_phone, meeting_id)
        assert code == apply_response.get("code")
        assert msg in apply_response.get("message")

    @classmethod
    def cancel_apply(cls, token_phone, meeting_id, code, msg):
        cancel_response = App_Meeting_Api.cancel_apply(token_phone, meeting_id)
        print(cancel_response)
        assert code == cancel_response.get("code")
        assert msg in cancel_response.get("message")

    @classmethod
    def apply_pass(cls, token_phone, apply_list_id, code, msg):
        pass_response = App_Meeting_Api.apply_pass(token_phone, apply_list_id)
        assert code == pass_response.get("code")
        assert msg in pass_response.get("message")

    @classmethod
    def apply_reject(cls, token_phone, apply_list_id, code, msg):
        reject_response = App_Meeting_Api.apply_reject(token_phone, apply_list_id)
        assert code == reject_response.get("code")
        assert msg in reject_response.get("message")

    @classmethod
    def get_audit_list(cls, token_phone, meeting_id, apply_state, code, msg, user_name):
        list_response = App_Meeting_Api.get_audit_list(token_phone, meeting_id, apply_state)
        assert code == list_response.get("code")
        assert msg in list_response.get("message")
        if len(list_response.get("data").get("data")) > 0:
            assert user_name in list_response.get("data").get("data")[0].get("userName")

    @classmethod
    def get_my_send_meeting_list(cls, token_phone, meeting_state, code, msg, meeting_title):
        my_meeting_response = App_Meeting_Api.get_my_send_meeting_list(token_phone, meeting_state)
        assert code == my_meeting_response.get("code")
        assert msg in my_meeting_response.get("message")
        if len(my_meeting_response.get("data").get("data")) > 0:
            assert meeting_title in my_meeting_response.get("data").get("data")[0].get("meetingTitle")

    @classmethod
    def get_my_apply_meeting_list(cls, token_phone, meeting_state):
        apply_meeting_response = App_Meeting_Api.get_my_apply_meeting_list(token_phone, meeting_state)

    @classmethod
    def get_my_invite_meeting_list(cls, token_phone, invite_state):
        invite_meeting_response = App_Meeting_Api.get_my_apply_meeting_list(token_phone, invite_state)

    @classmethod
    def get_details(cls, token_phone, meeting_id):
        details_response = App_Meeting_Api.get_my_apply_meeting_list(token_phone, meeting_id)
