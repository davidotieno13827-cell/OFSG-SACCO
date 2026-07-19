# OFSG PLATFORM - DETAILED CAPABILITIES BREAKDOWN

**Date:** 17 July 2026
**All Prices in Kenya Shillings (KES)**
**Exchange Rate:** 1 USD = 129.34 KES

---

# SECTION 1: WHAT THE WEBSITE CAN DO

## CATEGORY 1: MEMBER MANAGEMENT

### Registration System
**What It Does:**
- Members create their own online account
- Enter: Username, Email, Password, Phone
- Add family information: Guardians, Next-of-Kin
- System sends activation email
- Member clicks email link to activate account
- Account becomes active and ready to use

**How It Works:**
1. Member goes to website
2. Clicks "Register New Member"
3. Fills in form with personal details
4. Creates secure password (minimum 10 characters)
5. System sends activation email
6. Member activates account
7. Member can now login

**What Gets Stored:**
- Full Name (from Django user profile)
- Email Address
- Phone Number (up to 15 digits)
- Username (unique identifier)
- Password (encrypted/hashed)
- Next-of-Kin Name and Phone
- Guardian 1 Name
- Guardian 2 Name
- Registration Date
- Active/Inactive Status

### Profile Management
**What Members Can Do:**
- Update Next-of-Kin information
- Update Guardian names and contact info
- Change password
- View their personal information
- Review registration date
- Check account status

**How It Works:**
1. Member logs in to account
2. Clicks "Profile" or "Update Profile"
3. See form with editable fields
4. Update guardian or next-of-kin details
5. Click "Save Profile"
6. Changes saved immediately
7. System shows confirmation message

**What Treasurers Can Do:**
- View all member profiles
- Search for member information
- Change member status (Active/Inactive)
- Deactivate members if needed

### Member Directory
**What It Shows:**
- Complete list of all registered members
- Username for each member
- Phone number for each member
- Member status (Active/Inactive)
- Registration date
- Total contributions
- Outstanding fines

**Who Can Access:**
- Admin (Full access)
- Treasurer (Full access)
- Overseer (Limited access - view only)
- Regular Members (Cannot access)

**Search Features:**
- Search by Username
- Search by Phone Number
- Filter by Status (Active/Inactive)
- Sort by registration date
- View full member details

### Member Detail Pages
**For Each Member Shows:**
- Complete profile information
- Phone number
- Next-of-Kin details
- Guardian information
- Member status
- Contribution history
- All fines (paid and unpaid)
- Recent transactions
- Total savings amount

---

## CATEGORY 2: FINANCIAL TRACKING

### Contribution Recording
**What It Tracks:**
- Monthly contributions (typically 1,000 KES)
- Annual General Meeting fees (typically 2,000 KES)
- Welfare/Social contributions
- Any other contribution types
- Date and time of contribution
- Contribution type
- Exact amount paid
- Which member contributed

**How It Works:**
1. Treasurer accesses "Add Contribution" page
2. Selects member from dropdown
3. Enters amount paid
4. Selects contribution type
5. System records date automatically
6. Treasurer clicks save
7. Contribution saved to database
8. Appears in member's history
9. Dashboard totals update

**What Gets Calculated:**
- Total contributions per member
- Total contributions per month
- Total contributions per type
- Organization totals
- Member savings equity
- Contribution trends

### Contribution Viewing
**Members Can See:**
- Their personal contribution history
- Date each contribution was paid
- Type of contribution
- Amount paid
- Total cumulative savings
- Number of contribution entries

**Treasurers Can See:**
- All member contributions
- Organization-wide totals
- Contributions by date range
- Contributions by type
- Member comparison data
- Trend information

**Dashboard Display:**
- Table showing recent contributions
- Total savings displayed prominently
- Contribution count
- Latest contributions listed first

---

### Fine Management System
**What It Tracks:**
- Fine type (Late Payment, Non-Attendance, Other)
- Member being fined
- Fine amount
- Date fine issued
- Paid/Unpaid status
- Payment date (if paid)
- Person who issued fine

**How Fines Are Added:**
1. Treasurer clicks "Add Fine"
2. Selects member
3. Chooses fine type or enters custom reason
4. Enters fine amount
5. System records date automatically
6. Saves fine record
7. Fine appears in member's outstanding fines
8. Affects member's dashboard totals

