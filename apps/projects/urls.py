from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'projects.views.list',
      name='projects_gallery'),
  url(r'^create/$', 'projects.views.create',
      name='projects_create'),
  url(r'^(?P<slug>[\w-]+)/$', 'projects.views.show',
      name='projects_show'),
  url(r'^(?P<slug>[\w-]+)/description/$', 'projects.views.show_detailed',
      name='projects_show_detailed'),
  url(r'^(?P<slug>[\w-]+)/contactfollowers/$',
      'projects.views.contact_followers',
      name='projects_contact_followers'),

  # Project Edit URLs
  url(r'^(?P<slug>[\w-]+)/edit/$', 'projects.views.edit',
      name='projects_edit'),
  url(r'^(?P<slug>[\w-]+)/edit/description/$',
      'projects.views.edit_description',
      name='projects_edit_description'),
  url(r'^(?P<slug>[\w-]+)/edit/image/$',
      'projects.views.edit_image',
      name='projects_edit_image'),
  url(r'^(?P<slug>[\w-]+)/edit/media/$',
      'projects.views.edit_media',
      name='projects_edit_media'),
  url(r'^(?P<slug>[\w-]+)/edit/media/delete/$',
      'projects.views.delete_media',
      name='projects_delete_media'),
  url(r'^(?P<slug>[\w-]+)/edit/links/$',
      'projects.views.edit_links',
      name='projects_edit_links'),
  url(r'^(?P<slug>[\w-]+)/edit/links/delete/$',
      'projects.views.edit_links_delete',
      name='projects_edit_links_delete'),
)
