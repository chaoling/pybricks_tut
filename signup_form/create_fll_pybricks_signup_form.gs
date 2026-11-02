/**
 * Creates and publishes the Google signup form for the virtual FLL Pybricks
 * course, then links it to a response spreadsheet.
 *
 * Run createFLLPybricksSignupForm() from script.google.com.
 * The generated URLs are printed in the execution log. Re-running the
 * function returns the same form instead of creating duplicates.
 */

const COURSE_CONFIG = Object.freeze({
  formTitle: 'FLL Robot Programming with Pybricks — Fall 2026 Signup',
  responseSpreadsheetTitle: 'FLL Pybricks Fall 2026 — Signup Responses',
  courseName: 'FLL Robot Programming with Pybricks',
  grades: '4–9',
  format: 'Virtual robot environment',
  schedule: 'Tuesdays, 5:00–6:00 PM (Arizona time)',
  startDate: 'September 1, 2026',
  duration: '12 weeks; one 60-minute session per week',
  website: 'https://azhopechineseschool.org/',
  timeZone: 'America/Phoenix',
});

const PROPERTY_KEYS = Object.freeze({
  formId: 'FLL_PYBRICKS_SIGNUP_FORM_ID',
  spreadsheetId: 'FLL_PYBRICKS_SIGNUP_SPREADSHEET_ID',
});

/**
 * Main entry point. Creates the form once and reuses it on later runs.
 *
 * @return {{formUrl: string, editUrl: string, spreadsheetUrl: string,
 *   formId: string, spreadsheetId: string, reused: boolean}}
 */
function createFLLPybricksSignupForm() {
  const existing = getExistingArtifacts_();
  if (existing) {
    logResult_(existing);
    return existing;
  }

  // The second argument publishes the form for responders when supported by
  // the account's current Google Forms publication model.
  const form = FormApp.create(COURSE_CONFIG.formTitle, true);
  configureForm_(form);
  addStudentSection_(form);
  addGuardianSection_(form);
  addCourseInterestSection_(form);
  addAcknowledgementSection_(form);

  const spreadsheet = SpreadsheetApp.create(
    COURSE_CONFIG.responseSpreadsheetTitle
  );
  spreadsheet.setSpreadsheetTimeZone(COURSE_CONFIG.timeZone);
  configureCourseInfoSheet_(spreadsheet, form);

  form.setDestination(
    FormApp.DestinationType.SPREADSHEET,
    spreadsheet.getId()
  );
  publishAndOpenForm_(form);

  const result = buildResult_(form, spreadsheet, false);
  addArtifactLinksToCourseInfoSheet_(spreadsheet, result);

  const properties = PropertiesService.getScriptProperties();
  properties.setProperties({
    [PROPERTY_KEYS.formId]: form.getId(),
    [PROPERTY_KEYS.spreadsheetId]: spreadsheet.getId(),
  });

  logResult_(result);
  return result;
}

function configureForm_(form) {
  form
    .setDescription(
      [
        'A 12-week online course for students in grades 4–9 who want to build FLL-level robot programming skills using Python, Pybricks, and the Gears virtual robot environment.',
        '',
        'Schedule: ' + COURSE_CONFIG.schedule,
        'First class: ' + COURSE_CONFIG.startDate,
        'Format: ' + COURSE_CONFIG.format,
        '',
        'New students are welcome to try a class. Completing this form expresses interest and does not guarantee placement. Course details: ' + COURSE_CONFIG.website,
      ].join('\n')
    )
    .setConfirmationMessage(
      'Thank you! Your signup was received. The school will contact you with enrollment or tryout details. Visit ' +
        COURSE_CONFIG.website +
        ' for course information.'
    )
    .setCustomClosedFormMessage(
      'Registration is currently closed. Please visit ' +
        COURSE_CONFIG.website +
        ' for contact information and course updates.'
    )
    .setCollectEmail(false)
    .setLimitOneResponsePerUser(false)
    .setPublishingSummary(false)
    .setShowLinkToRespondAgain(true)
    .setProgressBar(true)
    .setShuffleQuestions(false)
    .setIsQuiz(false);
}