**How Fines Are Marked Paid:**
1. Member pays fine (cash or mobile money)
2. Treasurer locates fine record
3. Treasurer clicks "Mark Fine as Paid"
4. Status changes from "Unpaid" to "Paid"
5. Fine amount subtracted from outstanding total
6. Member's dashboard updates
7. Payment date recorded

**Fines Can Be For:**
- Late Payment of monthly contribution
- Non-attendance at meetings
- Non-compliance with rules
- Any other penalties organization sets

---

### Financial Reporting
**Member Dashboard Shows:**
- Total Savings Equity: Total of all contributions
- Outstanding Fines: Total unpaid fines
- Member Status: Active or Inactive
- Recent Contributions: Table of last 5-10
- Outstanding Fine Summary: List of unpaid fines

**Treasurer Dashboard Shows:**
- Total Active Members: Count of active members
- Total Inactive Members: Count of inactive
- Recent Contributions: Last 8 contributions
- Outstanding Fines: List of unpaid fines
- Organization Totals: Total savings, total fines
- Quick Statistics: Various totals and counts

**Management Summary Shows:**
- Organization-wide statistics
- Recent member registrations
- Recent contributions
- Outstanding fines
- Financial overview
- Activity summary

---

## CATEGORY 3: SECURITY FEATURES

