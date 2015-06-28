from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements

from nnsh.behavior import MessageFactory as _


class IRegiForm(model.Schema):
    """
       Marker/Form interface for RegiForm
    """

    # -*- Your Zope schema definitions here ... -*-
    embededCode = schema.Text(
        title=_(u"Registration embeded code"),
        required=False,
    )

alsoProvides(IRegiForm, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class RegiForm(object):
    """
       Adapter for RegiForm
    """
    implements(IRegiForm)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    embededCode = context_property("embededCode")