function addStudentSection_(form) {
  form
    .addSectionHeaderItem()
    .setTitle('Student information')
    .setHelpText('Tell us who will attend the course.');

  form.addTextItem().setTitle('Student full name').setRequired(true);

  form
    .addTextItem()
    .setTitle('Student preferred name')
    .setHelpText('Optional, if different from the name above.');

  form
    .addListItem()
    .setTitle('Grade level in Fall 2026')
    .setChoiceValues(['4', '5', '6', '7', '8', '9'])
    .setRequired(true);

  form.addTextItem().setTitle('School name').setRequired(false);

  form
    .addMultipleChoiceItem()
    .setTitle('Student’s current programming and robotics experience')
    .setHelpText('Choose the description that fits best.')
    .setChoiceValues([
      'No prior programming or robotics experience',
      'Beginner — has tried block coding such as Scratch or SPIKE',
      'Some Python experience',
      'Some LEGO robotics or FLL experience',
      'Experienced with both Python and LEGO robotics',
    ])
    .showOtherOption(true)
    .setRequired(true);

  form
    .addParagraphTextItem()
    .setTitle('What would the student like to learn or accomplish?')
    .setRequired(false);
}

function addGuardianSection_(form) {
  form
    .addPageBreakItem()
    .setTitle('Parent or guardian contact')
    .setHelpText('We will use this information only for course communication.');

  form.addTextItem().setTitle('Parent/guardian full name').setRequired(true);

  const emailValidation = FormApp.createTextValidation()
    .setHelpText('Enter a valid email address, such as name@example.com.')
    .requireTextIsEmail()
    .build();

  form
    .addTextItem()
    .setTitle('Parent/guardian email')
    .setHelpText('Enrollment and meeting information will be sent here.')
    .setValidation(emailValidation)
    .setRequired(true);

  const phoneValidation = FormApp.createTextValidation()
    .setHelpText('Use 7–25 characters: digits, spaces, +, parentheses, periods, or hyphens.')
    .requireTextMatchesPattern('^[0-9+() .-]{7,25}$')
    .build();

  form
    .addTextItem()
    .setTitle('Parent/guardian phone number')
    .setValidation(phoneValidation)
    .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle('Preferred contact method')
    .setChoiceValues(['Email', 'Phone call', 'Text message'])
    .setRequired(true);
}

function addCourseInterestSection_(form) {
  form
    .addPageBreakItem()
    .setTitle('Class and tryout interest')
    .setHelpText('The class meets online every Tuesday from 5:00–6:00 PM Arizona time.');

  form
    .addMultipleChoiceItem()
    .setTitle('How would you like to participate?')
    .setChoiceValues([
      'Enroll in the 12-week course',
      'Try one class before deciding',
      'Please send me more information first',
    ])
    .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle('Can the student regularly attend Tuesdays, 5:00–6:00 PM Arizona time?')
    .setChoiceValues(['Yes', 'Usually, with occasional conflicts', 'No / unsure'])
    .setRequired(true);

  form
    .addCheckboxItem()
    .setTitle('Student technology access')
    .setHelpText('Select everything currently available. This helps us prepare for the virtual class.')
    .setChoiceValues([
      'Computer or Chromebook with a modern web browser',
      'Reliable internet connection',
      'Mouse or trackpad',
      'Headphones or speakers and a microphone',
    ])
    .setRequired(true);

  form
    .addParagraphTextItem()
    .setTitle('Accessibility needs, learning considerations, or questions')
    .setHelpText('Optional. Share anything that would help us support the student.')
    .setRequired(false);

  form
    .addMultipleChoiceItem()
    .setTitle('How did you hear about this course?')
    .setChoiceValues([
      'AZ Hope Chinese School website',
      'School email or newsletter',
      'Friend or family member',
      'Teacher or FLL team',
      'Social media or flyer',
    ])
    .showOtherOption(true)
    .setRequired(false);
}

function addAcknowledgementSection_(form) {
  const acknowledgementValidation = FormApp.createCheckboxValidation()
    .setHelpText('Check the box to submit this signup.')
    .requireSelectExactly(1)
    .build();

  form
    .addCheckboxItem()
    .setTitle('Parent/guardian acknowledgement')
    .setHelpText(
      'This course uses an online virtual robotics environment. Enrollment and tryout details will be confirmed separately.'
    )
    .setChoiceValues([
      'I am the student’s parent/guardian and agree to be contacted about this course.',
    ])
    .setValidation(acknowledgementValidation)
    .setRequired(true);
}

