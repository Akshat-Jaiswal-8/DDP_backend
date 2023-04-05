from datetime import datetime
from django.db import models
from ninja import ModelSchema, Schema

from ddpui.models.org import Org, OrgSchema
from django.contrib.auth.models import User


class OrgUser(models.Model):
    """a user from a client NGO"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, null=True)
    # todo: add role

    def __str__(self):
        return self.user.email  # pylint: disable=no-member


class OrgUserCreate(Schema):
    """payload to create a new OrgUser"""

    email: str
    password: str


class OrgUserUpdate(Schema):
    """payload to update an existing OrgUser"""

    email: str = None
    active: bool = None


class OrgUserResponse(Schema):
    """structure for returning an OrgUser in an http response"""

    email: str
    org: OrgSchema = None
    active: bool

    @staticmethod
    def from_orguser(orguser: OrgUser):
        """helper to turn an OrgUser into an OrgUserResponse"""
        return OrgUserResponse(
            email=orguser.user.email, org=orguser.org, active=orguser.user.is_active
        )


class Invitation(models.Model):
    """Docstring"""

    invited_email = models.CharField(max_length=50)
    invited_by = models.ForeignKey(OrgUser, on_delete=models.CASCADE)
    invited_on = models.DateTimeField()
    invite_code = models.CharField(max_length=36)


class InvitationSchema(Schema):
    """Docstring"""

    invited_email: str
    invited_by: OrgUserResponse = None
    invited_on: datetime = None
    invite_code: str = None

    @staticmethod
    def from_invitation(invitation: Invitation):
        """Docstring"""
        return InvitationSchema(
            invited_email=invitation.invited_email,
            invited_by=OrgUserResponse.from_orguser(invitation.invited_by),
            invited_on=invitation.invited_on,
            invite_code=invitation.invite_code,
        )


class AcceptInvitationSchema(Schema):
    """Docstring"""

    invite_code: str
    password: str
