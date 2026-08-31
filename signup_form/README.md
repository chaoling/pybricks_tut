# Google signup form

This folder contains a complete Google Apps Script that creates and publishes the course signup form and connects it to a Google Sheets response file.

## Create the form

1. Sign in to the Google account that should own the form.
2. Open [Google Apps Script](https://script.google.com/) and select **New project**.
3. Replace the starter code in `Code.gs` with all the code from `create_fll_pybricks_signup_form.gs`.
4. Select `createFLLPybricksSignupForm` in the function menu and click **Run**.
5. Approve the requested Google Forms and Google Sheets permissions.
6. Open **Execution log** and copy the three printed links:
   - `PUBLIC SIGNUP URL` — share this with families.
   - `FORM EDIT URL` — keep this private for course staff.
   - `RESPONSE SPREADSHEET` — keep this private; registrations appear here.

The form is configured to accept responses immediately. Submit one test response before sharing the public link.

## What the script includes

- Course details for grades 4–9, Tuesdays from 5:00–6:00 PM Arizona time, beginning September 1, 2026.
- Enrollment, tryout, availability, technology-access, and parent/guardian questions.
- Email, phone-number, and acknowledgement validation.
- A linked response spreadsheet with a `Course Info` tab containing all administrative links.
- Explicit form publication and response acceptance.
- No forced one-response-per-account limit, so a family can register siblings.
- Safe reruns: running the main function again returns the existing links instead of creating duplicates.

## Create a replacement form

If a genuinely new form is needed, first run `resetFLLPybricksSignupFormProject`, then run `createFLLPybricksSignupForm` again. Resetting only forgets the stored file IDs; it does **not** delete the prior form or spreadsheet.

## Before sharing

Open the form edit link and verify:

1. The public link opens in a private/incognito browser window.
2. A test response reaches the response spreadsheet.
3. The course contact process and enrollment capacity are ready.
4. The latest course description is available at [azhopechineseschool.org](https://azhopechineseschool.org/).

The script intentionally does not publish or change a GitHub Pages site.
