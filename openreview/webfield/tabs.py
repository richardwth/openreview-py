from ..rendered_js import RenderedJS

class WebfieldTab(RenderedJS):
  def __init__(self, heading, id):
    super(WebfieldTab, self).__init__()
    self.heading = heading
    self.id = id

class AllSubmittedPapers(WebfieldTab):
  def __init__(self):
    super(AllSubmittedPapers, self).__init__(
      heading = 'All Submitted Papers', id = 'all-submitted-papers')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
      '// All Submitted Papers tab',
      'var submissionListOptions = _.assign({}, paperDisplayOptions, {',
      '  showTags: true,',
      '  tagInvitations: tagInvitations,',
      '  container: \'#all-submitted-papers\'',
      '});',
      '',
      'Webfield.ui.submissionList(notes, {',
      '  heading: null,',
      '  container: \'#all-submitted-papers\',',
      '  search: {',
      '    enabled: true,',
      '    subjectAreas: SUBJECT_AREAS,',
      '    onResults: function(searchResults) {',
      '      var blindedSearchResults = searchResults.filter(function(note) {',
      '        return note.invitation === DISPLAY_INVITATION;',
      '      });',
      '      Webfield.ui.searchResults(blindedSearchResults, submissionListOptions);',
      '      Webfield.disableAutoLoading();',
      '    },',
      '    onReset: function() {',
      '      Webfield.ui.searchResults(notes, submissionListOptions);',
      '      if (notes.length === PAGE_SIZE) {',
      '        Webfield.setupAutoLoading(DISPLAY_INVITATION, PAGE_SIZE, submissionListOptions);',
      '      }',
      '    }',
      '  },',
      '  displayOptions: submissionListOptions,',
      '  fadeIn: false',
      '});',
      '',
      'if (notes.length === PAGE_SIZE) {',
      '  Webfield.setupAutoLoading(DISPLAY_INVITATION, PAGE_SIZE, submissionListOptions);',
      '}'
    ]
    self.js_blocks = [self.commands_block]

class MyTasks(WebfieldTab):
  def __init__(self):
    super(MyTasks, self).__init__(
      heading = 'My Tasks', id = 'my-tasks')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
      '  // My Tasks tab',
      '  if (userGroups.length) {',
      '    var tasksOptions = {',
      '      container: \'#my-tasks\',',
      '      emptyMessage: \'No outstanding tasks for ICLR 2018\'',
      '    }',
      '    Webfield.ui.taskList(assignedNotePairs, tagInvitations, tasksOptions)',
      '',
      '    // Custom links for ICLR',
      '    var acId = CONFERENCE + \'/Area_Chairs\';',
      '    if (_.includes(userGroups, acId)) {',
      '      $(\'#my-tasks .submissions-list\').prepend([',
      '        \'<li class="note invitation-link">\',',
      '          \'<a href="/group?id=\' + acId + \'">ICLR 2018 Area Chair Console</a>\',',
      '        \'</li>\'',
      '      ].join(\'\'));',
      '    }',
      '',
      '    var pcId = CONFERENCE + \'/Program_Chairs\';',
      '    if (_.includes(userGroups, pcId)) {',
      '      $(\'#my-tasks .submissions-list\').prepend([',
      '        \'<li class="note invitation-link">\',',
      '          \'<a href="/reviewers?invitation=\' + CONFERENCE + \'/-/Paper_Assignments&label=reviewers">\',',
      '            \'ICLR 2018 Reviewer Assignments Browser\',',
      '          \'</a>\',',
      '        \'</li>\'',
      '      ].join(\'\'));',
      '',
      '      $(\'#my-tasks .submissions-list\').prepend([',
      '        \'<li class="note invitation-link">\',',
      '          \'<a href="/group?id=\' + pcId + \'">ICLR 2018 Program Chair Console</a>\',',
      '        \'</li>\'',
      '      ].join(\'\'));',
      '    }',
      '  } else {',
      '    $(\'.tabs-container a[href="#my-tasks"]\').parent().hide();',
      '  }',
      '',
    ]
    self.js_blocks = [self.commands_block]