### Password Security
**Requirements:**
- Minimum 10 characters long
- Must include uppercase letter (A-Z)
- Must include lowercase letter (a-z)
- Must include number (0-9)
- Must include special character (!@#$%^&*)
- Cannot be too similar to username
- Cannot be common weak password

**Storage:**
- Passwords stored as encrypted hash
- Original password never visible
- Admin cannot see your password
- Cannot be recovered, only reset
- Each password unique and secure

### Session Security
**Features:**
- Secure HTTPS encryption
- Session cookies secure (HTTPS only)
- Automatic logout after inactivity
- Cannot use session on different network
- Multiple devices require separate login
- Failed login attempts tracked
- Account locked after 5 failed attempts
- 30-minute lockout period

### Data Access Control
**Admin Can:**
- Access everything
- Create and delete accounts
- View all financial records
- Change any data
- Manage all staff

**Treasurer Can:**
- View all member information
- Add contributions
- Add and mark fines as paid
- View financial reports
- Cannot delete members
- Cannot change system settings

**Overseer Can:**
- View member directory
- See member details
- View member status
- Cannot edit any data
- Cannot manage finances
- Cannot access settings

**Regular Members Can:**
- See own profile
- View own contributions
- View own fines
- Update own profile
- Cannot see other members
- Cannot access reports

### Protection Features
**Protection Against:**
- Unauthorized access (passwords)
- Cross-site attacks (CSRF tokens)
- Clickjacking (X-Frame headers)
- SQL injection (parameterized queries)
- Brute force attacks (rate limiting)
- Session hijacking (secure cookies)

---

## CATEGORY 4: EMAIL SYSTEM

### Activation Emails
**When Sent:**
- When new member registers
- Contains activation link
- Member clicks link to activate account
- Account becomes available

**Includes:**
- Member username
- Personalized greeting
- Activation link
- Instructions for activation
- Time limit for activation

### Password Reset Emails
**When Sent:**
- When admin resets password
- When member requests password change
- Contains temporary password or reset link

**Includes:**
- New temporary password
- Instructions for first login
- Security reminder
- Support contact information

### Notification Emails
**Can Include:**
- New fine issued notification
- Contribution recorded notification
- Account status change notification
- Profile update confirmation
- System announcements

### Email Format
**Supports:**
- Plain text emails
- HTML formatted emails
- Personalizable templates
- Custom text and images
- Professional formatting

---

# SECTION 2: WHAT THE WEBSITE CANNOT DO

## CATEGORY 1: IMAGE AND DOCUMENT STORAGE
❌ Cannot store member profile pictures
❌ Cannot store passport photos
❌ Cannot store ID documents
❌ Cannot display member photos in directory
❌ Cannot verify identity through photos
❌ Cannot scan documents automatically
❌ Cannot process image recognition
❌ Cannot create digital signatures

**Workaround:** Use Standard or Premium plan to store these

---

## CATEGORY 2: PAYMENT PROCESSING
❌ Cannot process M-Pesa payments
❌ Cannot process bank transfers
❌ Cannot process credit cards
❌ Cannot collect payments online
❌ Cannot integrate with payment gateway
❌ Cannot charge automatic monthly fees
❌ Cannot process refunds automatically
❌ Cannot hold funds securely

**Workaround:** Members pay cash to treasurer, treasurer records in system

---

## CATEGORY 3: OFFLINE ACCESS
❌ Cannot work without internet connection
❌ Cannot sync data offline
❌ Cannot cache data locally
❌ Cannot operate when server down
❌ Cannot access data without connection

**Workaround:** Use at location with WiFi or mobile data

---

## CATEGORY 4: MOBILE APPLICATION
❌ No native mobile app for Android
❌ No native mobile app for iPhone
❌ Cannot work as offline app
❌ Cannot access without web browser
❌ No iOS version available

**Workaround:** Website works on mobile phone browsers (just slower)

---

## CATEGORY 5: ADVANCED REPORTING
❌ Cannot generate automatic charts/graphs
❌ Cannot export to Excel automatically
❌ Cannot create PDF reports automatically
❌ Cannot schedule report emails
❌ Cannot analyze trends automatically
❌ Cannot predict future trends
❌ Cannot generate compliance reports automatically

**Workaround:** Manual export and analysis using spreadsheet programs

---

## CATEGORY 6: AUTOMATIC CALCULATIONS
❌ Cannot automatically calculate compound interest
❌ Cannot auto-apply fines on schedule
❌ Cannot automatically process refunds
❌ Cannot calculate loan amounts
❌ Cannot compute tax automatically
❌ Cannot generate automatic invoices

**Workaround:** Manual calculations using calculator or spreadsheet

---

## CATEGORY 7: COMMUNICATION FEATURES
❌ Cannot send SMS text messages
❌ Cannot receive SMS commands
❌ Cannot make phone calls
❌ Cannot send voice messages
❌ Cannot integrate with WhatsApp
❌ Cannot send bulk SMS
❌ Cannot schedule SMS

**Workaround:** Use email for communications

---

## CATEGORY 8: MULTI-ORGANIZATION SUPPORT
❌ Cannot manage multiple SACCO groups
❌ Cannot share data between groups
❌ Cannot manage different organizations
❌ One system = One organization only
❌ Cannot transfer data between groups
❌ Cannot create sub-groups

**Workaround:** Set up separate system for each organization

---

## CATEGORY 9: ADVANCED FEATURES
❌ Cannot process blockchain transactions
❌ Cannot manage cryptocurrency
❌ Cannot create NFTs
❌ Cannot use artificial intelligence
❌ Cannot analyze machine learning
❌ Cannot create smart contracts
❌ Cannot manage digital assets

**Workaround:** Not needed for typical SACCO operations

---

## CATEGORY 10: DISASTER RECOVERY (Simple Plan Only)
❌ No automatic daily backups (Simple plan)
❌ No backup redundancy
❌ No disaster recovery system
❌ No backup verification
❌ No recovery time guarantee
❌ Data loss possible if server fails

**Workaround:** Upgrade to Standard or Premium for automatic backups

---

# SECTION 3: DETAILED PRICING BREAKDOWN

## SIMPLE PLAN (2,583 KES per month)

### Monthly Cost Components:
1. **Render Web Server (Starter Tier)** - 905 Kenya Shillings
   - Hosts website
   - ~10-20 simultaneous users
   - Basic performance
   - 99.5% uptime

2. **PostgreSQL Database (Starter Tier)** - 905 Kenya Shillings
   - Stores all data
   - 1 GB capacity
   - Basic performance
   - No backup redundancy

3. **Email Service (SendGrid Free Tier)** - 0 Kenya Shillings
   - 100 emails per day limit
   - Free tier included
   - Standard templates
   - Manual configuration

4. **Domain Name (Annual Cost Amortized)** - 162 Kenya Shillings per month
   - Annual registration: ~2,000 Kenya Shillings
   - Divided by 12 months
   - Your website address
   - Renewal required annually

5. **Operating Buffer/Contingency** - 647 Kenya Shillings
   - For unexpected costs
   - Maintenance reserves
   - Miscellaneous fees
   - Safety margin

**TOTAL SIMPLE PLAN: 2,583 Kenya Shillings per month**
**Annual Cost: 30,996 Kenya Shillings**

### What's Included in Simple Plan:
- Member registration system
- Contribution tracking system
- Fine management system
- Member search and directory
- Email activation and notifications
- Secure login system
- Dashboard for members and treasurer
- Role-based access control (Admin, Treasurer, Overseer)
- Text-only database
- Support for 500-1,000 members
- Unlimited contribution records
- Unlimited fine records
- 3,000 emails per month maximum

### Limitations of Simple Plan:
- No picture storage
- No document storage
- Limited to 10-20 simultaneous users
- No automatic backups
- No file redundancy
- Manual backup required
- Basic performance only
- Limited email capacity
- No advanced features

---

## STANDARD PLAN (6,241 KES per month)

### Monthly Cost Components:
1. **Render Web Server (Standard Tier)** - 1,940 Kenya Shillings
   - Faster hosting
   - ~50-100 simultaneous users
   - Better performance
   - 99.8% uptime

2. **PostgreSQL Database (Standard Tier)** - 905 Kenya Shillings
   - Standard tier database
   - Standard performance
   - Basic backup included
   - 10 GB capacity

3. **Email Service (SendGrid Starter Plan)** - 1,940 Kenya Shillings
   - Professional email tier
   - Up to 50,000 emails per month
   - HTML templates
   - Professional support

4. **File Storage (AWS S3 or Equivalent)** - 1,293 Kenya Shillings
   - Cloud file storage
   - 100+ GB capacity
   - Automatic backup of files
   - Secure access control

5. **Domain Name (Annual Cost Amortized)** - 162 Kenya Shillings per month
   - Annual registration fee
   - Your website address
   - Professional domain presence

**TOTAL STANDARD PLAN: 6,241 Kenya Shillings per month**
**Annual Cost: 74,892 Kenya Shillings**

### What's Included in Standard Plan (Everything in Simple PLUS):
- **Profile Picture Storage** - Store member profile photos
- **Passport Photo Storage** - Store member passport photos
- **ID Document Storage** - Store digital copies of ID documents
- **File Downloads** - Members and staff can download documents
- **Professional Email** - 50,000 emails per month
- **Better Performance** - Faster page loads and responses
- **Support 1,000-5,000 members** - Larger capacity
- **100+ GB File Storage** - Plenty of document space
- **Enhanced Dashboard** - Better reporting features
- **Automatic File Organization** - Documents organized by member

### When to Use Standard Plan:
- Growing organization (500-2,000 members)
- Need to store documents
- More staff members accessing system
- Want professional email features
- Need faster performance
- Want digital document backup
- Multiple treasurers/staff

---

## PREMIUM PLAN (12,448 KES per month)

### Monthly Cost Components:
1. **Render Web Server (Professional Tier)** - 3,880 Kenya Shillings
   - Professional-grade hosting
   - ~200-500 simultaneous users
   - Excellent performance
   - 99.95% uptime guarantee

2. **PostgreSQL Database (Professional Tier)** - 2,587 Kenya Shillings
   - Professional database tier
   - Excellent performance
   - Advanced backup system
   - 100+ GB capacity

3. **Email Service (SendGrid Enhanced Plan)** - 3,880 Kenya Shillings
   - Up to 500,000 emails per month
   - Advanced templates
   - Email automation
   - Priority support

4. **File Storage (AWS S3 Scaled Tier)** - 1,940 Kenya Shillings
   - Large-scale cloud storage
   - 1+ TB capacity
   - Advanced features
   - Enhanced redundancy

5. **Domain Name (Annual Cost Amortized)** - 162 Kenya Shillings per month
   - Professional domain
   - Your website address

**TOTAL PREMIUM PLAN: 12,448 Kenya Shillings per month**
**Annual Cost: 149,384 Kenya Shillings**

### What's Included in Premium Plan (Everything in Standard PLUS):
- **Automatic Daily Backups** - Scheduled automatic backups
- **Disaster Recovery** - Data recovery capability
- **99.95% Uptime Guarantee** - Maximum availability
- **Advanced Analytics** - Detailed analytics and reports
- **Export to CSV Format** - Export data for spreadsheets
- **Complete Audit Logs** - Full activity history
- **Priority Technical Support** - Faster response times
- **Support 5,000-50,000+ members** - Enterprise capacity
- **1+ TB File Storage** - Massive document storage
- **Security Certifications** - Advanced security features
- **Compliance Reporting** - For regulatory compliance
- **Performance Optimization** - System tuning and optimization
- **Regular Security Audits** - Professional security reviews

### When to Use Premium Plan:
- Large organization (5,000+ members)
- Mission-critical system
- High security requirements
- Compliance/regulatory needs
- 100+ staff users
- Guaranteed uptime needed
- Complete audit trail required
- Advanced analytics needed

---

# SECTION 4: SIDE-BY-SIDE PLAN COMPARISON

## STORAGE COMPARISON

### Simple Plan: Text-Only
- Database: 5-10 MB
- Pictures: None
- Documents: None
- Total: 5-10 MB
- Cost: 2,583 KES

### Standard Plan: With Documents
- Database: 20-50 MB
- Pictures: Profile photos (stored)
- Documents: ID documents (stored)
- File Storage: 100+ GB available
- Total Capacity: 100+ GB
- Cost: 6,241 KES

### Premium Plan: Enterprise
- Database: 100+ MB
- All files from Standard
- File Storage: 1+ TB available
- Total Capacity: 1+ TB (1,000 GB)
- Cost: 12,448 KES

---

## USER CAPACITY COMPARISON

### Simple Plan
- Simultaneous Users: 10-20 comfortable
- Peak Usage: 20-30 possible
- Total Members: 500-1,000 max
- Staff Access: 5-10 users

### Standard Plan
- Simultaneous Users: 50-100 comfortable
- Peak Usage: 100-150 possible
- Total Members: 1,000-5,000 max
- Staff Access: 20-50 users

### Premium Plan
- Simultaneous Users: 200-500 comfortable
- Peak Usage: 500-1,000 possible
- Total Members: 5,000-50,000+ max
- Staff Access: 50-200+ users

---

## PERFORMANCE COMPARISON

### Simple Plan
- Page Load Time: 2-3 seconds
- Database Response: Standard
- Email Delivery: 5-10 minutes
- File Downloads: Not available
- System Updates: Ad-hoc

### Standard Plan
- Page Load Time: 1-2 seconds
- Database Response: Fast
- Email Delivery: 1-5 minutes
- File Downloads: Immediate
- System Updates: Regular

### Premium Plan
- Page Load Time: <1 second
- Database Response: Very Fast
- Email Delivery: <1 minute
- File Downloads: Instant
- System Updates: Automatic

---

## EMAIL CAPACITY COMPARISON

### Simple Plan
- Daily Limit: 100 emails
- Monthly Limit: 3,000 emails
- Tier: Free SendGrid
- Templates: Basic
- Scheduling: Not available

### Standard Plan
- Daily Limit: ~1,667 emails
- Monthly Limit: 50,000 emails
- Tier: SendGrid Starter
- Templates: Professional HTML
- Scheduling: Available

### Premium Plan
- Daily Limit: ~16,667 emails
- Monthly Limit: 500,000 emails
- Tier: SendGrid Enhanced
- Templates: Advanced
- Scheduling: Full automation

---

## BACKUP & RECOVERY COMPARISON

### Simple Plan
- Automatic Backups: None
- Manual Backups: User responsibility
- Recovery Time: Varies
- Data Loss Risk: Medium to High
- Backup Retention: N/A

### Standard Plan
- Automatic Backups: Limited
- Manual Backups: Recommended
- Recovery Time: Variable
- Data Loss Risk: Lower
- Backup Retention: N/A

### Premium Plan
- Automatic Backups: Daily
- Manual Backups: Also available
- Recovery Time: Fast
- Data Loss Risk: Very Low
- Backup Retention: 30 days

---

## UPTIME GUARANTEE COMPARISON

### Simple Plan
- Uptime: ~99.5%
- Downtime/Month: ~3.6 hours
- SLA: Not guaranteed
- Support: Community

### Standard Plan
- Uptime: ~99.8%
- Downtime/Month: ~1.4 hours
- SLA: Best effort
- Support: Standard

### Premium Plan
- Uptime: 99.95%
- Downtime/Month: ~22 minutes
- SLA: Guaranteed
- Support: Priority 24/7

---

# PRICING SUMMARY TABLE

| Item | Simple | Standard | Premium |
|------|--------|----------|---------|
| Web Server | 905 KES | 1,940 KES | 3,880 KES |
| Database | 905 KES | 905 KES | 2,587 KES |
| Email | 0 KES | 1,940 KES | 3,880 KES |
| File Storage | 0 KES | 1,293 KES | 1,940 KES |
| Domain | 162 KES | 162 KES | 162 KES |
| Buffer | 647 KES | 0 KES | 0 KES |
| **MONTHLY** | **2,583 KES** | **6,241 KES** | **12,448 KES** |
| **ANNUAL** | **30,996 KES** | **74,892 KES** | **149,384 KES** |

---

**END OF DETAILED BREAKDOWN**

For complete user manual, see: OFSG_PLATFORM_COMPLETE_GUIDE.md
For quick reference, see: OFSG_PRICING_REFERENCE.md

---

Version 1.0 | July 2026 | All prices in Kenya Shillings
