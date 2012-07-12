from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets.navigation import Renderer

class MyNavRenderer(Renderer):
    
     #_template = ViewPageTemplateFile('templates/navigation.pt')
     recurse = ViewPageTemplateFile('templates/navigation_recurse.pt')