class MySubmittedPapers(WebfieldTab):
  def __init__(self):
    super(MyTasks, self).__init__(
      heading = 'My Submitted Papers', id = 'my-submitted-papers')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
      '  // My Submitted Papers tab',
      '  if (authorNotes.length) {',
      '    Webfield.ui.searchResults(',
      '      authorNotes,',
      '      _.assign({}, paperDisplayOptions, {container: \'#my-submitted-papers\'})',
      '    );',
      '  } else {',
      '    $(\'.tabs-container a[href="#my-submitted-papers"]\').parent().hide();',
      '  }',
      '',
      '  // My Assigned Papers tab (only show if not empty)',
      '  if (assignedNotes.length) {',
      '    Webfield.ui.searchResults(',
      '      assignedNotes,',
      '      _.assign({}, paperDisplayOptions, {container: \'#my-assigned-papers\'})',
      '    );',
      '  } else {',
      '    $(\'.tabs-container a[href="#my-assigned-papers"]\').parent().hide();',
      '  }'
    ]
    self.js_blocks = [self.commands_block]

class MyAssignedPapers(WebfieldTab):
  def __init__(self):
    super(MyTasks, self).__init__(
      heading = 'My Assigned Papers', id = 'my-assigned-papers')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
    '// My Assigned Papers tab (only show if not empty)',
    'if (assignedNotes.length) {',
    'Webfield.ui.searchResults(',
    '  assignedNotes,',
    '  _.assign({}, paperDisplayOptions, {container: \'#my-assigned-papers\'})',
    ');',
    '} else {',
    '  $(\'.tabs-container a[href="#my-assigned-papers"]\').parent().hide();',
    '}'
    ]
    self.js_blocks = [self.commands_block]

class MyCommentsReviews(WebfieldTab):
  def __init__(self):
    super(MyTasks, self).__init__(
      heading = 'My Comments & Reviews', id = 'my-comments-reviews')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
      '  // My Comments & Reviews tab (only show if not empty)',
      '  if (commentNotes.length) {',
      '    Webfield.ui.searchResults(',
      '      commentNotes,',
      '      _.assign({}, commentDisplayOptions, {',
      '        container: \'#my-comments-reviews\',',
      '        emptyMessage: \'No comments or reviews to display\'',
      '      })',
      '    );',
      '  } else {',
      '    $(\'.tabs-container a[href="#my-comments-reviews"]\').parent().hide();',
      '  }',
      '',
      '  $(\'#notes .spinner-container\').remove();',
      '  $(\'.tabs-container\').show();',
      '',
      '  // Show first available tab',
      '  if (initialPageLoad) {',
      '    $(\'.tabs-container ul.nav-tabs li a:visible\').eq(0).click();',
      '    initialPageLoad = false;',
      '  }',
      '}',
    ]
    self.js_blocks = [self.commands_block]

class WithdrawnPapers(WebfieldTab):
  def __init__(self):
    super(MyTasks, self).__init__(
      heading = 'WithdrawnPapers', id = 'withdrawn-papers')

    # the RenderedJS base class expects a list of code blocks.
    # js_blocks is a list consisting of a single code block (itself a list)
    self.commands_block = [
      '  // Withdrawn Papers tab',
      '  if (withdrawnNotes.length) {',
      '    Webfield.ui.searchResults(',
      '      withdrawnNotes,',
      '      _.assign({}, paperDisplayOptions, {showTags: false, container: \'#withdrawn-papers\'})',
      '    );',
      '  } else {',
      '    $(\'.tabs-container a[href="#withdrawn-papers"]\').parent().hide();',
      '  }'
    ]
    self.js_blocks = [self.commands_block]
