# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IBelowContent, IBelowContentBody
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
#from nnsh.content.epaper import IEpaper
#from nnsh.content.forum import IForum
#from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
#from plone import api


#grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class AttachedFile_IBelowContentBody_Interface(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
    grok.context(Interface)
    grok.require('zope2.View')
    template = ViewPageTemplateFile('template/attachedfile.pt')

#    def isAnonymous(self):
#        return api.user.is_anonymous()

    def render(self):
        return self.template()

