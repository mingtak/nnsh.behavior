from five import grok
from plone.indexer import indexer
from plone.app.contenttypes.interfaces import IFolder
from nnsh.content.webprofile import IWebProfile

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from nnsh.content.themecontent import IThemeContent

from nnsh.behavior import MessageFactory as _


class ISelectTheme(model.Schema):
    """
       Marker/Form interface for SelectTheme
    """

    # -*- Your Zope schema definitions here ... -*-
    selectTheme = RelationChoice(
        title=_(u'Select theme'),
        description=_(u'Select theme for this folder.'),
        source=ObjPathSourceBinder(object_provides=IThemeContent.__identifier__),
        default=None,
        required=False,
    )




alsoProvides(ISelectTheme, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class SelectTheme(object):
    """
       Adapter for SelectTheme
    """
    implements(ISelectTheme)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    selectTheme = context_property('selectTheme')


@indexer(IWebProfile)
@indexer(IFolder)
def selectTheme_indexer(obj):
    if obj.selectTheme:
        selectTheme = obj.selectTheme.to_object.getId()
    else:
        selectTheme = None
    return selectTheme
grok.global_adapter(selectTheme_indexer, name='selectTheme')
