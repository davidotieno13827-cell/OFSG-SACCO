# OFSG SELF-HELP GROUP PLATFORM
## Complete User Manual & Pricing Guide

**Document Date:** 17 July 2026
**Exchange Rate Used:** 1 USD = 129.34 Kenya Shillings (KES)

---

# TABLE OF CONTENTS
1. [Platform Overview](#platform-overview)
2. [What the Website CAN Do](#what-the-website-can-do)
3. [What the Website CANNOT Do](#what-the-website-cannot-do)
4. [Pricing Tiers Comparison](#pricing-tiers-comparison)
5. [Simple Plan Detailed Guide](#simple-plan-detailed-guide)
6. [Standard Plan Detailed Guide](#standard-plan-detailed-guide)
7. [Premium Plan Detailed Guide](#premium-plan-detailed-guide)
8. [User Manual](#user-manual)
9. [How to Register](#how-to-register)
10. [How to Use Dashboard](#how-to-use-dashboard)
11. [How to Manage Contributions](#how-to-manage-contributions)
12. [How to Track Fines](#how-to-track-fines)

---

# PLATFORM OVERVIEW

The OFSG Platform is a web-based management system designed specifically for self-help groups and SACCO (Savings and Credit Cooperative Organization) organizations. It helps manage member registrations, track financial contributions, manage penalties, and maintain member records.

**Current Version:** Text-Only System (No Picture Storage)
**Current Server:** Local Development (Ready for Deployment to Render)
**Database:** PostgreSQL
**Web Framework:** Django Python

---

# WHAT THE WEBSITE CAN DO

## 1. MEMBER MANAGEMENT FEATURES

### Registration and Account Creation
- Members can create their own accounts online
- New members provide: Username, Email, Phone Number, Password
- Automatic email verification/activation link sent to email
- Guardian and Next-of-Kin information stored securely
- Account must be activated before member can log in

### Member Profile Management
- Members can update their profile information
- Update Next-of-Kin name and phone number
- Update Guardian 1 and Guardian 2 details
- View complete member information stored in system
- Change password for security

### Member Search and Directory
- Treasurer and Overseer staff can search for members
- Search by Username or Phone Number
- Filter members by Status (Active or Inactive)
- View complete list of all members registered
- See registration date for each member

### Member Information Tracking
- Full Name (stored from registration)
- Email Address
- Phone Number (maximum 15 digits)
- Registration Date
- Active/Inactive Status
- Next-of-Kin Name and Phone
- Guardian 1 and Guardian 2 Names and Phones
- Member contribution history
- Outstanding fines

---

## 2. FINANCIAL MANAGEMENT FEATURES

### Contribution Tracking
- Record monthly member contributions (typically 1,000 Kenya Shillings)
- Record AGM (Annual General Meeting) fees (typically 2,000 Kenya Shillings)
- Record Welfare/Social contributions
- Store contribution date and time automatically
- Display contribution history for each member
- Calculate total savings per member
- View contribution trends

### Contribution Management (Treasurer Features)
- Add new contribution records
- Link contributions to specific members
- Track contribution type (Monthly, AGM, Welfare)
- View all contributions made by each member
- Generate contribution reports
- Calculate organization total contributions

### Fine Management System
- Record fines for late payment
- Record fines for non-attendance
- Record other penalties as needed
- Mark fines as paid or unpaid
- Track fine issuance date
- Manage fine amounts

### Fine Processing (Treasurer/Overseer Features)
- Add new fines to members
- Mark fines as paid when collected
- View outstanding fines (unpaid)
- View paid fines (completed)
- Track which fines are pending payment
- Generate fine reports

### Financial Dashboards and Reports
- Member Personal Dashboard shows:
  - Total savings/contributions amount
  - Number of contribution entries
  - Outstanding fine total
  - Individual fine details
  - Recent contributions list

- Treasurer Dashboard shows:
  - Total number of active members
  - Total number of inactive members
  - Recent new member registrations
  - All contributions made
  - All outstanding fines
  - Organization-wide totals
  - Recent transactions

---

## 3. STAFF AND ROLE MANAGEMENT

### Role-Based Access Control
- **Admin/Superuser** - Full system access, can manage everything
- **Treasurer** - Can view all members, add contributions, manage fines
- **Overseer** - Can view member directory and basic information
- **Regular Members** - Can only see their own profile and contributions

### Staff Authentication
- Secure login with username and password
- Password complexity requirements enforced
- Failed login attempt protection (blocks after multiple attempts)
- Session security with HTTPS encryption
- Automatic logout after inactivity

---

## 4. EMAIL COMMUNICATION

### Automated Email Notifications
- New member account activation emails
- Password reset confirmation emails
- Account status update notifications
- Supports HTML and plain text email formats
- Configurable email templates

---

## 5. SECURITY FEATURES

### Account Security
- Passwords stored securely (hashed encryption)
- Password must be minimum 10 characters
- Password must include numbers, letters, special characters
- Cannot reuse similar patterns
- Cannot be common weak passwords

### Access Control
- Session cookies secured (HTTPS only)
- CSRF (Cross-Site Request Forgery) protection
- X-Frame clickjacking protection
- Content Security Policy headers
- Rate limiting on login attempts

### Data Protection
- Database encryption
- Secure file storage (when applicable)
- Role-based access restrictions
- Activity logging available

---

# WHAT THE WEBSITE CANNOT DO

## 1. IMAGE AND DOCUMENT STORAGE
❌ Cannot store member profile pictures
❌ Cannot store passport photos
❌ Cannot store ID documents/scans
❌ Cannot display member photos in directory
❌ Cannot verify identity visually through photos

## 2. OFFLINE FUNCTIONALITY
❌ Cannot work without internet connection
❌ Cannot sync data offline
❌ Cannot operate without web server

## 3. MOBILE APPLICATION
❌ Not a mobile phone application
❌ Only works through web browser
❌ No Android app available
❌ No iOS app available

## 4. ADVANCED REPORTING
❌ Cannot generate complex graphs/charts
❌ Cannot export to Excel automatically
❌ Cannot create PDF reports automatically
❌ Cannot schedule automated reports
❌ Cannot analyze financial trends

## 5. PAYMENT PROCESSING
❌ Cannot process M-Pesa payments directly
❌ Cannot accept online bank transfers
❌ Cannot process credit card payments
❌ Payment records must be entered manually

## 6. MULTIPLE SACCO MANAGEMENT
❌ Cannot manage multiple SACCO groups
❌ One system = one organization only
❌ Cannot share data between different groups

## 7. SMS COMMUNICATION
❌ Cannot send SMS text messages
❌ Cannot receive SMS commands
❌ Only email notifications available

## 8. VOICE CALLS
❌ Cannot make phone calls
❌ Cannot send voice messages
❌ No telephone integration

## 9. AUTOMATIC CALCULATIONS
❌ Cannot automatically calculate compound interest
❌ Cannot auto-apply fines on schedule
❌ Fines must be added manually
❌ Interest calculations must be done separately

## 10. BACKUP AND DISASTER RECOVERY
❌ No automatic daily backups (on Simple plan)
❌ No disaster recovery system
❌ Data loss possible if server fails
❌ No redundant copies automatically created

---

# PRICING TIERS COMPARISON

## EXCHANGE RATE
**1 United States Dollar (USD) = 129.34 Kenya Shillings (KES)**

---

## SIMPLE PLAN
### Monthly Cost: 2,583 Kenya Shillings (~20 USD)
### Annual Cost: 30,996 Kenya Shillings (~240 USD)

**Components Included:**
- Render Web Server (Starter): 905 KES/month
- PostgreSQL Database (Starter): 905 KES/month
- Email Service (Free SendGrid tier): 0 KES/month
- Domain Name Registration: 162 KES/month (amortized annual)
- Operating Budget/Buffer: 647 KES/month

**What You Get:**
- Text-only member database (no pictures)
- Support for 500-1,000 active members
- Unlimited transaction records
- Up to 100 emails per day
- 1 GB database storage
- Basic member dashboard
- Contribution tracking
- Fine management
- Member search
- Staff roles (Admin, Treasurer, Overseer)

**Limitations:**
- No picture/document storage
- 10-20 simultaneous users comfortable
- Basic features only
- Manual backup required
- No data redundancy

---

## STANDARD PLAN
### Monthly Cost: 6,241 Kenya Shillings (~48.25 USD)
### Annual Cost: 74,892 Kenya Shillings (~579 USD)

**Components Included:**
- Render Web Server (Standard): 1,940 KES/month
- PostgreSQL Database (Standard): 905 KES/month
- SendGrid Email (Paid Starter): 1,940 KES/month
- AWS S3 File Storage: 1,293 KES/month
- Domain Name Registration: 162 KES/month (amortized annual)
- Operating Buffer: 0 KES/month

**What You Get (Everything in Simple PLUS):**
- Member profile picture storage
- Passport photo storage
- ID document storage
- All text-only features
- Up to 50,000 emails per month
- 100 GB+ file storage for documents
- File download capability
- Faster performance
- 50-100 simultaneous users supported
- Automatic file serving

**Additional Features:**
- View member profile pictures
- Download ID documents
- Download passport photos
- Backup member documents digitally
- Visual member identification
- Professional document storage

**Limitations:**
- Medium-level scalability
- Single server (no redundancy)
- No advanced analytics
- No automatic backups
- Limited concurrent users

---

## PREMIUM PLAN
### Monthly Cost: 12,448 Kenya Shillings (~96.25 USD)
### Annual Cost: 149,384 Kenya Shillings (~1,155 USD)

**Components Included:**
- Render Web Server (Professional): 3,880 KES/month
- PostgreSQL Database (Professional): 2,587 KES/month
- SendGrid Email (Enhanced): 3,880 KES/month
- AWS S3 File Storage (Scaled): 1,940 KES/month
- Domain Name Registration: 162 KES/month
- Backup and Monitoring Service: 0 KES/month (included)

**What You Get (Everything in Standard PLUS):**
- All Standard features
- Up to 500,000 emails per month
- 1 TB+ file storage
- Automatic daily backups
- Advanced monitoring
- 200-500 simultaneous users supported
- Faster database performance
- Priority support
- Improved uptime (99.95%)

**Additional Features:**
- Automated backup system
- Disaster recovery capability
- Advanced member analytics
- Export to CSV format
- Activity logging
- System health monitoring
- Regular security audits

---

# SIMPLE PLAN DETAILED GUIDE

## Overview
The Simple Plan is the most cost-effective option for organizations just starting or with limited budget. It includes all essential features needed to manage member contributions and fines.

## Monthly Cost Breakdown
| Component | Cost | Description |
|-----------|------|-------------|
| Render Web Server | 905 KES | Hosts the website |
| PostgreSQL Database | 905 KES | Stores all member data |
| Email Service | 0 KES | Free tier (100 emails/day) |
| Domain | 162 KES | Your website address |
| Buffer/Operations | 647 KES | Contingency and maintenance |
| **TOTAL** | **2,583 KES** | **Per Month** |

## Annual Cost
**2,583 × 12 = 30,996 Kenya Shillings per year**

## What You Can Do With Simple Plan

### Member Management
✅ Register new members online
✅ Store member contact information
✅ Record next-of-kin and guardian details
✅ Search for members by name or phone
✅ View member registration dates
✅ Manage member active/inactive status
✅ Update member profile details

### Financial Tracking
✅ Record monthly contributions
✅ Record AGM fees
✅ Record welfare contributions
✅ View contribution history per member
✅ Calculate total savings per member
✅ Track all contributions organization-wide
✅ Record and manage fines
✅ Mark fines as paid or unpaid

### Reporting
✅ View personal contribution dashboard
✅ View outstanding fines list
✅ See recent contributions
✅ View member directory
✅ Generate summary reports
✅ Calculate totals manually

### User Access
✅ Create multiple staff accounts
✅ Set role permissions (Admin, Treasurer, Overseer)
✅ Manage staff access levels
✅ View staff activity
✅ Secure login with password protection

## Limitations of Simple Plan

❌ No picture storage (profile pictures)
❌ No passport photo storage
❌ No ID document storage
❌ Cannot support more than 10-20 simultaneous users
❌ No automatic backups
❌ No data redundancy
❌ No advanced analytics
❌ Manual backup required
❌ Limited to 100 emails per day
❌ Cannot send bulk notifications

## Who Should Use Simple Plan

- **Small organizations** (100-500 members)
- **New SACCO groups** testing the system
- **Budget-conscious groups** with limited funds
- **Groups doing identity verification in-person**
- **Organizations that don't need digital documents**
- **Groups with minimal concurrent users**

## Capacity Limits

| Metric | Capacity |
|--------|----------|
| Members | 500-1,000 |
| Contribution Records | 50,000+ |
| Fine Records | 10,000+ |
| Simultaneous Users | 10-20 |
| Database Size | 5-10 MB |
| Monthly Emails | 3,000 (100/day) |
| Document Storage | 0 (none) |
| Daily Transactions | 100-200 |

---

# STANDARD PLAN DETAILED GUIDE

## Overview
The Standard Plan adds professional document storage capabilities and higher capacity. Ideal for growing organizations that need to maintain digital copies of member documents.

## Monthly Cost Breakdown
| Component | Cost | Description |
|-----------|------|-------------|
| Render Web Server | 1,940 KES | Faster web hosting |
| PostgreSQL Database | 905 KES | Standard database tier |
| Email Service | 1,940 KES | Professional email (50K/month) |
| File Storage (S3) | 1,293 KES | AWS cloud storage for files |
| Domain | 162 KES | Your website address |
| **TOTAL** | **6,241 KES** | **Per Month** |

## Annual Cost
**6,241 × 12 = 74,892 Kenya Shillings per year**

## What You Can Do With Standard Plan

### Everything in Simple Plan PLUS:

### Document Management
✅ Store member profile pictures (digital backup)
✅ Store member passport photos (digital backup)
✅ Store member ID documents (PDF/image)
✅ Download member documents
✅ View member photos in member detail pages
✅ Organize documents by member
✅ Secure document access (only authorized users)
✅ Backup member documents automatically

### Enhanced Functionality
✅ Support 50-100 simultaneous users
✅ Faster performance and response times
✅ Up to 50,000 emails per month
✅ 100+ GB file storage space
✅ Automatic file serving and downloads
✅ Better database performance
✅ Increased upload file size limit

### Professional Features
✅ Professional email support (SendGrid)
✅ HTML email templates
✅ Bulk notification capability
✅ Email scheduling
✅ Better uptime reliability
✅ Enhanced database backup options
✅ Faster file downloads

### Enhanced Reporting
✅ Better member detail pages
✅ Document download links
✅ Member portfolio view
✅ Document organization

## What Cannot Be Done in Standard Plan

❌ Automatic compound interest calculation
❌ Advanced data analytics
❌ Export to Excel format
❌ Generate PDF reports automatically
❌ Multi-group management
❌ Payment gateway integration
❌ SMS notifications
❌ Automatic backup scheduling
❌ Advanced security features
❌ Mobile app access

## Who Should Use Standard Plan

- **Medium organizations** (500-2,000 members)
- **Groups needing digital record-keeping**
- **Organizations requiring document backup**
- **Growing SACCO with 30-50+ users accessing system**
- **Groups wanting visual member identification**
- **Professional organizations needing document compliance**
- **Groups requiring member document verification**

## Capacity Limits

| Metric | Capacity |
|--------|----------|
| Members | 1,000-5,000 |
| Contribution Records | 100,000+ |
| Fine Records | 50,000+ |
| Simultaneous Users | 50-100 |
| Database Size | 20-50 MB |
| File Storage | 100+ GB |
| Monthly Emails | 50,000 |
| Document Upload Size | 5 MB per file |
| Daily Transactions | 500-1,000 |

## File Storage on Standard Plan

### Supported File Types
- **Images:** JPG, PNG, GIF
- **Documents:** PDF, DOC, DOCX
- **ID Documents:** JPG, PNG, PDF

### File Organization
- Organized by member ID
- Automatic categorization (profile picture, passport, ID)
- Secure access control
- Version history maintained

### Storage Examples
- 500 members × 3 documents (photo, passport, ID) = 500 MB
- Plenty of space in 100+ GB allocation

---

# PREMIUM PLAN DETAILED GUIDE

## Overview
The Premium Plan is the most comprehensive solution for large organizations, organizations with high security requirements, or mission-critical systems requiring maximum reliability.

## Monthly Cost Breakdown
| Component | Cost | Description |
|-----------|------|-------------|
| Render Web Server | 3,880 KES | Professional-grade hosting |
| PostgreSQL Database | 2,587 KES | Professional database tier |
| Email Service | 3,880 KES | Premium email (500K/month) |
| File Storage (S3 Scaled) | 1,940 KES | Large-scale file storage |
| Domain | 162 KES | Your website address |
| Backup Service | Included | Automatic backup service |
| **TOTAL** | **12,448 KES** | **Per Month** |

## Annual Cost
**12,448 × 12 = 149,384 Kenya Shillings per year**

## What You Can Do With Premium Plan

### Everything in Standard Plan PLUS:

### Advanced Capacity
✅ Support 200-500 simultaneous users
✅ Up to 500,000 emails per month
✅ 1 TB+ file storage space
✅ Enterprise-grade performance
✅ Very fast database queries
✅ Large file upload support (up to 50 MB)

### Backup and Recovery
✅ Automatic daily backups
✅ Backup retention (30-day history)
✅ Disaster recovery capability
✅ Point-in-time recovery
✅ Backup encryption
✅ Verified backup testing

### Advanced Features
✅ Activity audit logs (complete history)
✅ System health monitoring
✅ Uptime monitoring (99.95% guaranteed)
✅ Performance analytics
✅ Advanced security options
✅ Rate limiting and DDoS protection
✅ Export to CSV format capability
✅ Data analytics dashboard

### Support and Management
✅ Priority technical support
✅ Regular security audits
✅ System optimization recommendations
✅ Performance tuning
✅ Advanced troubleshooting
✅ Dedicated account manager

### Compliance Features
✅ Data retention policies
✅ Access control logging
✅ Compliance reporting
✅ Security certifications
✅ Audit trail (complete)
✅ Regulatory compliance support

## What Cannot Be Done in Premium Plan

❌ Real-time payment processing integration
❌ Multi-currency support
❌ Video conferencing features
❌ Machine learning analytics
❌ Blockchain integration
❌ NFT management
❌ Cryptocurrency transactions

## Who Should Use Premium Plan

- **Large organizations** (5,000+ members)
- **Mission-critical SACCO systems**
- **Organizations with high security requirements**
- **Groups needing guaranteed uptime**
- **Organizations with compliance requirements**
- **Groups with 100+ concurrent staff users**
- **Mission-critical financial operations**
- **Organizations requiring audit trails**

## Capacity Limits

| Metric | Capacity |
|--------|----------|
| Members | 5,000-50,000+ |
| Contribution Records | 500,000+ |
| Fine Records | 100,000+ |
| Simultaneous Users | 200-500 |
| Database Size | 100+ MB |
| File Storage | 1 TB (1,000 GB) |
| Monthly Emails | 500,000 |
| Document Upload Size | 50 MB per file |
| Daily Transactions | 5,000-10,000+ |
| Backup Retention | 30 days |

---

# USER MANUAL

## Getting Started with OFSG Platform

### System Requirements
- Internet connection (required)
- Web browser (Chrome, Firefox, Safari, Edge)
- Email address (for account activation)
- Phone number (for member record)

### Accessing the Platform
1. Open web browser (Chrome, Firefox, Safari, or Edge)
2. Type website address in address bar
3. You will see the OFSG Platform homepage
4. Click "Member Login" or "Leader/Admin Sign In"

---

# HOW TO REGISTER

## New Member Registration Process

### Step 1: Go to Registration Page
1. Open the OFSG Platform website
2. Click "Register New Member" button
3. You will see the registration form

### Step 2: Fill in Basic Information

**Username**
- Enter your unique username
- Example: "john_kipchoge_23"
- Must be unique (no other member can have same username)
- Can include letters, numbers, underscores

**Email Address**
- Enter your email address
- Example: "john.kipchoge@email.com"
- Must be valid (platform will send activation link)
- Check spam folder if activation email doesn't arrive

**Phone Number**
- Enter your phone number (maximum 15 digits)
- Example: "0722123456"
- Should include country code (+254) or national prefix (07xx)

### Step 3: Fill in Family Information

**Next of Kin Name**
- Enter name of person to contact in emergency
- Example: "Jane Kipchoge"
- Leave blank if you prefer to fill later

**Next of Kin Phone**
- Enter phone number of next of kin
- Example: "0722654321"
- Leave blank if you prefer to fill later

**Guardian 1**
- Enter first guardian or trustee name
- Example: "Peter Kipchoge"
- Leave blank if not applicable

**Guardian 2**
- Enter second guardian or trustee name
- Example: "Ann Kipchoge"
- Leave blank if not applicable

### Step 4: Create Password

**Password**
- Must be at least 10 characters long
- Must include:
  - Upper case letter (A-Z)
  - Lower case letter (a-z)
  - Number (0-9)
  - Special character (!@#$%^&*)
- Example: "MyPassword123!"
- Do NOT use your username or easy-to-guess words

**Confirm Password**
- Type the same password again
- Must match exactly
- System will show error if passwords don't match

### Step 5: Submit Registration
1. Review all information entered
2. Click "Create Account" button
3. Wait for confirmation message

### Step 6: Check Your Email
1. Check your email inbox
2. Look for email from "OFSG Platform"
3. Subject: "Activate your OFSG account"
4. Click the activation link in email
5. Your account will be activated
6. You can now login

### Troubleshooting Registration

**Email Not Received**
- Check spam/junk folder
- Check if email address was typed correctly
- Wait 5-10 minutes
- Try registering again with correct email

**Password Doesn't Meet Requirements**
- Check that password is at least 10 characters
- Include uppercase letter (A-Z)
- Include lowercase letter (a-z)
- Include number (0-9)
- Include special character (!@#$%^&*)

**Username Already Taken**
- Username exists for another member
- Choose a different username
- Add numbers or underscore to make it unique
- Try: "john_kipchoge_2024"

---

# HOW TO LOGIN

## Member Login Process

### Step 1: Go to Login Page
1. Go to OFSG Platform website
2. Click "Member Login" button
3. You will see login form with two fields

### Step 2: Enter Credentials

**Username**
- Enter the username you registered with
- Example: "john_kipchoge_23"
- Must match exactly (case-sensitive)

**Password**
- Enter your password
- Example: "MyPassword123!"
- Must match exactly (case-sensitive)
- Password is hidden (shown as dots)

### Step 3: Submit Login
1. Click "Secure Login" button
2. Wait for page to load
3. If correct, you will see dashboard
4. If incorrect, error message appears

### After Login - Your Dashboard
- You will see "Welcome back, [your username]" at top
- Dashboard shows your account information
- You can access Profile and Logout options

### Troubleshooting Login

**Incorrect Username or Password Error**
- Check that username is spelled correctly
- Confirm CAPS LOCK is NOT on
- Verify password is correct (remember it's case-sensitive)
- If forgotten, use admin to reset

**Account Not Activated Error**
- You may not have activated your account
- Check email for activation link
- Click activation link
- Try logging in again

**Too Many Failed Login Attempts**
- System blocks account after 5 failed attempts
- Wait 30 minutes before trying again
- Contact administrator for help

---

# HOW TO USE DASHBOARD

## Member Dashboard Overview

### Welcome Section
At top of dashboard:
- "Welcome back, [your username]"
- "Member since: [month/year]"
- "Logout" button

### Main Dashboard Cards

**Card 1: Total Savings Equity**
- Shows total amount of all your contributions
- Displays: "Ksh [amount]"
- Shows number of contribution entries
- Updated automatically when contributions added

**Card 2: Outstanding Fines**
- Shows total amount of unpaid fines
- Displays: "Ksh [amount]"
- If no fines: "No outstanding fines at the moment"
- Shows details of each unpaid fine

**Card 3: Member Status**
- Shows if you are "Active" or "Inactive"
- Explains: "Your profile and payment records are available for review in this portal"
- Can only be changed by administrator

### Dashboard Actions

**Quick Actions Section**
- "Update Profile" button - Click to update your details
- Takes you to Profile page
- Can update guardians and next-of-kin information

### Recent Contributions Table

**What You See:**
- Table with three columns: Date | Type | Amount
- Lists your recent contributions (last 5-10)
- Date shown in format: "Jan 15, 2024"
- Type shown as: "Monthly", "AGM", or "Welfare"
- Amount shown as: "Ksh [number]"

**If No Contributions:**
- Table shows: "No contributions found yet"
- Contributions will appear as soon as treasurer adds them

### Outstanding Fines Summary

**What You See:**
- List of all unpaid fines (if any)
- For each fine shows:
  - Type of fine (e.g., "Late Payment Fine")
  - Amount (e.g., "Ksh 500")
  - Date issued
  - Mark as "Unpaid"

**If No Fines:**
- Shows: "No outstanding fines are currently recorded"

### Edit Profile Button
- Located in "Quick actions" section
- Click to update your personal details
- Can update:
  - Next of Kin name and phone
  - Guardian 1 name
  - Guardian 2 name

---

# HOW TO MANAGE CONTRIBUTIONS

## For Regular Members: View Your Contributions

### Viewing Your Contribution History

**On Dashboard:**
1. Scroll down to "Recent Contributions" section
2. View table of your contributions
3. See: Date | Type | Amount

**Information Shown:**
- **Date:** When contribution was recorded (e.g., "Jan 15, 2024")
- **Type:** "Monthly" (Ksh 1,000) | "AGM" (Ksh 2,000) | "Welfare"
- **Amount:** Total paid (e.g., "Ksh 1,000")

**Total Savings Shown:**
- Top of dashboard shows: "Total Savings Equity"
- Displays total of ALL your contributions added together
- Example: If you paid 5 times × 1,000 = "Ksh 5,000"

### Understanding Contributions

**Monthly Contribution**
- Regular monthly payment
- Expected amount: Ksh 1,000
- Recorded once per month (usually)
- Shows as "Monthly" in type column

**AGM Fee**
- Annual General Meeting fee
- Expected amount: Ksh 2,000
- Recorded once per year (at AGM)
- Shows as "AGM" in type column

**Welfare Contribution**
- Social welfare or emergency fund
- Amount varies
- Shows as "Welfare" in type column

---

## For Treasurer Staff: Add New Contributions

### Access Contribution Recording

**Step 1: Login as Treasurer**
1. Login with treasurer username and password
2. After login, look for treasurer-specific menu options
3. Click "Add Contribution" option

### Step 2: Select Member

**Member Dropdown**
- Click dropdown that shows "Select Member"
- List of all members will appear
- Search by typing member name
- Select the correct member from list

### Step 3: Enter Contribution Details

**Amount**
- Enter the contribution amount paid
- Example: "1000" (for Ksh 1,000)
- Use numbers only
- No currency symbol needed

**Contribution Type**
- Click dropdown showing "Select Type"
- Choose from:
  - "Monthly Contribution" (regular monthly payment)
  - "AGM Fee" (annual fee)
  - "Welfare/Social" (emergency/social fund)
- Select the appropriate type

**Date Paid**
- Date is recorded automatically
- Shows today's date
- Cannot be changed for current entries

### Step 4: Save Contribution

1. Click "Save" or "Add Contribution" button
2. System will show confirmation
3. Contribution appears in member's history
4. Dashboard totals update automatically

### Tips for Recording Contributions

- **Accuracy:** Double-check member name before saving
- **Correct Type:** Select correct contribution type
- **Correct Amount:** Verify amount matches cash received
- **Timing:** Record same day contribution is received if possible
- **Backup:** Keep paper receipt as backup record

---

# HOW TO TRACK FINES

## For Regular Members: Check Your Fines

### Viewing Your Outstanding Fines

**On Dashboard:**
1. Look for "Outstanding Fines" card (top of dashboard)
2. Shows total amount: "Ksh [amount]"
3. Scroll down to "Outstanding Fine Summary" section
4. See list of all unpaid fines

**Fine Details Shown:**
- **Fine Type:** Reason for fine (e.g., "Late Payment", "Non-attendance")
- **Amount:** How much is owed (e.g., "Ksh 500")
- **Status:** "Unpaid" or "Paid"
- **Date Issued:** When fine was recorded

**Understanding Fine Types**

**Late Payment Fine**
- Issued when monthly contribution not paid on time
- Amount: Usually Ksh 500
- Reason: Encourages timely payment of Ksh 1,000 contribution

**Non-Attendance Fine**
- Issued when member doesn't attend required meetings
- Amount: Usually Ksh 500
- Reason: Encourages participation in SACCO activities

**Other Fines**
- May be recorded for other reasons
- Amount and description vary
- Check with treasurer if unclear

### Paying Your Fines

1. Contact treasurer or leader
2. Inform them which fines you want to pay
3. Provide payment (cash or mobile money)
4. Treasurer records payment in system
5. Status changes from "Unpaid" to "Paid"
6. Fine disappears from "Outstanding Fines"

---

## For Treasurer Staff: Record New Fines

### Access Fine Recording

**Step 1: Login as Treasurer**
1. Login with treasurer credentials
2. Look for treasurer menu options
3. Click "Add Fine" option

### Step 2: Select Member

**Member Selection**
- Click dropdown showing "Select Member"
- Choose the member being fined
- Must select one member per fine
- If not sure, ask another treasurer

### Step 3: Enter Fine Details

**Fine Type**
- Click dropdown showing "Select Fine Type"
- Choose reason for fine:
  - "Late Payment" (contribution not paid on time)
  - "Non-attendance" (didn't attend meeting)
  - Other reason (type custom description)

**Amount**
- Enter the fine amount
- Standard amounts:
  - Late Payment: Ksh 500
  - Non-attendance: Ksh 500
  - Other: As decided by organization
- Use numbers only

**Date Issued**
- Date recorded automatically
- Cannot be changed

**Status**
- Leave as "Unpaid" initially
- Will be marked "Paid" when payment received

### Step 4: Save Fine

1. Click "Save" or "Add Fine" button
2. System confirms fine recorded
3. Fine appears in member's outstanding fines list
4. Dashboard totals update

### Step 5: Marking Fine as Paid

**When Payment Received:**
1. Go to member's fine record
2. Click "Mark Fine as Paid" button
3. Status changes from "Unpaid" to "Paid"
4. Fine amount subtracted from outstanding total
5. Member can see fine is paid on their dashboard

### Fine Management Best Practices

- **Consistency:** Apply same fines to all members
- **Documentation:** Keep records of when fines issued
- **Communication:** Inform member of new fine
- **Fairness:** Give member chance to explain
- **Tracking:** Record which staff member added fine
- **Follow-up:** Track if fines are paid

---

## For Treasurer: View All Organization Fines

### Management Summary View

**Access Summary:**
1. Look for "Management Summary" option in menu
2. Shows organization-wide information

**Fines Information:**
- Total outstanding fines: "Ksh [amount]"
- List of unpaid fines with members and amounts
- Recently issued fines
- Total fines collected

### Using Fine Reports

**To Understand System's Fines:**
1. Review all outstanding fines regularly (weekly)
2. Identify members with multiple unpaid fines
3. Follow up with members about payment
4. Record when fines are paid
5. Report to leadership on collection rate

---

# MEMBER DIRECTORY (FOR STAFF ONLY)

## Accessing Member Directory

### Who Can Access
- Admin staff
- Treasurer
- Overseer
- Not available to regular members

### How to Access

**Step 1: Login**
1. Login with your staff account (Admin, Treasurer, or Overseer)
2. Click "Member Directory" or "Members List" in menu

**Step 2: View All Members**
- See complete list of all registered members
- Shows:
  - Username
  - Phone number
  - Status (Active/Inactive)
  - Registration date
  - Total contributions
  - Outstanding fines

### Search Function

**Search by Username**
1. Click search box at top of member list
2. Type member's username
3. List filters to show matching member
4. Click member name to view details

**Search by Phone Number**
1. Click search box
2. Type phone number
3. List shows member with that phone
4. View their full record

### Filter by Status

**Active Members Only**
1. Click filter dropdown
2. Select "Active"
3. Shows only members with status: Active

**Inactive Members Only**
1. Click filter dropdown
2. Select "Inactive"
3. Shows only deactivated members

### View Member Details

**Click on Member Name**
1. Click any member in list
2. Opens member detail page
3. Shows:
   - Complete member information
   - All contributions
   - All fines (paid and unpaid)
   - Contact information
   - Registration date
   - Guardian information

---

# UPDATING YOUR PROFILE

## Access Profile Update

### Step 1: Go to Profile Page

**From Dashboard:**
1. Click "Profile" in top navigation menu
2. OR click "Update Profile" button in dashboard

### Step 2: Edit Information

**Heading:** "Update Nomination Details"

**Fields You Can Edit:**

**Next of Kin Name**
- Click text box
- Clear existing name
- Type new next-of-kin name
- Example: "Grace Kipchoge"

**Next of Kin Phone**
- Click phone number field
- Clear existing number
- Type new phone number
- Example: "0722222222"

**Guardian 1**
- Click guardian name field
- Update first guardian name
- Example: "Ann Kipchoge"

**Guardian 2**
- Click guardian name field
- Update second guardian name
- Example: "Peter Kipchoge"

### Step 3: Save Changes

1. Review all information entered
2. Click "Save Profile" button
3. System confirms changes saved
4. Message shows "Profile updated successfully"
5. You can now see updated information

### Why Update These Fields

**Next of Kin**
- Person to contact in case of emergency
- Important for welfare emergencies
- Should be someone you trust

**Guardians**
- Financial decision-makers
- Important for succession/inheritance
- Should be documented for organization records

---

# LOGGING OUT

## How to Logout Safely

### Option 1: From Dashboard

**Top Right Corner:**
1. Click "Logout" button
2. You will be logged out
3. Redirected to login page

### Option 2: From Navigation Menu

**In Top Navigation Bar:**
1. Click "Logout" button
2. Confirmed logged out
3. Session ended

### After Logout

- You are completely logged out
- All sessions terminated
- Someone else cannot access your account
- Browser cannot access secure pages
- Must login again to access dashboard

### Security Tips

- **Always Logout:** When finished using platform
- **Shared Computers:** Always logout (don't leave logged in)
- **Personal Devices:** Consider logging out after use
- **Public WiFi:** Always logout when using public internet
- **Close Browser:** After logout, close browser window for extra security

---

# TROUBLESHOOTING GUIDE

## Common Issues and Solutions

### Issue 1: Cannot Remember Username
**Solution:**
- Contact your organization's administrator
- Provide your email address
- They can tell you your username
- Or reset your account

### Issue 2: Cannot Remember Password
**Solution:**
- Contact organization administrator
- Request password reset
- Administrator sets temporary password
- You can then login and change it

### Issue 3: Account Won't Login
**Possible Reasons:**
- Account not yet activated (check email)
- Username or password incorrect
- Too many failed login attempts (wait 30 minutes)
- Account deactivated by admin

**What To Do:**
- Check email for activation link
- Verify password spelling
- Wait 30 minutes then try again
- Contact administrator

### Issue 4: Contributions Not Showing
**Reasons:**
- Treasurer hasn't recorded yet
- Recording takes 5-10 minutes to appear
- Data not yet saved

**What To Do:**
- Refresh page (press F5 or Ctrl+R)
- Wait a few minutes
- Contact treasurer to verify payment recorded
- Check email for confirmation

### Issue 5: Fine Amount Incorrect
**Reasons:**
- Treasurer recorded wrong amount
- Old fine from previous month
- Misunderstanding about fine reason

**What To Do:**
- Ask treasurer to clarify
- Request fine amount correction if wrong
- Provide documentation if you disagree
- Follow organization dispute process

### Issue 6: Cannot Update Profile
**Reasons:**
- Profile page not loading
- Internet connection problem
- Changes not being saved

**What To Do:**
- Refresh page
- Check internet connection
- Try again
- Contact admin if still not working

### Issue 7: Emails Not Received
**Reasons:**
- Email address wrong in system
- Email in spam folder
- Email system delayed

**What To Do:**
- Check spam/junk folder
- Verify email address in profile
- Wait 15 minutes for email
- Contact admin to resend email

### Issue 8: System Very Slow
**Reasons:**
- Internet connection slow
- Server busy (many users online)
- Browser having issues

**What To Do:**
- Check internet speed
- Reload page (F5 key)
- Try different browser
- Try again later

### Issue 9: Error Message on Page
**Reasons:**
- Temporary server issue
- Browser not compatible
- Data validation error

**What To Do:**
- Note the exact error message
- Refresh page
- Try different browser
- Contact administrator with message

### Issue 10: Cannot Download Files
**Reasons:**
- File may not exist
- Permissions not set correctly
- Browser issue

**What To Do:**
- Check if logged in as authorized staff
- Verify file exists for member
- Try different browser
- Contact admin

---

# SECURITY AND PRIVACY

## Your Data is Protected

### How Your Password is Protected
- Password not stored in plain text
- Password encrypted using advanced algorithm
- Even administrators cannot see your password
- No one can recover your original password
- You must reset it if forgotten

### How Your Data is Protected
- All data encrypted
- Data stored securely
- Only authorized staff can view your information
- Activity logged and monitored
- Regular security checks performed

### Privacy Rules

**Who Can See Your Information:**
- You can see your own profile
- Treasurer can see all member information
- Admin can see everything
- Overseer can see directory only
- No outside person has access

**Your Information Will Not Be:**
- Sold to anyone
- Shared with third parties
- Used for marketing
- Given to government without permission
- Accessed by unauthorized people

---

# FREQUENTLY ASKED QUESTIONS

**Q: How long until my account is activated?**
A: Usually within 1-2 hours. Check email for activation link.

**Q: Can I change my username?**
A: No, username cannot be changed once created. Create new account if needed.

**Q: What if I never received activation email?**
A: Check spam folder. Wait 15 minutes. Contact admin to resend.

**Q: How often is my contribution history updated?**
A: Updated immediately when treasurer records contribution.

**Q: Can I download my data?**
A: Not automatically. Contact administrator to request data export.

**Q: Is the website safe to use?**
A: Yes, website uses HTTPS encryption and secure passwords.

**Q: What if I think my account was hacked?**
A: Contact administrator immediately. They can reset your password.

**Q: Can I use the website on my phone?**
A: Yes, website works on phones with web browsers (no app needed).

**Q: How much data does the website use?**
A: Very minimal. Mostly text-based (no pictures on Simple plan).

**Q: Is there a mobile app?**
A: No, use web browser instead. Works on all devices.

**Q: Can I print my statements?**
A: Yes, use browser print function (Ctrl+P or Cmd+P).

---

# GLOSSARY OF TERMS

**Admin/Administrator** - System manager with full access to everything

**Contribution** - Money paid to the SACCO (savings group)

**Dashboard** - Your personal page showing financial summary

**Fine** - Penalty charged for late payment or non-attendance

**Guardian** - Person designated to make decisions if member unavailable

**Login** - Process of entering username and password to access account

**Member** - Person registered in the SACCO organization

**Next of Kin** - Family member to contact in emergency

**Overseer** - Staff member who can view member directory

**Password** - Secret code to secure your account

**Profile** - Your personal information page

**SACCO** - Savings and Credit Cooperative Organization

**Session** - Time logged into website

**Status** - Whether your membership is Active or Inactive

**Treasurer** - Staff member who records money and fines

**Username** - Unique name used to login to account

---

# SUPPORT AND CONTACT

## Getting Help

### For Account Issues
- Contact your SACCO Administrator
- Provide your username
- Describe the problem clearly
- Administrator will assist

### For Technical Problems
- Try refreshing page first (F5 key)
- Check your internet connection
- Try different browser
- Contact administrator with error message

### For Questions About Fines/Contributions
- Contact Treasurer
- Ask for clarification
- Request correction if needed
- Follow organization process

---

# DOCUMENT INFORMATION

**Document Version:** 1.0
**Created:** 17 July 2026
**Last Updated:** 17 July 2026
**Exchange Rate:** 1 USD = 129.34 Kenya Shillings
**Currency:** All prices in Kenya Shillings (KES)
**Language:** English (No abbreviations)

---

**END OF COMPLETE GUIDE**

For support, contact your OFSG Administrator.
For technical issues, contact your system support team.
For financial questions, contact your Treasurer.