function publishAndOpenForm_(form) {
  // Newer Forms use explicit publication. Older forms may not support advanced
  // responder permissions, so guard the call for account compatibility.
  if (form.supportsAdvancedResponderPermissions()) {
    form.setPublished(true);
  }
  form.setAcceptingResponses(true);
}

function configureCourseInfoSheet_(spreadsheet, form) {
  const sheet = spreadsheet.getSheets()[0];
  sheet.setName('Course Info');

  const values = [
    ['Course setup', 'Value'],
    ['Course', COURSE_CONFIG.courseName],
    ['Grades', COURSE_CONFIG.grades],
    ['Format', COURSE_CONFIG.format],
    ['Schedule', COURSE_CONFIG.schedule],
    ['Start date', COURSE_CONFIG.startDate],
    ['Duration', COURSE_CONFIG.duration],
    ['Website', COURSE_CONFIG.website],
    ['Form ID', form.getId()],
    ['Public signup URL', 'Added after setup'],
    ['Form edit URL', 'Added after setup'],
    ['Response spreadsheet URL', 'Added after setup'],
  ];

  sheet.getRange(1, 1, values.length, 2).setValues(values);
  sheet.getRange(1, 1, 1, 2).setFontWeight('bold').setBackground('#0B5394').setFontColor('#FFFFFF');
  sheet.getRange(1, 1, values.length, 2).setWrap(true).setVerticalAlignment('top');
  sheet.setFrozenRows(1);
  sheet.setColumnWidth(1, 190);
  sheet.setColumnWidth(2, 520);
}

function addArtifactLinksToCourseInfoSheet_(spreadsheet, result) {
  const sheet = spreadsheet.getSheetByName('Course Info');
  sheet.getRange('B10').setValue(result.formUrl);
  sheet.getRange('B11').setValue(result.editUrl);
  sheet.getRange('B12').setValue(result.spreadsheetUrl);
  SpreadsheetApp.flush();
}

function getExistingArtifacts_() {
  const properties = PropertiesService.getScriptProperties();
  const formId = properties.getProperty(PROPERTY_KEYS.formId);
  const spreadsheetId = properties.getProperty(PROPERTY_KEYS.spreadsheetId);

  if (!formId || !spreadsheetId) {
    return null;
  }

  try {
    const form = FormApp.openById(formId);
    const spreadsheet = SpreadsheetApp.openById(spreadsheetId);
    return buildResult_(form, spreadsheet, true);
  } catch (error) {
    // A file may have been deleted or access may have changed. Clear only the
    // saved IDs so the next lines can safely create a replacement set.
    properties.deleteProperty(PROPERTY_KEYS.formId);
    properties.deleteProperty(PROPERTY_KEYS.spreadsheetId);
    console.warn('Saved form files could not be reopened; creating replacements. ' + error);
    return null;
  }
}

function buildResult_(form, spreadsheet, reused) {
  return {
    formUrl: form.getPublishedUrl(),
    editUrl: form.getEditUrl(),
    spreadsheetUrl: spreadsheet.getUrl(),
    formId: form.getId(),
    spreadsheetId: spreadsheet.getId(),
    reused: reused,
  };
}

function logResult_(result) {
  const message = [
    result.reused ? 'Existing signup form found.' : 'Signup form created successfully.',
    'PUBLIC SIGNUP URL: ' + result.formUrl,
    'FORM EDIT URL: ' + result.editUrl,
    'RESPONSE SPREADSHEET: ' + result.spreadsheetUrl,
  ].join('\n');

  console.log(message);
  Logger.log(message);
}

/**
 * Run this only when you intentionally want the next main-function run to
 * create a new form and spreadsheet. It does not delete the existing files.
 */
function resetFLLPybricksSignupFormProject() {
  const properties = PropertiesService.getScriptProperties();
  properties.deleteProperty(PROPERTY_KEYS.formId);
  properties.deleteProperty(PROPERTY_KEYS.spreadsheetId);
  console.log(
    'Saved IDs cleared. Run createFLLPybricksSignupForm() to create a new form and response spreadsheet.'
  );
}
