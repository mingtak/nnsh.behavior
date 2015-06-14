from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from nnsh.behavior import MessageFactory as _


class IAttachedFile(model.Schema):
    """
       Marker/Form interface for AttachedFile
    """
    file = NamedBlobFile(
        title=_(u"File"),
        description=_(u"Attached file"),
        required=False,
    )

    # -*- Your Zope schema definitions here ... -*-


alsoProvides(IAttachedFile, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class AttachedFile(object):
    """
       Adapter for AttachedFile
    """
    implements(IAttachedFile)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    file = context_property('file')
